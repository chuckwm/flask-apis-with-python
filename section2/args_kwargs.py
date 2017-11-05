def addtion_simplified(*args):
    return(sum(args))

print(addtion_simplified(3, 5 , 7, 9, 10))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56, name='Jose', location='UK')
