class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f"저는 {self.age}살 {self.address}에 사는 {self.name}입니다.") 

