def for_each(iterable, func):
    for item in iterable:
        func(item)


def first(iterable, predicate):
    return next((item for item in iterable if predicate(item)), None)


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



if __name__ == '__main__':
    def a(x): print x

    print '-> for_each'
    for_each(range(3), a)

    print '-> first'
    def b(x): return x == 3
    print first(range(4), b)

    print '-> last'
    def c(x): return x > 1
    print last(range(4), c)

    def g3(x): return x > 3
    def l3(x): return x < 3
    def e3(x): return x == 3
    print '-> group_into'
    print group_into(range(7), g3=g3, l3=l3, e3=e3)
