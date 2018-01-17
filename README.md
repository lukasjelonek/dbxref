# DB XREF resolver and retriever tool

A tool that resolves database cross references (dbxrefs). It can return a list of
locations where the cross reference points to in different formats, like HTML,
XML, flat file or json. It can also retrieve the data for some of the supported
databases and convert it into json.

The intended audience for this tool are bioinformatician that need to collect
data for dbxrefs and postprocess it. By returning everything in json format the
need for normalization and special parsing of the data is reduced.

# Getting started for development (Setup)

Prerequisites:

* git
* python3

Supported bioinformatic databases:

* Ontologies
  * Gene Ontology

Checkout the repository:

~~~~
git clone git@git.computational.bio.uni-giessen.de:SOaAS/dbxref.git
~~~~

Setup a virtualenv for development and install it in editable mode:

~~~~
virtualenv --python=python3 venv; source venv/bin/activate;
pip install -e .
~~~~

Use the application:

~~~~
dbxref resolve GO:0097281
~~~~
