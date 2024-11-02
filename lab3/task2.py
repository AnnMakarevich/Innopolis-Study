def find_common_participants(group_1, group_2, separator=','):
    # Разделяем строки на списки фамилий
    participants_1 = group_1.split(separator)
    participants_2 = group_2.split(separator)

    # Находим пересечение списков
    common_participants = set(participants_1).intersection(set(participants_2))

    # Сортируем список и возвращаем его
    return sorted(common_participants)




group_1 = "Иванов|Петров|Сидоров"
group_2 = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(group_1, group_2)
print(common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
