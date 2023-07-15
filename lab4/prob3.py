class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"I'm {self.name}")

    def move(self):
        print("Moving ...")

class Cat(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Cat, self).__init__(name)
   
    def show_info(self):
        super().show_info()
        print(f"and is {self.color}\nbelonging to {self.owner}")
    
    def move(self):
       print("Cat likes to walk more than run")

class Dog(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super(Dog, self).__init__(name)
   
    def show_info(self):
        super().show_info()
        print(f"and is {self.color}\nbelonging to {self.owner}")
    
    def move(self):
       print("Dog likes to walk more than run")
    
    def eat_cat(self, cat):
        print(f"Dog {self.name} eat cat {cat.name}")
        
        
if __name__ == '__main__':
    pet1 = Pet("Thongdeang")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
