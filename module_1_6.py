my_dict = {"IT": 150000, "Производство": 100000, "Образование": 40000}

print(my_dict)
print(f'Зароботная плата в сфере {list(my_dict.keys())[0] } {my_dict["IT"]} рублей')

my_dict.update({"Торговля": 50000, "Реклама": 120000})
removed_dict = my_dict.pop("Реклама")

print(f'удаленное занчение ключа {removed_dict}')
print(my_dict)

my_set = {1, 2, 4, 2, 'Яблоко', 'Апельсин', "Яблоко"}
print(my_set)
my_set.update([3, 5, "Груша"])
my_set.discard('Апельсин')
print(my_set)
