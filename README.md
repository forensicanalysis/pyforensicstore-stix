pyforensicstore-stix
====================

This package bundles the official STIX 2 schema repo and convert it to a python package that
can then be accessed by querying for entrypoints called `forensicstore_schemas`.

A minimal usage example can be seen below. The example assumes the package is installed 
in the environment:

```python
import pkg_resources

def get_schemas():
    schemas = {}
    for entry_point in pkg_resources.iter_entry_points('forensicstore_schemas'):
        print("Trying to load", entry_point)
        schemas[entry_point.name] = entry_point.load()
    return schemas


if __name__ == '__main__':
    schemas = get_schemas()
    print("keys:", schemas.keys())
    print("file:", schemas['file'])
    print("kill-chain-phase:", schemas['kill-chain-phase'])
```
