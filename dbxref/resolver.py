def resolve(strings):
    from dbxref.config import load_providers
    # read providers.json
    providers = load_providers()
    results = []
    for s in strings:
        dbxref = convert_string_to_dbxref(s)
        if dbxref['db'] in providers:
            provider = providers[dbxref['db']]
            urls = []
            for r in provider['resources']:
                for url_template in provider['resources'][r]:
                    urls.append( {
                        'type': r,
                        'url': url_template.replace('%i', dbxref['id']).replace('%d', dbxref['db'])
                        } ) 
            results.append({'dbxref': dbxref['db'] + ':' + dbxref['id'], 'locations': urls})
        else:
            print("No provider found")
    return results

def convert_string_to_dbxref(string):
    """
    A dbxref is dictionary with two keys: db and id.
    """
    split = string.split(':', 1)
    return {'db': split[0], 'id': split[1]}
