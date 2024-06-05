immutable_var = (5, 4, 'b', 'c', 3.2, 8.1, False)
print('Immutable Var:', immutable_var)
print(type(immutable_var))

# immutable_var[3] = 'boom'
# print(immutable_var)
   # Объект «кортеж» не поддерживает назначение элементов (обращение к ним и операции с ними невозможны)

immutable_var1 = (3, 2, ['a', 'b'], True, [4, 5.5], False)
print('Immutable Var1:', immutable_var1)
print(type(immutable_var1))
immutable_var1[2][1] = 'boom'
immutable_var1[4][0] = 401
print('Immutable Var1:', immutable_var1)
immutable_var2 = immutable_var1 * 2
print('Immutable Var2:', immutable_var2)
immutable_var3 = immutable_var1 + (9, 8, ['full', 'finish'])
print('Immutable Var3:', immutable_var3)

mutable_list = [2, False, 3.14, 'do', 're', 5001]
print('Mutable List:', mutable_list)
mutable_list[4] = True
mutable_list.append('re')
mutable_list.extend([2024.06, 'love', 'GOD'])
mutable_list.remove(5001)
print('Mutable List:', mutable_list)

# отправлено 2024/06/05 18:20 по теме "Неизменяемые и изменяемые объекты. Кортежи"






