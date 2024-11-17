immutable_var = (1, 2.5, 'Str', False, ['l', 'i', 's', 't'])
print(immutable_var)

''' 
--------при попытке изменить элемент кортежа возникатет ошибка, 
т.к. кортеж является неизменяемой структурой данных------------

immutable_var[0] = 3 
print(immutable_var)
'''
mutable_list = ['A', 2, 2.5, 65]
print(mutable_list)
mutable_list[0:2] = 'b', False
mutable_list_new = mutable_list
print(mutable_list_new)
