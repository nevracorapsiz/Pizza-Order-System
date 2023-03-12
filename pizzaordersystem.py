import csv, re
from datetime import datetime

# Pizza Class

class Pizza:

    def __init__(self,name,description,cost):
        self.name=name
        self.cost=cost
        self.description=description
    def get_description(self):
        return self.description   
    def get_cost(self):
        return self.cost
    
# Pizza Subclasses
   
class Classic(Pizza):
    name="Klasik Pizza"
    desc="Mozzarella peyniri, pizza sosu, sucuk, sosis, mantar, yeşilbiber, siyah zeytin"
    cost=15
    def __init__(self):
        super().__init__(Classic.name,Classic.desc,Classic.cost)

class Margarita(Pizza):
    name="Margerita Pizza"
    desc="Mozzarella peyniri, pizza sosu"
    cost=10
    def __init__(self):
        super().__init__(Margarita.name,Margarita.desc,Margarita.cost)
        
class TurkishPizza(Pizza):
    name="Turkish Pizza"
    desc="Özel pizza sosu, mozzarella peyniri, küp sucuk, kırmızı köz biber ve mantar"
    cost=18
    def __init__(self):
        super().__init__(TurkishPizza.name,TurkishPizza.desc,TurkishPizza.cost)
        
class DominosPizza(Pizza):
    name="Dominos Pizza"
    desc="Özel pizza sosu, mozzarella peyniri, sosis, soğan, mantar, mısır"
    cost=20
    def __init__(self):
        super().__init__(DominosPizza.name,DominosPizza.desc,DominosPizza.cost)
        
class SadePizza(Pizza):
    name="Sade Pizza"
    desc="Özel pizza sosu, mozzarella peyniri, sosis, mantar, mısır, yeşilbiber"
    cost=10
    def __init__(self):
        super().__init__(SadePizza.name,SadePizza.desc,SadePizza.cost)

# Sause Class

class Sauses:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    
    def get_description(self):
        return "{} sosu".format(self.name)

    def get_cost(self):
        return "Sos ücreti: {}".format(self.cost)

# Sause Subclasses

class OliveSauce(Sauses):
    name="Zeytin"
    cost=5
    def __init__(self):
        super().__init__(OliveSauce.name,OliveSauce.cost)

class MushroomSauce(Sauses):
    name="Mantar"
    cost=5
    def __init__(self):
        super().__init__(MushroomSauce.name,MushroomSauce.cost)

class CheeseSauce(Sauses):
    name="Keçi Peyniri"
    cost=5
    def __init__(self):
        super().__init__(CheeseSauce.name,CheeseSauce.cost)

class MeatSauce(Sauses):
    name="Et"
    cost=5
    def __init__(self):
        super().__init__(MeatSauce.name,MeatSauce.cost)

class OnionSauce(Sauses):
    name="Soğan"
    cost=5
    def __init__(self):
        super().__init__(OnionSauce.name,OnionSauce.cost)

class CornSauce(Sauses):
    name="Mısır"
    cost=5
    def __init__(self):
        super().__init__(CornSauce.name,CornSauce.cost)

# Choice Screen

def choice():    
    pizza=input("Pizza secimi yapiniz: ")
    while pizza not in ["1","2","3","4"]:
        pizza=input("Lütfen 1 ile 4 arasinda bir değer giriniz: ")

    sause=input("Lütfen sos seçimi yapiniz: ")
    while sause not in ["11","12","13","14","15","16"]:
        sause=input("Lütfen 11 ile 16 arasinda bir değer giriniz: ")

    if pizza=="1":
        pizza=Classic()
    elif pizza=="2":
        pizza=Margarita()
    elif pizza=="3":
        pizza=TurkishPizza()
    else:
        pizza=SadePizza()

    if sause=="11":
        sause=OliveSauce()
    elif sause=="12":
        sause=MushroomSauce()
    elif sause=="13":
        sause=CheeseSauce()
    elif sause=="14":
        sause=MeatSauce()
    elif sause=="15":
        sause=OnionSauce()
    else:
        sause=CornSauce()

    global pizza_name, pizza_description, pizza_cost, sause_name, sause_cost, total_cost

    pizza_name=pizza.name
    pizza_description=pizza.description
    pizza_cost=pizza.cost
    sause_name=sause.name
    sause_cost=sause.cost
    total_cost=pizza.cost+sause.cost

# Validation Control

def control():

    global customer_name,custumer_id,card_num,card_password

    customer_name=input("İsminiz: ")
    while customer_name.isdigit():
        customer_name=input("Lütfen geçerli bir isim giriniz: ")

    custumer_id=input("TC kimlik numaranizi giriniz: ")
    while (custumer_id.isdigit() is False) or len(custumer_id)!=11 or custumer_id[0]=="0":
        custumer_id=input("Lütfen 11 haneli TC Kimlik numaranızı giriniz: ")

    card_num=input("Kredi karti numaraninizi giriniz: ")
    regex=r"\d{4}\s\d{4}\s\d{4}\s\d{4}"
    while not re.search(regex,card_num):
        card_num=input("Lütfen 16 haneli kredi kart numaranızı aralarında boşluk bırakacak şekilde giriniz: ")

    card_password=input("Kredi kartı şifrenizi giriniz: ")
    while (card_password.isdigit() is False) or len(card_password)!=4:
        card_password=input("Lütfen 4 haneli kart şifrenizi giriniz: ")

def main():
    with open(r"C:\Users\Nevra\Desktop\menu.txt","r") as menu:
        print(menu.read())
    
    choice()
    
    print("SEPET İÇERİĞİ\n{}: {} tl\nİlave {}: {} tl\nToplam Tutar: {} tl".format(pizza_name, pizza_cost, sause_name, sause_cost, total_cost))
    print("Lütfen sipariş oluşturmak için bilgilerinizi giriniz.")

    control()
    
    time=datetime.now()
    print("SIPARISINIZ OLUSTURULMUSTUR! SIPARIS SAATI: {}".format(time))

    with open(r"C:\Users\Nevra\Desktop\Order_Database.csv",'a') as database:
        data=[pizza_name,pizza_description,pizza_cost,sause_name,sause_cost,total_cost,customer_name,custumer_id,card_num,card_password,time]
        writer = csv.writer(database)
        writer.writerow(data)

        

if __name__ == "__main__":
    main()
    
