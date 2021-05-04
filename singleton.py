class Singleton:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s1 = Singleton()
print("Object created", s1, "id =", id(s1))

# Singleton.instance = '<__main__.Singleton object at 0x0000027671C5DF70>'

s2 = Singleton()
print("Object created", s2, "id =", id(s2))

if s1 is s2:
    print("Objects is the same")

if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")
