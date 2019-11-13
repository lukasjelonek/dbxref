import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from dbxref import config
from itertools import groupby
from diskcache import Cache
from appdirs import user_cache_dir

import json

def retrieve(dbxrefs, ignore_cache=False):
    cache = init_cache()

    # normalize db notation
    normalize_db_notation(dbxrefs)
    dbxrefs = sorted(dbxrefs, key=lambda x: x['db'])

    # lookup from cache
    uncached = []
    cached = []
    if ignore_cache:
      uncached = dbxrefs
    else :
      (cached, uncached) = find_cached_entries(cache, dbxrefs)

    # load uncached
    loaded_uncached = load_uncached_entries(uncached)
    cache_entries(cache, loaded_uncached)

    # compile results
    results = []
    results.extend(cached)
    results.extend(loaded_uncached)
    return results

def normalize_db_notation(dbxrefs):
  # take first prefix that matches the db
  for dbxref in dbxrefs:
    key = dbxref['db']
    if config.has_provider(key):
        provider = config.get_provider(key)
        for prefix in provider['prefixes']:
          if key.lower() ==  prefix.lower():
            dbxref['db'] = prefix
    logger.debug("'{}' -> '{}'".format(key, dbxref['db']))

def load_with_external_provider(provider, dbxrefs):
    logger.debug('Loading {0} via external provider'.format(dbxrefs))
    script = provider['retriever']['location']
    call = '{} {}'.format(script, ' '.join(list(map(toString, dbxrefs))))
    logger.debug("Running '{}'".format(call))
    import subprocess
    result = subprocess.check_output(call, shell=True)
    return json.loads(result.decode('utf-8'))

def load_with_internal_provider(provider, dbxrefs):
    import importlib
    retrieve_method = getattr(importlib.import_module(provider['retriever']['location']), 'retrieve')
    retrieved = retrieve_method(dbxrefs)
    return retrieved

def toString(dbxref):
    return '{}:{}'.format(dbxref['db'], dbxref['id'])

def init_cache():
  cachedir = user_cache_dir('dbxref')
  cache = Cache(cachedir)
  return cache

def cache_entries(cache, entries):
  expiration_time = 86400 # one day
  for e in entries:
    logger.debug('Caching {}'.format(e['id']))
    cache.set(e['id'], e, expire=expiration_time)

def find_cached_entries(cache, dbxrefs):
  cached = []
  uncached = []
  for d in dbxrefs:
    key = toString(d)
    if key in cache:
      logger.debug("Found {} in cache".format(key))
      cached.append(cache[key])
    else:
      uncached.append(d)
  return (cached, uncached)

def load_uncached_entries(dbxrefs):
  results = []
  for key, dbxrefs in groupby(dbxrefs, lambda x: x['db']):
      if config.has_provider(key):
          provider = config.get_provider(key)
          logger.debug('{0} is supported'.format(key))
          if 'retriever' in provider:
            if provider['retriever']['type'] == 'external':
                results.extend( load_with_external_provider(provider, list(dbxrefs)))
            elif provider['retriever']['type'] == 'internal':
                results.extend(load_with_internal_provider(provider, list(dbxrefs)))
            else:
                raise Exception('Unknown retriever type', provider['retriever']['type'])
          else:
            logger.debug('{0} is not supported'.format(key))
            results.extend( map(lambda x: {'id': toString(x), 'status': 'not supported'}, dbxrefs))
      else:
          logger.debug('{0} is not supported'.format(key))
          results.extend( map(lambda x: {'id': toString(x), 'status': 'not supported'}, dbxrefs))
  return (results)
