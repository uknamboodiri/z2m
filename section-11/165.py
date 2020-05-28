# modules and packages
from shopping.shopping_cart import buy
from shopping.items import products

print(dir(products))
help(shopping)
# print(help(buy))

if __name__ == '__main__':
    print(buy(10, 20))
    print(products.add_to_wish_list('Bread'))

print(__name__)
