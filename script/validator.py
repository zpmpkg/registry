from jsonschema import validate
import glob
import yaml
import json
import sys
import os


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    root = os.path.join(path, "../")

    for f in glob.glob(root + "*.schema"):
        with open(f, 'r') as s:
            schema = json.load(s)

        file = os.path.splitext(f)[0]
        for g in ["yml", "yaml", "json"]:
            val_file = "{}.{}".format(file, g)
            if os.path.isfile(val_file):
                with open(val_file, 'r') as stream:
                    validate(yaml.load(stream), schema)

    for (f, s) in [
        ("modules.json", "schema/registry.json"),
        ("registry.json", "schema/registry.json"),
        ("registries.json", "schema/registries.json")]:
        with open(s, 'r') as s:
            schema = json.load(s)
            with open(f, 'r') as stream:
                validate(json.load(stream), schema)


if __name__ == "__main__":
    main()
