class Toy:
    def __init__(self, color, is_soft_toy):
        self.color = color
        self.is_soft_toy = is_soft_toy
        self.my_dict = {
            "name": 'Panda',
            "price": 100.99,
            "sku": "XCSDEFG"
        }

    def __getitem__(self, item):
        return self.my_dict[item]


T1 = Toy('red', True)
print(T1["sku"])
