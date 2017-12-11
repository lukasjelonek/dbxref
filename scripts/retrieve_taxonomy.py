#!/usr/bin/env python3

import env
import dbxref.config
import dbxref.resolver
import requests
import xml.etree.ElementTree as ET
import logging
import json
import argparse

logger = logging.getLogger(__name__)
ns = {'TaxaSet': 'https://eutils.ncbi.nlm.nih.gov/'}

def main():
	parser = argparse.ArgumentParser(description='Retrieve taxonomy xml documents for dbxrefs and convert them into json')
	parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref and ......................')
	parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
	documents = []
	for entry in resolved:
		xml_url = entry['locations']['xml_ncbi'][0]
		logger.debug('URL: %s', xml_url)
		r = requests.get(xml_url)
		logger.debug('Content: %s', r.text)
		root = ET.fromstring(r.text)

		output = {'id': entry['dbxref']}
		error = root.find('ERROR')
		if error is not None:
			output['message'] = error.text.strip()
		else:
			for child in root.findall('Taxon'):
				output['name'] = child.find('ScientificName').text.strip()
				lineage = child.find('Lineage')
				if lineage.text is not None:
					output['lineage'] = lineage.text.strip()
				else:
					output['lineage'] = 'No lineage found'
		if 'name' not in output and 'message' not in output:
			output['message'] = 'No entries found! Possibly invalid ID provided'
		documents.append(output)
	print (json.dumps(documents))

main()
