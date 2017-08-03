import tests.env
import unittest
from dbxref import resolver

class TestDbxrefResolve(unittest.TestCase):

    def test_conversion_of_string_to_dbxref(self):

        data = [
                ('GO:1234', {'db': 'GO', 'id': '1234'}),
                ('https://www.google.de', {'db': 'https', 'id': '//www.google.de'}),
                ('db:sub:id', {'db': 'db', 'id': 'sub:id'}),
                
                ]
        for d in data:
            with self.subTest(d=d):
                self.assertEqual(resolver.convert_string_to_dbxref(d[0]), d[1])


    def test_resolve_enzyme(self):
        self.assertNotEqual(resolver.resolve(["EC:1.1.1.1"]), [])

    def test_check_dbxref_exists(self):
        import logging
        from dbxref.resolver import FOUND, NOT_FOUND, UNSUPPORTED
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.WARNING)
        resolver.logger.setLevel(logging.DEBUG)
        data = [
                # existent ids
                ('GO:0097281', FOUND),
                ('EC:1.1.1.1', FOUND),
                ('UniProtKB/Swiss-Prot:P12345', FOUND),
                ('UniProtKB/TrEMBL:A2VB99', FOUND),
                ('taxon:452271', FOUND),
                ('pubmed:19037750', FOUND),
                ('PDB:4AJY', FOUND),
                ('http://www.google.de', FOUND),
                ('https://www.google.de', FOUND),

                # non existent ids
                ('GO:123', NOT_FOUND),
                ('EC:hoho', NOT_FOUND),
                ('UniProtKB/Swiss-Prot:45', NOT_FOUND),
                ('UniProtKB/TrEMBL:99', NOT_FOUND),
                ('taxon:hoho', NOT_FOUND),
                ('pubmed:hoho', NOT_FOUND),
                ('PDB:hoho', NOT_FOUND),
                ('http://wurst', NOT_FOUND),
                ('https://wurst', NOT_FOUND),

                # currently unsupported
                #('GeneID:956582', FOUND),
                #('GI:731497', FOUND),
                #('PFAM:PF00002', FOUND),
                #('RFAM:RF00360', FOUND),
                #('InterPro:IPR002928', FOUND),
                #('SO:0000704', FOUND),

                #('InterPro:hoho', NOT_FOUND),
                #('GI:hoho', NOT_FOUND),
                #('GeneID:hoho', NOT_FOUND),
                #('PFAM:hoho', NOT_FOUND),
                #('RFAM:hoho', NOT_FOUND),
                #('SO:123', NOT_FOUND),
                ]

        for d in data:
            with self.subTest(d=d):
                self.assertEqual(resolver.check_dbxref_exists(d[0]), d[1] )

    def test_check_urls(self):
        import json
        data = '[]'
        data3 = '[{"locations": [{"type": "xml", "url": "http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:1234&format=oboxml"}, {"type": "html", "url": "http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:1234"}], "dbxref": "GO:1234"},{"dbxref": "UniProtKB/Swiss-Prot:P12345", "locations": [{"url": "http://www.uniprot.org/uniprot/P12345.xml", "type": "xml"}, {"url": "http://www.uniprot.org/uniprot/P12345", "type": "html"}]}, {"dbxref": "UniProtKB/TrEMBL:A2VB99", "locations": [{"url": "http://www.uniprot.org/uniprot/A2VB99.xml", "type": "xml"}, {"url": "http://www.uniprot.org/uniprot/A2VB99", "type": "html"}]}, {"dbxref": "taxon:452271", "locations": [{"url": "http://www.uniprot.org/taxonomy/452271.rdf", "type": "xml"}, {"url": "http://www.uniprot.org/taxonomy/452271", "type": "html"}]}, {"dbxref": "SO:0000704", "locations": [{"url": "http://www.sequenceontology.org/browser/current_svn/term/SO:0000704", "type": "html"}]}, {"dbxref": "RFAM:RF00360", "locations": [{"url": "http://rfam.xfam.org/family/RF00360?content-type=text%2Fxml", "type": "xml"}, {"url": "http://rfam.xfam.org/family/RF00360", "type": "html"}]}, {"dbxref": "pubmed:19037750", "locations": [{"url": "http://www.ncbi.nlm.nih.gov/pubmed/19037750", "type": "html"}]}, {"dbxref": "PFAM:PF00002", "locations": [{"url": "http://pfam.xfam.org/family/PF00002", "type": "html"}]}, {"dbxref": "PDB:4AJY", "locations": [{"url": "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=xml&compression=NO&structureId=4AJY", "type": "xml"}, {"url": "http://www.rcsb.org/pdb/explore/explore.do?structureId=4AJY", "type": "html"}]}, {"dbxref": "InterPro:IPR002928", "locations": [{"url": "http://www.ebi.ac.uk/interpro/entry/IPR002928", "type": "html"}]}, {"dbxref": "http://www.google.de", "locations": [{"url": "http://www.google.de", "type": "html"}]}, {"dbxref": "https://www.google.de", "locations": [{"url": "https://www.google.de", "type": "html"}]}, {"dbxref": "GeneID:956582", "locations": [{"url": "http://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&db=gene&dopt=xml&sort=&val=956582&retmode=file", "type": "xml"}, {"url": "http://www.ncbi.nlm.nih.gov/gene/956582", "type": "html"}]}, {"dbxref": "GO:0097281", "locations": [{"url": "http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0097281&format=oboxml", "type": "xml"}, {"url": "http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0097281", "type": "html"}]}, {"dbxref": "GI:731497", "locations": [{"url": "http://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&db=protein&dopt=xml&sort=&val=731497&retmode=file", "type": "xml"}, {"url": "http://www.ncbi.nlm.nih.gov/protein/GI:731497", "type": "html"}]}, {"dbxref": "EC:1.1.1.1", "locations": [{"url": "http://enzyme.expasy.org/EC/1.1.1.1", "type": "html"}]}]'
        data = json.loads(data3)
        #resolver.check_urls(data)
        

