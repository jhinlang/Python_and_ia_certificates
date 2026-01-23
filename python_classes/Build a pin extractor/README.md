# 🔐 Pin Extractor (Python)

## 📌 Description

**Pin Extractor** est un petit projet Python réalisé dans le cadre de la
certification **Python de FreeCodeCamp**.

Le programme permet d'extraire des **codes secrets (PINs)** à partir de
poèmes.\
Chaque poème est analysé ligne par ligne afin de générer un code
numérique basé sur la longueur de certains mots.

La fonction peut traiter **un ou plusieurs poèmes en une seule fois**.

------------------------------------------------------------------------

## 🧠 Principe de fonctionnement

Pour chaque poème :

1.  Le poème est découpé en lignes.
2.  Pour chaque ligne :
    -   On récupère le mot dont l'index correspond au numéro de la
        ligne.
    -   On ajoute au code le **nombre de lettres** de ce mot.
    -   Si le mot n'existe pas, on ajoute `0`.
3.  Le résultat est un **code secret** sous forme de chaîne de
    caractères.
4.  Tous les codes sont stockés dans une liste retournée par la
    fonction.

------------------------------------------------------------------------

## 🛠️ Fonction principale

``` python
def pin_extractor(poems):
```

-   **Paramètre** :
    -   `poems` → liste de chaînes de caractères (chaque chaîne
        représente un poème)
-   **Retour** :
    -   liste de chaînes représentant les codes secrets

------------------------------------------------------------------------

## 📄 Exemples de poèmes

``` python
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"
```

------------------------------------------------------------------------

## ▶️ Exemple d'utilisation

``` python
print(pin_extractor([poem, poem2, poem3]))
```

### Sortie possible

    ['5234', '5444', '11111']

------------------------------------------------------------------------

## 🎯 Objectifs pédagogiques

-   Manipulation des chaînes de caractères
-   Utilisation des listes
-   Boucles `for`
-   Fonction `enumerate`
-   Raisonnement algorithmique

------------------------------------------------------------------------

## 📚 Contexte

Projet réalisé dans le cadre de la **certification Python --
FreeCodeCamp**.\
L'objectif est de comprendre la logique du code et non de copier une
solution.

------------------------------------------------------------------------

## ✅ Statut

✔️ Fonctionnel\
✔️ Conforme aux exigences FreeCodeCamp\
✔️ Compatible Obsidian
