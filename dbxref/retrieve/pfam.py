#!/usr/bin/env python3
import dbxref.resolver
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import logging
import json
import argparse
#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger().setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

ns = {'pfam': 'https://pfam.xfam.org/'}

def main():
    parser = argparse.ArgumentParser(description='Retrieve pfam xml documents for dbxrefs and convert them into json')
    parser.add_argument('--basic', '-b', action='store_true', help='Include dbxref and description')
    parser.add_argument('--annotation', '-a', action='store_true', help='Include annotation')
    parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not (args.basic or args.annotation):
        args.basic = True
        args.annotation = True
    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)

    documents = retrieve(dbxrefs, basic=args.basic, annotation=args.annotation)
    print(json.dumps(documents))

def retrieve(dbxrefs, basic=True, annotation=True):
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
      if 'xml' in entry['locations']:
        xml_url = entry['locations']['xml'][0]
        logger.debug('URL: %s', xml_url)
        r = requests.get(xml_url)
        logger.debug('Content: %s', r.text)

        output = {'id': entry['dbxref']}

        try:
          root = ET.fromstring(r.text)

          tree = str(ET.tostring(root))
          if '<error>' in tree:
               output['message'] = tree[tree.find('<error>')+7:tree.rfind('</error>')]
          else:
              for child in root.findall('pfam:entry', ns):
                  if basic:
                      output.update(read_basic(child))
                  if annotation:
                      output.update(read_annotation(child))
        except (KeyError, AttributeError) as e:
            logger.warn('Error in retrieving %s', str(entry))
            raise
        except (ParseError, RuntimeError) as e:
            output['message'] = 'an error occurred'
            try:
                html = HTML.document_fromstring(r.text.replace('\n', ' '))
                if html.get_element_by_id('noResultsMessage') is not None:
                    output['message'] = 'no results found; probably invalid ID'
            except:
                pass
        documents.append(output)
    return documents

def read_basic(entry):
    description = entry.find('pfam:description', ns).text.strip()
    return {'description': description}

def read_annotation(entry):
    annotation = {
            'domain': entry.attrib['id'],
            'accession': entry.attrib['accession'],
            'terms' : []
            }

    comment = entry.find('pfam:comment', ns)
    if comment:
      annotation['comment'] = comment.text.strip()

    go_terms = entry.find('pfam:go_terms', ns)
    if go_terms:
      categories = go_terms.findall('pfam:category', ns)
      for category in categories:
          terms = category.findall('pfam:term', ns)
          for term in terms:
              annotation['terms'].append({
                  'id': term.attrib['go_id'],
                  'description': term.text
                  })
    return annotation

if __name__ == "__main__":
  main()
