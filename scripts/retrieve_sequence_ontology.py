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
		obo_url = entry['locations']['obo'][0]
		logger.debug('URL: %s', obo_url)
		r = requests.get(obo_url)
		logger.debug('Content: %s', r.text)
		lines = r.text.strip().split('\n')
		elements = []
		output = {}
		d = {}
		for line in lines:
			if line == '[Term]' and len(elements) > 0:
				d = resolve_elements(elements)
				if 'id' in d and d['id'] == entry['dbxref']:
					output = format_output(d)
				else:
					d = {}
				elements = []
			else:
				elements.append(line.strip())
		d = resolve_elements(elements)
		if 'id' in d and d['id'] == entry['dbxref']:
			output = format_output(d)
		documents.append(output)
	print (json.dumps(documents))

def resolve_elements(es):
	dict = {}
	for element in es:
		if len(element) > 0:
			if element.split(': ')[0] in dict:
				dict[element.split(': ')[0]].append(element.split(': ')[1])
			else:
				dict[element.split(': ')[0]] = [element.split(': ')[1]]
	for key in dict.keys():
		if key != 'synonym' and len(dict[key]) == 1:
			dict[key] = dict[key][0]
	return (dict)

def format_output(d):
	out = {}
	if 'id' in d:
		out['dbxref'] = d['id']
	if 'def' in d:
		de = d['def'].split('" ')
		de = de[0].replace('"', '')
		de = de.replace('\\', '')
		out['definition'] = de
	else:
		out['definition'] = ""
	if 'name' in d:
		out['name'] = d['name'].replace('_', ' ')
	else:
		out['name'] = ""
	if 'namespace' in d:
		out['namespace'] = d['namespace']
	else:
		out['namespace'] = ""
	if 'is_a' in d:
		out['parent'] = d['is_a']
	else:
		out['parent'] = ""
	if 'synonym' in d:
		out['synonyms'] = []
		for synonym in d['synonym']:
			sy = synonym.split('" ')
			sy[0] = sy[0].replace('\\', '')
			sy[0] = sy[0].replace('"', '')
			sy[1] = sy[1].replace('[', '')
			sy[1] = sy[1].replace(']', '')
			sy[1] = sy[1].replace(' ', '')
			out['synonyms'].append({'name': sy[0], 'type': sy[1].lower()})
	return (out)

main()
