# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:#10/23/23
    # Functions that start with two underscores are not intended to be called directly.
    def __init__(self, n = "", fc = "", a = "", ff = ""):
        """Creates an instance of the dog class and sets attribrutes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """Return a string representation of a dog."""
        s="Dog's name is " + self.name + "\n"
        s+="Dog's fur color is " + self.fur_color + "\n"
        s+="Dog's age is "+ str(self.age) + "\n"
        s+="Dog's favorite food is "+ self.favorite_food +"\n"
        s+="Dpg's fetch count is "+ str(self.fetch_count) + " times\n"
        return s
    
    def play_fetch(self, num_times):
        self.fetch_count += num_times

mydog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")

print(mydog)
print(chrisdog)

mydog.play_fetch(20)
chrisdog.play_fetch(3)

print(mydog)
print(f"{chrisdog.name} has played fetch {chrisdog.fetch_count} times")