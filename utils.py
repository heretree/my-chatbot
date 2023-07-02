import yaml

def get_api_keys(filename):
    with open(filename, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as error:
            print(f"Error reading YAML file: {error}")
            raise Exception("can't load keys from {}".format(filename))
    return data