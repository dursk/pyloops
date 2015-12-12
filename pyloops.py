"""
NOTE: Some of these functions return None if nothing is found,
      or use None as a default if no match is found. This is an issue
      since None could potentially be a value the consumer is looking for.
"""
from collections import defaultdict


def first(iterable, predicate):
    return next((item for item in iterable if predicate(item)), None)


def first_n(iterable, predicate, num):
    matches = []
    while len(matches) < num:
        val = next((item for item in iterable if predicate(item)), None)
        if val:
            matches.append(val)
        else:
            break
    return matches


def last(iterable, predicate):
    return next(reversed(item for item in iterable if predicate(item)), None)


def concat(iterable):
    return reduce(lambda x, y: x + y, iterable, [])


def flatten(iterable, accessor):
    return reduce(lambda prev, curr: prev + accessor(curr), iterable, [])


def group_into(iterable, keyfunc):
    ret = defaultdict(list)
    for item in iterable:
        ret[keyfunc(item)].append(item)
    return ret
