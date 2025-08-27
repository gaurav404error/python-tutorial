class Product:
    def __init__(self,name,price,stock):
        self.name= name
        self.price= price
        self.stock= stock
    def get_price(self):
        return self.price
    
    def check_availability(self,qty):
        if qty > 0 and qty < self.stock:
            return True 
        else:
            return False

p = Product("Gaurav ji",1000000,50)
print(p.get_price())


print(p.check_availability(51))