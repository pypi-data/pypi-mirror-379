# educode/exercises.py
"""Base de données des 100 exercices EduCode"""

from .core import Exercise

def get_all_exercises():
    """Retourne la liste complète des 100 exercices"""
    
    exercises = []
    
    # === NIVEAU FACILE (40 exercices) ===
    
    # Fonctions basiques (1-10)
    exercises.extend([
        Exercise(
            id="001",
            title="Fonction carré",
            description="Écrivez une fonction `carre(n)` qui retourne le carré d'un nombre.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "carre", "inputs": [2], "expected": 4},
                {"function": "carre", "inputs": [0], "expected": 0},
                {"function": "carre", "inputs": [-3], "expected": 9},
                {"function": "carre", "inputs": [10], "expected": 100},
            ],
            solution_template="def carre(n):\n    # Votre code ici\n    pass",
            hints=[
                "Un carré c'est n * n",
                "Attention aux nombres négatifs !",
                "N'oubliez pas le return"
            ]
        ),
        
        Exercise(
            id="002", 
            title="Maximum de deux nombres",
            description="Créez une fonction `maximum(a, b)` qui retourne le plus grand des deux nombres.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "maximum", "inputs": [5, 3], "expected": 5},
                {"function": "maximum", "inputs": [1, 8], "expected": 8},
                {"function": "maximum", "inputs": [7, 7], "expected": 7},
                {"function": "maximum", "inputs": [-2, -5], "expected": -2},
            ],
            solution_template="def maximum(a, b):\n    # Utilisez if/else\n    pass"
        ),
        
        Exercise(
            id="003",
            title="Valeur absolue", 
            description="Implémentez une fonction `valeur_absolue(n)` qui retourne la valeur absolue d'un nombre.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "valeur_absolue", "inputs": [5], "expected": 5},
                {"function": "valeur_absolue", "inputs": [-3], "expected": 3},
                {"function": "valeur_absolue", "inputs": [0], "expected": 0},
                {"function": "valeur_absolue", "inputs": [-100], "expected": 100},
            ]
        ),
        
        Exercise(
            id="004",
            title="Pair ou impair",
            description="Écrivez une fonction `est_pair(n)` qui retourne True si n est pair, False sinon.",
            difficulty="facile",
            category="Fonctions basiques", 
            test_cases=[
                {"function": "est_pair", "inputs": [4], "expected": True},
                {"function": "est_pair", "inputs": [7], "expected": False},
                {"function": "est_pair", "inputs": [0], "expected": True},
                {"function": "est_pair", "inputs": [-2], "expected": True},
            ],
            hints=["Utilisez l'opérateur modulo %", "n % 2 == 0 pour les pairs"]
        ),
        
        Exercise(
            id="005",
            title="Calculatrice simple",
            description="Créez une fonction `calculer(a, b, operation)` qui effectue l'opération (+, -, *, /) sur a et b.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "calculer", "inputs": [10, 5, "+"], "expected": 15},
                {"function": "calculer", "inputs": [10, 5, "-"], "expected": 5},
                {"function": "calculer", "inputs": [10, 5, "*"], "expected": 50},
                {"function": "calculer", "inputs": [10, 5, "/"], "expected": 2.0},
            ]
        ),
        
        Exercise(
            id="006",
            title="Température Celsius vers Fahrenheit",
            description="Fonction `celsius_vers_fahrenheit(c)` qui convertit une température.",
            difficulty="facile", 
            category="Fonctions basiques",
            test_cases=[
                {"function": "celsius_vers_fahrenheit", "inputs": [0], "expected": 32.0},
                {"function": "celsius_vers_fahrenheit", "inputs": [100], "expected": 212.0},
                {"function": "celsius_vers_fahrenheit", "inputs": [25], "expected": 77.0},
            ],
            hints=["Formule: F = C * 9/5 + 32"]
        ),
        
        Exercise(
            id="007",
            title="Age en jours",
            description="Fonction `age_en_jours(annees)` qui calcule l'âge approximatif en jours.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "age_en_jours", "inputs": [1], "expected": 365},
                {"function": "age_en_jours", "inputs": [0], "expected": 0},
                {"function": "age_en_jours", "inputs": [2], "expected": 730},
            ]
        ),
        
        Exercise(
            id="008",
            title="Périmètre rectangle",
            description="Fonction `perimetre_rectangle(longueur, largeur)` qui calcule le périmètre.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "perimetre_rectangle", "inputs": [5, 3], "expected": 16},
                {"function": "perimetre_rectangle", "inputs": [2, 2], "expected": 8},
                {"function": "perimetre_rectangle", "inputs": [10, 1], "expected": 22},
            ]
        ),
        
        Exercise(
            id="009",
            title="Moyenne de trois nombres",
            description="Fonction `moyenne_trois(a, b, c)` qui calcule la moyenne arithmétique.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "moyenne_trois", "inputs": [1, 2, 3], "expected": 2.0},
                {"function": "moyenne_trois", "inputs": [10, 20, 30], "expected": 20.0},
                {"function": "moyenne_trois", "inputs": [0, 0, 0], "expected": 0.0},
            ]
        ),
        
        Exercise(
            id="010",
            title="Nombre positif, négatif ou zéro",
            description="Fonction `signe(n)` qui retourne 'positif', 'négatif' ou 'zéro'.",
            difficulty="facile",
            category="Fonctions basiques",
            test_cases=[
                {"function": "signe", "inputs": [5], "expected": "positif"},
                {"function": "signe", "inputs": [-3], "expected": "négatif"},
                {"function": "signe", "inputs": [0], "expected": "zéro"},
            ]
        ),
    ])
    
    # Chaînes de caractères (11-20)
    exercises.extend([
        Exercise(
            id="011",
            title="Longueur d'une chaîne",
            description="Fonction `longueur_chaine(s)` qui retourne le nombre de caractères.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "longueur_chaine", "inputs": ["hello"], "expected": 5},
                {"function": "longueur_chaine", "inputs": [""], "expected": 0},
                {"function": "longueur_chaine", "inputs": ["Python"], "expected": 6},
            ]
        ),
        
        Exercise(
            id="012",
            title="Premier caractère",
            description="Fonction `premier_caractere(s)` qui retourne le premier caractère d'une chaîne non vide.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "premier_caractere", "inputs": ["hello"], "expected": "h"},
                {"function": "premier_caractere", "inputs": ["Python"], "expected": "P"},
                {"function": "premier_caractere", "inputs": ["a"], "expected": "a"},
            ]
        ),
        
        Exercise(
            id="013",
            title="Derniers caractères",
            description="Fonction `dernier_caractere(s)` qui retourne le dernier caractère.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "dernier_caractere", "inputs": ["hello"], "expected": "o"},
                {"function": "dernier_caractere", "inputs": ["Python"], "expected": "n"},
                {"function": "dernier_caractere", "inputs": ["a"], "expected": "a"},
            ]
        ),
        
        Exercise(
            id="014",
            title="Inverser une chaîne",
            description="Fonction `inverser_chaine(s)` qui retourne la chaîne inversée.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "inverser_chaine", "inputs": ["hello"], "expected": "olleh"},
                {"function": "inverser_chaine", "inputs": ["abc"], "expected": "cba"},
                {"function": "inverser_chaine", "inputs": ["a"], "expected": "a"},
            ],
            hints=["Utilisez le slicing s[::-1]"]
        ),
        
        Exercise(
            id="015",
            title="Répéter une chaîne",
            description="Fonction `repeter_chaine(s, n)` qui répète la chaîne n fois.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "repeter_chaine", "inputs": ["hello", 3], "expected": "hellohellohello"},
                {"function": "repeter_chaine", "inputs": ["a", 5], "expected": "aaaaa"},
                {"function": "repeter_chaine", "inputs": ["test", 0], "expected": ""},
            ]
        ),
        
        Exercise(
            id="016",
            title="Compter les voyelles",
            description="Fonction `compter_voyelles(s)` qui compte le nombre de voyelles (a,e,i,o,u).",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "compter_voyelles", "inputs": ["hello"], "expected": 2},
                {"function": "compter_voyelles", "inputs": ["aeiou"], "expected": 5},
                {"function": "compter_voyelles", "inputs": ["bcdfg"], "expected": 0},
                {"function": "compter_voyelles", "inputs": ["Python"], "expected": 1},
            ]
        ),
        
        Exercise(
            id="017",
            title="Enlever les espaces",
            description="Fonction `enlever_espaces(s)` qui supprime tous les espaces.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "enlever_espaces", "inputs": ["hello world"], "expected": "helloworld"},
                {"function": "enlever_espaces", "inputs": ["a b c"], "expected": "abc"},
                {"function": "enlever_espaces", "inputs": ["nospace"], "expected": "nospace"},
            ]
        ),
        
        Exercise(
            id="018",
            title="Première lettre majuscule",
            description="Fonction `premiere_majuscule(s)` qui met la première lettre en majuscule.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "premiere_majuscule", "inputs": ["hello"], "expected": "Hello"},
                {"function": "premiere_majuscule", "inputs": ["python"], "expected": "Python"},
                {"function": "premiere_majuscule", "inputs": ["A"], "expected": "A"},
            ]
        ),
        
        Exercise(
            id="019",
            title="Contient caractère",
            description="Fonction `contient_caractere(s, c)` qui vérifie si la chaîne contient le caractère.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "contient_caractere", "inputs": ["hello", "e"], "expected": True},
                {"function": "contient_caractere", "inputs": ["hello", "x"], "expected": False},
                {"function": "contient_caractere", "inputs": ["Python", "P"], "expected": True},
            ]
        ),
        
        Exercise(
            id="020",
            title="Concaténer avec séparateur",
            description="Fonction `concatener_avec_sep(a, b, sep)` qui joint deux chaînes avec un séparateur.",
            difficulty="facile",
            category="Chaînes de caractères",
            test_cases=[
                {"function": "concatener_avec_sep", "inputs": ["hello", "world", " "], "expected": "hello world"},
                {"function": "concatener_avec_sep", "inputs": ["a", "b", "-"], "expected": "a-b"},
                {"function": "concatener_avec_sep", "inputs": ["test", "case", "_"], "expected": "test_case"},
            ]
        ),
    ])
    
    # Listes basiques (21-30)
    exercises.extend([
        Exercise(
            id="021",
            title="Somme d'une liste",
            description="Fonction `somme_liste(liste)` qui calcule la somme de tous les éléments.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "somme_liste", "inputs": [[1, 2, 3, 4]], "expected": 10},
                {"function": "somme_liste", "inputs": [[-1, 1, -2, 2]], "expected": 0},
                {"function": "somme_liste", "inputs": [[]], "expected": 0},
                {"function": "somme_liste", "inputs": [[5]], "expected": 5},
            ]
        ),
        
        Exercise(
            id="022", 
            title="Maximum d'une liste",
            description="Fonction `max_liste(liste)` qui trouve le plus grand élément.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "max_liste", "inputs": [[1, 5, 2, 8, 3]], "expected": 8},
                {"function": "max_liste", "inputs": [[-1, -5, -2]], "expected": -1},
                {"function": "max_liste", "inputs": [[7]], "expected": 7},
            ]
        ),
        
        Exercise(
            id="023",
            title="Minimum d'une liste",
            description="Fonction `min_liste(liste)` qui trouve le plus petit élément.", 
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "min_liste", "inputs": [[1, 5, 2, 8, 3]], "expected": 1},
                {"function": "min_liste", "inputs": [[-1, -5, -2]], "expected": -5},
                {"function": "min_liste", "inputs": [[7]], "expected": 7},
            ]
        ),
        
        Exercise(
            id="024",
            title="Longueur d'une liste",
            description="Fonction `longueur_liste(liste)` qui retourne le nombre d'éléments.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "longueur_liste", "inputs": [[1, 2, 3]], "expected": 3},
                {"function": "longueur_liste", "inputs": [[]], "expected": 0},
                {"function": "longueur_liste", "inputs": [['a', 'b', 'c', 'd', 'e']], "expected": 5},
            ]
        ),
        
        Exercise(
            id="025",
            title="Premier élément",
            description="Fonction `premier_element(liste)` qui retourne le premier élément d'une liste non vide.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "premier_element", "inputs": [[1, 2, 3]], "expected": 1},
                {"function": "premier_element", "inputs": [['hello', 'world']], "expected": "hello"},
                {"function": "premier_element", "inputs": [[42]], "expected": 42},
            ]
        ),
        
        Exercise(
            id="026",
            title="Dernier élément",
            description="Fonction `dernier_element(liste)` qui retourne le dernier élément.",
            difficulty="facile",
            category="Listes basiques", 
            test_cases=[
                {"function": "dernier_element", "inputs": [[1, 2, 3]], "expected": 3},
                {"function": "dernier_element", "inputs": [['hello', 'world']], "expected": "world"},
                {"function": "dernier_element", "inputs": [[42]], "expected": 42},
            ]
        ),
        
        Exercise(
            id="027",
            title="Inverser une liste",
            description="Fonction `inverser_liste(liste)` qui retourne la liste inversée.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "inverser_liste", "inputs": [[1, 2, 3]], "expected": [3, 2, 1]},
                {"function": "inverser_liste", "inputs": [['a', 'b', 'c']], "expected": ['c', 'b', 'a']},
                {"function": "inverser_liste", "inputs": [[42]], "expected": [42]},
            ]
        ),
        
        Exercise(
            id="028",
            title="Compter occurrences",
            description="Fonction `compter_occurrences(liste, element)` qui compte les occurrences d'un élément.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "compter_occurrences", "inputs": [[1, 2, 1, 3, 1], 1], "expected": 3},
                {"function": "compter_occurrences", "inputs": [['a', 'b', 'a', 'c'], 'a'], "expected": 2},
                {"function": "compter_occurrences", "inputs": [[1, 2, 3], 5], "expected": 0},
            ]
        ),
        
        Exercise(
            id="029",
            title="Contient élément",
            description="Fonction `contient_element(liste, element)` qui vérifie la présence d'un élément.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "contient_element", "inputs": [[1, 2, 3], 2], "expected": True},
                {"function": "contient_element", "inputs": [['a', 'b', 'c'], 'd'], "expected": False},
                {"function": "contient_element", "inputs": [[1, 2, 3], 3], "expected": True},
            ]
        ),
        
        Exercise(
            id="030",
            title="Joindre listes",
            description="Fonction `joindre_listes(liste1, liste2)` qui concatène deux listes.",
            difficulty="facile",
            category="Listes basiques",
            test_cases=[
                {"function": "joindre_listes", "inputs": [[1, 2], [3, 4]], "expected": [1, 2, 3, 4]},
                {"function": "joindre_listes", "inputs": [[], [1, 2]], "expected": [1, 2]},
                {"function": "joindre_listes", "inputs": [['a'], ['b', 'c']], "expected": ['a', 'b', 'c']},
            ]
        ),
    ])
    
    # Boucles et conditions (31-40)
    exercises.extend([
        Exercise(
            id="031",
            title="Nombres de 1 à N",
            description="Fonction `nombres_un_a_n(n)` qui retourne une liste des nombres de 1 à n.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "nombres_un_a_n", "inputs": [5], "expected": [1, 2, 3, 4, 5]},
                {"function": "nombres_un_a_n", "inputs": [1], "expected": [1]},
                {"function": "nombres_un_a_n", "inputs": [3], "expected": [1, 2, 3]},
            ]
        ),
        
        Exercise(
            id="032",
            title="Somme des N premiers entiers",
            description="Fonction `somme_n_premiers(n)` qui calcule 1 + 2 + ... + n.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "somme_n_premiers", "inputs": [5], "expected": 15},
                {"function": "somme_n_premiers", "inputs": [1], "expected": 1},
                {"function": "somme_n_premiers", "inputs": [10], "expected": 55},
            ]
        ),
        
        Exercise(
            id="033", 
            title="Table de multiplication",
            description="Fonction `table_multiplication(n)` qui retourne la table de n (n×1 à n×10).",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "table_multiplication", "inputs": [2], "expected": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]},
                {"function": "table_multiplication", "inputs": [5], "expected": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]},
            ]
        ),
        
        Exercise(
            id="034",
            title="Nombres pairs jusqu'à N",
            description="Fonction `nombres_pairs(n)` qui retourne tous les nombres pairs de 0 à n.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "nombres_pairs", "inputs": [10], "expected": [0, 2, 4, 6, 8, 10]},
                {"function": "nombres_pairs", "inputs": [5], "expected": [0, 2, 4]},
                {"function": "nombres_pairs", "inputs": [1], "expected": [0]},
            ]
        ),
        
        Exercise(
            id="035",
            title="Factorielle",
            description="Fonction `factorielle(n)` qui calcule n! = n × (n-1) × ... × 1.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "factorielle", "inputs": [5], "expected": 120},
                {"function": "factorielle", "inputs": [0], "expected": 1},
                {"function": "factorielle", "inputs": [3], "expected": 6},
                {"function": "factorielle", "inputs": [1], "expected": 1},
            ],
            hints=["Par convention, 0! = 1", "Utilisez une boucle for ou while"]
        ),
        
        Exercise(
            id="036",
            title="Compter les chiffres",
            description="Fonction `compter_chiffres(n)` qui compte le nombre de chiffres d'un entier.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "compter_chiffres", "inputs": [123], "expected": 3},
                {"function": "compter_chiffres", "inputs": [7], "expected": 1},
                {"function": "compter_chiffres", "inputs": [1000], "expected": 4},
                {"function": "compter_chiffres", "inputs": [0], "expected": 1},
            ]
        ),
        
        Exercise(
            id="037",
            title="Somme des chiffres",
            description="Fonction `somme_chiffres(n)` qui additionne tous les chiffres d'un nombre.",
            difficulty="facile",
            category="Boucles et conditions", 
            test_cases=[
                {"function": "somme_chiffres", "inputs": [123], "expected": 6},
                {"function": "somme_chiffres", "inputs": [999], "expected": 27},
                {"function": "somme_chiffres", "inputs": [0], "expected": 0},
                {"function": "somme_chiffres", "inputs": [5], "expected": 5},
            ]
        ),
        
        Exercise(
            id="038",
            title="Puissance",
            description="Fonction `puissance(base, exposant)` qui calcule base^exposant sans utiliser **.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "puissance", "inputs": [2, 3], "expected": 8},
                {"function": "puissance", "inputs": [5, 0], "expected": 1},
                {"function": "puissance", "inputs": [3, 2], "expected": 9},
                {"function": "puissance", "inputs": [10, 1], "expected": 10},
            ]
        ),
        
        Exercise(
            id="039",
            title="PGCD (Plus Grand Commun Diviseur)",
            description="Fonction `pgcd(a, b)` qui calcule le PGCD de deux nombres.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "pgcd", "inputs": [48, 18], "expected": 6},
                {"function": "pgcd", "inputs": [7, 5], "expected": 1},
                {"function": "pgcd", "inputs": [12, 8], "expected": 4},
            ],
            hints=["Utilisez l'algorithme d'Euclide", "Tant que b != 0: a, b = b, a % b"]
        ),
        
        Exercise(
            id="040",
            title="Suite de Fibonacci",
            description="Fonction `fibonacci(n)` qui retourne le n-ième nombre de Fibonacci.",
            difficulty="facile",
            category="Boucles et conditions",
            test_cases=[
                {"function": "fibonacci", "inputs": [0], "expected": 0},
                {"function": "fibonacci", "inputs": [1], "expected": 1},
                {"function": "fibonacci", "inputs": [5], "expected": 5},
                {"function": "fibonacci", "inputs": [10], "expected": 55},
            ],
            hints=["F(0)=0, F(1)=1", "F(n) = F(n-1) + F(n-2)"]
        ),
    ])
    
    # === NIVEAU MOYEN (40 exercices) ===
    
    # Listes et algorithmes (41-55)
    exercises.extend([
        Exercise(
            id="041",
            title="Tri à bulles",
            description="Fonction `tri_bulles(liste)` qui trie une liste avec l'algorithme du tri à bulles.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "tri_bulles", "inputs": [[3, 1, 4, 1, 5]], "expected": [1, 1, 3, 4, 5]},
                {"function": "tri_bulles", "inputs": [[5, 4, 3, 2, 1]], "expected": [1, 2, 3, 4, 5]},
                {"function": "tri_bulles", "inputs": [[1]], "expected": [1]},
            ],
            hints=["Comparez les éléments adjacents", "Échangez si nécessaire", "Répétez jusqu'à ce que trié"]
        ),
        
        Exercise(
            id="042",
            title="Recherche linéaire", 
            description="Fonction `recherche_lineaire(liste, element)` qui retourne l'index de l'élément (-1 si absent).",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "recherche_lineaire", "inputs": [[1, 3, 5, 7], 5], "expected": 2},
                {"function": "recherche_lineaire", "inputs": [[1, 3, 5, 7], 6], "expected": -1},
                {"function": "recherche_lineaire", "inputs": [['a', 'b', 'c'], 'b'], "expected": 1},
            ]
        ),
        
        Exercise(
            id="043",
            title="Suppression des doublons",
            description="Fonction `supprimer_doublons(liste)` qui supprime les éléments dupliqués.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "supprimer_doublons", "inputs": [[1, 2, 2, 3, 1]], "expected": [1, 2, 3]},
                {"function": "supprimer_doublons", "inputs": [['a', 'b', 'a', 'c']], "expected": ['a', 'b', 'c']},
                {"function": "supprimer_doublons", "inputs": [[1, 2, 3]], "expected": [1, 2, 3]},
            ]
        ),
        
        Exercise(
            id="044",
            title="Rotation de liste",
            description="Fonction `rotation_liste(liste, n)` qui effectue une rotation de n positions vers la droite.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "rotation_liste", "inputs": [[1, 2, 3, 4, 5], 2], "expected": [4, 5, 1, 2, 3]},
                {"function": "rotation_liste", "inputs": [['a', 'b', 'c'], 1], "expected": ['c', 'a', 'b']},
                {"function": "rotation_liste", "inputs": [[1, 2, 3], 0], "expected": [1, 2, 3]},
            ]
        ),
        
        Exercise(
            id="045",
            title="Intersection de listes",
            description="Fonction `intersection(liste1, liste2)` qui retourne les éléments communs.",
            difficulty="moyen",
            category="Listes et algorithmes", 
            test_cases=[
                {"function": "intersection", "inputs": [[1, 2, 3], [2, 3, 4]], "expected": [2, 3]},
                {"function": "intersection", "inputs": [['a', 'b'], ['b', 'c']], "expected": ['b']},
                {"function": "intersection", "inputs": [[1, 2], [3, 4]], "expected": []},
            ]
        ),
        
        Exercise(
            id="046",
            title="Aplatir une liste de listes",
            description="Fonction `aplatir(liste_de_listes)` qui transforme [[1,2], [3,4]] en [1,2,3,4].",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "aplatir", "inputs": [[[1, 2], [3, 4]]], "expected": [1, 2, 3, 4]},
                {"function": "aplatir", "inputs": [[['a'], ['b', 'c']]], "expected": ['a', 'b', 'c']},
                {"function": "aplatir", "inputs": [[[], [1, 2]]], "expected": [1, 2]},
            ]
        ),
        
        Exercise(
            id="047",
            title="Partition paire/impaire",
            description="Fonction `partition_paire_impaire(liste)` qui sépare les nombres pairs et impairs.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "partition_paire_impaire", "inputs": [[1, 2, 3, 4, 5]], "expected": ([2, 4], [1, 3, 5])},
                {"function": "partition_paire_impaire", "inputs": [[2, 4, 6]], "expected": ([2, 4, 6], [])},
                {"function": "partition_paire_impaire", "inputs": [[1, 3, 5]], "expected": ([], [1, 3, 5])},
            ]
        ),
        
        Exercise(
            id="048",
            title="Sous-séquence croissante maximale",
            description="Fonction `sous_sequence_croissante(liste)` qui trouve la plus longue sous-séquence croissante.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "sous_sequence_croissante", "inputs": [[1, 3, 2, 4, 5]], "expected": [1, 2, 4, 5]},
                {"function": "sous_sequence_croissante", "inputs": [[5, 4, 3, 2, 1]], "expected": [5]},
                {"function": "sous_sequence_croissante", "inputs": [[1, 2, 3]], "expected": [1, 2, 3]},
            ]
        ),
        
        Exercise(
            id="049",
            title="Somme de sous-liste maximale",
            description="Fonction `somme_max_sous_liste(liste)` qui trouve la somme maximale d'une sous-liste contiguë.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "somme_max_sous_liste", "inputs": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "expected": 6},
                {"function": "somme_max_sous_liste", "inputs": [[1, 2, 3, 4]], "expected": 10},
                {"function": "somme_max_sous_liste", "inputs": [[-1, -2, -3]], "expected": -1},
            ],
            hints=["Algorithme de Kadane", "Gardez trace de la somme max locale et globale"]
        ),
        
        Exercise(
            id="050",
            title="Mélanger une liste",
            description="Fonction `melanger_liste(liste)` qui mélange aléatoirement les éléments (algorithme Fisher-Yates).",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "melanger_liste", "inputs": [[1, 2, 3, 4, 5]], "expected": "ANY"},  # Test spécial
            ],
            hints=["Utilisez random.randint", "Échangez chaque élément avec un élément aléatoire"]
        ),
        
        Exercise(
            id="051",
            title="Produit cartésien",
            description="Fonction `produit_cartesien(liste1, liste2)` qui génère tous les couples (a,b).",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "produit_cartesien", "inputs": [[1, 2], ['a', 'b']], "expected": [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]},
                {"function": "produit_cartesien", "inputs": [[1], [2]], "expected": [(1, 2)]},
            ]
        ),
        
        Exercise(
            id="052",
            title="Médiane d'une liste",
            description="Fonction `mediane(liste)` qui calcule la médiane d'une liste de nombres.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "mediane", "inputs": [[1, 2, 3, 4, 5]], "expected": 3},
                {"function": "mediane", "inputs": [[1, 2, 3, 4]], "expected": 2.5},
                {"function": "mediane", "inputs": [[7]], "expected": 7},
            ]
        ),
        
        Exercise(
            id="053",
            title="Mode statistique",
            description="Fonction `mode_statistique(liste)` qui trouve l'élément le plus fréquent.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "mode_statistique", "inputs": [[1, 2, 2, 3, 2]], "expected": 2},
                {"function": "mode_statistique", "inputs": [['a', 'b', 'a', 'c', 'a']], "expected": 'a'},
                {"function": "mode_statistique", "inputs": [[1, 1, 2, 2]], "expected": 1},  # Premier trouvé
            ]
        ),
        
        Exercise(
            id="054",
            title="Générer permutations",
            description="Fonction `permutations(liste)` qui génère toutes les permutations d'une liste.",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "permutations", "inputs": [[1, 2, 3]], "expected": [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]},
                {"function": "permutations", "inputs": [['a', 'b']], "expected": [['a', 'b'], ['b', 'a']]},
            ]
        ),
        
        Exercise(
            id="055",
            title="Compression RLE",
            description="Fonction `compression_rle(liste)` qui compresse avec Run Length Encoding. Ex: [1,1,2,3,3,3] -> [(1,2), (2,1), (3,3)].",
            difficulty="moyen",
            category="Listes et algorithmes",
            test_cases=[
                {"function": "compression_rle", "inputs": [[1, 1, 2, 3, 3, 3]], "expected": [(1, 2), (2, 1), (3, 3)]},
                {"function": "compression_rle", "inputs": [['a', 'a', 'b', 'c', 'c']], "expected": [('a', 2), ('b', 1), ('c', 2)]},
                {"function": "compression_rle", "inputs": [[1, 2, 3]], "expected": [(1, 1), (2, 1), (3, 1)]},
            ]
        ),
    ])
    
    # Dictionnaires et structures (56-70)
    exercises.extend([
        Exercise(
            id="056",
            title="Compter fréquences",
            description="Fonction `compter_frequences(liste)` qui retourne un dictionnaire {élément: nombre_occurrences}.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "compter_frequences", "inputs": [['a', 'b', 'a', 'c', 'b', 'a']], "expected": {'a': 3, 'b': 2, 'c': 1}},
                {"function": "compter_frequences", "inputs": [[1, 2, 1, 1]], "expected": {1: 3, 2: 1}},
                {"function": "compter_frequences", "inputs": [[]], "expected": {}},
            ]
        ),
        
        Exercise(
            id="057",
            title="Fusionner dictionnaires",
            description="Fonction `fusionner_dicts(dict1, dict2)` qui combine deux dictionnaires (dict2 prioritaire).",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "fusionner_dicts", "inputs": [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}], "expected": {'a': 1, 'b': 3, 'c': 4}},
                {"function": "fusionner_dicts", "inputs": [{}, {'x': 1}], "expected": {'x': 1}},
                {"function": "fusionner_dicts", "inputs": [{'a': 1}, {}], "expected": {'a': 1}},
            ]
        ),
        
        Exercise(
            id="058",
            title="Inverser dictionnaire",
            description="Fonction `inverser_dictionnaire(d)` qui échange clés et valeurs.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "inverser_dictionnaire", "inputs": [{'a': 1, 'b': 2}], "expected": {1: 'a', 2: 'b'}},
                {"function": "inverser_dictionnaire", "inputs": [{'x': 'hello', 'y': 'world'}], "expected": {'hello': 'x', 'world': 'y'}},
            ]
        ),
        
        Exercise(
            id="059",
            title="Filtrer dictionnaire",
            description="Fonction `filtrer_dict(d, condition)` qui garde seulement les éléments où condition(valeur) est True.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "filtrer_dict", "inputs": [{'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1], "expected": {'b': 2, 'c': 3}},
                {"function": "filtrer_dict", "inputs": [{'x': 10, 'y': 5, 'z': 15}, lambda x: x >= 10], "expected": {'x': 10, 'z': 15}},
            ]
        ),
        
        Exercise(
            id="060",
            title="Grouper par clé",
            description="Fonction `grouper_par_cle(liste_dicts, cle)` qui groupe les dictionnaires par une clé commune.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "grouper_par_cle", "inputs": [[{'nom': 'Alice', 'age': 25}, {'nom': 'Bob', 'age': 25}, {'nom': 'Charlie', 'age': 30}], 'age'], "expected": {25: [{'nom': 'Alice', 'age': 25}, {'nom': 'Bob', 'age': 25}], 30: [{'nom': 'Charlie', 'age': 30}]}},
            ]
        ),
        
        Exercise(
            id="061",
            title="Valeurs par défaut",
            description="Fonction `dict_avec_defauts(d, defauts)` qui ajoute les valeurs par défaut manquantes.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "dict_avec_defauts", "inputs": [{'a': 1}, {'a': 10, 'b': 2, 'c': 3}], "expected": {'a': 1, 'b': 2, 'c': 3}},
                {"function": "dict_avec_defauts", "inputs": [{}, {'x': 1, 'y': 2}], "expected": {'x': 1, 'y': 2}},
            ]
        ),
        
        Exercise(
            id="062",
            title="Clés communes",
            description="Fonction `cles_communes(dict1, dict2)` qui retourne les clés présentes dans les deux dictionnaires.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "cles_communes", "inputs": [{'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6}], "expected": ['b', 'c']},
                {"function": "cles_communes", "inputs": [{'x': 1}, {'y': 2}], "expected": []},
            ]
        ),
        
        Exercise(
            id="063",
            title="Statistiques liste",
            description="Fonction `stats_liste(liste)` qui retourne {'min': ..., 'max': ..., 'moyenne': ..., 'total': ...}.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "stats_liste", "inputs": [[1, 2, 3, 4, 5]], "expected": {'min': 1, 'max': 5, 'moyenne': 3.0, 'total': 15}},
                {"function": "stats_liste", "inputs": [[10]], "expected": {'min': 10, 'max': 10, 'moyenne': 10.0, 'total': 10}},
            ]
        ),
        
        Exercise(
            id="064",
            title="Cache LRU simple",
            description="Fonction `cache_lru(taille_max)` qui retourne un dictionnaire cache avec méthodes get/set LRU.",
            difficulty="moyen", 
            category="Dictionnaires et structures",
            test_cases=[
                # Test complexe - on testera manuellement
            ]
        ),
        
        Exercise(
            id="065",
            title="Dictionnaire aplati",
            description="Fonction `aplatir_dict(d, separateur='.')` qui transforme {'a': {'b': 1}} en {'a.b': 1}.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "aplatir_dict", "inputs": [{'a': {'b': 1, 'c': 2}, 'd': 3}, '.'], "expected": {'a.b': 1, 'a.c': 2, 'd': 3}},
                {"function": "aplatir_dict", "inputs": [{'x': {'y': {'z': 1}}}, '_'], "expected": {'x_y_z': 1}},
            ]
        ),
        
        Exercise(
            id="066",
            title="Différence entre dictionnaires",
            description="Fonction `diff_dicts(dict1, dict2)` qui retourne les différences entre deux dictionnaires.",
            difficulty="moyen",
            category="Dictionnaires et structures", 
            test_cases=[
                {"function": "diff_dicts", "inputs": [{'a': 1, 'b': 2}, {'a': 1, 'b': 3, 'c': 4}], "expected": {'modifié': {'b': (2, 3)}, 'ajouté': {'c': 4}, 'supprimé': {}}},
            ]
        ),
        
        Exercise(
            id="067",
            title="Tri par valeurs dictionnaire",
            description="Fonction `trier_dict_par_valeurs(d, reverse=False)` qui trie un dictionnaire par ses valeurs.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "trier_dict_par_valeurs", "inputs": [{'a': 3, 'b': 1, 'c': 2}, False], "expected": {'b': 1, 'c': 2, 'a': 3}},
                {"function": "trier_dict_par_valeurs", "inputs": [{'x': 10, 'y': 5}, True], "expected": {'x': 10, 'y': 5}},
            ]
        ),
        
        Exercise(
            id="068",
            title="Index inversé",
            description="Fonction `creer_index_inverse(documents)` qui crée un index mot -> [liste_documents].",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "creer_index_inverse", "inputs": [["hello world", "world peace", "hello peace"]], "expected": {'hello': [0, 2], 'world': [0, 1], 'peace': [1, 2]}},
            ]
        ),
        
        Exercise(
            id="069",
            title="Dictionnaire à deux dimensions",
            description="Fonction `dict_2d()` qui crée un dictionnaire permettant d[x][y] = valeur avec création automatique.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                # Test spécial pour classe/objet
            ]
        ),
        
        Exercise(
            id="070",
            title="Sérialisation dictionnaire",
            description="Fonction `serialiser_dict(d)` qui transforme un dictionnaire en chaîne 'cle1=val1;cle2=val2'.",
            difficulty="moyen",
            category="Dictionnaires et structures",
            test_cases=[
                {"function": "serialiser_dict", "inputs": [{'a': 1, 'b': 2}], "expected": "a=1;b=2"},
                {"function": "serialiser_dict", "inputs": [{'x': 'hello', 'y': 'world'}], "expected": "x=hello;y=world"},
            ]
        ),
    ])
    
    # Chaînes avancées (71-80)
    exercises.extend([
        Exercise(
            id="071",
            title="Palindrome",
            description="Fonction `est_palindrome(s)` qui vérifie si une chaîne est un palindrome (ignore la casse et espaces).",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "est_palindrome", "inputs": ["A man a plan a canal Panama"], "expected": True},
                {"function": "est_palindrome", "inputs": ["race a car"], "expected": False},
                {"function": "est_palindrome", "inputs": ["Madam"], "expected": True},
            ],
            hints=["Supprimez espaces et ponctuation", "Comparez avec la version inversée"]
        ),
        
        Exercise(
            id="072",
            title="Anagrammes",
            description="Fonction `sont_anagrammes(s1, s2)` qui vérifie si deux chaînes sont anagrammes.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "sont_anagrammes", "inputs": ["listen", "silent"], "expected": True},
                {"function": "sont_anagrammes", "inputs": ["hello", "world"], "expected": False},
                {"function": "sont_anagrammes", "inputs": ["evil", "vile"], "expected": True},
            ]
        ),
        
        Exercise(
            id="073",
            title="Rotation de chaînes",
            description="Fonction `est_rotation(s1, s2)` qui vérifie si s2 est une rotation de s1.",
            difficulty="moyen", 
            category="Chaînes avancées",
            test_cases=[
                {"function": "est_rotation", "inputs": ["abcde", "cdeab"], "expected": True},
                {"function": "est_rotation", "inputs": ["abcde", "abced"], "expected": False},
                {"function": "est_rotation", "inputs": ["hello", "llohe"], "expected": True},
            ],
            hints=["s2 doit être dans s1 + s1"]
        ),
        
        Exercise(
            id="074",
            title="Compression de chaînes",
            description="Fonction `comprimer_chaine(s)` qui compresse 'aabcccccaaa' en 'a2b1c5a3'.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "comprimer_chaine", "inputs": ["aabcccccaaa"], "expected": "a2b1c5a3"},
                {"function": "comprimer_chaine", "inputs": ["abc"], "expected": "abc"},  # Plus court que compressé
                {"function": "comprimer_chaine", "inputs": ["aabbcc"], "expected": "a2b2c2"},
            ]
        ),
        
        Exercise(
            id="075",
            title="Sous-chaîne commune la plus longue",
            description="Fonction `plus_longue_sous_chaine_commune(s1, s2)` qui trouve la LCS.",
            difficulty="moyen",
            category="Chaînes avancées", 
            test_cases=[
                {"function": "plus_longue_sous_chaine_commune", "inputs": ["ABCDGH", "AEDFHR"], "expected": "ADH"},
                {"function": "plus_longue_sous_chaine_commune", "inputs": ["ABC", "DEF"], "expected": ""},
                {"function": "plus_longue_sous_chaine_commune", "inputs": ["HELLO", "YELLOW"], "expected": "ELLO"},
            ]
        ),
        
        Exercise(
            id="076",
            title="Distance d'édition",
            description="Fonction `distance_edition(s1, s2)` qui calcule la distance de Levenshtein.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "distance_edition", "inputs": ["kitten", "sitting"], "expected": 3},
                {"function": "distance_edition", "inputs": ["hello", "hello"], "expected": 0},
                {"function": "distance_edition", "inputs": ["abc", "def"], "expected": 3},
            ]
        ),
        
        Exercise(
            id="077",
            title="Validation expression régulière simple",
            description="Fonction `valider_regex_simple(texte, motif)` qui valide avec * et ? seulement.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "valider_regex_simple", "inputs": ["hello", "h*o"], "expected": False},
                {"function": "valider_regex_simple", "inputs": ["hello", "he*o"], "expected": False},
                {"function": "valider_regex_simple", "inputs": ["heo", "he*o"], "expected": True},
            ]
        ),
        
        Exercise(
            id="078",
            title="Formatage de texte",
            description="Fonction `formater_texte(texte, largeur)` qui justifie le texte sur une largeur donnée.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "formater_texte", "inputs": ["hello world this is a test", 10], "expected": ["hello     ", "world this", "is a test "]},
            ]
        ),
        
        Exercise(
            id="079",
            title="Extraction de mots",
            description="Fonction `extraire_mots(texte)` qui extrait tous les mots (lettres seulement).",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "extraire_mots", "inputs": ["Hello, world! How are you?"], "expected": ["Hello", "world", "How", "are", "you"]},
                {"function": "extraire_mots", "inputs": ["123 abc 456 def"], "expected": ["abc", "def"]},
            ]
        ),
        
        Exercise(
            id="080",
            title="Camel case vers snake case",
            description="Fonction `camel_vers_snake(s)` qui transforme 'camelCase' en 'camel_case'.",
            difficulty="moyen",
            category="Chaînes avancées",
            test_cases=[
                {"function": "camel_vers_snake", "inputs": ["camelCase"], "expected": "camel_case"},
                {"function": "camel_vers_snake", "inputs": ["XMLHttpRequest"], "expected": "xml_http_request"},
                {"function": "camel_vers_snake", "inputs": ["snake_case"], "expected": "snake_case"},
            ]
        ),
    ])
    
    # === NIVEAU DIFFICILE (20 exercices) ===
    
    # Algorithmes complexes (81-90)
    exercises.extend([
        Exercise(
            id="081",
            title="Recherche binaire",
            description="Fonction `recherche_binaire(liste_triee, element)` qui utilise la recherche binaire.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "recherche_binaire", "inputs": [[1, 3, 5, 7, 9, 11], 7], "expected": 3},
                {"function": "recherche_binaire", "inputs": [[1, 3, 5, 7, 9, 11], 4], "expected": -1},
                {"function": "recherche_binaire", "inputs": [[1], 1], "expected": 0},
            ],
            hints=["Comparez avec l'élément du milieu", "Réduisez l'espace de recherche de moitié"]
        ),
        
        Exercise(
            id="082",
            title="Tri rapide (QuickSort)",
            description="Fonction `tri_rapide(liste)` qui implémente l'algorithme de tri rapide.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "tri_rapide", "inputs": [[3, 6, 8, 10, 1, 2, 1]], "expected": [1, 1, 2, 3, 6, 8, 10]},
                {"function": "tri_rapide", "inputs": [[5, 4, 3, 2, 1]], "expected": [1, 2, 3, 4, 5]},
                {"function": "tri_rapide", "inputs": [[1]], "expected": [1]},
            ]
        ),
        
        Exercise(
            id="083",
            title="Tri par fusion (MergeSort)",
            description="Fonction `tri_fusion(liste)` qui implémente le tri par fusion.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "tri_fusion", "inputs": [[3, 6, 8, 10, 1, 2, 1]], "expected": [1, 1, 2, 3, 6, 8, 10]},
                {"function": "tri_fusion", "inputs": [[5, 4, 3, 2, 1]], "expected": [1, 2, 3, 4, 5]},
            ]
        ),
        
        Exercise(
            id="084",
            title="Plus court chemin (Dijkstra)",
            description="Fonction `dijkstra(graphe, start, end)` qui trouve le plus court chemin dans un graphe pondéré.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "dijkstra", "inputs": [{'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}, 'A', 'D'], "expected": (['A', 'B', 'C', 'D'], 4)},
            ]
        ),
        
        Exercise(
            id="085",
            title="Problème du sac à dos",
            description="Fonction `sac_a_dos(objets, capacite)` qui résout le problème du sac à dos 0/1.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "sac_a_dos", "inputs": [[(60, 10), (100, 20), (120, 30)], 50], "expected": (220, [False, True, True])},
            ],
            hints=["Programmation dynamique", "dp[i][w] = valeur max avec i objets et capacité w"]
        ),
        
        Exercise(
            id="086",
            title="N-Reines",
            description="Fonction `n_reines(n)` qui trouve une solution au problème des N reines sur un échiquier n×n.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "n_reines", "inputs": [4], "expected": [[1, 3, 0, 2]]},  # Une solution possible
                {"function": "n_reines", "inputs": [8], "expected": "ANY"},  # Au moins une solution
            ]
        ),
        
        Exercise(
            id="087",
            title="Arbre de Huffman",
            description="Fonction `huffman_encode(texte)` qui encode un texte avec l'algorithme de Huffman.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                # Test complexe - vérification manuelle
            ]
        ),
        
        Exercise(
            id="088", 
            title="Détection de cycle dans graphe",
            description="Fonction `detecter_cycle(graphe)` qui détecte s'il y a un cycle dans un graphe dirigé.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                {"function": "detecter_cycle", "inputs": [{'A': ['B'], 'B': ['C'], 'C': ['A']}], "expected": True},
                {"function": "detecter_cycle", "inputs": [{'A': ['B'], 'B': ['C'], 'C': []}], "expected": False},
            ]
        ),
        
        Exercise(
            id="089",
            title="Algorithme de coloration de graphe",
            description="Fonction `colorier_graphe(graphe)` qui colorie un graphe avec le minimum de couleurs.",
            difficulty="difficile", 
            category="Algorithmes complexes",
            test_cases=[
                {"function": "colorier_graphe", "inputs": [{'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}], "expected": {'A': 0, 'B': 1, 'C': 2}},
            ]
        ),
        
        Exercise(
            id="090",
            title="Résolution de Sudoku",
            description="Fonction `resoudre_sudoku(grille)` qui résout une grille de Sudoku 9x9.",
            difficulty="difficile",
            category="Algorithmes complexes",
            test_cases=[
                # Grille de test complexe
            ],
            hints=["Backtracking", "Vérifiez lignes, colonnes et carrés 3x3"]
        ),
    ])
    
    # Structures de données avancées (91-100)
    exercises.extend([
        Exercise(
            id="091",
            title="Pile (Stack)",
            description="Classe `Pile` avec méthodes push, pop, peek, is_empty, size.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe - vérification spéciale
            ]
        ),
        
        Exercise(
            id="092",
            title="File (Queue)", 
            description="Classe `File` avec méthodes enqueue, dequeue, front, is_empty, size.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe
            ]
        ),
        
        Exercise(
            id="093",
            title="Liste chaînée",
            description="Classe `ListeChainee` avec méthodes insert, delete, find, size.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe
            ]
        ),
        
        Exercise(
            id="094",
            title="Arbre binaire de recherche",
            description="Classe `ArbreBinaire` avec méthodes insert, search, delete, inorder.",
            difficulty="difficile",
            category="Structures de données avancées", 
            test_cases=[
                # Test de classe complexe
            ]
        ),
        
        Exercise(
            id="095",
            title="Table de hachage",
            description="Classe `TableHachage` qui implémente une table de hachage avec gestion des collisions.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe
            ]
        ),
        
        Exercise(
            id="096",
            title="Arbre AVL auto-équilibré",
            description="Classe `ArbreAVL` qui maintient l'équilibre automatiquement.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test très complexe
            ]
        ),
        
        Exercise(
            id="097",
            title="Graphe avec DFS et BFS",
            description="Classe `Graphe` avec implémentation DFS (parcours en profondeur) et BFS (parcours en largeur).",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe
            ]
        ),
        
        Exercise(
            id="098",
            title="Union-Find (Disjoint Set)",
            description="Classe `UnionFind` pour gérer des ensembles disjoints avec union et find optimisés.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de classe
            ]
        ),
        
        Exercise(
            id="099",
            title="LRU Cache complet",
            description="Classe `LRUCache` complète avec toutes les optimisations (O(1) pour get et put).",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                # Test de performance
            ]
        ),
        
        Exercise(
            id="100",
            title="Interpréteur d'expressions mathématiques",
            description="Fonction `evaluer_expression(expr)` qui évalue une expression comme '3 + 4 * (2 - 1)'.",
            difficulty="difficile",
            category="Structures de données avancées",
            test_cases=[
                {"function": "evaluer_expression", "inputs": ["3 + 4 * 2"], "expected": 11},
                {"function": "evaluer_expression", "inputs": ["(1 + 2) * 3"], "expected": 9},
                {"function": "evaluer_expression", "inputs": ["10 / 2 + 3 * 4"], "expected": 17.0},
            ],
            hints=["Utilisez l'algorithme Shunting Yard", "Séparez en tokens", "Gérez la priorité des opérateurs"]
        ),
    ])
    
    # === EXERCICES BONUS (50 exercices supplémentaires) ===
    
    # Mathématiques et logique (101-115)
    exercises.extend([
        Exercise(
            id="101",
            title="Nombres premiers",
            description="Fonction `est_premier(n)` qui vérifie si un nombre est premier.",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "est_premier", "inputs": [7], "expected": True},
                {"function": "est_premier", "inputs": [4], "expected": False},
                {"function": "est_premier", "inputs": [2], "expected": True},
                {"function": "est_premier", "inputs": [1], "expected": False},
                {"function": "est_premier", "inputs": [17], "expected": True},
            ],
            hints=["Un nombre premier n'a que 1 et lui-même comme diviseurs", "Testez jusqu'à racine carrée de n"]
        ),
        
        Exercise(
            id="102",
            title="Crible d'Ératosthène",
            description="Fonction `crible_eratosthene(n)` qui trouve tous les nombres premiers jusqu'à n.",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "crible_eratosthene", "inputs": [10], "expected": [2, 3, 5, 7]},
                {"function": "crible_eratosthene", "inputs": [20], "expected": [2, 3, 5, 7, 11, 13, 17, 19]},
                {"function": "crible_eratosthene", "inputs": [2], "expected": [2]},
            ]
        ),
        
        Exercise(
            id="103",
            title="Convertisseur de bases",
            description="Fonction `convertir_base(nombre, base_origine, base_cible)` qui convertit entre bases numériques.",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "convertir_base", "inputs": ["1010", 2, 10], "expected": "10"},
                {"function": "convertir_base", "inputs": ["FF", 16, 10], "expected": "255"},
                {"function": "convertir_base", "inputs": ["10", 10, 2], "expected": "1010"},
            ]
        ),
        
        Exercise(
            id="104",
            title="Séquence de Collatz",
            description="Fonction `collatz(n)` qui génère la séquence de Collatz jusqu'à atteindre 1.",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "collatz", "inputs": [3], "expected": [3, 10, 5, 16, 8, 4, 2, 1]},
                {"function": "collatz", "inputs": [1], "expected": [1]},
                {"function": "collatz", "inputs": [4], "expected": [4, 2, 1]},
            ],
            hints=["Si pair: n/2, si impair: 3n+1"]
        ),
        
        Exercise(
            id="105",
            title="Calculateur de combinaisons",
            description="Fonction `combinaisons(n, r)` qui calcule C(n,r) = n!/(r!(n-r)!).",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "combinaisons", "inputs": [5, 2], "expected": 10},
                {"function": "combinaisons", "inputs": [4, 0], "expected": 1},
                {"function": "combinaisons", "inputs": [6, 3], "expected": 20},
            ]
        ),
        
        Exercise(
            id="106",
            title="Algorithme d'Euclide étendu",
            description="Fonction `euclide_etendu(a, b)` qui trouve x, y tels que ax + by = pgcd(a,b).",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "euclide_etendu", "inputs": [30, 18], "expected": (6, -1, 2)},  # pgcd, x, y
                {"function": "euclide_etendu", "inputs": [7, 5], "expected": (1, 3, -4)},
            ]
        ),
        
        Exercise(
            id="107",
            title="Exponentiation modulaire",
            description="Fonction `exp_modulaire(base, exp, mod)` qui calcule (base^exp) % mod efficacement.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "exp_modulaire", "inputs": [2, 10, 1000], "expected": 24},
                {"function": "exp_modulaire", "inputs": [3, 4, 5], "expected": 1},
            ]
        ),
        
        Exercise(
            id="108",
            title="Test de primalité de Miller-Rabin",
            description="Fonction `miller_rabin(n, k)` qui teste la primalité avec k itérations.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "miller_rabin", "inputs": [97, 5], "expected": True},
                {"function": "miller_rabin", "inputs": [99, 5], "expected": False},
            ]
        ),
        
        Exercise(
            id="109",
            title="Fraction continue",
            description="Fonction `fraction_continue(x, precision)` qui développe un nombre en fraction continue.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "fraction_continue", "inputs": [3.14159, 5], "expected": [3, 7, 15, 1, 292]},
            ]
        ),
        
        Exercise(
            id="110",
            title="Équation de Pell",
            description="Fonction `resoudre_pell(d)` qui trouve la plus petite solution de x² - d*y² = 1.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "resoudre_pell", "inputs": [2], "expected": (3, 2)},
                {"function": "resoudre_pell", "inputs": [3], "expected": (2, 1)},
            ]
        ),
        
        Exercise(
            id="111",
            title="Matrice multiplication",
            description="Fonction `multiplier_matrices(A, B)` qui multiplie deux matrices.",
            difficulty="moyen",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "multiplier_matrices", "inputs": [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], "expected": [[19, 22], [43, 50]]},
                {"function": "multiplier_matrices", "inputs": [[[1, 0], [0, 1]], [[2, 3], [4, 5]]], "expected": [[2, 3], [4, 5]]},
            ]
        ),
        
        Exercise(
            id="112",
            title="Déterminant matrice",
            description="Fonction `determinant(matrice)` qui calcule le déterminant d'une matrice carrée.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "determinant", "inputs": [[[1, 2], [3, 4]]], "expected": -2},
                {"function": "determinant", "inputs": [[[2, 1, 3], [1, 0, 1], [1, 2, 1]]], "expected": -2},
            ]
        ),
        
        Exercise(
            id="113",
            title="Résolution système linéaire",
            description="Fonction `gauss_jordan(A, b)` qui résout le système Ax = b par élimination de Gauss-Jordan.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "gauss_jordan", "inputs": [[[2, 1], [1, 1]], [3, 2]], "expected": [1.0, 1.0]},
            ]
        ),
        
        Exercise(
            id="114",
            title="Transformée de Fourier discrète",
            description="Fonction `fft_simple(signal)` qui calcule une FFT basique.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                # Test complexe - vérification manuelle
            ]
        ),
        
        Exercise(
            id="115",
            title="Intégration numérique",
            description="Fonction `integrer_simpson(f, a, b, n)` qui intègre par la méthode de Simpson.",
            difficulty="difficile",
            category="Mathématiques et logique",
            test_cases=[
                {"function": "integrer_simpson", "inputs": [lambda x: x**2, 0, 1, 100], "expected": 0.3333},  # Approximation
            ]
        ),
    ])
    
    # Jeux et puzzles (116-125)
    exercises.extend([
        Exercise(
            id="116",
            title="Jeu de la vie de Conway",
            description="Fonction `jeu_de_la_vie(grille, iterations)` qui simule le jeu de la vie.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                # Grille 3x3 avec patterns simples
            ],
            hints=["Règles: <2 voisins=mort, 2-3=survit, >3=mort, ==3=naît"]
        ),
        
        Exercise(
            id="117",
            title="Résolveur de labyrinthe",
            description="Fonction `resoudre_labyrinthe(labyrinthe, start, end)` qui trouve le chemin.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                # Labyrinthe simple avec solution unique
            ]
        ),
        
        Exercise(
            id="118",
            title="Solitaire (Klondike)",
            description="Fonction `mouvement_valide_solitaire(carte, pile)` qui valide un mouvement.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                {"function": "mouvement_valide_solitaire", "inputs": [("Rouge", 7), ("Noir", 8)], "expected": True},
                {"function": "mouvement_valide_solitaire", "inputs": [("Rouge", 7), ("Rouge", 8)], "expected": False},
            ]
        ),
        
        Exercise(
            id="119",
            title="Tour de Hanoï",
            description="Fonction `hanoi(n, source, destination, auxiliaire)` qui résout les tours de Hanoï.",
            difficulty="moyen",
            category="Jeux et puzzles",
            test_cases=[
                {"function": "hanoi", "inputs": [2, "A", "C", "B"], "expected": [("A", "B"), ("A", "C"), ("B", "C")]},
                {"function": "hanoi", "inputs": [1, "A", "C", "B"], "expected": [("A", "C")]},
            ]
        ),
        
        Exercise(
            id="120",
            title="Mots croisés validateur",
            description="Fonction `valider_mots_croises(grille, mots)` qui valide une grille de mots croisés.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                # Test avec grille simple
            ]
        ),
        
        Exercise(
            id="121",
            title="2048 logique de jeu",
            description="Fonction `mouvement_2048(grille, direction)` qui simule un mouvement dans 2048.",
            difficulty="moyen",
            category="Jeux et puzzles",
            test_cases=[
                {"function": "mouvement_2048", "inputs": [[[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "gauche"], "expected": [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]},
            ]
        ),
        
        Exercise(
            id="122",
            title="Bataille navale",
            description="Fonction `placer_navire(grille, navire, position, orientation)` pour placer un navire.",
            difficulty="moyen",
            category="Jeux et puzzles",
            test_cases=[
                {"function": "placer_navire", "inputs": [[[0]*10 for _ in range(10)], 3, (0, 0), "horizontal"], "expected": True},
            ]
        ),
        
        Exercise(
            id="123",
            title="Mastermind",
            description="Fonction `evaluer_mastermind(secret, guess)` qui retourne (bien_places, mal_places).",
            difficulty="moyen",
            category="Jeux et puzzles",
            test_cases=[
                {"function": "evaluer_mastermind", "inputs": [[1, 2, 3, 4], [1, 3, 2, 5]], "expected": (1, 2)},
                {"function": "evaluer_mastermind", "inputs": [[1, 2, 3, 4], [1, 2, 3, 4]], "expected": (4, 0)},
            ]
        ),
        
        Exercise(
            id="124",
            title="Générateur de Sudoku",
            description="Fonction `generer_sudoku(difficulte)` qui génère une grille de Sudoku valide.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                # Test de validité de la grille générée
            ]
        ),
        
        Exercise(
            id="125",
            title="Échecs - mouvements valides",
            description="Fonction `mouvements_valides_piece(piece, position, echiquier)` pour une pièce d'échecs.",
            difficulty="difficile",
            category="Jeux et puzzles",
            test_cases=[
                # Tests pour différentes pièces
            ]
        ),
    ])
    
    # Traitement de données (126-135)
    exercises.extend([
        Exercise(
            id="126",
            title="Parser CSV avancé",
            description="Fonction `parser_csv(contenu, delimiteur, quote)` qui parse un CSV avec gestion des guillemets.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "parser_csv", "inputs": ['nom,age\n"Doe, John",25\nJane,30', ',', '"'], "expected": [["nom", "age"], ["Doe, John", "25"], ["Jane", "30"]]},
            ]
        ),
        
        Exercise(
            id="127",
            title="Nettoyage de données",
            description="Fonction `nettoyer_donnees(df)` qui nettoie un dataset (supprime doublons, valeurs nulles).",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "nettoyer_donnees", "inputs": [[{"nom": "John", "age": 25}, {"nom": "John", "age": 25}, {"nom": "Jane", "age": None}]], "expected": [{"nom": "John", "age": 25}, {"nom": "Jane"}]},
            ]
        ),
        
        Exercise(
            id="128",
            title="Pivot table",
            description="Fonction `pivot_table(data, index, columns, values, aggfunc)` qui crée une table pivot.",
            difficulty="difficile",
            category="Traitement de données",
            test_cases=[
                # Test complexe avec données groupées
            ]
        ),
        
        Exercise(
            id="129",
            title="Détection d'outliers",
            description="Fonction `detecter_outliers(donnees, methode)` qui trouve les valeurs aberrantes.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "detecter_outliers", "inputs": [[1, 2, 3, 4, 5, 100], "iqr"], "expected": [100]},
            ]
        ),
        
        Exercise(
            id="130",
            title="Corrélation de Pearson",
            description="Fonction `correlation_pearson(x, y)` qui calcule le coefficient de corrélation.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "correlation_pearson", "inputs": [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]], "expected": 1.0},
                {"function": "correlation_pearson", "inputs": [[1, 2, 3], [3, 2, 1]], "expected": -1.0},
            ]
        ),
        
        Exercise(
            id="131",
            title="Régression linéaire simple",
            description="Fonction `regression_lineaire(x, y)` qui calcule la droite de régression y = ax + b.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "regression_lineaire", "inputs": [[1, 2, 3, 4], [2, 4, 6, 8]], "expected": (2.0, 0.0)},  # a, b
            ]
        ),
        
        Exercise(
            id="132",
            title="Normalisation données",
            description="Fonction `normaliser(donnees, methode)` qui normalise selon différentes méthodes.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "normaliser", "inputs": [[1, 2, 3, 4, 5], "min_max"], "expected": [0.0, 0.25, 0.5, 0.75, 1.0]},
                {"function": "normaliser", "inputs": [[1, 2, 3, 4, 5], "z_score"], "expected": [-1.414, -0.707, 0.0, 0.707, 1.414]},  # Approximation
            ]
        ),
        
        Exercise(
            id="133",
            title="Clustering K-means simple",
            description="Fonction `kmeans_simple(points, k, iterations)` qui groupe les points en k clusters.",
            difficulty="difficile",
            category="Traitement de données",
            test_cases=[
                # Test avec points 2D simples
            ]
        ),
        
        Exercise(
            id="134",
            title="Analyse de fréquence de texte",
            description="Fonction `analyser_frequences(texte)` qui analyse les fréquences des mots et caractères.",
            difficulty="moyen",
            category="Traitement de données",
            test_cases=[
                {"function": "analyser_frequences", "inputs": ["hello world hello"], "expected": {"mots": {"hello": 2, "world": 1}, "caracteres": {"h": 2, "e": 2, "l": 6, "o": 2, " ": 2, "w": 1, "r": 1, "d": 1}}},
            ]
        ),
        
        Exercise(
            id="135",
            title="Détecteur de tendances",
            description="Fonction `detecter_tendance(serie_temporelle)` qui détecte les tendances dans une série.",
            difficulty="difficile",
            category="Traitement de données",
            test_cases=[
                {"function": "detecter_tendance", "inputs": [[1, 2, 3, 4, 5, 6]], "expected": "croissante"},
                {"function": "detecter_tendance", "inputs": [[6, 5, 4, 3, 2, 1]], "expected": "décroissante"},
                {"function": "detecter_tendance", "inputs": [[1, 3, 2, 4, 3, 5]], "expected": "oscillante"},
            ]
        ),
    ])
    
    # Sécurité et cryptographie (136-145)
    exercises.extend([
        Exercise(
            id="136",
            title="Chiffrement César",
            description="Fonction `cesar(texte, decalage, mode)` qui chiffre/déchiffre avec César.",
            difficulty="facile",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "cesar", "inputs": ["HELLO", 3, "chiffrer"], "expected": "KHOOR"},
                {"function": "cesar", "inputs": ["KHOOR", 3, "dechiffrer"], "expected": "HELLO"},
            ]
        ),
        
        Exercise(
            id="137",
            title="Chiffrement de Vigenère",
            description="Fonction `vigenere(texte, cle, mode)` qui chiffre avec la clé de Vigenère.",
            difficulty="moyen",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "vigenere", "inputs": ["HELLO", "KEY", "chiffrer"], "expected": "RIJVS"},
            ]
        ),
        
        Exercise(
            id="138",
            title="Générateur de hash simple",
            description="Fonction `hash_simple(texte)` qui génère un hash basique non-cryptographique.",
            difficulty="moyen",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "hash_simple", "inputs": ["hello"], "expected": "99162322"},  # Exemple
            ]
        ),
        
        Exercise(
            id="139",
            title="Validateur de mot de passe",
            description="Fonction `valider_mdp(mdp)` qui vérifie la force d'un mot de passe.",
            difficulty="facile",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "valider_mdp", "inputs": ["Password123!"], "expected": {"valide": True, "score": 10}},
                {"function": "valider_mdp", "inputs": ["123"], "expected": {"valide": False, "score": 1}},
            ]
        ),
        
        Exercise(
            id="140",
            title="Générateur de mots de passe",
            description="Fonction `generer_mdp(longueur, inclure_symboles, inclure_chiffres)` qui génère un mot de passe sécurisé.",
            difficulty="moyen",
            category="Sécurité et cryptographie",
            test_cases=[
                # Test de longueur et composition
            ]
        ),
        
        Exercise(
            id="141",
            title="Chiffrement XOR",
            description="Fonction `xor_cipher(texte, cle)` qui chiffre/déchiffre avec XOR.",
            difficulty="moyen",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "xor_cipher", "inputs": ["HELLO", "KEY"], "expected": "\x03\x00\x1e\x1e\x1a"},  # Résultat en bytes
            ]
        ),
        
        Exercise(
            id="142",
            title="RSA simple (génération de clés)",
            description="Fonction `generer_cles_rsa(taille_bits)` qui génère une paire de clés RSA basique.",
            difficulty="difficile",
            category="Sécurité et cryptographie",
            test_cases=[
                # Test de validité mathématique des clés
            ]
        ),
        
        Exercise(
            id="143",
            title="Détecteur d'injection SQL",
            description="Fonction `detecter_injection_sql(requete)` qui détecte les tentatives d'injection.",
            difficulty="moyen",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "detecter_injection_sql", "inputs": ["SELECT * FROM users WHERE id = 1"], "expected": False},
                {"function": "detecter_injection_sql", "inputs": ["SELECT * FROM users WHERE id = 1 OR 1=1"], "expected": True},
            ]
        ),
        
        Exercise(
            id="144",
            title="Analyse de fréquence cryptographique",
            description="Fonction `analyser_frequence_crypto(texte_chiffre)` pour casser des chiffrements par substitution.",
            difficulty="difficile",
            category="Sécurité et cryptographie",
            test_cases=[
                # Analyse des fréquences des lettres
            ]
        ),
        
        Exercise(
            id="145",
            title="Générateur de nombres pseudo-aléatoires",
            description="Fonction `lcg(seed, a, c, m)` qui implémente un générateur congruentiel linéaire.",
            difficulty="difficile",
            category="Sécurité et cryptographie",
            test_cases=[
                {"function": "lcg", "inputs": [1, 7, 5, 11], "expected": [1, 1, 1, 1, 1]},  # Première séquence
            ]
        ),
    ])
    
    # Optimisation et performance (146-150)
    exercises.extend([
        Exercise(
            id="146",
            title="Cache LFU (Least Frequently Used)",
            description="Classe `LFUCache` qui implémente un cache avec éviction LFU.",
            difficulty="difficile",
            category="Optimisation et performance",
            test_cases=[
                # Test de classe complexe
            ]
        ),
        
        Exercise(
            id="147",
            title="Pool de threads simple",
            description="Classe `ThreadPool` qui gère un pool de workers pour exécuter des tâches.",
            difficulty="difficile",
            category="Optimisation et performance",
            test_cases=[
                # Test avec threading
            ]
        ),
        
        Exercise(
            id="148",
            title="Memoization automatique",
            description="Fonction `memoize(func)` qui crée un décorateur de mémoisation automatique.",
            difficulty="moyen",
            category="Optimisation et performance",
            test_cases=[
                # Test avec fonction fibonacci
            ]
        ),
        
        Exercise(
            id="149",
            title="Profilage de performance",
            description="Fonction `profiler_execution(func, *args)` qui mesure le temps d'exécution et l'usage mémoire.",
            difficulty="moyen",
            category="Optimisation et performance",
            test_cases=[
                # Test de mesure de performance
            ]
        ),
        
        Exercise(
            id="150",
            title="Algorithme génétique simple",
            description="Fonction `algorithme_genetique(population_init, fitness, generations)` pour optimisation.",
            difficulty="difficile",
            category="Optimisation et performance",
            test_cases=[
                # Test d'optimisation d'une fonction simple
            ],
            hints=["Sélection, croisement, mutation", "Maximiser la fonction fitness"]
        ),
    ])
    
    return exercises