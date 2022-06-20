def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ... print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    subset = [[]]
    n = 1
    while True:
        yield subset
        subset = subset + [s + [n] for s in subset]
        n += 1


def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if t.is_leaf():
        yield t.label
    for b in t.branches:
        for s in sum_paths_gen(b):  # indicating s in a value here
            yield t.label + s


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches
