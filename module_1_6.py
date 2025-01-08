my_dict = {'Pavel':1985, 'Artem':2015, 'Natalia':2005}
print(f"Dict: {my_dict}\nExisting value:{my_dict.get('Natalia')}"
      f"\nNot existing value:{my_dict.get('katerina')}"
      f"\nDeleted value:{my_dict.pop('Artem')}")
my_dict.update({'Konstantin':1999, 'Egor':2009, 'Olga':1996})
print(f"Modified dictionary: {my_dict}")

my_set = {15, 156, 158, 15, 156, 158, 15,  "Яблоко", "Апельсин", "Яблоко",}
print("Set:", my_set)
my_set.remove("Апельсин")
my_set.add(8965577)
print("Modified set:", my_set)