def get_install_location():
    """Finds the location directory of the tool"""
    import os
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    install_dir = os.path.dirname(script_dir)
    return install_dir

def load_providers():
    import yaml
    data = []
    with open(get_install_location() + '/providers.yaml') as data_file:
        data = yaml.load(data_file)
    return index_providers(data)

def index_providers(providers):
    index = {}
    for p in providers:
        for db in p['prefixes']:
            index[db] = p
    return index
