immutable_var = (1, 2, 'a', 'b')

print("Immutable tuple:", immutable_var)

try:
    immutable_var[0] = 10
except TypeError as e:
    print("Ошибка:", e, "- Нельзя изменять элементы кортежа, так как он является неизменяемым объектом.")

mutable_list = [1, 2, 'a', 'b']

mutable_list.append('Modified')

print("Mutable list:", mutable_list)
