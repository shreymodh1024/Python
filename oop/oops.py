class student:
    college_name = 'new lj'
    name = 'spiderMonkey' 
    #these are class attributes

    # its a parameterized constructor
    def __init__(self, fullname= None, roll_no= None):
        self.name = fullname
        self.roll_no = roll_no
        #these are object attributes
        
        print("checking init")

    def welcome(self):
        print("welcome student!")
    
s1 = student('pushpa')
print(s1.name, s1.roll_no)
s1.welcome()
