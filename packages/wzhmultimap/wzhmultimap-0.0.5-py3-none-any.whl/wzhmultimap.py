from collections import defaultdict


class multimap(defaultdict):
    """The Multimap in Python.

    >>> issubclass(multimap, defaultdict)
    True
    """

    def __init__(self):
        """Ctor (Initializer).

        >>> multimap().default_factory
        <class 'set'>
        """
        super().__init__(set)

    def count(self, key):
        """Return the number of values of the given key.

        >>> mp = multimap()
        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> mp.count("foo")
        3
        >>> mp.count(0xfeed)
        2
        >>> mp.count("lorem")
        0
        """
        return len(self[key])

    def keys(self):
        """Return a set contained the keys of the multimap.

        >>> mp = multimap()
        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> mp.keys() == {"foo", 0xfeed}
        True

        >>> mp["foo"] = set()
        >>> mp.keys() == {"foo", 0xfeed}
        False
        >>> mp.keys() == {0xfeed}
        True

        >>> del mp[0xfeed]
        >>> mp.keys()
        set()
        """
        res = set()
        rm = set()
        for k in super().keys():
            if self.count(k) == 0:
                rm.add(k)
            else:
                res.add(k)
        for k in rm:
            del self[k]
        return res

    def values(self):
        """Return the uniqued set of all the values in the multimap.

        >>> mp = multimap()
        >>> mp.values()
        set()

        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> mp.values() == {"bar", "baz", 0xcafe, 998244353}
        True
        """
        res = set()
        for k in self.keys():
            res.update(self[k])
        return res

    def items(self):
        """Return a set contained all the k-v tuples of the multimap.

        >>> mp = multimap()
        >>> mp.items()
        set()

        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> mp.items() == {("foo", "bar"), ("foo", "baz"), ("foo", 0xcafe), \
            (0xfeed, 998244353), (0xfeed, "baz")}
        True
        """
        res = set()
        for k in self.keys():
            for v in self[k]:
                res.add((k, v))
        return res

    def __str__(self):
        """Stringify the multimap.

        >>> mp = multimap()
        >>> str(mp)
        'multi{}'

        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> ''.join(sorted(str(mp))) # This is the only way to test it.
        "         '''''''''''',,,,111222334455556666668999:::::aaabbbfffilmoooooortuzz{}"
        """
        if self:
            res = "multi{"
            for k in self.keys():
                for v in self[k]:
                    res += repr(k) + ": " + repr(v) + ", "
            return res[:-2] + "}"
        else:
            return "multi{}"

    __repr__ = __str__

    def __len__(self):
        """Return the number of k-v tuples in the multimap.

        >>> mp = multimap()
        >>> len(mp)
        0

        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> len(mp)
        5
        """
        res = 0
        for k in self.keys():
            res += len(self[k])
        return res

    def __bool__(self):
        """Return whether the multimap is empty.

        >>> mp = multimap()
        >>> bool(mp)
        False

        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> bool(mp)
        True

        >>> mp["foo"] = set()
        >>> mp[0xfeed] = set()
        >>> bool(mp)
        False
        """
        return len(self.keys()) != 0

    __nonzero__ = __bool__

    def insert(self, key, *value):
        """Add some values of a key to the multimap.

        >>> mp = multimap()
        >>> mp.insert("foo", "bar", "baz", 0xcafe)
        >>> mp.insert(0xfeed, 998244353, "baz")
        >>> mp.items() == {(0xfeed, 998244353), (0xfeed, "baz"), \
            ("foo", "bar"), ("foo", "baz"), ("foo", 0xcafe)}
        True
        """
        if value != []:
            self[key] |= set(value)

    def erase(self, key, *value):
        """Remove some values of a key from the multimap.

        >>> mp = multimap()
        >>> mp["foo"] = {"baz", "bar", 0xcafe}
        >>> mp[0xfeed] = {998244353, "baz"}
        >>> mp.erase("foo", 998244353, "bar")
        >>> mp.items() == {("foo", "baz"), ("foo", 0xcafe), \
            (0xfeed, 998244353), (0xfeed, "baz")}
        True
        """
        self[key] -= set(value)
        if self[key] == set():
            del self[key]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
