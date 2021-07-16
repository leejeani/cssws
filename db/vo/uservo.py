# uservo.py  Model 역할을 하는 Class
class UserVO:
    def __init__(self,id,pwd,name):
        self.id = id;
        self.pwd = pwd;
        self.name = name;
    def __str__(self):
        return '%s, %s, %s' % (self.id,self.pwd,self.name);
    def getId(self):
        return self.id;
    def setId(self, id):
        self.id = id;
    def getPwd(self):
        return self.pwd;
    def setPwd(self, pwd):
        self.pwd = pwd;
    def getName(self):
        return self.name;
    def setName(self, name):
        self.name = name;








