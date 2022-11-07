#reff: https://medium.com/@ruchibaheti86/behavior-driven-development-bdd-in-python-218021e815a8 
from behave import given, when, then 
from calculator import add, subtract, multiply, divide

@given(u'Calculator program is running')
def step_impl(context):
    print(u'Step: Calculator program is running') 

@when(u'I input "{a}" and "{b}" to calculator')
def step_impl(context, a, b): 
    print(u'Step: When I input "{}" and "{}" to calculator'.format(a, b)) 
    context.result = add(a, b) 
    print(u'Stored result "{}" in context'.format( context.result ) ) 

@then(u'I get result "{out}"') 
def step_impl(context, out): 
    if(context.result == int(out)): 
        print(u'Step: Then I get result "{}", "{}"'.format( context.result, out  ) )
        pass 
    else: 
        raise Exception("Invalid calculation. Please check implementation.")


@given(u'Calculator program has executed')
def step_impl(context):
    print('Step: Calculator program has executed')

@when(u'I provide "{x}" and "{y}" to the calculator')
def step_impl(context, x ,y): 
    print(u'Step: When I provide "{}" and "{}" to the calculator '.format(x, y))
    context.result1 = subtract(x, y) 
    print('Stored result "{}" in the context'.format( context.result1 ) )

@then(u'I get the result "{out}"')
def step_impl(context, out): 
    if(context.result1 == int(out) ):
        print(u'Step: Then I get result "{}", "{}" '.format(context.result1, out))
        pass 
    else: 
        raise Exception(u'Wrong calculation. Bug in code.')

@given(u'Calculator program has been executed')
def step_impl(context):
    print('Step: Calculator program has been executed')

@when(u'I provide "{v}" and "{w}" to a calculator')
def step_impl(context, v ,w): 
    print(u'Step: When I provide "{}" and "{}" to a calculator '.format(v, w))
    context.result2 = multiply(v, w) 
    print('Stored result "{}" in a context'.format( context.result2 ) )

@then(u'I get a result "{out}"')
def step_impl(context, out): 
    if(context.result2 == int(out) ):
        print(u'Step: Then I get a result "{}", "{}" '.format(context.result2, out))
        pass 
    else: 
        raise Exception(u'A wrong calculation. Bug in code.')

@given(u'Calculator program is executing')
def step_impl(context):
    print('Step: Calculator program is executing')

@when(u'I provide "{s}" and "{t}" to the calculator program')
def step_impl(context, s, t): 
    print(u'Step: When I provide "{}" and "{}" to the calculator program '.format(s, t))
    context.result3 = divide(s, t) 
    print('Stored result "{}" in the contexting'.format( context.result3 ) )

@then(u'I get resulting factor "{out}"')
def step_impl(context, out): 
    if(context.result3 == int(out) ):
        print(u'Step: Then I get resulting factor "{}", "{}" '.format(context.result3, out))
        pass 
    else: 
        raise Exception(u'THE Wrong calculation. Bug in code.')
