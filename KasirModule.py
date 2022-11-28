### Code created by s_payyy01
### Python 3.11
### Req Module : Rich
### Module VERSION = 1.0.0

try:
    #from rich.table import Table
    from rich.console import Console
    from rich.panel import Panel
    from rich.columns import Columns
    from datetime import datetime
    con = Console()
except:
    import os
    os.system("pip install rich")
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    os.system("exit")

class Menu:
    """Membuat Tabel Menu
    
    Contoh Penggunaan:
        List = [("Menu Name1","Menu var1"),("Menu Name2","Menu var2")]
        \n\tMenu(List1)
    """

    def __init__(self, data: list) -> None:
        self.data = data
        self.__table()

    def __table(self):
        menu_renderable = []
        for a in self.data:
            dat = (Panel(f"{a[0]}", expand=True, title=f"{a[1]}"))
            menu_renderable.append(dat)
        con.print(Columns(menu_renderable))

class Bon:
    """Membuat Output Struk.

    Contoh penggunaan:\n
        List1 = [("Nama","Barang","Jumlah","Harga","Diskon"),(...)] or List2 = ["Nama","Barang","Jumlah","Harga","Diskon"]

        Bon(List , hide print in terminal: True or False, default is True) 
    """

    def __init__(self,data:list,printin = True) -> None:
        self.data = data
        self.printin = printin
        self.__struk()

    def __struk(self):
        tanggal = datetime.now()
        try:
            for isi in self.data:
                name:str = isi[0]
                barang:str = isi[1]
                jumlah:int = isi[2] or 1
                harga:int = isi[3]
                diskon:int = isi[4] or None
                self.__printstruk(tanggal,name, barang, jumlah, harga, diskon)
        except:
            name:str = self.data[0]
            barang:str = self.data[1]
            jumlah:int = self.data[2] or 1
            harga:int = self.data[3]
            diskon:int = self.data[4] or None
            return self.__printstruk(tanggal,name, barang, jumlah, harga, diskon)

    def __printstruk(self,a,b,c,d,e,f):
        ss = (
                    """
{}
    #############################
    Nama   : {}
    Barang : {}
    Jumlah : {}
    Harga  : {}
    Diskon : {}
    #############################
                """.format(a.strftime('%w %B %Y'),b,c,d,e,f)
            )
        with open("struk.txt","a") as a:
            a.write(ss)
        
        if self.printin == False:
            pass
        else:
            print(ss)


#Testing

#listss = [("Monster","mon"),("Hewan","hw"),("Hewanasdd","asd")]
#Menu(listss)

#listt = ["Pay2","Indomie","1",1000,0]
#Bon(listt,printin= False)