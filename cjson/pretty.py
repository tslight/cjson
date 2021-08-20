def pplist(l, indent=0, tree=""):
    for e in l:
        if isinstance(e, dict):
            tree += ppdict(e, indent, tree)
        elif isinstance(e, list):
            tree += pplist(e, indent+4, tree)
        else:
            tree += (' ' * indent + str(e) + '\n')
    return tree


def ppdict(d, indent=0, tree=""):
    for key, value in d.items():
        tree += (' ' * indent + str(key))
        if isinstance(value, dict):
            tree += ppdict(value, indent+4, tree)
        elif isinstance(value, list):
            tree += pplist(value, indent+4, tree)
        else:
            tree += (' ' * (indent+4) + str(value) + '\n')
    return tree
