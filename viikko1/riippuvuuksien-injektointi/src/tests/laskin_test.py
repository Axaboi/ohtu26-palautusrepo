import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")

    def test_perakkaiset_toimitukset_oikein(self):
        io = StubIO(["2", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        summa_1 = io.outputs[0]

        self.assertEqual(io.outputs[0], summa_1)

        io = StubIO(["3", "4", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        summa_2 = io.outputs[0]

        self.assertEqual(io.outputs[0], summa_2)

        self.assertNotEqual(summa_1, summa_2)