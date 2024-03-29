class Store:
    def __init__(self, name, address, slogan):
        self.name = name
        self.address = address
        self.slogan = slogan

    def __str__(self):
        return f"Store: {self.name}, Address: {self.address}, Slogan: {self.slogan}"


shops = {
    'shop1': Store('\"Хламовик\"', 'ул. Дауншифтеров, д. 1', 'Вы прошли, а мы - нашли!'),
    'shop2': Store('\"Best Garbage\"', 'ул. Дауншифтеров, д. 2', 'Случайно выброшенное неслучайно тут!'),
    'shop3': Store('\"ГpUб@ViK\"', 'ул. Дауншифтеров, д. 3', 'Всё ещё только смотришь на звёзды?')
}

for key, value in shops.items():
    print(f"{value}")

choice = None

user_input = input("Введите цифру: ")

for variable in shops:
    if user_input in variable:
        choice = shops[variable]
        break

print("Значение переменной выбранной пользователем: ", choice)
