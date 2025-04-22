# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, n=','):
    participants_1 = set(group_1.split(n))
    participants_2 = set(group_2.split(n))
    coomon_participants = participants_1.intersection(participants_2)
    return sorted(coomon_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, n="|")
print("Список общих участников:", common_participants)