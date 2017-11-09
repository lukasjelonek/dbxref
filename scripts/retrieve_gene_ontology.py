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
	parser = argparse.ArgumentParser(description='Retrieve gene ontology documents for dbxrefs and convert them into json')
	parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref, definition, name and synonyms')
	parser.add_argument('--relations', '-r', action='store_true', help='Include dbxrefs and type of parent and children')
	parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
	documents = []
	for entry in resolved:
		json_url = entry['locations']['json'][0]
		logger.debug('URL: %s', json_url)
		r = requests.get(json_url)
		logger.debug('Content: %s', r.text)
		d = json.loads(r.text)
		output = {'id': entry['dbxref']}
		if args.basic:
			output.update(read_basic(d))
		if args.relations:
			output.update(read_relations(d))
		if not args.basic and not args.relations:
			output.update(read_basic(d))
			output.update(read_relations(d))
		documents.append(output)
	print (json.dumps(documents))

def read_basic(d):
	out = {'definition': d['results'][0]['definition']['text']}
	out['name'] = d['results'][0]['name']
	out['synonyms'] = d['results'][0]['synonyms']
	return (out)

def read_relations(d):
	out = {'relations': {'children': d['results'][0]['children']}}
	for child in out['relations']['children']:
		child['type'] = child.pop('relation')
	out['relations']['parents'] = parse_history(d['results'][0]['history'])
	return (out)

def parse_history(h):
	out = []
	for history in reversed(h):
		if history['category'] == "RELATION":
			if history['action'] == "Updated" or history['action'] == "Added":
				out.append(history)
			if history['action'] == "Deleted":
				for i in reversed(range(len(out))):
					if out[i]['text'] == history['text']:
						del out[i]
						break
	for i in range(len(out)):
		out[i] = parse_text(out[i]['text'])
	return (out)

def parse_text(t):
	words = t.split(' ')
	type = ''
	out = {}
	for word in words:
		if 'GO:' in word:
			out['id'] = word
			break
		else:
			if type == '':
				type = word
			else:
				type += "_" + word
	out['type'] = type
	return (out)

main()
