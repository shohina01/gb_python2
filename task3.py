number = int(input('Введите номер месяца: '))
w, sp, sm, f = 'зима', 'весна', 'лето', 'осень'
season_list = [w, w, sp, sp, sp, sm, sm, sm, f, f, f, w]
print(season_list[number - 1])


month_dict = {1: w, 2: w, 3: sp, 4: sp, 5: sp, 6: sm, 7: sm, 8: sm, 9: f, 10: f, 11: f, 12: w}
print(month_dict[number])
