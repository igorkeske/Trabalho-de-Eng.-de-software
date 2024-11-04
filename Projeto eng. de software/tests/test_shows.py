# tests/test_shows.py
import unittest
from src.shows import Show, ListaDeShows

class TestListaDeShows(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDeShows()

    def test_adicionar_show(self):
        show = Show("Guns N' Roses", "2024-11-10", "Allianz Parque")
        self.lista.adicionar_show(show)
        self.assertEqual(len(self.lista.shows), 1)

    def test_listar_shows(self):
        show1 = Show("Guns N' Roses", "2024-11-10", "Allianz Parque")
        show2 = Show("Queen", "2024-12-15", "Maracanã")
        self.lista.adicionar_show(show1)
        self.lista.adicionar_show(show2)

        shows = self.lista.listar_shows()
        self.assertEqual(shows, [
            ("Guns N' Roses", "2024-11-10", "Allianz Parque"),
            ("Queen", "2024-12-15", "Maracanã")
        ])

    def test_lista_vazia(self):
        self.assertEqual(self.lista.listar_shows(), [])

if __name__ == '__main__':
    unittest.main()
