class Calculator:
    name=" "
    price=0

    def getDeatails(self,n,p):
        self.name=n
        self.price=p

    def details(self):
        temp=self.name+ '\'s' + "price is " + str(self.price)
        print(temp)

casio=Calculator()
#casio.name='casio'
#casio.price=500
casio.getDeatails('casio',500)
casio.details()

camel=Calculator()
#camel.name='camel'
#camel.price=1000
camel.getDeatails('camel',1000)
camel.details()