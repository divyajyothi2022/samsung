
# Method overloading
class Math:
    def add(self, a, b):
        return a + b
    def add(self,a, b, c):
        return "a" + "b" + "c"
    def add(self, *args):
        return sum(args)
my_math = Math()
print(my_math.add(1, 2))
print(my_math.add(1,2,3))
print(my_math.add(1, 2, 3, 4, 5))



# Method over riding
class Animal:
    def make_sound(self):
        print("the animal makes a sound")
class dog(Animal):
    def make_sound(self):
        print("the dog barks")
class cat(dog):
    def make_sound(self):
        print("the cats makes a sound meows")
ob=cat()
ob.make_sound()
b=dog()
b.make_sound()
c=Animal()
c.make_sound()


