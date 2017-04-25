#!/usr/bin/env python


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print '-start-'
        result = func(*args, **kwargs)
        print '-end-'
        return result
    return wrapper


def decorator_with_arg_func(arg=None):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print '-start-'
            print 'Args: ' + str(arg)
            result = func(*args, **kwargs)
            print '-end-'
            return result
        return wrapper
    return real_decorator


class DecoratorWithoutArguments(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(*args)


class DecoratorWithArguments(object):

    def __init__(self, arg='Some arg'):
        self.arg = arg

    def __call__(self, func):
        def wrapped_f(*args):
            print "Decorator arguments:", self.arg
            return func(*args)
        return wrapped_f


@decorator_func
def some_func1():
    return 'Test decorator function #1'


@decorator_with_arg_func(arg='this is arg')
def some_func2():
    return 'Test decorator function #2'


@DecoratorWithoutArguments
def some_func3():
    return 'Test decorator class #1'


@DecoratorWithArguments("this is another arg")
def some_func4():
    return 'Test decorator class #2'


delimeter = '-' * 40 + '\n'

print some_func1()
print delimeter

print some_func2()
print delimeter

print some_func3()
print delimeter

print some_func4()
print delimeter
