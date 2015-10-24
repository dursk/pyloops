"""
NOTE: Some of these functions return None if nothing is found,
      or use None as a default if no match is found. This is an issue
      since None could potentially be a value the consumer is looking for.
"""

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
    try:
        return [item for item in iterable if predicate(item)][-1]
    except IndexError:
        return None


def group_into(iterable, **kwargs):
    return {
        group_name: [item for item in iterable if predicate(item)]
        for group_name, predicate in kwargs.iteritems()
    }
