class StringClass:
    l_string = " "

    def getString(self):
        self.l_string = input("Write a string : ")

    def printString(self):
        print(self.l_string.upper())

string_class = StringClass()
string_class.getString()
string_class.printString()