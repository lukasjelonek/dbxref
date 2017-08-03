import requests
import logging
logger = logging.getLogger(__name__)

from dbxref.config import load_providers
providers = load_providers()

FOUND='FOUND'
NOT_FOUND='NOT_FOUND'
UNSUPPORTED='UNSUPPORTED'

def resolve(strings, check_existence=True):
    results = []
    for s in strings:
        exists = True
        if check_existence:
           exists = check_dbxref_exists(s) 
        dbxref = convert_string_to_dbxref(s)
        if exists and dbxref['db'] in providers:
            provider = providers[dbxref['db']]
            urls = []
            for r in provider['resources']:
                for url_template in provider['resources'][r]:
                    urls.append( {
                        'type': r,
                        'url': compile_url(url_template, dbxref)
                        } ) 
            results.append({'dbxref': dbxref['db'] + ':' + dbxref['id'], 'locations': urls})
    return results

def check_dbxref_exists(string):
    dbxref = convert_string_to_dbxref(string)
    if dbxref['db'] in providers:
        provider = providers[dbxref['db']]
        urls = []
        exists = FOUND
        if 'check_existence' in provider:
            url = compile_url(provider['check_existence'], dbxref)
            logger.debug('Checking existence of dbxref at "%s"', url)
            exists = check_url_exists(url)
            if exists == NOT_FOUND:
                logger.info('The dbxref "%s" cannot be found. It will be ignored.', string)
            return exists
        else:
            return UNSUPPORTED
    return UNSUPPORTED

def compile_url(template, dbxref):
    return template.replace('%i', dbxref['id']).replace('%d', dbxref['db'])

def check_url_exists(url):
    try:
        r = requests.head(url, allow_redirects=True)
        r.close()
        if r.status_code <= 400:
            return FOUND
        else:
            return NOT_FOUND
    except:
        return NOT_FOUND

def convert_string_to_dbxref(string):
    """
    A dbxref is dictionary with two keys: db and id.
    """
    split = string.split(':', 1)
    return {'db': split[0], 'id': split[1]}
