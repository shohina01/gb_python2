products = []
counter = 1
command = ''
while command != 'стоп':
    name = input('Название: ')
    price = input('Цена: ')
    amount = input('Количество: ')
    units = input('Единица измерения: ')
    products.append(
        (counter, {'n': name, 'price': price, 'amount': amount, 'units': units})
    )
    counter += 1
    command = input('Для остановки ввода напишите: "стоп" ')

result_list = {}
for num, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_list.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)

for key, value in result_list.items():
    result_list[key] = list(set(value))
print(result_list)

