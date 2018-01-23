def get_providers_path():
    import pkg_resources
    return pkg_resources.resource_filename('dbxref', 'providers.yaml')

def load_providers():
    return _load_providers(get_providers_path())

def _load_providers(path):
    import yaml
    data = []
    with open(path) as data_file:
        data = yaml.load(data_file)
    return normalize_index(index_providers(data))

def index_providers(providers):
    index = {}
    for p in providers:
        for db in p['prefixes']:
            index[db] = p
    return index

def normalize_index(index):
    'create a new index with lowercase keys'
    return {k.lower():v for (k,v) in index.items()}

def has_provider(provider):
    return _has_provider(load_providers(), provider)

def _has_provider(providers, provider):
    return provider.lower() in providers

def get_provider(provider):
    return load_providers()[provider.lower()]
