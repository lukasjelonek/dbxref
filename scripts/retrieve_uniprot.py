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

ns = {'uniprot': 'http://uniprot.org/uniprot'}

def main():
    parser = argparse.ArgumentParser(description='Retrieve uniprot xml documents for dbxrefs and convert them into json')
    parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref and description')
    parser.add_argument('--sequence', '-s', action='store_true', help='Include sequence')
    parser.add_argument('--organism', '-o', action='store_true', help='Include organism info')
    parser.add_argument('--annotation', '-a', action='store_true', help='Include annotation')
    parser.add_argument('--features', '-f', action='store_true', help='Include features (NOT IMPLEMENTED YET)')
    parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if not (args.basic or args.sequence or args.organism or args.annotation or args.features):
        args.basic = True
        args.sequence = True
        args.organism = True
        args.annotation = True
        args.features = True
    resolved = dbxref.resolver.resolve(args.dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        xml_url = entry['locations']['xml'][0]
        logger.debug('URL: %s', xml_url)
        r = requests.get(xml_url)
        logger.debug('Content: %s', r.text)
        root = ET.fromstring(r.text)

        output = {'id': entry['dbxref']}

        for child in root.findall('uniprot:entry', ns):
            if args.basic:
                output.update(read_basic(child))
            if args.sequence:
                output.update(read_sequence(child))
            if args.organism:
                output.update(read_taxonomy(child))
            if args.annotation:
                output.update(read_annotation(child))
            if args.features:
                output.update(read_features(child))
        documents.append(output)
    print(json.dumps(documents))

    
def read_basic(entry):
    protein = entry.find('uniprot:protein', ns)
    recname = protein.find('uniprot:recommendedName', ns)
    fullName = recname.find('uniprot:fullName', ns).text
    shortName = recname.find('uniprot:shortName', ns)

    if shortName is not None:
        return {'description': fullName + '(' + shortName.text + ')'}
    else:
        return {'description': fullName }

def read_sequence(entry):
    sequence = entry.find('uniprot:sequence', ns).text
    # remove whitespaces
    sequence = ''.join(sequence.split())
    return {'sequence': sequence}

def read_taxonomy(entry):
    organism = entry.find('uniprot:organism', ns)
    taxid = organism.find('uniprot:dbReference', ns).attrib
    return {'organism': 'Taxon:' + taxid['id'] }

def read_annotation(entry):
    annotation = {
            'accessions': read_accessions(entry),
            'dbxrefs' : read_dbrefs(entry), 
            'keywords': read_keywords(entry)
            }
    annotation.update(read_names(entry))
    return annotation

def read_dbrefs(entry):
    dbrefs = entry.findall('uniprot:dbReference', ns)
    refs = []
    for dbref in dbrefs:
        type = dbref.attrib['type']
        id = dbref.attrib['id']
        if type == 'GO':
            id = id.split(':')[1]
        refs.append(type + ':' + id)
    return refs

def read_names(entry):
    protein = entry.find('uniprot:protein', ns)
    recname = protein.find('uniprot:recommendedName', ns)
    recommended_name = {
            'full' : recname.find('uniprot:fullName', ns).text, 
            }
    short = recname.find('uniprot:shortName', ns)
    if short is not None:
        recommended_name['short'] = short.text
    alternative_names = []
    altnames = protein.findall('uniprot:alternativeName', ns)
    for altname in altnames:
        alternative_name = {'full': altname.find('uniprot:fullName', ns).text}
        short = altname.find('uniprot:shortName', ns)
        if short is not None:
            alternative_name['short'] = short.text
        alternative_names.append(alternative_name)
    return { 
            'recommended_name': recommended_name,
            'alternative_names': alternative_names
           }

def read_accessions(entry):
    accessions = []
    for acc in entry.findall('uniprot:accession', ns):
        accessions.append(acc.text)
    return accessions

def read_keywords(entry):
    keywords = []
    for kw in entry.findall('uniprot:keyword', ns):
        keywords.append(kw.text)
    return keywords

def read_features(entry):
    return {}

main()
