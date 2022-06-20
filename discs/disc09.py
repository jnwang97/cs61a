class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    sum_lnk = 0
    while lnk is not Link.empty:
        sum_lnk += lnk.first
        lnk = lnk.rest
    return sum_lnk

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    if Link.empty in lst_of_lnks:
        return Link.empty
    else:
        product = 1
        for link in lst_of_lnks:
            product *= link.first
        return Link(product, multiply_lnks([link.rest for link in lst_of_lnks]))


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.is_leaf():
        if t.label % 2 == 1:
            t.label += 1
    else:
        if t.label % 2 == 1:
            t.label += 1
        for b in t.branches:
            make_even(b)


def square_tree(t):
    if t.is_leaf():
        t.label = t.label ** 2
    else:
        t.label = t.label ** 2
        for b in t.branches:
            square_tree(b)


def find_path(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    def has_value(tree, v):
        if tree.label == v:
            return True
        else:
            state = False
            for branch in tree.branches:
                if has_value(branch, v):
                    state = True
            return state
    if not has_value(t, entry):
        return False
    else:
        path = []
        if t.is_leaf():
            path.append(t.label)
        else:
            path.append(t.label)
            for b in t.branches:
                if has_value(b, entry):
                    path += find_path(b, entry)
        return path


def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            total_next, count_next = sum_helper(b)
            total += total_next
            count += count_next
        return total, count
    total, count = sum_helper(t)
    return total / count


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    b_com = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), b_com)


def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    map_fn(t.label)
    for b in t.branches:
        for sub_b in b.branches:
            map_fn(sub_b.label)

