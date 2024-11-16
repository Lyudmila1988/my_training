my_dict = {
    'Vasya': 1975,
    'Egor': 1999,
    'Masha': 2002
}
print("Dict:", my_dict)

print("Existing value:", my_dict.get('Masha'))

print("Not existing value:", my_dict.get('Ivan', None))

my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915

deleted_value = my_dict.pop('Egor', None)
print("Deleted value:", deleted_value)

print("Modified dictionary:", my_dict)

my_set = {1, 'Яблоко', 42.314, 'Яблоко', 1, 42.314}  # Повторяющиеся значения будут удалены

print("Set:", my_set)

my_set.add(13)
my_set.add((5, 6, 1.6))

my_set.discard('Яблоко')

print("Modified set:", my_set)
