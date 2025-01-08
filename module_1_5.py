# 2. Задайте переменные разных типов данных:
immutable_var = (1,2,3,"Python","Pycharm")
print(immutable_var)

# 3. Изменение значений переменных:
#immutable_var[3] =5
#print(immutable_var)
# raceback (most recent call last):
#   File "/home/vladimir/PythonProject_ Urban/module_1_5.py", line 4, in <module>
#     immutable_var[3] =5
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# Error: объект 'tuple' не поддерживает назначение элементов

# 4. Создание изменяемых структур данных:
mutable_list = [1,2,3,"Python","Pycharm"]
print(mutable_list)
mutable_list_1 = mutable_list+["Gawa"]
print(mutable_list_1)
mutable_list[3] = "Gawa"
print(mutable_list)