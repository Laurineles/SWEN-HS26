CHF_ZU_EUR = 1.097

class BankKonto:
    def __init__(self, name, startbetrag):
        self.name = name
        self.saldo = startbetrag

    def einbezahlen(self, betrag):
        self.saldo = self.saldo + betrag

    def abheben(self, betrag):
        if betrag <= self.saldo:
            self.saldo = self.saldo - betrag
            return True
        else:
            print("Nicht genug Geld, geh arbeiten")
            return False

    def kontostand(self):
        return self.saldo

    def kontostand_in_eur(self):
        return round(self.saldo * CHF_ZU_EUR, 2)

    def überweisen(self, anderes_konto, betrag):
        if self.abheben(betrag):   
            anderes_konto.einbezahlen(betrag)
        else:
            print(f"{self.name} hat zu wenig Geld")
            
konto_anna = BankKonto("Anna", 200)
konto_peter = BankKonto("Peter", 100)

konto_anna.einbezahlen(100)
print(f"Annas Kontostand: {konto_anna.kontostand()}")

konto_anna.überweisen(konto_peter, 50)
print("Nach der Überweisung:")
print(f"Annas Kontostand: {konto_anna.kontostand()}")
print(f"Peters Kontostand: {konto_peter.kontostand()}")

print(f"Annas Kontostand in Euro: {konto_anna.kontostand_in_eur()}")

konto_peter.abheben(1000)
print(f"Peters Kontostand nach Überziehen: {konto_peter.kontostand()}")