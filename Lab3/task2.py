# Напишите функцию find_common_participants
def find_common_participants(str1, str2, splitter=','):
    gr1, gr2 = set(str1.split(splitter)), set(str2.split(splitter))
    return sorted(gr1.intersection(gr2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
