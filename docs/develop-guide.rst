Developer Guide
===============

Document structures
-------------------

Return JSON of dbxref commands
##############################

dbxref returns json lists. Each entry in the list is a json object with at
least the 'id' property. Additional properties should be the same for similar
databases. For example most of the databases will contain a free text
description of the entry which should be available via the 'description'
property. Each database may have it's unique fields. These can be named as
required.

Resolve command
###############

Returns a list of json objects. Each object contains the id and locations.
Locations is an object that provides the urls to the different file formats
available for the entry. Valid formats are: 'html', 'xml', 'json', 'text'. If
you need additional formats, feel free to add them. Each format is a property
on the object and contains a list of all available urls. If a format is not
available for an entry, it should not be present in the locations object.


Handling of non existent dbxrefs
###############################

The proposed format for entries that cannot be found in the databases is as following:

`
[{'id': '<db>:<id>', "message": "no results found; probably invalid ID"}]
`

Handling of webservice errors
#############################

Try to be as precise as possible when an error occurs. The default (unprecise) response should be

`
[{'id': '<db>:<id>', "message": "Could not retrieve the requested entry due to problems."}]
`

You can include the original reponse:

`
[{'id': '<db>:<id>', "message": "Could not retrieve the requested entry due to problems.", "response" : "<original reponse>"}]
`

