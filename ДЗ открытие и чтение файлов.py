# задание 1
with open('folder/recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        products_count = int(file.readline())
        products = []
        for _ in range(products_count):
            prod = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = prod
            products.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish_name] = products

# print(cook_book)


# задание 2
def get_shop_list_by_dishes(dishes, person_count):
  res = {}
  for dish in dishes:
    # print(cook_book[dish])
    # print()
    # print(dish)
    # print()
    # print(cook_book.keys())
    if dish in cook_book.keys():
      # print('Ура')
      # print(cook_book[dish])
      for value in cook_book[dish]:
        # print(value)
        # print(value['ingredient_name'])
        # print(type(value['quantity']))
        # print(value['measure'])
        # print(type(value['quantity']))
        res.setdefault(value['ingredient_name'], {'quantity': 0, 'measure': value['measure']})
        res[value['ingredient_name']]['quantity'] += int(value['quantity']) * person_count
        # print(res[value['ingredient_name']]['quantity'])
    else:
      print(f'Нет такого блюда {dish}')

  # print(res)
  return res

list_dish = ['Запеченный картофель', 'Утка по-пекински']
print(get_shop_list_by_dishes(list_dish, 2))


# задание 3
list_files = ['1.txt', '2.txt', '3.txt']

def read(files):
    res = []
    list_files = []
    len_str = []
    text_files = []
    for file in files:
        # print(file)
        list_files.append(file)
        import os
        a = os.path.join(os.getcwd(), 'folder', file)
        with open(a, 'rt', encoding='utf-8') as f:
            len_str.append(len(f.readlines()))
            # print(f.readlines())
            # print(len(f.readlines()))
        with open(a, 'rt', encoding='utf-8') as f:
            text_files.append(f.readlines())

    res = sorted(list(zip(len_str, list_files, text_files)))
    # print(res)

    for r in res:
        with open('folder/4.txt', 'at', encoding='utf-8') as new_file:
            new_file.write(f'{r[1]}\n{r[0]}\n{"".join(r[2])}\n')


read(list_files)