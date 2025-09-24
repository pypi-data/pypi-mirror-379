from uncertainties import ufloat
from pint import UnitRegistry

ureg = UnitRegistry()


class Grandeur:
    """
    Une classe pour représenter une grandeur physique avec une valeur,
    une incertitude et une unité.
    """

    def __init__(self, value, uncertainty, unit):
        if isinstance(value, str):
            val, err = self._parse_string(value)
            self.val_inc = ufloat(val, err)
            self.unit = ureg.parse_expression(unit)
        else:
            self.val_inc = ufloat(value, uncertainty)
            self.unit = ureg.parse_expression(unit)

    def _parse_string(self, s):
        """Parse une chaîne de caractères comme '12.34(5)' en valeur et incertitude."""
        if '(' in s and ')' in s:
            val_str, err_str = s.replace(')', '').split('(')
            # Traite l'incertitude sur les derniers chiffres significatifs
            num_decimals_val = len(val_str.split('.')[-1]) if '.' in val_str else 0
            err = int(err_str) * 10 ** (-num_decimals_val)
            return float(val_str), err
        raise ValueError("Format de chaîne invalide. Utilisez 'valeur(incertitude)' ou 'valeur'")

    def __repr__(self):
        """Représentation de l'objet pour l'affichage."""
        return f"{self.val_inc} {self.unit:~}"

    # Exemple de méthode pour une régression linéaire
    @staticmethod
    def linear_regression(x_data, y_data, scipy=None):
        """
        Effectue une régression linéaire sur des données de grandeurs.
        Retourne la pente, l'ordonnée à l'origine, et leurs incertitudes.
        """
        import numpy as np
        from scipy.stats import linregress

        x_values = np.array([g.val_inc.nominal_value for g in x_data])
        y_values = np.array([g.val_inc.nominal_value for g in y_data])
        x_errors = np.array([g.val_inc.std_dev for g in x_data])
        y_errors = np.array([g.val_inc.std_dev for g in y_data])

        # Régression standard
        slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)

        # Les incertitudes des paramètres de la régression sont complexes à calculer
        # manuellement, mais `scipy` fournit `std_err`. On peut l'utiliser comme
        # une première approximation de l'incertitude de la pente.
        # Pour une méthode plus rigoureuse, considérez une régression non linéaire ou
        # une méthode de bootstrap.

        slope_inc = Grandeur(slope, std_err, y_data[0].unit / x_data[0].unit)
        intercept_inc = Grandeur(intercept, std_err * np.mean(x_values), y_data[0].unit)  # Simplification

        return slope_inc, intercept_inc

    # D'autres méthodes peuvent être ajoutées pour les opérations (+, -, *, /, etc.)
    # en utilisant les méthodes magiques de Python.


def monte_carlo_uncertainty(func, n_simulations, *args):
    """
    Calcule l'incertitude d'une fonction via la méthode de Monte-Carlo.
    """
    import numpy as np

    # Génère des échantillons aléatoires pour chaque variable d'entrée
    simulated_values = []
    for _ in range(n_simulations):
        # Pour chaque argument, on échantillonne une valeur selon sa loi normale
        simulated_args = [np.random.normal(arg.val_inc.nominal_value, arg.val_inc.std_dev) for arg in args]

        # On exécute la fonction avec les valeurs simulées
        try:
            result = func(*simulated_args)
            simulated_values.append(result)
        except Exception as e:
            print(f"Erreur lors de la simulation : {e}")
            continue

    if not simulated_values:
        raise ValueError("Aucun résultat valide n'a été obtenu avec la simulation.")

    # Calcule la moyenne et l'écart-type des résultats
    mean_result = np.mean(simulated_values)
    std_dev_result = np.std(simulated_values)

    # On retourne un objet `Grandeur` avec les incertitudes calculées
    return Grandeur(mean_result, std_dev_result, 'dimensionless')
