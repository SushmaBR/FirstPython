class Bottle:
    content=""
    def Fill(self,c):
        self.content=c

    def Empty(self):
        self.content=""

    def ShowContent(self):
        if (self.content!=""):
            print("This bottle contains ",self.content)
        else:
            print("Bottle is empty")

waterBottle=Bottle()
waterBottle.Fill("water")
waterBottle.ShowContent()

SodaBottle=Bottle()
SodaBottle.Fill("Soda")
SodaBottle.ShowContent()
SodaBottle.Empty()
SodaBottle.ShowContent()
