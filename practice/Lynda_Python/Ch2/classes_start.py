#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

#anotherClass is inheriting the methods from myClass
class anotherClass(myClass):
  def method1(self):
    #we are inheriting the method of myClass
    #self is similar to "this" keyword
    myClass.method1(self)
    print("anotherClass method1")

   #method overriding, as we are not calling the inherited function 
  def method2(self, someString):
    print("anotherClass method2 ")

def main():
  c = myClass()
  c.method1()
  c.method2("This is string")

  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string2")


if __name__ == "__main__":
  main()
