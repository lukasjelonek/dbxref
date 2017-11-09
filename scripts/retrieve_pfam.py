#!/usr/bin/env python3
import env
import dbxref.config
import dbxref.resolver
import requests
import xml.etree.ElementTree as ET
import logging
import json
import argparse
#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger().setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

ns = {'pfam': 'http://pfam.xfam.org/'}

def main():
    parser = argparse.ArgumentParser(description='Retrieve pfam xml documents for dbxrefs and convert them into json')
    parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref and description')
    parser.add_argument('--annotation', '-a', action='store_true', help='Include annotation')
    parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not (args.basic or args.annotation):
        args.basic = True
        args.annotation = True
    resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        xml_url = entry['locations']['xml'][0]
        logger.debug('URL: %s', xml_url)
        r = requests.get(xml_url)
        logger.debug('Content: %s', r.text)
        root = ET.fromstring(r.text)

        output = {'dbxref': entry['dbxref']}

        for child in root.findall('pfam:entry', ns):
            if args.basic:
                output.update(read_basic(child))
            if args.annotation:
                output.update(read_annotation(child))
        documents.append(output)
    print(json.dumps(documents))

    
def read_basic(entry):
    description = entry.find('pfam:description', ns).text.strip()
    return {'description': description}

def read_annotation(entry):
    annotation = {
            'id': entry.attrib['id'],
            'accession': entry.attrib['accession'],
            'terms' : [],
            'comment': entry.find('pfam:comment', ns).text.strip()
            }
    go_terms = entry.find('pfam:go_terms', ns)
    categories = go_terms.findall('pfam:category', ns)
    for category in categories:
        terms = category.findall('pfam:term', ns)
        for term in terms:
            annotation['terms'].append({
                'id': term.attrib['go_id'], 
                'description': term.text 
                })
    return annotation

main()
