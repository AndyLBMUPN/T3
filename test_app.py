
import unittest
from app import calcular_promedio


class TestSistemaAcademico(unittest.TestCase):

    def test_promedio(self):
        self.assertEqual(
            calcular_promedio([14, 16, 18]), 16
        )

    def test_nota_unica(self):
        self.assertEqual(
            calcular_promedio([20]), 20
        )

    def test_sin_notas(self):
        with self.assertRaises(ValueError):
            calcular_promedio([])


if __name__ == "__main__":
    unittest.main()
