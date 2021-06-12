class family:
    vab1=5
    def mallick(self):
        print("My name is amit kumar mallick ")

    def rout(self):
        print("My name is Rachita Priyadarsini Rout .")

class title1(family):
    '''This is inherits from family class .'''
    def mr(self):
        print("My name is Rachita Priyadarsini Mallick .")
class title2(family):
    """
    It is also inherits from family .
    """
    pass
family1=title1()
family2=title2()
print(family1.vab1)