#!/usr/bin/env python3

import env
import dbxref.config
import dbxref.resolver
import requests
import logging
import json
import argparse
import re

logger = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser(description='Retrieve enzyme text documents for dbxrefs and convert them into json')
	parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref, definition, name and synonyms')
	parser.add_argument('--references', '-r', action='store_true', help='Include uniprot dbxrefs')
	parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
	documents = []
	for entry in resolved:
		txt_url = entry['locations']['text'][0]
		logger.debug('URL: %s', txt_url)
		r = requests.get(txt_url)
		logger.debug('Content: %s', r.text)
		lines = r.text.split('\n')
		output = {'dbxref': entry['dbxref']}
		refs = []
		comment = ""
		reaction = ""
		for line in lines:
			line_elements = line.strip().split('   ')
			if line_elements[0] == 'DE':
				output['name'] = line_elements[1]
			if line_elements[0] == 'AN':
				if 'alternative_names' in output:
					output['alternative_names'].append(line_elements[1])
				else:
					output['alternative_names'] = [line_elements[1]]
			if line_elements[0] == 'CA':
				if re.match(re.compile('^\(\d+\) '), line_elements[1]):
					if len(reaction) == 0:
						reaction += line_elements[1][line_elements[1].find(' ')+1:]
					else:
						if 'reaction_catalysed' in output:
							output['reaction_catalysed'].append(reaction)
						else:
							output['reaction_catalysed'] = [reaction]
						reaction = line_elements[1][line_elements[1].find(' ')+1:]
				else:
					if len(reaction) == 0:
						reaction = line_elements[1]
					else:
						reaction = reaction + " " + line_elements[1]
			if line_elements[0] == 'CF':
				if 'cofactors' in output:
					output['cofactors'].append(line_elements[1])
				else:
					output['cofactors'] = [line_elements[1]]
			if line_elements[0] == 'CC':
				if "-!-" in line_elements[1]:
					if len(comment) == 0:
						comment += line_elements[1][4:]
					else:
						if 'comments' in output:
							output['comments'].append(comment)
						else:
							output['comments'] = [comment]
						comment = line_elements[1][4:]
				else:
					comment += line_elements[2]
			if line_elements[0] == 'PR':
				link = line_elements[1].replace(';', '').split()
				if 'prosite' in output:
					output['prosite'].append(link[1])
				else:
					output['prosite'] = [link[1]]
			if line_elements[0] == 'DR':
				for i in range(1, len(line_elements)):
					for e in line_elements[i].split(';  '):
						if len(e) > 1:
							l = e.split(', ')
							l[1] = l[1].replace(' ', '')
							l[1] = l[1].replace(';', '')
							refs.append(l[0])
			if len(refs) > 0:
				output['uniprot'] = refs
		if len(reaction) > 0:
			if 'reaction_catalysed' in output:
				output['reaction_catalysed'].append(reaction)
			else:
				output['reaction_catalysed'] = [reaction]
		if len(comment) > 0:
			if 'comments' in output:
				output['comments'].append(comment)
			else:
				output['comments'] = [comment]
		documents.append(format_output(output, args))
	print(json.dumps(documents))

def format_output(d, args):
	out = {'dbxref': d['dbxref']}
	definition = {}
	if args.basic:
		if 'name' in d:
			out['name'] = d['name']
		if 'alternative_names' in d:
			out['synonyms'] = d.pop('alternative_names')
		if 'reaction_catalysed' in d:
			definition['reaction_catalysed'] = d['reaction_catalysed']
		if 'cofactors' in d:
			definition['cofactors'] = d['cofactors']
		if 'comments' in d:
			definition['comments'] = d['comments']
		if len(definition) == 1:
			out['deifinition'] = definition[0]
		elif len(definition) > 1:
			out['deifinition'] = definition
	if 'uniprot' in d and args.references:
		out['uniprot'] = d['uniprot']
	return (out)

main()
