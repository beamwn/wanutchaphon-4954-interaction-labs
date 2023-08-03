import abc


class Animal(abc.ABC):

    """
prob2.py: This file illustrates the usage of an abstract class and DocStrings

Class Animal is an abstract class that has abstract method move"""
    @abc.abstractmethod
    def move(self):
        """Mathod move is an abstrct method of an abstract class Animal"""
        pass

class Human(Animal):
    def move(self):
        """I can walk and run"""
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        """I can crawl"""
        print("I can crawl")


class Dog(Animal):
    def move(self):
        """I can bark"""
        print("I can bark")


if __name__ == "__main__":

    print(Animal.__doc__)
    print(Animal.move.__doc__)
    print("=== Below is the output of the code ===")
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()
    #animals = [Human(), snake(), Dog()]
    #for animal in animals:
        #animal.move()