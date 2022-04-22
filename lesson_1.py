# class Alina():
#     def __init__(self):
#         print('Hello world!')
# Alina()

"""

class - tip dannyh - object

"""



class Transport:
    def __init__(self, title, model, type, year):      #inicializirivat - inicializator
        self.title = title
        self.model = model
        self.type = type
        self.year = year

    


bmw = Transport('BMW', 'e34', 'car', 1990)         # instance Trransport
mercedes = Transport('Mercedes', 'w124', 'car', 1990)            # instance Trransport



class Dog:       # povedenie   -   metod
    def __init__(self, name, age, type):          # atribut
        self.name = name
        self.age = age
        self.type = type
    
    def voice(self):          # povedenie   -   metod
        print(f'{self.name} gaf! gaf!')

    def eat(self):       # povedenie   -   metod
        print(f'{self.name} eat meat.')

    def sleep(self):        # povedenie   -   metod
        print(f'{self.name} want to sleep.')

    def info(self, w , h):         # povedenie   -   metod
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Type: {self.type}
        Weight: {w}
        Height: {h}
        """)

        
rex = Dog('Rex', 15, 'pitbul')
rex.voice()
rex.eat()
rex.info(60, 1.70)


