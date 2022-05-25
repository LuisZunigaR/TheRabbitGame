class AlphanumericString:
    def __init__(self, string):
        self.string = string

    def getlowercharacters(self):
        lowers = ""
        for character in self.string:
            if character.islower():
                lowers = lowers + character
        return lowers

    def getuppercharacters(self):
        uppers = ""
        for character in self.string:
            if character.isupper():
                uppers = uppers + character
        return uppers

    def getdigits(self):
        digits = ""
        for character in self.string:
            if character.isdigit():
                digits = digits + character
        return digits

    def getdigitssorted(self):
        pairs = ""
        odds = ""
        digits = self.getdigits()
        for num in digits:
            if int(num) % 2 == 0:
                pairs = pairs + num
            else:
                odds = odds + num
        return pairs + odds
            

    def sortstring(self):
        return self.getlowercharacters() + self.getuppercharacters() + self.getdigitssorted()


string = AlphanumericString("ASDDweredsXYZ124asdASDAD9857362awsdADDDAD")
print string.sortstring()

