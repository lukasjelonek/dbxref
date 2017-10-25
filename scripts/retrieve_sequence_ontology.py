#!/usr/bin/env python3
import env
import dbxref.config
import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser(description='Retrieve sequence ontology csv documents for dbxrefs and convert them into json')
	parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
	documents = []
	for entry in resolved:
		csv_url = entry['locations']['csv'][0]
		logger.debug('URL: %s', csv_url)
		r = requests.get(csv_url)
		logger.debug('Content: %s', r.text)
		elements = r.text.strip().replace('\n', '\t').split('\t')
		output = {'dbxref': entry['dbxref'], 'name': elements[7], 'definition': elements[8], 'parent': elements[9]}
		documents.append(output)
	print (json.dumps(documents))

main()
