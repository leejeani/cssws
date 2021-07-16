# itemvo.py  Model 역할을 하는 Class
class ItemVO:
    def __init__(self,id,name,price,regdate):
        self.id = id;
        self.name = name;
        self.price = price;
        self.regdate = regdate;
    def __str__(self):
        return '%d, %s, %f, %s' % (self.id,self.name,self.price,self.regdate);
    def getId(self):
        return self.id;

    def getName(self):
        return self.name;
    def setName(self, name):
        self.name = name;
    def getPrice(self):
        return self.price;
    def setPrice(self, price):
        self.price = price;
    def getRegdate(self):
        return self.regdate;
    def setRegdate(self, regdate):
        self.regdate = regdate;








