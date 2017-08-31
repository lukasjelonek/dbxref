#!/usr/bin/env python3
import argparse
import os
import logging

def main():
    parser = argparse.ArgumentParser(description='Lookup locations of database cross references and retrieve them as json')
    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    info_parser = subparsers.add_parser('info')
    info_parser.set_defaults(func=info)
    #TODO implement

    resolve_parser = subparsers.add_parser('resolve')
    resolve_parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    resolve_parser.add_argument('--no_check', '-n', action='store_false', default=True, help="Do not check existence of cross reference")
    resolve_parser.add_argument('--verbose', '-v', action='store_true', default=True, help="Show debug output")
    resolve_parser.set_defaults(func=resolve)

    retrieve_parser = subparsers.add_parser('retrieve')
    retrieve_parser.set_defaults(func=retrieve)
    retrieve_parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    retrieve_parser.add_argument('--verbose', '-v', action='store_true', default=True, help="Show debug output")

    args = parser.parse_args()
    config = {} # TODO implement
    if (args.verbose):
        logging.basicConfig(level=logging.INFO)
    args.parser = parser
    args.func(args, config)

def help(args, config):
    args.parser.print_help()

def info(args, config):
    #TODO implement
    print ('info')

def resolve(args, config):
    from dbxref import resolver
    import json
    print(json.dumps(resolver.resolve(args.dbxrefs, check_existence=args.no_check)))

def retrieve(args, config):
    from dbxref import retriever
    retriever.retrieve(args.dbxrefs)

if __name__ == "__main__":
    main()
