import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotesumma(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu", 3)
        summa = maito.hinta() + mehu.hinta()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.assertEqual(self.kori.hinta(), summa)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_kaksi_kertaa_tuotteen_hinta(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        tulo = 2 * maito1.hinta()
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)
        self.assertEqual(self.kori.hinta(), tulo)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostos_nimi_ja_lukumaara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoksella_on_sama_nimi_ja_lukumaara_kaksi(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito1.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_saman_tuotteen_poistamisen_jalkeen_ostoksen_lukumaara_on_yksi(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)
        self.kori.poista_tuote(maito2)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)