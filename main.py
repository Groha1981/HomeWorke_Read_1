with open('recipe.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        components = int(file.readline())
        components_list = []
        for i in range(components):
            product, quantity, measure = file.readline().strip().split(' | ')
            components_list.append({
                'product': product,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = components_list
print(f'cook_book = {cook_book}')
