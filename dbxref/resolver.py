import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
import logging
logger = logging.getLogger(__name__)

from dbxref.config import load_providers
providers = load_providers()

cache = FileCache(".web_cache", forever=True)
sess = CacheControl(requests.Session(), cache=cache)

STATUS_EXISTS='found'
STATUS_NOT_EXISTS='not found'
STATUS_UNKNOWN='status unknown'
STATUS_NOT_CHECKED='status not checked'
STATUS_CHECK_NOT_SUPPORTED='check of status not supported'
STATUS_CHECK_TIMEOUT='status check timed out'
STATUS_UNSUPPORTED_DB='database unsupported'

def resolve(strings, check_existence=True):
    results = []
    for s in strings:
        status = STATUS_NOT_CHECKED
        if check_existence:
           status = check_dbxref_exists(s)
        dbxref = convert_string_to_dbxref(s)
        if dbxref['db'] in providers:
            provider = providers[dbxref['db']]
            locations = {}
            for _type in provider['resources']:
                urls = []
                for url_template in provider['resources'][_type]:
                    urls.append(compile_url(url_template, dbxref))
                locations[_type] = urls
            results.append({'dbxref': dbxref['db'] + ':' + dbxref['id'], 'locations': locations, 'status': status})
        else:
            results.append({'dbxref': dbxref['db'] + ':' + dbxref['id'], 'status': STATUS_UNSUPPORTED_DB})
    return results

def check_dbxref_exists(string):
    dbxref = convert_string_to_dbxref(string)
    if dbxref['db'] in providers:
        provider = providers[dbxref['db']]
        urls = []
        exists = STATUS_NOT_CHECKED
        if 'check_existence' in provider:
            url = compile_url(provider['check_existence'], dbxref)
            logger.debug('Checking existence of dbxref at "%s"', url)
            exists = check_url_exists(url)
            return exists
        else:
            return STATUS_CHECK_NOT_SUPPORTED
    return STATUS_UNSUPPORTED_DB

def compile_url(template, dbxref):
    return template.replace('%i', dbxref['id']).replace('%d', dbxref['db'])

def check_url_exists(url):
    try:
        r = sess.head(url, allow_redirects=True, timeout=1)
        r.close()
        if r.status_code <= 400:
            return STATUS_EXISTS
        else:
            logger.debug('The server responded with status code: %s', r.status_code)
            return STATUS_NOT_EXISTS
    except requests.exceptions.Timeout as ex:
        logger.info('Timeout for URL: "%s"', url)
        return STATUS_CHECK_TIMEOUT
    except:
        return STATUS_NOT_EXISTS

def convert_string_to_dbxref(string):
    """
    A dbxref is dictionary with two keys: db and id.
    """
    split = string.split(':', 1)
    return {'db': split[0], 'id': split[1]}
