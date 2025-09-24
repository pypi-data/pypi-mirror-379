import matplotlib.pyplot as plt

def plot_with_errors(x_data, y_data, title="", xlabel="", ylabel="", fmt='o', figsize=(10, 6)):
    """
    Trace un graphique avec des barres d'erreur pour les données de grandeurs.
    """
    import numpy as np

    x_values = np.array([g.val_inc.nominal_value for g in x_data])
    y_values = np.array([g.val_inc.nominal_value for g in y_data])
    x_errors = np.array([g.val_inc.std_dev for g in x_data])
    y_errors = np.array([g.val_inc.std_dev for g in y_data])

    plt.figure(figsize=figsize)
    plt.errorbar(x_values, y_values, xerr=x_errors, yerr=y_errors, fmt=fmt, capsize=5, label="Points de données")
    plt.title(title)
    plt.xlabel(f"{xlabel} ({x_data[0].unit:~})")
    plt.ylabel(f"{ylabel} ({y_data[0].unit:~})")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()