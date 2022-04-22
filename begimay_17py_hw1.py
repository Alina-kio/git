class Bmw:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    
    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')
    
    def stop_engine(self):
        print(f'{self.title} {self.model} engine stoped!')

    def info(self):
        print(f"""
        Name: {self.title}
        Model: {self.model}
        Weight: {self.weight}
        Hp: {self.hp}
        Nm: {self.nm}
        Max_speed: {self.max_speed}
        Color: {self.color}
        """)
bmw = Bmw('Bmw', 'M5', '2 ton', 340, '', '80 км/ч', 'black')
bmw.start_engine()
bmw.stop_engine()
bmw.info()

class Mercedes:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    
    def start_engine(self):
        print(f'{self.title} + {self.model} engine started!')
    
    def stop_engine(self):
        print(f'{self.title} + {self.model} engine stoped!')

    def info(self):
        print(f"""
        Name: {self.title}
        Model: {self.model}
        Weight: {self.weight}
        Hp: {self.hp}
        Nm: {self.nm}
        Max_speed: {self.max_speed}
        Color: {self.color}
        """)
mercedes = Mercedes('Mercedes', 'S-class', '2.5 ton', 380, '', '90 км/ч', 'red')
mercedes.start_engine()
mercedes.stop_engine()
mercedes.info()