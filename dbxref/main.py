#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import os
import logging
from dbxref import resolver, config
from pbr.version import VersionInfo
import json

__version__ = VersionInfo('dbxref').semantic_version().release_string()

def main():
    parser = argparse.ArgumentParser(description='Version ' + __version__ + '\nLookup locations of database cross references and retrieve them as json', formatter_class=RawTextHelpFormatter)
    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    info_parser = subparsers.add_parser('info')
    info_parser.set_defaults(func=info)

    resolve_parser = subparsers.add_parser('resolve')
    resolve_parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    resolve_parser.add_argument('--no_check', '-n', action='store_false', default=True, help="Do not check existence of cross reference")
    resolve_parser.add_argument('--verbose', '-v', action='store_true', default=False, help="Show debug output")
    resolve_parser.set_defaults(func=resolve)

    retrieve_parser = subparsers.add_parser('retrieve')
    retrieve_parser.set_defaults(func=retrieve)
    retrieve_parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    retrieve_parser.add_argument('--ignore_cache', '-C', action='store_true', default=False, help="Ignore entries from cache. Fetched entries are still stored in cache.")
    retrieve_parser.add_argument('--verbose', '-v', action='store_true', default=False, help="Show debug output")

    args = parser.parse_args()
    config = {} # implement when needed
    if ('verbose' in vars(args) and args.verbose):
        logging.basicConfig(level=logging.INFO)
    args.parser = parser
    args.func(args, config)

def help(args, config):
    args.parser.print_help()

def info(args, cfg):
    print ('dbxref Version ' + __version__)
    print ('')
    print ('Supported dbxref databases:')
    providers = config.load_providers()
    for provider in providers:
      print ('   ' + provider['name'])
      print ('     Prefixes: ' + str.join(', ', [x for x in provider['prefixes']]))
      print ('     Formats : ' + str.join(', ', [x for x in provider['resources']]))

def resolve(args, config):
    print(json.dumps(resolver.resolve(resolver.convert_to_dbxrefs(args.dbxrefs), check_existence=args.no_check)))

def retrieve(args, config):
    from dbxref import retriever
    print(
      json.dumps(
        retriever.retrieve(
          resolver.convert_to_dbxrefs(args.dbxrefs),
          ignore_cache = args.ignore_cache
        )
      )
    )

if __name__ == "__main__":
    main()
