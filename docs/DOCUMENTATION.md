# Documentation — projetkenneth

## 1. Fonctionnement

`main.py` exécute les étapes suivantes :

1. Il redemande le nom tant que la réponse est vide.
2. Il demande l'âge avec la fonction `demander_age()`.
3. Il affiche le nom, l'âge actuel et l'âge de l'année suivante.

## 2. Organisation du code

| Fonction | Rôle |
|---|---|
| `lire_age(saisie)` | Convertit une saisie en âge, ou retourne `None` si elle est invalide |
| `demander_nom()` | Repose la question tant que le nom est vide |
| `demander_age()` | Repose la question tant que l'âge est invalide |
| `creer_message(nom, age)` | Prépare le texte affiché |
| `main()` | Enchaîne les étapes |

Un âge valide est un nombre entier compris entre 1 et 130.

## 3. Tests

```bash
pip install pytest
python -m pytest
```

## 4. Branches

| Branche | Description |
|---|---|
| `main` | Branche principale |
| `python` | Seconde branche du projet |

## 5. Suivi

Trois issues restent ouvertes sur GitHub : `backend`, `frontend` et `gere les conflits`.
