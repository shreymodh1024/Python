class Products:
    count = 0
    def __init__(self, name, price):
        self.__name = name
        self.price = price
        Products.count += 1


    @staticmethod
    def after_discount(p: Products, discount):
        final_price = p.price * (100-discount)/100
        print(f"final price of {p.name}: {final_price}")


p1 = Products('toy', 400)
p2 = Products('watch', 300)
p3 = Products('laptop', 1000)

print(p1.__name) #the variable is private you can't access it
