class phone:
    def __init__(self,r,n):
        self.RAM= r
        self.Brand ="APPLE"
        self.name =n
    def getInfo(self):
        print(self.RAM ,self.name)

s1=phone(18,"pro")
s2=phone(8,"Iphne")

s1.getInfo()
s2.getInfo()