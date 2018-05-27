
'''
Think about if these should be implemented as closures instead...
'''
def simple_addition(arg):
    '''
    @TODO: think about rewriting this using function closures instead
    '''
    result = 0
    for item in arg:
        result += item
    return result


def simple_subtraction(arg):
    '''
    @TODO: think about rewriting this using function closures instead
    '''
    result = arg[0]
    for i in range(1, len(arg)):
        result -= arg[i]
    return result

def simple_multiplication(arg):
    '''
    @TODO: think about rewriting this using function closures instead
    '''
    result = 1
    for item in arg:
        result *= item
    return result


def simple_division(arg):
    '''
    @TODO: think about rewriting this using function closures instead
    '''
    result = arg[0]
    for i in range(1, len(arg)):
        result /= arg[i]
    return result


def define_(name, to_be_bound):
    '''
    Can be removed, since this is done in the evaluate module...
    '''
    environment_as_dict[name] = to_be_bound


#Note: outer is a reference to outer environments, in the global environment, this is None
#@TODO: outer and def does currently not do anything. Refactor!
environment_as_dict = {'outer': None,'def!': define_, '+' : simple_addition, '-': simple_subtraction, '*': simple_multiplication,'/': simple_division}

def get_environment():
    return environment_as_dict