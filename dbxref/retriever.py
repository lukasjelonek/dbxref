import logging
logger = logging.getLogger(__name__)

from dbxref import config
from itertools import groupby
import json

def retrieve(dbxrefs):
    sorted(dbxrefs, key=lambda x: x['db'].lower()) # normalize db to lowercase to allow differently cased notations
    results = []
    for key, dbxrefs in groupby(dbxrefs, lambda x: x['db']):
        if config.has_provider(key):
            provider = config.get_provider(key)
            logger.debug('{0} is supported'.format(key))
            if provider['retriever']['type'] == 'external':
                results.extend( load_with_external_provider(provider, list(dbxrefs)))
            elif provider['retriever']['type'] == 'internal':
                results.extend(load_with_internal_provider(provider, list(dbxrefs)))
            else:
                raise Exception('Unknown retriever type', provider['retriever']['type'])
        else:
            logger.debug('{0} is not supported'.format(key))
            results.extend( map(lambda x: {'id': toString(x), 'status': 'not supported'}, dbxrefs))
    return (results)

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
