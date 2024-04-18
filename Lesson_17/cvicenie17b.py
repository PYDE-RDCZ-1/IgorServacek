class Kruh:
    def __init__(self, polomer):
        self.polomer = polomer
    def obsah_kruhu(self):
        return (self.polomer ** 2) * 3.14
    def oprava_polomeru(self, novy_polomer):
        self.polomer = novy_polomer


    kruh1 = Kruh(5)
    kruh1.oprava_polomeru(4)
    obsah = kruh1.obsah_kruhu()
    print(obsah)
# pridajte metódu na nastavenie polomeru