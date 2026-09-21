#practice question
class product:
    storage__type = "ssd"

    def __init__(self,name,price):
     self.name=name
     self.price=price 

    @classmethod
    def get__storage(cls): 
        print(f"storage type={cls.storage__type}")    

prd1=product("phone",50000)
prd2=product("laptop",70000)

print(prd1.name)
print(prd2.price)

prd1.get__storage()