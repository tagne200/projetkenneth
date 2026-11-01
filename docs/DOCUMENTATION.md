# Documentation — projetkenneth

## 1. Fonctionnement

`main.py` exécute les étapes suivantes :

1. Il redemande le nom tant que la réponse est vide.
2. Il demande l'âge avec la fonction `demander_age()`.
3. Il affiche le nom, l'âge actuel et l'âge de l'année suivante.

## 2. Fonction `demander_age()`

La fonction boucle tant que l'âge vaut `0`. Si la saisie n'est pas un nombre, elle affiche un message d'erreur et repose la question.

## 3. Limites connues

- Un âge de `0` est redemandé.
- Un âge négatif est accepté.
- Le bloc `except` capture toutes les erreurs, y compris une interruption au clavier. `except ValueError` serait plus précis.

## 4. Code désactivé

La fin du fichier contient une vérification de mot de passe en commentaire. Elle n'est pas exécutée.

## 5. Branches

| Branche | Description |
|---|---|
| `main` | Branche principale |
| `python` | Seconde branche du projet |

## 6. Suivi

Trois issues restent ouvertes sur GitHub : `backend`, `frontend` et `gere les conflits`.
