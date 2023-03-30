from scipy import integrate

# Définir la fonction à intégrer
def f(x):
    return x ** 2

# Calculer l'intégrale de la fonction de 0 à 1
result, error = integrate.quad(f, 0, 1)

# Afficher le résultat
print(f"L'intégrale de x^2 de 0 à 1 est : {result:.3f} avec une erreur de {error:.3e}.")
