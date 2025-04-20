import papermill as pm

for i in range(1, 14):  # de 1 à 13
    pm.execute_notebook(
        "lakhina.ipynb",  # Notebook source
        f"notebook_dataset_{i}.ipynb",  # Notebook sauvegardé avec un nom unique
        parameters={"chosen_dataset": i}  # Changer le paramètre
    )
    print(f"Exécution terminée pour chosen_dataset = {i}")
