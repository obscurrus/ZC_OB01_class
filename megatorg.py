class Store:
    def __init__(self, name, address, slogan):
        self.name = name
        self.address = address
        self.slogan = slogan
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def del_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item)

    def upd_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price

    def __str__(self):
        return f"{self.slogan} Заходите в {self.name}, по адресу: {self.address}"


'''testing zone'''
shops = {
    'shop1': Store('\"Хламовик\"', 'ул. Дауншифтеров, д. 1', 'Вы прошли, а мы - нашли!'),
    'shop2': Store('\"Best Garbage\"', 'ул. Дауншифтеров, д. 2', 'Случайно выброшенное неслучайно тут!'),
    'shop3': Store('\"ГpUб@ViK\"', 'ул. Дауншифтеров, д. 3', 'Всё ещё только смотришь на звёзды?')
}
print(f'Вот список наших магазинов:\n')
for key, value in shops.items():
    print(value)

print('\nВы прошли всевозможные тестирования и как выживший, приняты на работу нашим товароведом!'
      '\nВыберите магазин соответствующий вашему фетишу и приступайте скорее!\n')

shop = None

choice = input(f'Введите номер дома для выбора магазина ')

for variable in shops:
    if choice in variable:
        shop = shops[variable]
        break

print("Отличный выбор! Вы отправляетесь в магазин: ", shop.name)

'''начинаем работу товароведа'''
print("Начинаем работу. Выберите операцию. Для выхода в меню - буква Ы.")

while True:
    print("1. Разбираем хлам и назначаем цены")
    print("2. Накосячил? Исправься!")
    print("3. Раскупили - удали!")
    print("4. Проверить, чё натыкал")
    print("5. Я устал. Я ухожу (Ы)")

    operation = input("Чё делаем? ")

    if operation == "1":
        while True:
            item = input("ЧТо продаём? ")
            if not item:
                print("\"Что\" - это что-то, а не пусто!")
                continue
            if item.lower() == "ы":
                break
            try:
                price = float(input("Почём? "))
            except ValueError:
                print('цЫфрыыыыы!!')
                continue
            # for shop in shops.values():
            shop.add_item(item, price)

    elif operation == "2":
        while True:
            item = input("Что исправляем? ")
            if not item:
                print("\"Что\" - это что-то, а не пусто!")
                continue
            if item.lower() == "ы":
                break
            try:
                new_price = float(input("Новая цена: "))
            except ValueError:
                print('цЫфрыыыыы!!')
                continue
            # for shop in shops.values():
            shop.upd_price(item, new_price)

    elif operation == "3":
        while True:
            item = input("Что кончилось? ")
            if not item:
                print("\"Что\" - это что-то, а не пусто!")
                continue
            if item.lower() == "ы":
                break
            # for shop in shops.values():
            shop.del_item(item)

    elif operation == "4":
        while True:
            item = input("Введите название товара (000 чтобы показать всё): ")
            if item.lower() == "ы":
                break
            if item == "000":
                print(f'У нас в магазине {shop.name} вы можете купить: ')
                for key in shop.items:
                    print(f'{key} за {shop.get_price(key)} р.')
                continue
            if item not in shop.items:
                print("Нету такого")
                continue
            # for shop in shops.values():
            print(f"Цена товара в {shop.name}: {shop.get_price(item)} р.")

    elif operation == "5":
        print("Слабак ты, жидкий гомо.")
        break

    elif operation.lower() == "ы":
        print("Ыыыыы...")
        break

    else:
        print("Непонял... Чё это было?")
