from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return len(self._ostokset)

    def hinta(self):
        return self._ostokset[0].hinta() if self._ostokset else 0

    def lisaa_tuote(self, lisattava: Tuote):
        self._ostokset.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        pass
