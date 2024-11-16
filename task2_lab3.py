
def find_common_participants(x, y, z=","):
    list1 = x.split(z)
    list2 = y.split(z)

    sol = list(set(list1).intersection(list2))
    sol.sort()

    return(sol)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)
