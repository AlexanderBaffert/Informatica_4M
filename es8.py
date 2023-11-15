#Baffert Alexander es8
#Classe
class  Conto:
    def __init__(self,id_conto,intestato,iban,saldo_disponibile,patrimonio_investito):
        self.id_conto=id_conto
        self.intestato=intestato
        self.iban=iban
        self.saldo_disponibile=saldo_disponibile
        self.patrimonio_investito=patrimonio_investito
    def deposito(self,deposito):
        self.saldo_disponibile=(deposito+self.saldo_disponibile)
    def prelievo(self,prelievo):
        self.saldo_disponibile=(prelievo-self.saldo_disponibile)
    def investimento(self,investimento):
        self.patrimonio_investito=(investimento+self.patrimonio_investito)
        self.saldo_disponibile=(self.saldo_disponibile-investimento)
    def Disinvesti(self,disinvesti):
        self.patrimonio_investito=(self.patrimonio_investito-disinvesti)
        self.saldo_disponibile=(self.saldo_disponibile+disinvesti)
constructor=Conto("345436", "Pino", "IT 12 A 12345 12345 123456789012", 1700000, 13000000)
print("-------------------------------------    -----")
print("---|     1)Depositare                 |---")
print("---|     2)Prelievo                   |---")
print("---|     3)Investi                    |---")
print("---|     4)Disinvesti                 |---")
print("---|     5)Visualizza Investimento    |---")
print("------------------------------------------")
menu=input("Che cosa vuole fare: ")
if menu=="1":
    dep=input("Vuoi depositare: ")
    if dep == "si":
        dexosito=float(input("Quanto vuoi depositare: "))
        constructor.deposito(dexosito)
        print(constructor.saldo_disponibile)
if menu=="2":
    pre=input("Vuoi fare un prelievo? ")
    if pre=="si":
        prevevo=float(input("Quanto vuole prelevare? "))
        constructor.prelievo(prevevo)
        print(constructor.saldo_disponibile)
if menu=="3":
    inv=input("Vuole investire? ")
    if inv=="si":
        investi=float(input("Quanto vuole investire? "))
        constructor.investimento(investi)
        print("Il tuo saldo e': ",constructor.saldo_disponibile)
        print("Il tuo investimento e': ",constructor.patrimonio_investito)
if menu=="4":
    dis=input("Vuole disinvestire? ")
    if dis=="si":
        disinv=float(input("Quanto vuole disinvestire? "))
        constructor.Disinvesti(disinv)
        print("Investimento ora e' di: ",constructor.patrimonio_investito)
        print("Saldo ora e' di: ",constructor.saldo_disponibile)
if menu=="5":
    print(constructor.patrimonio_investito)