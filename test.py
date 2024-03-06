# Importez la fonction que vous souhaitez tester
from app import addition

# Définissez des cas de test avec des assertions
def test_addition():
    assert addition(2, 3) == 5  # 2 + 3 = 5
    assert addition(-1, 1) == 0  # -1 + 1 = 0
    assert addition(0, 0) == 0  # 0 + 0 = 0
    assert addition(-5, -7) == -12  # -5 + (-7) = -12

# Exécutez les tests
if __name__ == "__main__":
    test_addition()
    print("Tous les tests ont réussi!")
