#!/usr/bin/env python3
import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)

def main():
  parser = argparse.ArgumentParser(description='Retrieve gene ontology documents for dbxrefs and convert them into json')
  parser.add_argument('--basic', '-b', action='store_true', help='Include id, definition, name and synonyms')
  parser.add_argument('--relations', '-r', action='store_true', help='Include id, parents and children')
  parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
  args = parser.parse_args()
  if not args.basic and not args.relations:
    args.basic = True
    args.relations = False
  dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)

  documents = retrieve(dbxrefs, basic=args.basic, relations=args.relations)
  print(json.dumps(documents))

def retrieve(dbxrefs, basic=True, relations=False):
  resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
  documents = []
  for entry in resolved:
    json_url = entry['locations']['json'][0]
    logger.debug('URL: %s', json_url)
    r = requests.get(json_url)
    logger.debug('Content: %s', r.text)
    d = json.loads(r.text)
    output = {'id': entry['dbxref']}
    if 'messages' in d:
      output['message'] = '; '.join(d['messages'])
    else:
      if len(d['results']) > 0:
        if basic:
          output.update(read_basic(d))
        if relations:
          output.update(read_relations(d))
      else: 
        output['message'] = "no results found, probably invalid ID"
    documents.append(output)
  return documents

def read_basic(d):
    out = {'definition': d['results'][0]['definition']['text'], 'synonyms': []}
    out['name'] = d['results'][0]['name']
    if 'aspect' in d['results'][0]:
      out['aspect'] = d['results'][0]['aspect']
    if 'synonyms' in d['results'][0]:
      out['synonyms'] = d['results'][0]['synonyms']
    return (out)

def read_relations(d):
  out = {'relations': {'children': [], 'parents': []}}
  if 'children' in d['results'][0]:
    out['relations']['children'] = d['results'][0]['children']
    for child in out['relations']['children']:
      child['type'] = child.pop('relation')
  if 'history' in d['results'][0]:
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

if __name__ == '__main__':
  main()
