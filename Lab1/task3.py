list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# TODO Разделите участников на две команды
team_count = int(len(list_players) / 2)
print(list_players[:team_count])
print(list_players[team_count:])