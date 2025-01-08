grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gs = grades
st = students
# Список по алфавиту
st_list = sorted(st)
#print(st_list)
ball_gs = {}
# Словарь с выводом среднего балла
for st, gs in zip(st_list,gs):
    ball_gs[st] = sum(gs)/len(gs)# Расчет среднего балла
print(ball_gs)