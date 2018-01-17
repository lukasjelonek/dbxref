def get_providers_path():
    import pkg_resources
    return pkg_resources.resource_filename('dbxref', 'providers.yaml')

def load_providers():
    import yaml
    data = []
    with open(get_providers_path()) as data_file:
        data = yaml.load(data_file)
    return index_providers(data)

def index_providers(providers):
    index = {}
    for p in providers:
        for db in p['prefixes']:
            index[db] = p
    return index
