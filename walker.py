from types import DictionaryType, ListType

def tree_walker(ds_tree, f):
    for key, node in ds_tree.values():
        ds_walker(node, f)

def iter_walker(ds_iter, f):
    for node in ds_iter:
        ds_walker(node, f)

def walker(ds, f):
    if isinstance(ds, DictionaryType):
        return tree_walker(ds, f)
    elif isinstance(ds, ListType):
        return list_walker(ds, f)

