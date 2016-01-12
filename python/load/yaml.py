import yaml


def load_file(file):
    with open(file) as f:
        document = yaml.load(f)
    return document
