#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)

def main():
  """For script usage of this retriever"""
  parser = argparse.ArgumentParser(description='Retrieve taxonomy xml documents for dbxrefs and convert them into json')
  parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref, scientificName, commonName, lineage and rank')
  parser.add_argument('--geneticcodes', '-g', action='store_true', help='Include geneticCode and mitochondrialGeneticCode')
  parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
  args = parser.parse_args()

  # set default values
  if not args.basic and not args.geneticcodes:
    args.basic = True
    args.geneticcodes = True

  documents = retrieve(args.dbxrefs, basic=args.basic, geneticcodes=args.geneticcodes)
  print (json.dumps(documents))

def retrieve(dbxrefs, basic=True, geneticcodes=True):
  """Retrieve the data for the dbxrefs and return a list"""
  resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
  documents = []
  for entry in resolved:
    json_url = entry['locations']['json'][0]
    logger.debug('URL: %s', json_url)
    r = requests.get(json_url)
    logger.debug('Content: %s', r.text)
    output = {'id': entry['dbxref']}
    d = {}
    try:
      d = json.loads(r.text)
    except:
      pass 
    if len(d) > 0:
      if basic:
        output.update(read_basic(d))
      if geneticcodes:
        output.update(read_geneticCodes(d))
    else:
      output['message'] = "An error occurred! probably invalid ID"
    documents.append(output)
  return documents

def read_basic(d):
  out = {}
  if 'scientificName' in d:
    out['scientificName'] = d['scientificName']
  if 'commonName' in d:
    out['commonName'] = d['commonName']
  if 'lineage' in d:
    # the lineage string contains a ';' separated list, that is converted here
    # into a true list
    lineage_list = d['lineage'].split("; ")
    if not lineage_list[-1].strip():
      lineage_list = lineage_list[:-1]
    out['lineage'] = lineage_list
  if 'rank' in d:
    out['rank'] = d['rank']
  return (out)

def read_geneticCodes(d):
  out = {'geneticCodes': {}}
  if 'geneticCode' in d:
    out['geneticCodes']['geneticCode'] = d['geneticCode']
  if 'mitochondrialGeneticCode' in d:
    out['geneticCodes']['mitochondrialGeneticCode'] = d['mitochondrialGeneticCode']
  return (out)

if __name__ == '__main__':
  main()
