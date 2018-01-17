import logging
logger = logging.getLogger(__name__)

from dbxref.config import load_providers
from itertools import groupby
import json

providers = load_providers()

def retrieve(dbxrefs, location=''):
    sorted(dbxrefs, key=lambda x: x['db'])
    results = []
    for key, dbxrefs in groupby(dbxrefs, lambda x: x['db']):
        if key.lower() in providers and 'retriever' in providers[key.lower()]:
            provider = providers[key.lower()]
            logger.debug('{0} is supported'.format(key))
            if provider['retriever']['type'] == 'external':
                retrieved = load_with_external_provider(provider, list(dbxrefs), location)
                results.extend(retrieved)
            elif provider['retriever']['type'] == 'internal':
                import importlib
                retrieve_method = getattr(importlib.import_module(provider['retriever']['location']), 'retrieve')
                retrieved = retrieve_method(dbxrefs)
                results.extend(retrieved)
            else:
                raise Exception('Unknown retriever type', provider['retriever']['type'])
        else:
            logger.debug('{0} is not supported'.format(key))
            results.extend( map(lambda x: {'id': toString(x), 'status': 'not supported'}, dbxrefs))
    if not location == '':
        return (results)
    else:
	    print(json.dumps(results, indent=4))


def load_with_external_provider(provider, dbxrefs, location):
    logger.debug('Loading {0} via external provider'.format(dbxrefs))
    script = provider['retriever']['location']
    call = location + '{} {}'.format(script, ' '.join(list(map(toString, dbxrefs))))
    logger.debug("Running '{}'".format(call))
    import subprocess
    result = subprocess.check_output(call, shell=True)
    return json.loads(result.decode('utf-8'))

def toString(dbxref):
    return '{}:{}'.format(dbxref['db'], dbxref['id'])
