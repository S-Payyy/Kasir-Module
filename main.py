from KasirModule import Bon
from KasirModule import Menu
from KasirModule import TabelProduk

menu = [("Menu 1","1"),("Menu 2","2")]
Menu(menu)

list1 = ["Pays","Kentang","1","2","2000"]
list2 = [("Pays1","Kentang","1","2","2000"),("Pays2","Kentang","1","2","2000"),("Pays3","Kentang","1","2","2000")]
Bon(list1,False) # Doesn't print in Terminal
Bon(list2,True) # Print in Terminal

data = [("1","Indomie","2000"),("2","Kentang","5000")]
TabelProduk(data)