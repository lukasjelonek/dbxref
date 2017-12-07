#!/usr/bin/env python3

import env
import dbxref.config
import dbxref.resolver
import requests
import logging
import json
import argparse
import re
import lxml.html as HTML

logger = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser(description='Retrieve enzyme text documents for dbxrefs and convert them into json')
	parser.add_argument('--basic', '-b', action='store_true', help='Include id, definition, name and synonyms')
	parser.add_argument('--references', '-r', action='store_true', help='Include id, uniprot dbxrefs')
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
		ls = r.text.replace('\n', ' ')
		try:
			html = HTML.document_fromstring(ls).head.text_content()
			output['message'] = html
			if output['message'] == ' 500 Internal Server Error ':
				output['message'] = '500 Internal Server Error; probably invalid ID'
		except:
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
							if 'reaction_catalyzed' in output:
								output['reaction_catalyzed'].append(reaction)
							else:
								output['reaction_catalyzed'] = [reaction]
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
								refs.append('UniProtKB/Swiss-Prot:' + l[0])
				output['dbxrefs'] = refs
			if len(reaction) > 0:
				if 'reaction_catalyzed' in output:
					output['reaction_catalyzed'].append(reaction)
				else:
					output['reaction_catalyzed'] = [reaction]
			if len(comment) > 0:
				if 'comments' in output:
					output['comments'].append(comment)
				else:
					output['comments'] = [comment]
		documents.append(format_output(output, args))
	print(json.dumps(documents))

def read_basic(d):
	out = {}
	definition = {}
	if 'message' in d:
		out['message'] = d['message']
	if 'name' in d:
		out['name'] = d['name']
	if 'alternative_names' in d:
		out['synonyms'] = d.pop('alternative_names')
	if 'reaction_catalyzed' in d:
		definition['reaction_catalyzed'] = d['reaction_catalyzed']
	if 'cofactors' in d:
		definition['cofactors'] = d['cofactors']
	if 'comments' in d:
		definition['comments'] = d['comments']
	if len(definition) == 1:
		out['deifinition'] = definition[0]
	elif len(definition) > 1:
		out['deifinition'] = definition
	return (out)

def format_output(d, args):
	out = {'id': d['dbxref']}
	if args.basic:
		out.update(read_basic(d))
	if args.references:
		out['dbxrefs'] = d['dbxrefs']
	if not args.basic and not args.references:
		out.update(read_basic(d))
		if 'dbxrefs' in d:
			out['dbxrefs'] = d['dbxrefs']
	return (out)

main()
