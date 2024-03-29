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

my_shop = None

choice = input(f'Введите номер дома для выбора магазина ')

for variable in shops:
    if choice in variable:
        my_shop = shops[variable]
        break

print("Отличный выбор! Вы отправляетесь в магазин: ", my_shop.name)

