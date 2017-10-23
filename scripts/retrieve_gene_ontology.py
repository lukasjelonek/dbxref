#!/usr/bin/env python3
import env
import dbxref.config
import dbxref.resolver
import requests
import json
import argparse

def main():
	parser = argparse.ArgumentParser(description='Retrieve gene ontology documents for dbxrefs and convert them into json')
	parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
	documents = []
	for entry in resolved:
		json_url = entry['locations']['json'][0]
		r = requests.get(json_url)
		output = {'dbxref': entry['dbxref']}
		d = json.loads(r.text)
		output['results'] = d['results']
#		for result in d['results']:
#			output.update(result)
#		output.update(d['results'][0])
		documents.append(output)
	print (json.dumps(documents))

main()
