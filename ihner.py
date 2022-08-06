class parent:
  def __init__(self, name):
    self.name = name

  def say_name(self):
    print(f"Hi I am {self.name}")


john = parent("John")

john.say_name()
