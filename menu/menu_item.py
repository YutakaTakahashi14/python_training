class MenuItem:
    def __init__(self,name):
        self.name = name

    def info(self):
        return self.name + '：' + str(self.price) + '円'
    
    def get_total_price(self,count):
        get_total_price = self.price * count
        return get_total_price
