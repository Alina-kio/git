class Dog:
    def __init__(self, name, age, voiceText):
        self.name = name
        self.age = age
        self.voiceText = voiceText
    
    def voice(self):
        print(f"{self.name} - {self.voiceText}")

class Cat:
    def __init__(self, name, age, voiceText):
        self.name = name
        self.age = age
        self.voiceText = voiceText
    def voice(self):
        print(f"{self.name} - {self.voiceText}")

class Cow:
    def __init__(self, name, age, voiceText):
        self.name = name
        self.age = age
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.name} - {self.voiceText}")

class Bear:
    def __init__(self, name, age, voiceText):
        self.name = name
        self.age = age
        self.voiceText = voiceText
    
    def voice(self):
        print(f"{self.name} - {self.voiceText}")


a = Dog('Rex', 15, 'gaf')
b = Cat('Cat', 15, 'myau')
c = Cow('Cow', 15, 'muuu')
d = Bear('Bear', 15, 'graa')
a.voice()
b.voice()
c.voice()
d.voice()





a = """to replace one substring with another in a string in Python,
use the replace() method: • replace(old, new): substring old
replaced with new; • replace(old, new, num): the num parameter indicates
how many occurrences of the substring old need to be replaced by new."""
# a.replace('a', '|||||||')
with open('rate.docx', 'a') as file:
    file.write(a.replace('a', '|'))