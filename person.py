# secret = 'kimalina'

# def test(text):
#     print(text)


class Person:         # module
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_full_name(self):
        return f'{self.name} {self.surname}'