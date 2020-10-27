DB XREF resolver and retriever tool
===================================

A tool that resolves database cross references (dbxrefs). It can return a list of
locations where the cross reference points to in different formats, like HTML,
XML, flat file or json. It can also retrieve the data for some of the supported
databases and convert it into json.

The intended audience for this tool are bioinformatician that need to collect
data for dbxrefs and postprocess it. By returning everything in json format the
need for normalization and special parsing of the data is reduced.

Getting started for development (Setup)
---------------------------------------

Prerequisites:

* git
* python3

Supported databases:

* Enzyme
* Gene Identifier
* Uniprot
* Taxonomy
* SequenceOntology
* RFAM
* Pubmed
* Protein Families
* PDB
* InterPro
* GeneID
* Gene Ontology
* HTTP


Checkout the repository::

    git clone git@git.computational.bio.uni-giessen.de:SOaAS/dbxref.git

Setup a virtualenv for development and install it in editable mode::

    # install in development environment
    virtualenv --python=python3 venv; source venv/bin/activate;
    pip install -e .

    # run tests
    python3 setup.py test

    # compile documentation
    python3 setup.py build_sphinx

Use the application::

    dbxref resolve GO:0097281

Use it as a library::

    # resolve urls for an entry
    from dbxref import resolver
    resolver.resolve([{'db': 'taxid', 'id': '12345'}])
    
    # => [{'dbxref': 'taxid:12345', 'locations': {'json': ['https://www.ebi.ac.uk/ena/data/taxonomy/v1/taxon/tax-id/12345'], 'xml_ncbi': ['https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=12345'], 'xml': ['http://www.uniprot.org/taxonomy/12345.rdf'], 'html': ['http://www.uniprot.org/taxonomy/12345']}, 'status': 'found'}]

    # retrieve an entry
    from dbxref import retriever
    retriever.retrieve([{'db':'taxid', 'id': '12345'}])

    # => [{'geneticCodes': {'geneticCode': '11'}, 'scientificName': 'Bacillus virus GA1', 'lineage': ['Viruses', 'Duplodnaviria', 'Heunggongvirae', 'Uroviricota', 'Caudoviricetes', 'Caudovirales', 'Podoviridae', 'Picovirinae', 'Salasvirus'], 'id': 'taxid:12345', 'rank': 'species'}]

