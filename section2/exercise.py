# Create two variables var1 and var2 both with the same value
var1 = 10
var2 = 10

# Create two variables , num1 and num2, which multiply together to give 16
num1 = 8
num2 = 2

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock proce: {}".format(store.name, int(Store.stock_price(store)))

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.franchise(store))
print(Store.franchise(store2))

print(Store.store_details(store))
print(Store.store_details(store2))
