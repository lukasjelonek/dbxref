#!/usr/bin/env python3
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Make bioinformatic observations on aminoacid sequences')
    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    info_parser = subparsers.add_parser('info')
    info_parser.set_defaults(func=info)
    #TODO implement

    resolve_parser = subparsers.add_parser('resolve')
    resolve_parser.set_defaults(func=resolve)
    #TODO implement

    retrieve_parser = subparsers.add_parser('retrieve')
    retrieve_parser.set_defaults(func=retrieve)
    #TODO implement

    args = parser.parse_args()
    config = {} # TODO implement
    args.parser = parser
    args.func(args, config)

def help(args, config):
    args.parser.print_help()

def info(args, config):
    #TODO implement
    print ('info')

def resolve(args, config):
    #TODO implement
    print ('resolve')

def retrieve(args, config):
    #TODO implement
    print ('retrieve')

if __name__ == "__main__":
    main()
