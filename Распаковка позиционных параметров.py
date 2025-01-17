def print_params(a=1 ,b='stroka', c=True):
    print(a, b, c)
# Вызовы функции с различными аргументами:
# Вызов без аргументов:
print_params()
# Вызов с одним аргументом
print_params(42)
# Вызов с именованным аргументом:
#print_params(d=25)       #Traceback (most recent call last):
                          #File "/home/vladimir/PythonProject_
                          # Urban/Распаковка позиционных параметров.py", line 9, in <module>
                          #print_params(d=25)
                          #TypeError: print_params() got an unexpected keyword argument 'd'
# Вызов с именованным аргументом (список):
print_params(c = [1,2,3])

# Создание списка и словаря для распаковки:
values_list = [3.14, 'text', False]
values_dict = {'a': 42, 'b': 'primer', 'c': True}
# Распаковка списка и словаря:
# Распаковка списка:
print_params(*values_list)
# Распаковка словаря:
print_params(**values_dict)
# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'stroka']
# Распаковка списка и добавление аргумента:
print_params(*values_list_2, 42)
