#pa and pi restaurant
class MenuItem:
    def _init_(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: ${item.price} - {item.description}")

# ngebuat makanan untuk menu
menu_item1 = MenuItem("pizza chicken hot", "RP.50.000,000", "saus tomat, keju mozzarella, ayam, dan cabai bubuk")
menu_item2 = MenuItem("pizza pepperoni", "RP.45.000,000", "pizza dengan topping utama pepperoni, zaitun, keju parut, dan paprika")
menu_item3 = MenuItem("pizza margarita", "RP.35.000,000", "pizza dengan saus tomat, keju mozzarela, dan kemangi atau basil")
menu_item4 = MenuItem("pizza vegetarian", "RP.45.000,000", "pizza dengan saus tomat, keju mozzarela, tomat, bombai, paprika, dan kemangi atau basil")
menu_item5 = MenuItem("pizza tuna lover", "RP.60.000,000", "pizza dengan saus tomat, keju mozzarela, tuna, dan bombai")
menu_item6 = MenuItem("pizza chorizo e funghi rossa", "RP.45.000,000", "pizza dengan saus tomat, keju mozzarela, daging chorizo atau sosis babi dan bombai")
menu_item7 = MenuItem("spaghetti bolognese", "RP.40.000,000", "spaghetti, dan saus bolognese")
menu_item8 = MenuItem("fusili tonno", "RP.35.000,000", "fusilli, saus tomat, minyak zaitun, dan tonno")
menu_item9 = MenuItem("spaghetti tono", "RP.35.000,000", "Spaghetti dengan saus tomat, bawang bombay, tonno, peterseli, dan minyak zaitun")
menu_item10 = MenuItem("spaghetti pomodoro ricotta", "RP.40.000,000", "Spaghetti, Saus Pomodoro, Dan Keju Ricotta Di Atasnya")
menu_item11 = MenuItem("spaghetti pesto", "RP.35.000,000", "spaghetti, dan saus pesto")
menu_item12 = MenuItem("fettucinne meatball", "RP.45.000,000", "fettucinne, saus bolognese, dan bola-bola daging diatasnya")
menu_item13 = MenuItem("fettucinne alfredo", "RP.45.000,000", "fettucinne, saus cream, ayam potong/suwir, jamur, dan kemangi")
menu_item14= MenuItem("fettucinne spinach bolognese", "RP.45.000,000", "fettucinne, bayam, dan saus bolognese")
menu_item15= MenuItem("fettucinne spinach funghi", "RP.45.000,000", "fettucinne, bayam, dan dicampur dengan saus cream jamur")
menu_item16= MenuItem("milkshake vanilla", "RP.15.000,000", "es krim vanilla, susu putih, dan sirup vanilla")
menu_item17= MenuItem("milkshake cokelat", "RP.15.000,000", "es krim cokelat, susu cokelat menggunakan powder cocoa, dan gula pasir")
menu_item18= MenuItem("milkshake strawberry", "RP.15.000,000", "es krim strawberry, susu putih, dan sirup strawberry")
menu_item19= MenuItem("jus mangga", "RP.20.000,000", "mangga, skm/susu kental manis, dan gula cair")
menu_item20= MenuItem("jus jeruk", "RP.15.000,000", "jeruk peras, dan sedikit gula")
menu_item21= MenuItem("jus alpukat", "RP.20.000,000", "alpukat, dan skm/susu kental manis cokelat")
menu_item22= MenuItem("jus semangka", "RP.15.000,000", "hanya semangka blender ")
menu_item23= MenuItem("lemon tea", "RP.15.000,000", "teh, lemon diperas, dan disediakan gula cair")
menu_item24= MenuItem("es teh", "RP.10.000,000", "es teh, dan disediakan gula cair")
menu_item25= MenuItem("cappuccino", "RP.20.000.000", "kopi, susu, dan sirup")
menu_item26= MenuItem("kopi vanila", "RP.20.000.000", "kopi hitam, sirup vanila, dan sirup")
menu_item27= MenuItem("double espresso", "RP.20.000.000", "kopi hitam")


# ngebuat menu nya
menu = Menu()
menu.add_item(menu_item1)
menu.add_item(menu_item2)
menu.add_item(menu_item3)
menu.add_item(menu_item4)
menu.add_item(menu_item5)
menu.add_item(menu_item6)
menu.add_item(menu_item7)
menu.add_item(menu_item8)
menu.add_item(menu_item9)
menu.add_item(menu_item10)
menu.add_item(menu_item11)
menu.add_item(menu_item12)
menu.add_item(menu_item13)
menu.add_item(menu_item14)
menu.add_item(menu_item15)
menu.add_item(menu_item16)
menu.add_item(menu_item18)
menu.add_item(menu_item18)


# nunjukin menu
menu.display_menu()