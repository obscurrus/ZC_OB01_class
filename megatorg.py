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


'''testing zone'''

shop1 = Store('\"Хламовик\"', 'ул. Дауншифтеров, д. 1', 'Вы прошли, а мы - нашли!')
shop2 = Store('\"Best Garbage\"', 'ул. Дауншифтеров, д. 2', 'Случайно выброшенное неслучайно тут!')
shop3 = Store('\"ГpUб@ViK\"', 'ул. Дауншифтеров, д. 3', 'Всё ещё только смотришь на звёзды?')

print(f'{shop1.slogan} Заходи в {shop1.name} по адресу {shop1.address}')
print(f'{shop2.slogan} Заходи в {shop2.name} по адресу {shop2.address}')
print(f'{shop3.slogan} Заходи в {shop3.name} по адресу {shop3.address}')


