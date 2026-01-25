a = 2
b = 4
id_a = id(a)
id_b = id(b)
variables = {**locals(), **globals()}
print('only locals: ', {**locals()})
print()
print('only globals: ', {**globals()})

for var in variables:
    exec('var_id=id(%s)'%var)
    if var_id == id_a:
        exec('the_variable=%s'%var)
print()
print(the_variable)
print(id(the_variable))