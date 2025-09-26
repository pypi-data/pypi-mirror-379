# educode/exercises.py
"""Base de données des +200 exercices EduCode"""

from .core import Exercise

def get_all_exercises():
    """Retourne la liste complète des +200 exercices"""
    
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
    
    exercises.extend([
        Exercise(
            id="151",
            title="Arbre de segments",
            description="Classe `ArbreSegments` pour requêtes de somme et mise à jour sur un intervalle.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "ArbreSegments", "inputs": [[1, 3, 5, 7, 9, 11]], "expected": "INIT"},
                {"function": "somme", "inputs": [2, 5], "expected": 21},
                {"function": "modifier", "inputs": [1, 6], "expected": None},
                {"function": "somme", "inputs": [2, 5], "expected": 24},
            ],
            solution_template="""class ArbreSegments:
    def __init__(self, arr):
        # Votre code ici
        pass
    
    def somme(self, l, r):
        # Somme de l'intervalle [l, r]
        pass
    
    def modifier(self, idx, val):
        # Modifie arr[idx] = val
        pass""",
            hints=[
                "Utilisez un arbre binaire complet",
                "Nœud i a enfants 2*i et 2*i+1",
                "Remontez les modifications vers la racine"
            ]
        ),
        
        Exercise(
            id="152",
            title="Algorithme de Kruskal",
            description="Fonction `kruskal(graphe)` qui trouve l'arbre couvrant minimum.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "kruskal", "inputs": [{"edges": [("A", "B", 1), ("B", "C", 2), ("A", "C", 3), ("C", "D", 1)], "vertices": ["A", "B", "C", "D"]}], "expected": [("A", "B", 1), ("C", "D", 1), ("B", "C", 2)]},
                {"function": "kruskal", "inputs": [{"edges": [("X", "Y", 5), ("Y", "Z", 3), ("X", "Z", 4)], "vertices": ["X", "Y", "Z"]}], "expected": [("Y", "Z", 3), ("X", "Z", 4)]},
            ],
            hints=[
                "Triez les arêtes par poids croissant",
                "Utilisez Union-Find pour détecter les cycles",
                "Ajoutez une arête si elle ne crée pas de cycle"
            ]
        ),
        
        Exercise(
            id="153",
            title="Flot maximum (Ford-Fulkerson)",
            description="Fonction `flot_maximum(graphe, source, puits)` qui calcule le flot maximum.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "flot_maximum", "inputs": [{("S", "A"): 10, ("S", "B"): 10, ("A", "T"): 10, ("B", "T"): 10, ("A", "B"): 1}, "S", "T"], "expected": 20},
                {"function": "flot_maximum", "inputs": [{("S", "A"): 3, ("S", "B"): 2, ("A", "T"): 4, ("B", "T"): 3, ("A", "B"): 1}, "S", "T"], "expected": 5},
            ],
            hints=[
                "Trouvez des chemins augmentants",
                "Utilisez BFS ou DFS",
                "Mettez à jour les capacités résiduelles"
            ]
        ),
        
        Exercise(
            id="154",
            title="Couplage maximum bipartite",
            description="Fonction `couplage_maximum(graphe_bipartite)` qui trouve le couplage maximum.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "couplage_maximum", "inputs": [{"U": ["u1", "u2", "u3"], "V": ["v1", "v2", "v3"], "edges": [("u1", "v1"), ("u1", "v2"), ("u2", "v2"), ("u3", "v3")]}], "expected": [("u1", "v1"), ("u2", "v2"), ("u3", "v3")]},
                {"function": "couplage_maximum", "inputs": [{"U": ["u1", "u2"], "V": ["v1", "v2", "v3"], "edges": [("u1", "v1"), ("u2", "v1"), ("u1", "v3")]}], "expected": [("u1", "v3"), ("u2", "v1")]},
            ]
        ),
        
        Exercise(
            id="155",
            title="Programmation dynamique - Édition de séquences",
            description="Fonction `alignement_sequences(seq1, seq2, cout_match, cout_gap, cout_mismatch)` pour aligner deux séquences.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "alignement_sequences", "inputs": ["ACGT", "ACT", 2, -1, -1], "expected": ("AC-T", "ACGT", 5)},
                {"function": "alignement_sequences", "inputs": ["GAT", "GAAT", 1, -1, -2], "expected": ("G-AT", "GAAT", 1)},
            ],
            hints=[
                "Matrice DP[i][j] = score optimal pour seq1[:i] et seq2[:j]",
                "Trois choix : match/mismatch, gap dans seq1, gap dans seq2"
            ]
        ),
        
        Exercise(
            id="156",
            title="Arbre de Fenwick (Binary Indexed Tree)",
            description="Classe `ArbreFenwick` pour sommes de préfixes avec mises à jour.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "ArbreFenwick", "inputs": [8], "expected": "INIT"},
                {"function": "update", "inputs": [3, 5], "expected": None},
                {"function": "query", "inputs": [3], "expected": 5},
                {"function": "update", "inputs": [1, 3], "expected": None},
                {"function": "query", "inputs": [3], "expected": 8},
                {"function": "range_query", "inputs": [2, 3], "expected": 5},
            ],
            solution_template="""class ArbreFenwick:
    def __init__(self, n):
        # Votre code ici
        pass
    
    def update(self, i, delta):
        # Ajoute delta à l'élément i
        pass
    
    def query(self, i):
        # Somme des éléments 1..i
        pass
    
    def range_query(self, l, r):
        # Somme des éléments l..r
        pass"""
        ),
        
        Exercise(
            id="157",
            title="Algorithme Z pour recherche de motifs",
            description="Fonction `algorithme_z(s)` qui calcule le tableau Z pour la recherche de motifs.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "algorithme_z", "inputs": ["aaabaaab"], "expected": [0, 2, 1, 0, 3, 2, 1, 0]},
                {"function": "algorithme_z", "inputs": ["abcabcabc"], "expected": [0, 0, 0, 6, 0, 0, 3, 0, 0]},
                {"function": "algorithme_z", "inputs": ["aaa"], "expected": [0, 2, 1]},
            ],
            hints=[
                "Z[i] = longueur max du préfixe commun entre s et s[i:]",
                "Utilisez la propriété Z-box pour optimiser"
            ]
        ),
        
        Exercise(
            id="158",
            title="Convolution de Karatsuba",
            description="Fonction `karatsuba(x, y)` qui multiplie deux entiers avec l'algorithme de Karatsuba.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "karatsuba", "inputs": [1234, 5678], "expected": 7006652},
                {"function": "karatsuba", "inputs": [12, 34], "expected": 408},
                {"function": "karatsuba", "inputs": [99, 99], "expected": 9801},
                {"function": "karatsuba", "inputs": [1, 123456789], "expected": 123456789},
            ],
            hints=[
                "Divisez en deux moitiés : x = a*10^n + b",
                "xy = ac*10^2n + (ad+bc)*10^n + bd",
                "Optimisation : ad+bc = (a+b)(c+d) - ac - bd"
            ]
        ),
        
        Exercise(
            id="159",
            title="Décomposition en facteurs premiers optimisée",
            description="Fonction `factorisation_pollard_rho(n)` qui factorise avec l'algorithme rho de Pollard.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "factorisation_pollard_rho", "inputs": [15], "expected": [3, 5]},
                {"function": "factorisation_pollard_rho", "inputs": [21], "expected": [3, 7]},
                {"function": "factorisation_pollard_rho", "inputs": [143], "expected": [11, 13]},
                {"function": "factorisation_pollard_rho", "inputs": [17], "expected": [17]},
            ]
        ),
        
        Exercise(
            id="160",
            title="Plus courte superstring",
            description="Fonction `plus_courte_superstring(mots)` qui trouve la plus courte chaîne contenant tous les mots.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "plus_courte_superstring", "inputs": [["ABCD", "BCDE", "CDEF"]], "expected": "ABCDEF"},
                {"function": "plus_courte_superstring", "inputs": [["AAA", "AAB", "BAA"]], "expected": "BAAAB"},
                {"function": "plus_courte_superstring", "inputs": [["ABC", "BCA", "CAB"]], "expected": "ABCAB"},
            ],
            hints=[
                "Problème du voyageur de commerce",
                "Calculez les chevauchements entre mots",
                "DP avec masquage de bits"
            ]
        ),
        
        Exercise(
            id="161",
            title="Arbre de suffixes compressé",
            description="Classe `ArbreSuffixes` qui construit un arbre de suffixes compressé avec l'algorithme d'Ukkonen.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "ArbreSuffixes", "inputs": ["banana"], "expected": "INIT"},
                {"function": "rechercher", "inputs": ["ana"], "expected": [1, 3]},
                {"function": "rechercher", "inputs": ["na"], "expected": [2, 4]},
                {"function": "rechercher", "inputs": ["xyz"], "expected": []},
            ]
        ),
        
        Exercise(
            id="162",
            title="Multiplication de matrices optimisée",
            description="Fonction `multiplication_matrices_optimale(dimensions)` qui trouve l'ordre optimal de multiplication.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "multiplication_matrices_optimale", "inputs": [[1, 2, 3, 4]], "expected": (18, "((M1M2)M3)")},
                {"function": "multiplication_matrices_optimale", "inputs": [[5, 10, 3, 12, 5]], "expected": (630, "(M1(M2(M3M4)))")},
            ],
            hints=[
                "DP[i][j] = coût minimum pour multiplier Mi...Mj",
                "Essayez tous les points de division k entre i et j"
            ]
        ),
        
        Exercise(
            id="163",
            title="Détection de palindrome de Manacher",
            description="Fonction `manacher(s)` qui trouve tous les palindromes en temps linéaire.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "manacher", "inputs": ["abacabad"], "expected": {"palindromes": ["a", "b", "a", "c", "aba", "a", "b", "a", "d"], "centre_max": 4, "longueur_max": 3}},
                {"function": "manacher", "inputs": ["racecar"], "expected": {"palindromes": ["racecar"], "centre_max": 3, "longueur_max": 7}},
            ]
        ),
        
        Exercise(
            id="164",
            title="Couverture minimale d'ensemble",
            description="Fonction `couverture_minimale(univers, ensembles)` qui trouve une couverture approximative.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "couverture_minimale", "inputs": [{1, 2, 3, 4, 5}, [{"A": {1, 2, 3}}, {"B": {2, 4}}, {"C": {3, 4, 5}}, {"D": {1, 5}}]], "expected": ["A", "C"]},
                {"function": "couverture_minimale", "inputs": [{1, 2, 3}, [{"X": {1}}, {"Y": {2}}, {"Z": {3}}, {"W": {1, 2, 3}}]], "expected": ["W"]},
            ],
            hints=[
                "Algorithme glouton",
                "Choisissez l'ensemble qui couvre le plus d'éléments non couverts"
            ]
        ),
        
        Exercise(
            id="165",
            title="Algorithme de Rabin-Karp avec hash rolling",
            description="Fonction `rabin_karp(texte, motif)` qui recherche toutes les occurrences d'un motif.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "rabin_karp", "inputs": ["abcabcabc", "abc"], "expected": [0, 3, 6]},
                {"function": "rabin_karp", "inputs": ["aaaaaaa", "aaa"], "expected": [0, 1, 2, 3, 4]},
                {"function": "rabin_karp", "inputs": ["hello world", "world"], "expected": [6]},
            ],
            hints=[
                "Hash polynomial rolling : hash(s[i+1:i+m+1]) = (hash(s[i:i+m]) - s[i]*base^(m-1))*base + s[i+m]",
                "Utilisez un nombre premier comme base"
            ]
        ),
        
        Exercise(
            id="166",
            title="Arbre cartésien",
            description="Fonction `construire_arbre_cartesien(arr)` qui construit un arbre cartésien à partir d'un tableau.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "construire_arbre_cartesien", "inputs": [[3, 2, 6, 1, 9]], "expected": {"racine": 1, "gauche": {"racine": 2, "gauche": {"racine": 3}}, "droite": {"racine": 6, "droite": {"racine": 9}}}},
                {"function": "construire_arbre_cartesien", "inputs": [[1, 2, 3]], "expected": {"racine": 1, "droite": {"racine": 2, "droite": {"racine": 3}}}},
            ],
            hints=[
                "Propriété tas : parent ≤ enfants",
                "Propriété BST : parcours inordre = tableau original",
                "Utilisez une pile pour construction en O(n)"
            ]
        ),
        
        Exercise(
            id="167",
            title="Partition équilibrée optimale",
            description="Fonction `partition_equilibree(arr, k)` qui divise un tableau en k sous-ensembles de sommes équilibrées.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "partition_equilibree", "inputs": [[1, 2, 3, 4, 5, 6], 3], "expected": [[1, 6], [2, 5], [3, 4]]},
                {"function": "partition_equilibree", "inputs": [[10, 20, 30, 40], 2], "expected": [[10, 40], [20, 30]]},
            ],
            hints=[
                "Problème NP-complet, utilisez heuristique",
                "Algorithme glouton : ajoutez à la partition de somme minimale"
            ]
        ),
        
        Exercise(
            id="168",
            title="Algorithme de Boyer-Moore pour recherche de motifs",
            description="Fonction `boyer_moore(texte, motif)` avec tables de bon suffixe et mauvais caractère.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "boyer_moore", "inputs": ["abaaabcdabcdabde", "abcd"], "expected": [4, 8]},
                {"function": "boyer_moore", "inputs": ["aaaaaaaa", "aa"], "expected": [0, 1, 2, 3, 4, 5, 6]},
                {"function": "boyer_moore", "inputs": ["hello world", "world"], "expected": [6]},
            ]
        ),
        
        Exercise(
            id="169",
            title="Décomposition de Cholesky",
            description="Fonction `cholesky(matrice)` qui décompose une matrice symétrique définie positive.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "cholesky", "inputs": [[[4, 2], [2, 2]]], "expected": [[2.0, 0.0], [1.0, 1.0]]},
                {"function": "cholesky", "inputs": [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]], "expected": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
            ],
            hints=[
                "A = L * L^T où L est triangulaire inférieure",
                "L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k] for k<j)) / L[j][j]"
            ]
        ),
        
        Exercise(
            id="170",
            title="Algorithme de Viterbi",
            description="Fonction `viterbi(observations, etats, transitions, emissions, initiales)` pour séquences cachées.",
            difficulty="difficile",
            category="Algorithmique avancée",
            test_cases=[
                {"function": "viterbi", "inputs": [["normal", "froid", "vertige"], ["sain", "fievre"], {"sain": {"sain": 0.7, "fievre": 0.3}, "fievre": {"sain": 0.4, "fievre": 0.6}}, {"sain": {"normal": 0.5, "froid": 0.4, "vertige": 0.1}, "fievre": {"normal": 0.1, "froid": 0.3, "vertige": 0.6}}, {"sain": 0.6, "fievre": 0.4}], "expected": (["sain", "sain", "fievre"], 0.01512)},
            ]
        ),
    ])
    
    # === INTELLIGENCE ARTIFICIELLE (171-185) ===
    
    exercises.extend([
        Exercise(
            id="171",
            title="Perceptron simple",
            description="Classe `Perceptron` qui apprend une fonction logique linéairement séparable.",
            difficulty="moyen",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "Perceptron", "inputs": [0.1], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[0, 0], [0, 1], [1, 0], [1, 1]], [0, 0, 0, 1], 100], "expected": None},
                {"function": "predire", "inputs": [[1, 1]], "expected": 1},
                {"function": "predire", "inputs": [[0, 0]], "expected": 0},
                {"function": "predire", "inputs": [[0, 1]], "expected": 0},
            ],
            solution_template="""class Perceptron:
    def __init__(self, taux_apprentissage):
        # Votre code ici
        pass
    
    def entrainer(self, X, y, epochs):
        # Entraîne le perceptron
        pass
    
    def predire(self, x):
        # Prédit la classe
        pass""",
            hints=[
                "Fonction d'activation : signe de (w·x + b)",
                "Mise à jour : w += α * (y_vrai - y_pred) * x"
            ]
        ),
        
        Exercise(
            id="172",
            title="K-means clustering",
            description="Fonction `kmeans(points, k, max_iter)` qui groupe les points en k clusters.",
            difficulty="moyen",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "kmeans", "inputs": [[[1, 1], [1, 2], [2, 1], [8, 8], [8, 9], [9, 8]], 2, 100], "expected": {"centroides": [[1.33, 1.33], [8.33, 8.33]], "clusters": [[0, 1, 2], [3, 4, 5]]}},
                {"function": "kmeans", "inputs": [[[0, 0], [1, 1], [2, 2]], 1, 10], "expected": {"centroides": [[1.0, 1.0]], "clusters": [[0, 1, 2]]}},
            ],
            hints=[
                "Initialisez k centroides aléatoirement",
                "Assignez chaque point au centroide le plus proche",
                "Recalculez les centroides",
                "Répétez jusqu'à convergence"
            ]
        ),
        
        Exercise(
            id="173",
            title="Arbre de décision simple",
            description="Classe `ArbreDecision` qui construit un arbre de décision binaire.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "ArbreDecision", "inputs": [], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[2, 3], [1, 1], [3, 3], [2, 1]], ["oui", "non", "oui", "non"]], "expected": None},
                {"function": "predire", "inputs": [[2.5, 2.5]], "expected": "oui"},
                {"function": "predire", "inputs": [[1.5, 1.5]], "expected": "non"},
            ],
            hints=[
                "Critère de division : impureté de Gini ou entropie",
                "Choisissez le seuil qui minimise l'impureté",
                "Arrêt : pureté maximale ou profondeur limite"
            ]
        ),
        
        Exercise(
            id="174",
            title="Algorithme génétique pour optimisation",
            description="Fonction `algorithme_genetique(fonction_fitness, taille_pop, generations)` qui optimise une fonction.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "algorithme_genetique", "inputs": [lambda x: -(x[0]**2 + x[1]**2), 20, 50, {"min_val": -5, "max_val": 5, "taille_chromosome": 2}], "expected": {"meilleur_fitness": 0.0, "meilleure_solution": [0.0, 0.0]}},
            ],
            hints=[
                "Sélection par tournoi ou roulette",
                "Croisement : moyenne pondérée",
                "Mutation : bruit gaussien"
            ]
        ),
        
        Exercise(
            id="175",
            title="Régression linéaire multiple",
            description="Classe `RegressionLineaire` qui apprend y = X*w + b par descente de gradient.",
            difficulty="moyen",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "RegressionLineaire", "inputs": [0.01], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[1, 2], [2, 3], [3, 4]], [3, 5, 7], 1000], "expected": None},
                {"function": "predire", "inputs": [[4, 5]], "expected": 9.0},
                {"function": "score_r2", "inputs": [[[1, 2], [2, 3]], [3, 5]], "expected": 1.0},
            ]
        ),
        
        Exercise(
            id="176",
            title="Réseau de neurones multicouches",
            description="Classe `ReseauNeurones` avec rétropropagation du gradient.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "ReseauNeurones", "inputs": [[2, 3, 1], 0.1], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 1000], "expected": None},
                {"function": "predire", "inputs": [[1, 1]], "expected": [0.0]},
                {"function": "predire", "inputs": [[0, 1]], "expected": [1.0]},
            ],
            hints=[
                "Forward pass : z = Wx + b, a = sigmoid(z)",
                "Backward pass : δ = (a - y) * sigmoid'(z)"
            ]
        ),
        
        Exercise(
            id="177",
            title="Algorithme Q-Learning",
            description="Classe `QLearning` pour l'apprentissage par renforcement dans un environnement grille.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "QLearning", "inputs": [3, 3, 4, 0.1, 0.9], "expected": "INIT"},
                {"function": "entrainer", "inputs": [1000, (0, 0), (2, 2), [(1, 1)]], "expected": None},
                {"function": "politique_optimale", "inputs": [(0, 0)], "expected": "droite"},
            ],
            solution_template="""class QLearning:
    def __init__(self, hauteur, largeur, nb_actions, alpha, gamma):
        # hauteur, largeur : taille grille
        # nb_actions : haut, bas, gauche, droite
        # alpha : taux apprentissage, gamma : facteur discount
        pass
    
    def entrainer(self, episodes, start, goal, obstacles):
        pass
    
    def politique_optimale(self, etat):
        pass"""
        ),
        
        Exercise(
            id="178",
            title="Support Vector Machine linéaire",
            description="Classe `SVM` qui trouve l'hyperplan de séparation optimal.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "SVM", "inputs": [1.0], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[1, 1], [2, 2], [3, 1], [2, 0]], [1, 1, -1, -1]], "expected": None},
                {"function": "predire", "inputs": [[1.5, 1.5]], "expected": 1},
                {"function": "predire", "inputs": [[3, 0]], "expected": -1},
            ]
        ),
        
        Exercise(
            id="179",
            title="Naive Bayes pour classification de texte",
            description="Classe `NaiveBayes` qui classifie des textes selon leurs mots.",
            difficulty="moyen",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "NaiveBayes", "inputs": [], "expected": "INIT"},
                {"function": "entrainer", "inputs": [["good movie great", "bad movie terrible", "excellent film good", "awful movie bad"], ["positif", "negatif", "positif", "negatif"]], "expected": None},
                {"function": "predire", "inputs": ["excellent movie"], "expected": "positif"},
                {"function": "predire", "inputs": ["terrible film"], "expected": "negatif"},
            ]
        ),
        
        Exercise(
            id="180",
            title="Algorithme A* pour pathfinding",
            description="Fonction `a_star(grille, start, goal)` qui trouve le chemin optimal.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "a_star", "inputs": [[[0, 0, 0], [1, 0, 0], [0, 0, 0]], (0, 0), (2, 2)], "expected": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]},
                {"function": "a_star", "inputs": [[[0, 1, 0], [0, 1, 0], [0, 0, 0]], (0, 0), (2, 2)], "expected": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]},
            ],
            hints=[
                "f(n) = g(n) + h(n) où g=coût, h=heuristique",
                "Heuristique : distance Manhattan",
                "Utilisez une priority queue"
            ]
        ),
        
        Exercise(
            id="181",
            title="Analyse en composantes principales (ACP)",
            description="Fonction `acp(donnees, nb_composantes)` qui réduit la dimensionnalité.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "acp", "inputs": [[[2, 3], [3, 4], [4, 5], [5, 6]], 1], "expected": {"composantes": [[-0.707, -0.707]], "variance_expliquee": [1.0], "donnees_transformees": [[-1.414], [-0.707], [0.0], [0.707]]}},
            ],
            hints=[
                "Centrez les données",
                "Calculez la matrice de covariance",
                "Trouvez les vecteurs propres"
            ]
        ),
        
        Exercise(
            id="182",
            title="Algorithme des k plus proches voisins",
            description="Classe `KNN` pour classification par k plus proches voisins.",
            difficulty="moyen",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "KNN", "inputs": [3], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[1, 2], [2, 3], [3, 1], [6, 8], [7, 9], [8, 7]], ["A", "A", "A", "B", "B", "B"]], "expected": None},
                {"function": "predire", "inputs": [[2, 2]], "expected": "A"},
                {"function": "predire", "inputs": [[7, 8]], "expected": "B"},
            ]
        ),
        
        Exercise(
            id="183",
            title="Réseaux de neurones convolutionnels (CNN) simple",
            description="Classe `CNN` avec une couche de convolution basique.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "CNN", "inputs": [(5, 5), (3, 3)], "expected": "INIT"},
                {"function": "convolution", "inputs": [[[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0]]], "expected": [[4, 3, 4], [2, 4, 3], [2, 3, 4]]},
            ],
            solution_template="""class CNN:
    def __init__(self, taille_image, taille_filtre):
        # Votre code ici
        self.filtre = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]  # Exemple
        pass
    
    def convolution(self, image):
        # Applique la convolution
        pass"""
        ),
        
        Exercise(
            id="184",
            title="Clustering hiérarchique",
            description="Fonction `clustering_hierarchique(points, methode)` qui construit un dendrogramme.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "clustering_hierarchique", "inputs": [[[1, 1], [2, 1], [1, 2], [5, 5], [6, 5], [5, 6]], "complete"], "expected": {"dendrogramme": [{"points": [0, 1, 2], "distance": 1.414}, {"points": [3, 4, 5], "distance": 1.414}], "clusters_finaux": [[0, 1, 2], [3, 4, 5]]}},
            ]
        ),
        
        Exercise(
            id="185",
            title="Détection d'anomalies par isolation forest",
            description="Classe `IsolationForest` qui détecte les anomalies par isolation.",
            difficulty="difficile",
            category="Intelligence artificielle",
            test_cases=[
                {"function": "IsolationForest", "inputs": [10], "expected": "INIT"},
                {"function": "entrainer", "inputs": [[[1, 2], [2, 1], [1.5, 1.5], [100, 100]]], "expected": None},
                {"function": "score_anomalie", "inputs": [[1.2, 1.8]], "expected": 0.2},
                {"function": "score_anomalie", "inputs": [[100, 100]], "expected": 0.9},
            ]
        ),
    ])
    
    # === TRAITEMENT D'IMAGES ET SIGNAUX (186-200) ===
    
    exercises.extend([
        Exercise(
            id="186",
            title="Filtre de convolution 2D",
            description="Fonction `convolution_2d(image, noyau)` qui applique un filtre de convolution.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "convolution_2d", "inputs": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]], "expected": [[1, 0, 1], [0, 1, 0], [1, 0, 1]]},
                {"function": "convolution_2d", "inputs": [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]], "expected": [[9, 9, 9], [9, 9, 9], [9, 9, 9]]},
            ],
            hints=[
                "Parcourez l'image avec le noyau",
                "Multipliez élément par élément et sommez",
                "Gérez les bords (padding ou troncature)"
            ]
        ),
        
        Exercise(
            id="187",
            title="Détection de contours (Sobel)",
            description="Fonction `detecter_contours_sobel(image)` qui utilise l'opérateur de Sobel.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "detecter_contours_sobel", "inputs": [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], "expected": [[255, 255, 255], [255, 255, 255], [255, 255, 255]]},
                {"function": "detecter_contours_sobel", "inputs": [[[100, 100, 100], [100, 200, 100], [100, 100, 100]]], "expected": [[141, 200, 141], [200, 283, 200], [141, 200, 141]]},
            ],
            hints=[
                "Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]",
                "Gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]",
                "Magnitude = sqrt(Gx² + Gy²)"
            ]
        ),
        
        Exercise(
            id="188",
            title="Transformation de Hough pour lignes",
            description="Fonction `transformee_hough(image_contours)` qui détecte les lignes droites.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "transformee_hough", "inputs": [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]], "expected": {"lignes": [(45, 0), (135, 2)], "accumulator": "ARRAY"}},
            ],
            hints=[
                "ρ = x*cos(θ) + y*sin(θ)",
                "Accumulez les votes dans l'espace (ρ, θ)",
                "Trouvez les pics dans l'accumulateur"
            ]
        ),
        
        Exercise(
            id="189",
            title="Segmentation par croissance de régions",
            description="Fonction `croissance_regions(image, seeds, seuil)` qui segmente l'image.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "croissance_regions", "inputs": [[[10, 12, 11], [13, 50, 15], [14, 16, 12]], [(0, 0)], 5], "expected": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]},
            ],
            hints=[
                "Commencez avec les graines (seeds)",
                "Ajoutez les pixels voisins similaires",
                "Utilisez une file pour le parcours"
            ]
        ),
        
        Exercise(
            id="190",
            title="Morphologie mathématique (érosion/dilatation)",
            description="Fonction `morphologie(image_binaire, operation, element_structurant)` pour érosion/dilatation.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "morphologie", "inputs": [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], "erosion", [[1, 1, 1], [1, 1, 1], [1, 1, 1]]], "expected": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]},
                {"function": "morphologie", "inputs": [[[0, 1, 0], [1, 1, 1], [0, 1, 0]], "dilatation", [[1, 1, 1], [1, 1, 1], [1, 1, 1]]], "expected": [[1, 1, 1], [1, 1, 1], [1, 1, 1]]},
            ]
        ),
        
        Exercise(
            id="191",
            title="Histogramme d'image et égalisation",
            description="Fonction `egaliser_histogramme(image)` qui égalise l'histogramme d'intensité.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "egaliser_histogramme", "inputs": [[[0, 1, 2], [0, 1, 2], [0, 1, 2]]], "expected": [[0, 127, 255], [0, 127, 255], [0, 127, 255]]},
            ],
            hints=[
                "Calculez l'histogramme cumulé",
                "Normalisez entre 0 et 255",
                "Mappez chaque intensité"
            ]
        ),
        
        Exercise(
            id="192",
            title="Filtre médian pour débruitage",
            description="Fonction `filtre_median(image, taille_fenetre)` qui supprime le bruit impulsionnel.",
            difficulty="facile",
            category="Traitement d'images",
            test_cases=[
                {"function": "filtre_median", "inputs": [[[1, 255, 3], [4, 5, 255], [7, 8, 9]], 3], "expected": [[4, 5, 5], [5, 5, 8], [5, 8, 8]]},
                {"function": "filtre_median", "inputs": [[[10, 20, 30], [40, 50, 60], [70, 80, 90]], 3], "expected": [[40, 50, 50], [50, 50, 60], [50, 60, 60]]},
            ]
        ),
        
        Exercise(
            id="193",
            title="Compression d'image par quantification",
            description="Fonction `quantifier_image(image, nb_niveaux)` qui réduit le nombre de niveaux.",
            difficulty="facile",
            category="Traitement d'images",
            test_cases=[
                {"function": "quantifier_image", "inputs": [[[0, 63, 127, 191, 255]], 4], "expected": [[0, 85, 170, 170, 255]]},
                {"function": "quantifier_image", "inputs": [[[100, 150, 200]], 2], "expected": [[127, 127, 255]]},
            ],
            hints=[
                "Divisez [0, 255] en nb_niveaux intervalles",
                "Mappez chaque pixel à son niveau"
            ]
        ),
        
        Exercise(
            id="194",
            title="Transformée de Fourier 2D discrète",
            description="Fonction `fft_2d(image)` qui calcule la FFT 2D d'une image.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "fft_2d", "inputs": [[[1, 0], [0, 1]]], "expected": [[(1+0j), (1+0j)], [(1+0j), (1+0j)]]},
            ],
            hints=[
                "Appliquez FFT sur les lignes puis colonnes",
                "Utilisez les propriétés de symétrie"
            ]
        ),
        
        Exercise(
            id="195",
            title="Mise en correspondance de templates",
            description="Fonction `template_matching(image, template)` qui trouve la meilleure correspondance.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "template_matching", "inputs": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[6, 7], [10, 11]]], "expected": {"position": (1, 1), "score": 1.0}},
            ],
            hints=[
                "Calculez la corrélation normalisée",
                "Parcourez toutes les positions possibles"
            ]
        ),
        
        Exercise(
            id="196",
            title="Extraction de caractéristiques SURF/SIFT simplifiée",
            description="Fonction `detecter_points_cles(image)` qui trouve les points d'intérêt.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "detecter_points_cles", "inputs": [[[0, 0, 0], [0, 255, 0], [0, 0, 0]]], "expected": [{"x": 1, "y": 1, "intensite": 255, "descripteur": [1, 0, 1, 0, 1, 0, 1, 0]}]},
            ]
        ),
        
        Exercise(
            id="197",
            title="Filtrage gaussien adaptatif",
            description="Fonction `filtre_gaussien_adaptatif(image, sigma)` avec noyau gaussien.",
            difficulty="moyen",
            category="Traitement d'images",
            test_cases=[
                {"function": "filtre_gaussien_adaptatif", "inputs": [[[100, 200, 100], [50, 150, 250], [100, 200, 100]], 1.0], "expected": [[112, 162, 138], [100, 150, 175], [112, 162, 138]]},
            ],
            hints=[
                "G(x,y) = exp(-(x²+y²)/(2σ²))",
                "Normalisez le noyau"
            ]
        ),
        
        Exercise(
            id="198",
            title="Décomposition en ondelettes 2D",
            description="Fonction `ondelettes_2d(image, niveau)` qui décompose l'image en sous-bandes.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "ondelettes_2d", "inputs": [[[4, 6], [2, 8]], 1], "expected": {"LL": [[5]], "LH": [[-1]], "HL": [[1]], "HH": [[3]]}},
            ],
            hints=[
                "Filtres passe-bas et passe-haut",
                "Sous-échantillonnage par 2"
            ]
        ),
        
        Exercise(
            id="199",
            title="Restauration d'image par filtre de Wiener",
            description="Fonction `filtre_wiener(image_degradee, psf, snr)` qui restaure une image dégradée.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "filtre_wiener", "inputs": [[[50, 100, 50]], [[0.5, 0.5]], 10], "expected": [[75, 75, 75]]},
            ]
        ),
        
        Exercise(
            id="200",
            title="Compression JPEG simplifiée",
            description="Fonction `jpeg_simple(image, qualite)` qui simule la compression JPEG.",
            difficulty="difficile",
            category="Traitement d'images",
            test_cases=[
                {"function": "jpeg_simple", "inputs": [[[128, 128, 128, 128], [128, 128, 128, 128], [128, 128, 128, 128], [128, 128, 128, 128]], 50], "expected": [[128, 128, 128, 128], [128, 128, 128, 128], [128, 128, 128, 128], [128, 128, 128, 128]]},
            ],
            hints=[
                "DCT 8x8, quantification, codage entropique",
                "Qualité influence la matrice de quantification"
            ]
        ),
    ])
    
    # === BASES DE DONNÉES ET SQL (201-215) ===
    
    exercises.extend([
        Exercise(
            id="201",
            title="Moteur de base de données simple",
            description="Classe `BaseDeDonnees` qui simule une base avec tables, insertion, sélection.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "BaseDeDonnees", "inputs": [], "expected": "INIT"},
                {"function": "creer_table", "inputs": ["users", ["id", "nom", "age"]], "expected": True},
                {"function": "inserer", "inputs": ["users", [1, "Alice", 25]], "expected": True},
                {"function": "inserer", "inputs": ["users", [2, "Bob", 30]], "expected": True},
                {"function": "selectionner", "inputs": ["users", "age > 25"], "expected": [[2, "Bob", 30]]},
            ],
            solution_template="""class BaseDeDonnees:
    def __init__(self):
        # Votre code ici
        pass
    
    def creer_table(self, nom_table, colonnes):
        pass
    
    def inserer(self, nom_table, valeurs):
        pass
    
    def selectionner(self, nom_table, condition):
        pass"""
        ),
        
        Exercise(
            id="202",
            title="Index B+ tree simple",
            description="Classe `IndexBPlus` qui implémente un index pour accès rapide.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "IndexBPlus", "inputs": [3], "expected": "INIT"},
                {"function": "inserer", "inputs": [10, "data10"], "expected": None},
                {"function": "inserer", "inputs": [5, "data5"], "expected": None},
                {"function": "rechercher", "inputs": [10], "expected": "data10"},
                {"function": "rechercher", "inputs": [15], "expected": None},
            ]
        ),
        
        Exercise(
            id="203",
            title="Jointure de tables",
            description="Fonction `jointure(table1, table2, cle1, cle2, type_jointure)` qui joint deux tables.",
            difficulty="moyen",
            category="Bases de données",
            test_cases=[
                {"function": "jointure", "inputs": [[{"id": 1, "nom": "Alice"}, {"id": 2, "nom": "Bob"}], [{"user_id": 1, "ville": "Paris"}, {"user_id": 3, "ville": "Lyon"}], "id", "user_id", "inner"], "expected": [{"id": 1, "nom": "Alice", "user_id": 1, "ville": "Paris"}]},
                {"function": "jointure", "inputs": [[{"id": 1, "nom": "Alice"}], [{"user_id": 1, "ville": "Paris"}], "id", "user_id", "left"], "expected": [{"id": 1, "nom": "Alice", "user_id": 1, "ville": "Paris"}]},
            ]
        ),
        
        Exercise(
            id="204",
            title="Optimiseur de requêtes simple",
            description="Fonction `optimiser_requete(requete_sql)` qui optimise l'ordre des opérations.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "optimiser_requete", "inputs": ["SELECT * FROM users WHERE age > 25 AND city = 'Paris'"], "expected": {"operations": ["FILTER city = 'Paris'", "FILTER age > 25", "SELECT *"], "cout_estime": 100}},
            ]
        ),
        
        Exercise(
            id="205",
            title="Transaction et verrous",
            description="Classe `GestionnaireTransactions` qui gère les transactions ACID.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "GestionnaireTransactions", "inputs": [], "expected": "INIT"},
                {"function": "commencer_transaction", "inputs": ["T1"], "expected": True},
                {"function": "verrouiller", "inputs": ["T1", "table1", "shared"], "expected": True},
                {"function": "valider", "inputs": ["T1"], "expected": True},
            ]
        ),
        
        Exercise(
            id="206",
            title="Parser SQL basique",
            description="Fonction `parser_sql(requete)` qui analyse une requête SQL simple.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "parser_sql", "inputs": ["SELECT nom, age FROM users WHERE age > 25"], "expected": {"type": "SELECT", "colonnes": ["nom", "age"], "from": "users", "where": "age > 25"}},
                {"function": "parser_sql", "inputs": ["INSERT INTO users VALUES (1, 'Alice', 25)"], "expected": {"type": "INSERT", "table": "users", "valeurs": [1, "Alice", 25]}},
            ]
        ),
        
        Exercise(
            id="207",
            title="Cache de requêtes LRU",
            description="Classe `CacheRequetes` qui met en cache les résultats de requêtes.",
            difficulty="moyen",
            category="Bases de données",
            test_cases=[
                {"function": "CacheRequetes", "inputs": [3], "expected": "INIT"},
                {"function": "get", "inputs": ["SELECT * FROM users"], "expected": None},
                {"function": "put", "inputs": ["SELECT * FROM users", [{"id": 1, "nom": "Alice"}]], "expected": None},
                {"function": "get", "inputs": ["SELECT * FROM users"], "expected": [{"id": 1, "nom": "Alice"}]},
            ]
        ),
        
        Exercise(
            id="208",
            title="Normalisation de schéma",
            description="Fonction `normaliser_schema(table, forme_normale)` qui normalise un schéma relationnel.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "normaliser_schema", "inputs": [{"nom": "commandes", "colonnes": ["id", "client", "adresse_client", "produit", "prix"], "dependances": [("client", "adresse_client")]}, "2NF"], "expected": {"tables": [{"nom": "clients", "colonnes": ["client", "adresse_client"]}, {"nom": "commandes", "colonnes": ["id", "client", "produit", "prix"]}]}},
            ]
        ),
        
        Exercise(
            id="209",
            title="Gestionnaire de stockage sur disque",
            description="Classe `GestionnaireStockage` qui gère les pages de données sur disque.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "GestionnaireStockage", "inputs": [1024], "expected": "INIT"},
                {"function": "allouer_page", "inputs": [], "expected": 0},
                {"function": "ecrire_page", "inputs": [0, b"hello world"], "expected": True},
                {"function": "lire_page", "inputs": [0], "expected": b"hello world"},
            ]
        ),
        
        Exercise(
            id="210",
            title="Estimation de cardinalité",
            description="Fonction `estimer_cardinalite(table, predicat)` qui estime le nombre de résultats.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "estimer_cardinalite", "inputs": [{"nom": "users", "nb_lignes": 1000, "histogrammes": {"age": {18: 50, 25: 200, 30: 300, 40: 450}}}, "age BETWEEN 25 AND 35"], "expected": 400},
            ]
        ),
        
        Exercise(
            id="211",
            title="Réplication maître-esclave",
            description="Classe `ReplicationManager` qui gère la réplication de données.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "ReplicationManager", "inputs": [], "expected": "INIT"},
                {"function": "ajouter_esclave", "inputs": ["esclave1"], "expected": True},
                {"function": "repliquer", "inputs": ["INSERT INTO users VALUES (1, 'Alice')"], "expected": True},
                {"function": "verifier_coherence", "inputs": [], "expected": True},
            ]
        ),
        
        Exercise(
            id="212",
            title="Détection de deadlock",
            description="Fonction `detecter_deadlock(graphe_attente)` qui détecte les interblocages.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "detecter_deadlock", "inputs": [{"T1": ["T2"], "T2": ["T3"], "T3": ["T1"]}], "expected": True},
                {"function": "detecter_deadlock", "inputs": [{"T1": ["T2"], "T2": ["T3"], "T3": []}], "expected": False},
            ]
        ),
        
        Exercise(
            id="213",
            title="Compression de données relationnelles",
            description="Fonction `comprimer_colonne(donnees, algorithme)` qui comprime une colonne.",
            difficulty="moyen",
            category="Bases de données",
            test_cases=[
                {"function": "comprimer_colonne", "inputs": [["A", "A", "B", "A", "C", "A"], "RLE"], "expected": {"donnees_compressees": [("A", 2), ("B", 1), ("A", 1), ("C", 1), ("A", 1)], "taux_compression": 0.83}},
                {"function": "comprimer_colonne", "inputs": [[1, 2, 3, 4, 5], "delta"], "expected": {"donnees_compressees": [1, 1, 1, 1, 1], "taux_compression": 0.6}},
            ]
        ),
        
        Exercise(
            id="214",
            title="Planificateur de requêtes distribuées",
            description="Fonction `planifier_requete_distribuee(requete, noeuds)` pour bases distribuées.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "planifier_requete_distribuee", "inputs": ["SELECT * FROM table1 JOIN table2 ON id", [{"noeud": "N1", "tables": ["table1"]}, {"noeud": "N2", "tables": ["table2"]}]], "expected": {"plan": ["SEND table1 FROM N1 TO N2", "JOIN ON N2", "RETURN FROM N2"], "cout_reseau": 1000}},
            ]
        ),
        
        Exercise(
            id="215",
            title="Backup incrémental",
            description="Classe `BackupManager` qui gère les sauvegardes incrémentielles.",
            difficulty="difficile",
            category="Bases de données",
            test_cases=[
                {"function": "BackupManager", "inputs": [], "expected": "INIT"},
                {"function": "backup_complet", "inputs": [{"table1": [{"id": 1, "nom": "Alice"}]}], "expected": "backup_1"},
                {"function": "backup_incremental", "inputs": [{"table1": [{"id": 2, "nom": "Bob"}]}], "expected": "backup_2"},
                {"function": "restaurer", "inputs": ["backup_2"], "expected": {"table1": [{"id": 1, "nom": "Alice"}, {"id": 2, "nom": "Bob"}]}},
            ]
        ),
        
        Exercise(
            id="216",
            title="Lire un fichier temporaire",
            description="Fonction `lire_fichier_temporaire(lignes)` qui crée un fichier temporaire avec les lignes fournies puis retourne tout le contenu sous forme de chaîne.",
            difficulty="facile",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "lire_fichier_temporaire", "inputs": [["Bonjour", "Monde", "Python"]], "expected": "Bonjour\nMonde\nPython"},
                {"function": "lire_fichier_temporaire", "inputs": [[]], "expected": ""},
                {"function": "lire_fichier_temporaire", "inputs": [["Une seule ligne"]], "expected": "Une seule ligne"},
            ],
            hints=[
                "Importez tempfile",
                "Écrivez les lignes dans le fichier temporaire",
                "read() pour lire tout le contenu",
                "join() avec \\n pour chaque ligne"
            ]
        ),

        Exercise(
            id="217",
            title="Écrire dans un fichier temporaire",
            description="Fonction `ecrire_fichier_temporaire(lignes, contenu)` qui crée un fichier temporaire et y écrit le contenu (liste de lignes ou texte).",
            difficulty="facile",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "ecrire_fichier_temporaire", "inputs": [["Hello World"]], "expected": True},
                {"function": "ecrire_fichier_temporaire", "inputs": [["Ligne 1", "Ligne 2"]], "expected": True},
                {"function": "ecrire_fichier_temporaire", "inputs": [[]], "expected": True},
            ],
            hints=[
                "Importez tempfile",
                "Mode 'w+' pour écrire",
                "write() ou writelines()",
                "Retournez True si écrit correctement"
            ]
        ),

        Exercise(
            id="218",
            title="Compter les lignes (fichier temporaire)",
            description="Fonction `compter_lignes_temporaire(lignes)` qui crée un fichier temporaire avec les lignes fournies, puis retourne le nombre de lignes.",
            difficulty="facile",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "compter_lignes_temporaire", "inputs": [["Bonjour", "Monde", "Python", "Test", "Fin"]], "expected": 5},
                {"function": "compter_lignes_temporaire", "inputs": [[]], "expected": 0},
                {"function": "compter_lignes_temporaire", "inputs": [["Une seule ligne"]], "expected": 1},
            ],
            hints=[
                "Importez le module `tempfile`",
                "Écrivez les lignes fournies dans le fichier temporaire",
                "Utilisez sum(1 for line in file) pour compter les lignes",
                "Fichier vide = 0 lignes"
            ]
        ),

        Exercise(
            id="219",
            title="Rechercher dans un fichier temporaire",
            description="Fonction `rechercher_dans_fichier_temporaire(lignes, mot)` qui crée un fichier temporaire avec les lignes fournies, puis retourne les numéros des lignes contenant le mot.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {
                    "function": "rechercher_dans_fichier_temporaire",
                    "inputs": [["Python est génial", "Java aussi", "Python domine", "C++ rapide", "Python un jour", "Go", "Rust", "Python encore"], "Python"],
                    "expected": [1, 3, 5, 8]
                },
                {
                    "function": "rechercher_dans_fichier_temporaire",
                    "inputs": [["Bonjour le monde", "Rien ici", "Encore rien"], "absent"],
                    "expected": []
                },
                {
                    "function": "rechercher_dans_fichier_temporaire",
                    "inputs": [["import os", "x=1", "def test():", "pass", "# commentaire", "print('ok')", "def autre():", "y=2", "z=3", "class A:", "init=0", "def final():", "end"], "def"],
                    "expected": [3, 7, 12]
                }
            ],
            hints=[
                "Importez le module `tempfile`",
                "Écrivez chaque ligne dans le fichier temporaire",
                "Parcourez le fichier avec enumerate() pour avoir le numéro de ligne",
                "Commencez la numérotation à 1",
                "Ajoutez le numéro si mot in ligne"
            ]
        ),

        Exercise(
            id="220",
            title="Copier un fichier temporaire",
            description="Fonction `copier_fichier_temporaire(lignes_source)` qui crée un fichier temporaire source, le copie dans un autre fichier temporaire et retourne True si succès.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "copier_fichier_temporaire", "inputs": [["ligne1", "ligne2"]], "expected": True},
                {"function": "copier_fichier_temporaire", "inputs": [[]], "expected": True},
            ],
            hints=[
                "Importez tempfile",
                "Écrivez les lignes dans un fichier temporaire source",
                "Ouvrez un fichier temporaire destination en mode 'w+' et copiez le contenu",
                "Retournez True si aucun problème"
            ]
        ),


        Exercise(
            id="221",
            title="Fusionner des fichiers temporaires",
            description="Fonction `fusionner_fichiers_temporaire(liste_lignes)` qui crée plusieurs fichiers temporaires avec leurs lignes respectives, fusionne tout dans un fichier temporaire de sortie et retourne True.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "fusionner_fichiers_temporaire", "inputs": [[["L1F1","L2F1"], ["L1F2","L2F2"]]], "expected": True},
                {"function": "fusionner_fichiers_temporaire", "inputs": [[[]]], "expected": True},
            ],
            hints=[
                "Importez tempfile",
                "Créez un fichier temporaire par sous-liste de lignes",
                "Écrivez tout dans un fichier temporaire de sortie",
                "Retournez True si succès"
            ]
        ),

        # 222 -> Statistiques
        Exercise(
            id="222",
            title="Statistiques de fichier temporaire",
            description="Fonction `stats_fichier_temporaire(lignes)` qui crée un fichier temporaire, écrit les lignes et retourne {'lignes': n, 'mots': m, 'caracteres': c}.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "stats_fichier_temporaire", "inputs": [["Python est super", "Bonjour le monde"]], "expected": {"lignes": 2, "mots": 6, "caracteres": 30}},
                {"function": "stats_fichier_temporaire", "inputs": [[]], "expected": {"lignes": 0, "mots": 0, "caracteres": 0}},
            ],
            hints=[
                "Importez tempfile",
                "Écrivez les lignes dans le fichier temporaire",
                "len(lignes) pour le nombre de lignes",
                "split() pour compter les mots",
                "len(contenu) pour le nombre de caractères"
            ]
        ),

        # 223 -> Remplacer
        Exercise(
            id="223",
            title="Remplacer dans un fichier temporaire",
            description="Fonction `remplacer_dans_fichier_temporaire(lignes, ancien, nouveau)` qui crée un fichier temporaire, remplace toutes les occurrences et retourne le nombre de remplacements.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "remplacer_dans_fichier_temporaire", "inputs": [["Python est Python"], "Python", "Java"], "expected": 2},
                {"function": "remplacer_dans_fichier_temporaire", "inputs": [["Bonjour le monde"], "absent", "présent"], "expected": 0},
            ],
            hints=[
                "Importez tempfile",
                "write() pour créer le fichier temporaire",
                "replace() pour modifier le contenu",
                "Retournez le nombre de remplacements"
            ]
        ),

        # 224 -> Lire CSV
        Exercise(
            id="224",
            title="Lire CSV temporaire",
            description="Fonction `lire_csv_temporaire(lignes, delimiteur=',')` qui crée un fichier temporaire avec les lignes CSV et retourne la liste de listes.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "lire_csv_temporaire", "inputs": [["nom,age,ville","Alice,25,Paris","Bob,30,Lyon"], ","], "expected": [["nom","age","ville"],["Alice","25","Paris"],["Bob","30","Lyon"]]},
                {"function": "lire_csv_temporaire", "inputs": [["x;y","1;2","3;4"], ";"], "expected": [["x","y"],["1","2"],["3","4"]]},
                {"function": "lire_csv_temporaire", "inputs": [[] , ","], "expected": []},
            ],
            hints=[
                "tempfile pour créer le fichier",
                "split(delimiteur) sur chaque ligne",
                "strip() pour enlever espaces superflus"
            ]
        ),

        # 225 -> Écrire CSV
        Exercise(
            id="225",
            title="Écrire CSV temporaire",
            description="Fonction `ecrire_csv_temporaire(donnees, delimiteur=',')` qui écrit les données dans un fichier temporaire CSV et retourne True.",
            difficulty="moyen",
            category="Manipulation de fichiers",
            test_cases=[
                {"function": "ecrire_csv_temporaire", "inputs": [[[["nom","age"],["Alice",25],["Bob",30]], ","]], "expected": True},
                {"function": "ecrire_csv_temporaire", "inputs": [[[["x","y","z"],[1,2,3]], ";"]], "expected": True},
                {"function": "ecrire_csv_temporaire", "inputs": [[[], ","]], "expected": True},
            ],
            hints=[
                "tempfile pour créer le fichier",
                "join() avec le délimiteur",
                "Convertissez tout en string",
                "Ajoutez \\n à la fin de chaque ligne"
            ]
        ),

        # === DICTIONNAIRES AVANCÉS (226-230) ===

        Exercise(
            id="226",
            title="Dictionnaire imbriqué - accès sécurisé",
            description="Fonction `acces_securise(dico, chemin)` qui accède à une valeur avec un chemin 'a.b.c'.",
            difficulty="moyen",
            category="Dictionnaires avancés",
            test_cases=[
                {"function": "acces_securise", "inputs": [{"a": {"b": {"c": 42}}}, "a.b.c"], "expected": 42},
                {"function": "acces_securise", "inputs": [{"x": {"y": 10}}, "x.y"], "expected": 10},
                {"function": "acces_securise", "inputs": [{"a": {"b": 1}}, "a.b.c"], "expected": None},
            ],
            hints=[
                "split() le chemin sur le point",
                "Parcourez niveau par niveau",
                "Retournez None si une clé n'existe pas"
            ]
        ),

        Exercise(
            id="227",
            title="Dictionnaire de compteurs",
            description="Classe `Compteur` qui hérite de dict et compte automatiquement les éléments.",
            difficulty="moyen",
            category="Dictionnaires avancés",
            test_cases=[
                {"function": "Compteur", "inputs": [["a", "b", "a", "c", "b", "a"]], "expected": {"a": 3, "b": 2, "c": 1}},
                {"function": "plus_frequent", "inputs": [], "expected": ("a", 3)},
                {"function": "incrementer", "inputs": ["d"], "expected": None},
            ],
            solution_template="""class Compteur(dict):
            def __init__(self, iterable=None):
                super().__init__()
                # Votre code ici
                
            def plus_frequent(self):
                # Retourne (element, count) le plus fréquent
                pass
                
            def incrementer(self, element):
                # Incrémente le compteur d'un élément
                pass""",
            hints=[
                "Héritez de dict",
                "Initialisez les compteurs dans __init__",
                "max() avec key= pour plus_frequent"
            ]
        ),

        Exercise(
            id="228",
            title="Cache avec expiration",
            description="Classe `CacheExpiration` qui supprime automatiquement les entrées expirées.",
            difficulty="difficile",
            category="Dictionnaires avancés",
            test_cases=[
                {"function": "CacheExpiration", "inputs": [5], "expected": "INIT"},
                {"function": "put", "inputs": ["key1", "value1"], "expected": None},
                {"function": "get", "inputs": ["key1"], "expected": "value1"},
                {"function": "get_after_expiry", "inputs": ["key1"], "expected": None},
            ],
            hints=[
                "Stockez timestamp avec chaque valeur",
                "Vérifiez l'expiration dans get()",
                "Nettoyez périodiquement les entrées expirées"
            ]
        ),

        Exercise(
            id="229",
            title="Dictionnaire ordonné par valeurs",
            description="Fonction `dict_trie_par_valeurs(dico, reverse=False)` qui maintient l'ordre par valeurs.",
            difficulty="moyen",
            category="Dictionnaires avancés",
            test_cases=[
                {"function": "dict_trie_par_valeurs", "inputs": [{"a": 3, "b": 1, "c": 2}, False], "expected": {"b": 1, "c": 2, "a": 3}},
                {"function": "dict_trie_par_valeurs", "inputs": [{"x": 10, "y": 5, "z": 15}, True], "expected": {"z": 15, "x": 10, "y": 5}},
                {"function": "dict_trie_par_valeurs", "inputs": [{}, False], "expected": {}},
            ],
            hints=[
                "sorted() avec key=lambda item: item[1]",
                "dict() pour reconstruire depuis les items triés",
                "reverse=True pour ordre décroissant"
            ]
        ),

        Exercise(
            id="230",
            title="Dictionnaire avec valeurs par défaut calculées",
            description="Classe `DictDefautCalcule` où les valeurs manquantes sont calculées par une fonction.",
            difficulty="difficile",
            category="Dictionnaires avancés",
            test_cases=[
                {"function": "DictDefautCalcule", "inputs": [lambda x: x*x], "expected": "INIT"},
                {"function": "get_item", "inputs": [5], "expected": 25},
                {"function": "get_item", "inputs": [3], "expected": 9},
                {"function": "contains", "inputs": [5], "expected": True},
            ],
            solution_template="""class DictDefautCalcule(dict):
            def __init__(self, fonction_defaut):
                super().__init__()
                self.fonction_defaut = fonction_defaut
                
            def __getitem__(self, key):
                # Votre code ici
                pass""",
            hints=[
                "Surchargez __getitem__",
                "Si clé absente, calculez avec la fonction",
                "Stockez la valeur calculée pour éviter recalcul"
            ]
        ),

        # === SETS AVANCÉS (231-235) ===

        Exercise(
            id="231",
            title="Opérations sur sets multiples",
            description="Fonction `operations_sets(liste_sets, operation)` qui applique une opération sur plusieurs sets.",
            difficulty="moyen",
            category="Sets avancés",
            test_cases=[
                {"function": "operations_sets", "inputs": [[{1, 2, 3}, {2, 3, 4}, {3, 4, 5}], "intersection"], "expected": {3}},
                {"function": "operations_sets", "inputs": [[{1, 2}, {3, 4}, {5, 6}], "union"], "expected": {1, 2, 3, 4, 5, 6}},
                {"function": "operations_sets", "inputs": [[{1, 2, 3}, {2, 3}], "difference"], "expected": {1}},
            ],
            hints=[
                "intersection: & entre tous les sets",
                "union: | entre tous les sets",
                "difference: premier set - tous les autres"
            ]
        ),

        Exercise(
            id="232",
            title="Set de Jaccard similarity",
            description="Fonction `similarite_jaccard(set1, set2)` qui calcule l'indice de Jaccard entre deux sets.",
            difficulty="moyen",
            category="Sets avancés",
            test_cases=[
                {"function": "similarite_jaccard", "inputs": [{1, 2, 3}, {2, 3, 4}], "expected": 0.5},
                {"function": "similarite_jaccard", "inputs": [{1, 2, 3}, {1, 2, 3}], "expected": 1.0},
                {"function": "similarite_jaccard", "inputs": [{1, 2}, {3, 4}], "expected": 0.0},
            ],
            hints=[
                "Jaccard = |intersection| / |union|",
                "Gérez le cas union vide",
                "Retournez un float"
            ]
        ),

        Exercise(
            id="233",
            title="Partitionnement d'un set",
            description="Fonction `partitionner_set(ensemble, condition)` qui divise un set selon une condition.",
            difficulty="moyen",
            category="Sets avancés",
            test_cases=[
                {"function": "partitionner_set", "inputs": [{1, 2, 3, 4, 5, 6}, lambda x: x % 2 == 0], "expected": ({2, 4, 6}, {1, 3, 5})},
                {"function": "partitionner_set", "inputs": [{"a", "bb", "ccc"}, lambda x: len(x) > 1], "expected": ({"bb", "ccc"}, {"a"})},
                {"function": "partitionner_set", "inputs": [{1, 2, 3}, lambda x: x > 5], "expected": (set(), {1, 2, 3})},
            ],
            hints=[
                "Créez deux sets vides",
                "Testez la condition sur chaque élément",
                "Retournez (vrais, faux)"
            ]
        ),

        Exercise(
            id="234",
            title="Set avec historique des modifications",
            description="Classe `SetAvecHistorique` qui garde trace des ajouts/suppressions.",
            difficulty="difficile",
            category="Sets avancés",
            test_cases=[
                {"function": "SetAvecHistorique", "inputs": [], "expected": "INIT"},
                {"function": "add", "inputs": [1], "expected": None},
                {"function": "add", "inputs": [2], "expected": None},
                {"function": "remove", "inputs": [1], "expected": None},
                {"function": "historique", "inputs": [], "expected": [("add", 1), ("add", 2), ("remove", 1)]},
            ],
            solution_template="""class SetAvecHistorique(set):
            def __init__(self):
                super().__init__()
                self._historique = []
                
            def add(self, element):
                # Votre code ici
                pass
                
            def remove(self, element):
                # Votre code ici
                pass
                
            def historique(self):
                # Retourne la liste des opérations
                pass""",
            hints=[
                "Héritez de set",
                "Gardez une liste _historique",
                "Enregistrez chaque opération"
            ]
        ),

        Exercise(
            id="235",
            title="Bloom filter simple",
            description="Classe `BloomFilter` qui implémente un filtre de Bloom basique avec sets.",
            difficulty="difficile",
            category="Sets avancés",
            test_cases=[
                {"function": "BloomFilter", "inputs": [100, 3], "expected": "INIT"},
                {"function": "add", "inputs": ["hello"], "expected": None},
                {"function": "add", "inputs": ["world"], "expected": None},
                {"function": "contains", "inputs": ["hello"], "expected": True},
                {"function": "contains", "inputs": ["absent"], "expected": False},
            ],
            solution_template="""class BloomFilter:
            def __init__(self, taille, nb_fonctions):
                self.taille = taille
                self.nb_fonctions = nb_fonctions
                self.bits = set()
                
            def _hash(self, element, seed):
                # Fonction de hachage simple
                pass
                
            def add(self, element):
                # Ajouter un élément
                pass
                
            def contains(self, element):
                # Vérifier la présence (peut-être faux positif)
                pass""",
            hints=[
                "Utilisez plusieurs fonctions de hash",
                "Set de bits = positions activées",
                "contains peut donner faux positifs mais jamais faux négatifs"
            ]
        ),
        
        Exercise(
            id="236",
            title="Classe simple - Personne",
            description="Classe `Personne` avec nom, age et méthodes de base (constructeur, __str__, anniversaire).",
            difficulty="facile",
            category="POO - Classes de base",
            test_cases=[
                {"function": "Personne", "inputs": ["Alice", 25], "expected": "INIT"},
                {"function": "__str__", "inputs": [], "expected": "Alice (25 ans)"},
                {"function": "anniversaire", "inputs": [], "expected": None},
                {"function": "age_after", "inputs": [], "expected": 26},
            ],
            solution_template="""class Personne:
            def __init__(self, nom, age):
                # Votre code ici
                pass
            
            def __str__(self):
                # Représentation string
                pass
            
            def anniversaire(self):
                # Incrémente l'âge de 1
                pass""",
            hints=[
                "self.nom et self.age dans __init__",
                "__str__ retourne une chaîne descriptive",
                "anniversaire modifie self.age"
            ]
        ),

        Exercise(
            id="237",
            title="Encapsulation - Compte bancaire",
            description="Classe `CompteBancaire` avec solde privé, dépôt, retrait et consultation sécurisée.",
            difficulty="moyen",
            category="POO - Encapsulation",
            test_cases=[
                {"function": "CompteBancaire", "inputs": [1000], "expected": "INIT"},
                {"function": "deposer", "inputs": [500], "expected": True},
                {"function": "retirer", "inputs": [200], "expected": True},
                {"function": "solde", "inputs": [], "expected": 1300},
                {"function": "retirer", "inputs": [2000], "expected": False},
            ],
            solution_template="""class CompteBancaire:
            def __init__(self, solde_initial):
                self.__solde = solde_initial  # Attribut privé
            
            def deposer(self, montant):
                # Ajouter de l'argent
                pass
            
            def retirer(self, montant):
                # Retirer si solde suffisant
                pass
            
            @property
            def solde(self):
                # Getter pour consulter le solde
                pass""",
            hints=[
                "__ devant attribut = privé",
                "Vérifiez montant > 0 et solde suffisant",
                "@property pour getter sécurisé"
            ]
        ),

        Exercise(
            id="238",
            title="Héritage simple - Animal et Chien",
            description="Classe `Animal` de base et classe `Chien` qui hérite avec spécialisation.",
            difficulty="moyen",
            category="POO - Héritage",
            test_cases=[
                {"function": "Chien", "inputs": ["Rex", 3, "Berger"], "expected": "INIT"},
                {"function": "se_presenter", "inputs": [], "expected": "Je suis Rex, un animal de 3 ans"},
                {"function": "aboyer", "inputs": [], "expected": "Rex aboie: Woof!"},
                {"function": "dormir", "inputs": [], "expected": "Rex dort paisiblement"},
            ],
            solution_template="""class Animal:
            def __init__(self, nom, age):
                self.nom = nom
                self.age = age
            
            def se_presenter(self):
                return f"Je suis {self.nom}, un animal de {self.age} ans"
            
            def dormir(self):
                return f"{self.nom} dort paisiblement"

        class Chien(Animal):
            def __init__(self, nom, age, race):
                # Votre code ici
                pass
            
            def aboyer(self):
                # Méthode spécifique aux chiens
                pass""",
            hints=[
                "super().__init__() pour appeler constructeur parent",
                "Ajoutez attributs spécifiques dans enfant",
                "Nouvelles méthodes dans classe fille"
            ]
        ),

        Exercise(
            id="239",
            title="Polymorphisme - Formes géométriques",
            description="Classes `Forme`, `Cercle`, `Rectangle` avec polymorphisme sur aire() et perimetre().",
            difficulty="moyen",
            category="POO - Polymorphisme",
            test_cases=[
                {"function": "Cercle", "inputs": [5], "expected": "INIT"},
                {"function": "aire_cercle", "inputs": [], "expected": 78.54},  # π * 5²
                {"function": "Rectangle", "inputs": [4, 6], "expected": "INIT"},
                {"function": "aire_rectangle", "inputs": [], "expected": 24},
                {"function": "test_polymorphisme", "inputs": [], "expected": [78.54, 24]},  # Test avec liste créée dans la fonction
            ],
            solution_template="""import math

        class Forme:
            def aire(self):
                raise NotImplementedError("Méthode à implémenter")
            
            def perimetre(self):
                raise NotImplementedError("Méthode à implémenter")

        class Cercle(Forme):
            def __init__(self, rayon):
                self.rayon = rayon
            
            def aire(self):
                return round(math.pi * self.rayon ** 2, 2)
            
            def perimetre(self):
                return round(2 * math.pi * self.rayon, 2)

        class Rectangle(Forme):
            def __init__(self, largeur, hauteur):
                self.largeur = largeur
                self.hauteur = hauteur
            
            def aire(self):
                return self.largeur * self.hauteur
            
            def perimetre(self):
                return 2 * (self.largeur + self.hauteur)

        def test_polymorphisme():
            # Fonction qui teste le polymorphisme
            cercle = Cercle(5)
            rectangle = Rectangle(4, 6)
            formes = [cercle, rectangle]
            return [forme.aire() for forme in formes]""",
            hints=[
                "math.pi pour π",
                "Même méthode, comportements différents = polymorphisme",
                "Test avec fonction qui crée les objets localement"
            ]
        ),

        Exercise(
            id="240",
            title="Méthodes magiques - Vecteur 2D",
            description="Classe `Vecteur2D` avec surcharge d'opérateurs (+, -, *, ==, str).",
            difficulty="moyen",
            category="POO - Méthodes magiques",
            test_cases=[
                {"function": "Vecteur2D", "inputs": [3, 4], "expected": "INIT"},
                {"function": "__str__", "inputs": [], "expected": "(3, 4)"},
                {"function": "__add__", "inputs": [{"x": 1, "y": 2}], "expected": {"x": 4, "y": 6}},
                {"function": "__mul__", "inputs": [2], "expected": {"x": 6, "y": 8}},
                {"function": "norme", "inputs": [], "expected": 5.0},
            ],
            solution_template="""import math

        class Vecteur2D:
            def __init__(self, x, y):
                self.x = x
                self.y = y
            
            def __str__(self):
                # Représentation string
                pass
            
            def __add__(self, autre):
                # Addition de vecteurs
                pass
            
            def __mul__(self, scalaire):
                # Multiplication par un scalaire
                pass
            
            def __eq__(self, autre):
                # Égalité de vecteurs
                pass
            
            def norme(self):
                # √(x² + y²)
                pass""",
            hints=[
                "__add__ crée nouveau Vecteur2D",
                "__mul__ multiplie composantes par scalaire",
                "__eq__ compare x et y des deux vecteurs"
            ]
        ),


        Exercise(
            id="241",
            title="Classe abstraite - Véhicule",
            description="Classe abstraite `Vehicule` et implémentations `Voiture`, `Velo` avec abc module.",
            difficulty="difficile",
            category="POO - Classes abstraites",
            test_cases=[
                {"function": "Voiture", "inputs": ["Toyota", 4], "expected": "INIT"},
                {"function": "demarrer", "inputs": [], "expected": "La Toyota démarre le moteur"},
                {"function": "nb_roues", "inputs": [], "expected": 4},
                {"function": "Velo", "inputs": ["VTT"], "expected": "INIT"},
                {"function": "demarrer", "inputs": [], "expected": "Le VTT commence à pédaler"},
            ],
            solution_template="""from abc import ABC, abstractmethod

        class Vehicule(ABC):
            def __init__(self, nom):
                self.nom = nom
            
            @abstractmethod
            def demarrer(self):
                pass
            
            @abstractmethod
            def nb_roues(self):
                pass

        class Voiture(Vehicule):
            def __init__(self, nom, roues):
                # Votre code ici
                pass
            
            def demarrer(self):
                pass
            
            def nb_roues(self):
                pass

        class Velo(Vehicule):
            def __init__(self, nom):
                # Votre code ici
                pass
            
            def demarrer(self):
                pass
            
            def nb_roues(self):
                return 2""",
            hints=[
                "from abc import ABC, abstractmethod",
                "@abstractmethod force l'implémentation",
                "super().__init__() dans classes filles"
            ]
        ),

        Exercise(
            id="242",
            title="Composition - Ordinateur et composants",
            description="Classe `Ordinateur` composée de `Processeur`, `RAM` et `DisqueDur`.",
            difficulty="moyen",
            category="POO - Composition",
            test_cases=[
                {"function": "Ordinateur", "inputs": [], "expected": "INIT"},
                {"function": "ajouter_processeur", "inputs": ["Intel i7", 3.2], "expected": None},
                {"function": "ajouter_ram", "inputs": [16], "expected": None},
                {"function": "specs", "inputs": [], "expected": {"cpu": "Intel i7 (3.2 GHz)", "ram": "16 GB", "stockage": "Non installé"}},
                {"function": "peut_demarrer", "inputs": [], "expected": True},
            ],
            solution_template="""class Processeur:
            def __init__(self, modele, frequence):
                self.modele = modele
                self.frequence = frequence
            
            def __str__(self):
                return f"{self.modele} ({self.frequence} GHz)"

        class RAM:
            def __init__(self, taille):
                self.taille = taille
            
            def __str__(self):
                return f"{self.taille} GB"

        class DisqueDur:
            def __init__(self, capacite):
                self.capacite = capacite

        class Ordinateur:
            def __init__(self):
                # Composants initialement None
                pass
            
            def ajouter_processeur(self, modele, freq):
                pass
            
            def ajouter_ram(self, taille):
                pass
            
            def specs(self):
                # Retourne dict avec spécifications
                pass
            
            def peut_demarrer(self):
                # True si CPU et RAM installés
                pass""",
            hints=[
                "Composition = objets contiennent d'autres objets",
                "Vérifiez if composant is not None",
                "Créez objets composants dans méthodes ajouter"
            ]
        ),

        Exercise(
            id="243",
            title="Singleton - Configuration",
            description="Classe `Configuration` en singleton avec paramètres globaux de l'application.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "Configuration", "inputs": [], "expected": "INIT"},
                {"function": "get_instance", "inputs": [], "expected": "SAME_INSTANCE"},
                {"function": "set_param", "inputs": ["debug", True], "expected": None},
                {"function": "get_param", "inputs": ["debug"], "expected": True},
                {"function": "singleton_test", "inputs": [], "expected": True},  # config1 is config2
            ],
            solution_template="""class Configuration:
            _instance = None
            
            def __new__(cls):
                # Pattern Singleton
                pass
            
            def __init__(self):
                if not hasattr(self, '_initialized'):
                    self._params = {}
                    self._initialized = True
            
            def set_param(self, cle, valeur):
                pass
            
            def get_param(self, cle, defaut=None):
                pass
            
            @classmethod
            def get_instance(cls):
                # Retourne l'instance unique
                pass""",
            hints=[
                "__new__ contrôle la création d'instance",
                "_instance stocke la référence unique",
                "Initialisez une seule fois avec flag _initialized"
            ]
        ),

        Exercise(
            id="244",
            title="Observer Pattern - Sujet et observateurs",
            description="Classes `Sujet` et `Observateur` implémentant le pattern Observer.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "Sujet", "inputs": [], "expected": "INIT"},
                {"function": "EmailObserver", "inputs": ["alice@mail.com"], "expected": "INIT"},
                {"function": "test_observer_pattern", "inputs": [], "expected": ["Email envoyé à alice@mail.com: Nouveau message"]},
            ],
            solution_template="""class Observateur:
            def update(self, message):
                raise NotImplementedError

        class Sujet:
            def __init__(self):
                self._observateurs = []
            
            def ajouter_observateur(self, observateur):
                self._observateurs.append(observateur)
            
            def retirer_observateur(self, observateur):
                if observateur in self._observateurs:
                    self._observateurs.remove(observateur)
            
            def notifier(self, message):
                # Notifie tous les observateurs
                resultats = []
                for observateur in self._observateurs:
                    resultats.append(observateur.update(message))
                return resultats

        class EmailObserver(Observateur):
            def __init__(self, email):
                self.email = email
            
            def update(self, message):
                return f"Email envoyé à {self.email}: {message}"

        class SMSObserver(Observateur):
            def __init__(self, telephone):
                self.telephone = telephone
            
            def update(self, message):
                return f"SMS envoyé à {self.telephone}: {message}"

        def test_observer_pattern():
            # Fonction de test qui crée les objets
            sujet = Sujet()
            observer = EmailObserver("alice@mail.com")
            sujet.ajouter_observateur(observer)
            return sujet.notifier("Nouveau message")""",
            hints=[
                "Liste d'observateurs dans Sujet",
                "notifier() appelle update() sur chaque observateur",
                "Observateurs implémentent interface commune"
            ]
        ),

        Exercise(
            id="245",
            title="Factory Pattern - Créateur de formes",
            description="Factory pour créer différents types de formes selon un paramètre.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "FormeFactory", "inputs": [], "expected": "INIT"},
                {"function": "creer_forme", "inputs": ["cercle", {"rayon": 5}], "expected": "Cercle(5)"},
                {"function": "creer_forme", "inputs": ["rectangle", {"largeur": 4, "hauteur": 6}], "expected": "Rectangle(4x6)"},
                {"function": "creer_forme", "inputs": ["triangle", {"base": 3, "hauteur": 4}], "expected": "Triangle(3,4)"},
            ],
            solution_template="""class Forme:
            pass

        class Cercle(Forme):
            def __init__(self, rayon):
                self.rayon = rayon
            
            def __str__(self):
                return f"Cercle({self.rayon})"

        class Rectangle(Forme):
            def __init__(self, largeur, hauteur):
                self.largeur = largeur
                self.hauteur = hauteur
            
            def __str__(self):
                return f"Rectangle({self.largeur}x{self.hauteur})"

        class Triangle(Forme):
            def __init__(self, base, hauteur):
                self.base = base
                self.hauteur = hauteur
            
            def __str__(self):
                return f"Triangle({self.base},{self.hauteur})"

        class FormeFactory:
            @staticmethod
            def creer_forme(type_forme, params):
                # Créer la forme selon le type
                pass""",
            hints=[
                "Dictionary pour mapper types -> classes",
                "**params pour passer arguments dynamiquement",
                "@staticmethod car pas besoin d'instance"
            ]
        ),

        Exercise(
            id="246",
            title="Décorateur de classe - Timer",
            description="Décorateur `@timer` qui mesure le temps d'exécution des méthodes d'une classe.",
            difficulty="difficile",
            category="POO - Décorateurs",
            test_cases=[
                {"function": "CalculateurDecore", "inputs": [], "expected": "INIT"},
                {"function": "factorielle", "inputs": [5], "expected": 120},
                {"function": "get_temps_execution", "inputs": [], "expected": 0.001},  # temps approximatif
            ],
            solution_template="""import time
        import functools

        def timer(cls):
            # Décorateur de classe
            class DecoratedClass(cls):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self._temps_execution = {}
                
                def __getattribute__(self, name):
                    attr = super().__getattribute__(name)
                    if callable(attr) and not name.startswith('_'):
                        @functools.wraps(attr)
                        def wrapper(*args, **kwargs):
                            # Mesurer le temps
                            pass
                        return wrapper
                    return attr
                
                def get_temps_execution(self):
                    # Retourne temps de la dernière méthode appelée
                    pass
            
            return DecoratedClass

        @timer
        class Calculateur:
            def factorielle(self, n):
                if n <= 1:
                    return 1
                return n * self.factorielle(n-1)
            
            def fibonacci(self, n):
                if n <= 1:
                    return n
                return self.fibonacci(n-1) + self.fibonacci(n-2)""",
            hints=[
                "__getattribute__ intercepte tous les accès",
                "time.time() avant et après l'appel",
                "functools.wraps préserve métadonnées"
            ]
        ),

        Exercise(
            id="247",
            title="Context Manager - Gestionnaire de fichiers",
            description="Classe `GestionnaireFichier` qui implémente le protocol context manager.",
            difficulty="difficile",
            category="POO - Protocoles",
            test_cases=[
                {"function": "GestionnaireFichier", "inputs": ["test.txt", "w"], "expected": "INIT"},
                {"function": "with_usage", "inputs": [], "expected": "SUCCESS"},
                {"function": "is_closed", "inputs": [], "expected": True},
            ],
            solution_template="""class GestionnaireFichier:
            def __init__(self, nom_fichier, mode):
                self.nom_fichier = nom_fichier
                self.mode = mode
                self.fichier = None
            
            def __enter__(self):
                # Ouverture du fichier
                pass
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                # Fermeture du fichier
                pass
            
            def write(self, contenu):
                if self.fichier:
                    self.fichier.write(contenu)
            
            def read(self):
                if self.fichier:
                    return self.fichier.read()
                return ""

        # Test usage:
        def test_context_manager():
            with GestionnaireFichier("test.txt", "w") as gf:
                gf.write("Hello World")
            # Fichier automatiquement fermé""",
            hints=[
                "__enter__ retourne self généralement",
                "__exit__ appelé même si exception",
                "Gérez la fermeture dans __exit__"
            ]
        ),

        Exercise(
            id="248",
            title="Métaclasse - Validation automatique",
            description="Métaclasse `ValidatedMeta` qui ajoute automatiquement validation aux setters.",
            difficulty="très difficile",
            category="POO - Métaclasses",
            test_cases=[
                {"function": "Personne", "inputs": ["Alice", 25], "expected": "INIT"},
                {"function": "set_age", "inputs": [30], "expected": None},
                {"function": "set_age_invalid", "inputs": [-5], "expected": "VALIDATION_ERROR"},
            ],
            solution_template="""class ValidatedMeta(type):
            def __new__(cls, name, bases, attrs):
                # Ajouter validation aux attributs avec contraintes
                for attr_name, attr_value in attrs.items():
                    if isinstance(attr_value, dict) and 'validation' in attr_value:
                        # Créer property avec validation
                        pass
                
                return super().__new__(cls, name, bases, attrs)

        class Personne(metaclass=ValidatedMeta):
            nom = {'validation': lambda x: isinstance(x, str) and len(x) > 0}
            age = {'validation': lambda x: isinstance(x, int) and 0 <= x <= 150}
            
            def __init__(self, nom, age):
                self.nom = nom
                self.age = age""",
            hints=[
                "Métaclasse contrôle création de classe",
                "__new__ modifie la classe avant création",
                "Créez properties dynamiquement avec validation"
            ]
        ),

        Exercise(
            id="249",
            title="Multiple Inheritance - Mixins",
            description="Classes mixin pour ajouter fonctionnalités (Serializable, Cacheable) à d'autres classes.",
            difficulty="difficile",
            category="POO - Héritage multiple",
            test_cases=[
                {"function": "Utilisateur", "inputs": ["Alice", "alice@mail.com"], "expected": "INIT"},
                {"function": "to_json", "inputs": [], "expected": '{"nom": "Alice", "email": "alice@mail.com"}'},
                {"function": "from_cache", "inputs": ["user_1"], "expected": "CACHE_HIT"},
                {"function": "save_to_cache", "inputs": ["user_1"], "expected": None},
            ],
            solution_template="""import json

        class SerializableMixin:
            def to_json(self):
                # Convertit attributs publics en JSON
                pass
            
            @classmethod
            def from_json(cls, json_str):
                # Crée instance depuis JSON
                pass

        class CacheableMixin:
            _cache = {}
            
            def save_to_cache(self, key):
                # Sauvegarde dans le cache
                pass
            
            @classmethod
            def from_cache(cls, key):
                # Récupère du cache
                pass
            
            def clear_cache(self):
                # Vide le cache
                pass

        class Utilisateur(SerializableMixin, CacheableMixin):
            def __init__(self, nom, email):
                self.nom = nom
                self.email = email
            
            def __eq__(self, other):
                return self.nom == other.nom and self.email == other.email""",
            hints=[
                "Mixin = classe avec fonctionnalités spécialisées",
                "vars(self) donne attributs d'instance",
                "Ordre d'héritage important pour MRO"
            ]
        ),

        Exercise(
            id="250",
            title="Property dynamique - Attributs calculés",
            description="Classe avec propriétés calculées dynamiquement et cache des résultats.",
            difficulty="difficile",
            category="POO - Properties avancées",
            test_cases=[
                {"function": "Rectangle", "inputs": [4, 6], "expected": "INIT"},
                {"function": "aire", "inputs": [], "expected": 24},
                {"function": "perimetre", "inputs": [], "expected": 20},
                {"function": "diagonale", "inputs": [], "expected": 7.21},
                {"function": "set_largeur", "inputs": [5], "expected": None},
                {"function": "aire_after_change", "inputs": [], "expected": 30},
            ],
            solution_template="""import math

        class Rectangle:
            def __init__(self, largeur, hauteur):
                self._largeur = largeur
                self._hauteur = hauteur
                self._cache = {}
            
            @property
            def largeur(self):
                return self._largeur
            
            @largeur.setter
            def largeur(self, value):
                if value > 0:
                    self._largeur = value
                    self._cache.clear()  # Vider le cache
            
            @property
            def hauteur(self):
                return self._hauteur
            
            @hauteur.setter  
            def hauteur(self, value):
                if value > 0:
                    self._hauteur = value
                    self._cache.clear()
            
            @property
            def aire(self):
                # Calcul avec cache
                pass
            
            @property
            def perimetre(self):
                # Calcul avec cache
                pass
            
            @property
            def diagonale(self):
                # √(largeur² + hauteur²) avec cache
                pass""",
            hints=[
                "Utilisez _cache pour éviter recalculs",
                "Videz cache quand dimensions changent",
                "Property = getter automatique"
            ]
        ),

        Exercise(
            id="251",
            title="Classe générique - Container",
            description="Classe générique `Container[T]` avec type checking et opérations sur collections.",
            difficulty="difficile",
            category="POO - Génériques",
            test_cases=[
                {"function": "Container", "inputs": [int], "expected": "INIT"},
                {"function": "add", "inputs": [5], "expected": True},
                {"function": "add", "inputs": ["string"], "expected": False},  # Type mismatch
                {"function": "get_all", "inputs": [], "expected": [5]},
                {"function": "filter_by", "inputs": [lambda x: x > 3], "expected": [5]},
            ],
            solution_template="""from typing import TypeVar, Generic, List, Callable, Optional

        T = TypeVar('T')

        class Container(Generic[T]):
            def __init__(self, type_class: type):
                self._type_class = type_class
                self._items: List[T] = []
            
            def add(self, item: T) -> bool:
                # Ajouter si bon type
                pass
            
            def remove(self, item: T) -> bool:
                # Supprimer item
                pass
            
            def get_all(self) -> List[T]:
                # Retourner tous les items
                pass
            
            def filter_by(self, predicate: Callable[[T], bool]) -> List[T]:
                # Filtrer selon prédicat
                pass
            
            def find_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
                # Premier élément satisfaisant condition
                pass""",
            hints=[
                "isinstance() pour vérifier le type",
                "TypeVar définit type générique",
                "List comprehension pour filter_by"
            ]
        ),

        Exercise(
            id="252",
            title="Builder Pattern - Constructeur complexe",
            description="Pattern Builder pour construire objets complexes étape par étape.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "PizzaBuilder", "inputs": [], "expected": "INIT"},
                {"function": "set_taille", "inputs": ["large"], "expected": "BUILDER"},
                {"function": "add_ingredient", "inputs": ["fromage"], "expected": "BUILDER"},
                {"function": "add_ingredient", "inputs": ["jambon"], "expected": "BUILDER"},
                {"function": "build", "inputs": [], "expected": "Pizza(large, [fromage, jambon])"},
            ],
            solution_template="""class Pizza:
            def __init__(self, taille, ingredients, pate="normale"):
                self.taille = taille
                self.ingredients = ingredients
                self.pate = pate
            
            def __str__(self):
                return f"Pizza({self.taille}, {self.ingredients})"

        class PizzaBuilder:
            def __init__(self):
                self._taille = "moyenne"
                self._ingredients = []
                self._pate = "normale"
            
            def set_taille(self, taille):
                # Fluent interface
                pass
            
            def add_ingredient(self, ingredient):
                # Fluent interface
                pass
            
            def set_pate(self, pate):
                # Fluent interface  
                pass
            
            def build(self):
                # Construire l'objet final
                pass

        # Usage: PizzaBuilder().set_taille("large").add_ingredient("fromage").build()""",
            hints=[
                "return self pour chaînage fluide",
                "build() crée l'objet final",
                "Builder accumule les paramètres"
            ]
        ),

        Exercise(
            id="253",
            title="Proxy Pattern - Cache intelligent",
            description="Proxy qui intercepte appels et ajoute cache, logging, validation.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "ProxyCalculateur", "inputs": [], "expected": "INIT"},
                {"function": "calculer_carre", "inputs": [5], "expected": 25},
                {"function": "calculer_carre", "inputs": [5], "expected": 25},  # From cache
                {"function": "get_cache_hits", "inputs": [], "expected": 1},
                {"function": "get_logs", "inputs": [], "expected": ["calculer_carre(5) = 25"]},
            ],
            solution_template="""import time

        class Calculateur:
            def calculer_carre(self, x):
                # Simulation calcul coûteux
                time.sleep(0.1)
                return x * x
            
            def calculer_cube(self, x):
                time.sleep(0.1)
                return x * x * x

        class ProxyCalculateur:
            def __init__(self):
                self._calculateur = Calculateur()
                self._cache = {}
                self._logs = []
                self._cache_hits = 0
            
            def calculer_carre(self, x):
                # Proxy avec cache et logging
                pass
            
            def calculer_cube(self, x):
                # Proxy avec cache et logging
                pass
            
            def get_cache_hits(self):
                return self._cache_hits
            
            def get_logs(self):
                return self._logs""",
            hints=[
                "Vérifiez cache avant d'appeler méthode réelle",
                "Loggez tous les appels avec paramètres",
                "Comptez les hits de cache"
            ]
        ),

        Exercise(
            id="254",
            title="Command Pattern - Système d'annulation",
            description="Pattern Command avec undo/redo pour éditeur de texte simple.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "EditeurTexte", "inputs": [], "expected": "INIT"},
                {"function": "test_command_pattern", "inputs": [], "expected": {"texte_initial": "Hello", "texte_apres_suppression": "Hel", "texte_apres_undo": "Hello"}},
            ],
            solution_template="""from abc import ABC, abstractmethod

        class Commande(ABC):
            @abstractmethod
            def executer(self, editeur):
                pass
            
            @abstractmethod
            def annuler(self, editeur):
                pass

        class InsererCommande(Commande):
            def __init__(self, texte):
                self.texte = texte
                self.position = None
            
            def executer(self, editeur):
                # Insérer texte à la fin
                self.position = len(editeur._contenu)
                editeur._contenu += self.texte
            
            def annuler(self, editeur):
                # Supprimer le texte inséré
                if self.position is not None:
                    editeur._contenu = editeur._contenu[:self.position]

        class SupprimerCommande(Commande):
            def __init__(self, nb_chars):
                self.nb_chars = nb_chars
                self.texte_supprime = ""
                self.position = None
            
            def executer(self, editeur):
                # Supprimer et sauvegarder
                self.position = len(editeur._contenu)
                if len(editeur._contenu) >= self.nb_chars:
                    self.texte_supprime = editeur._contenu[-self.nb_chars:]
                    editeur._contenu = editeur._contenu[:-self.nb_chars]
            
            def annuler(self, editeur):
                # Remettre le texte supprimé
                if self.texte_supprime:
                    editeur._contenu += self.texte_supprime

        class EditeurTexte:
            def __init__(self):
                self._contenu = ""
                self._historique = []
                self._position_historique = -1
            
            def executer(self, commande):
                # Exécuter et ajouter à l'historique
                commande.executer(self)
                # Supprimer l'historique redo si on exécute une nouvelle commande
                self._historique = self._historique[:self._position_historique + 1]
                self._historique.append(commande)
                self._position_historique += 1
            
            def undo(self):
                # Annuler dernière commande
                if self._position_historique >= 0:
                    commande = self._historique[self._position_historique]
                    commande.annuler(self)
                    self._position_historique -= 1
            
            def redo(self):
                # Refaire commande annulée
                if self._position_historique < len(self._historique) - 1:
                    self._position_historique += 1
                    commande = self._historique[self._position_historique]
                    commande.executer(self)
            
            @property
            def texte(self):
                return self._contenu

        def test_command_pattern():
            # Fonction de test qui crée les objets
            editeur = EditeurTexte()
            
            # Insérer "Hello"
            cmd_insert = InsererCommande("Hello")
            editeur.executer(cmd_insert)
            texte_initial = editeur.texte
            
            # Supprimer 2 caractères
            cmd_suppr = SupprimerCommande(2)
            editeur.executer(cmd_suppr)
            texte_apres_suppression = editeur.texte
            
            # Annuler la suppression
            editeur.undo()
            texte_apres_undo = editeur.texte
            
            return {
                "texte_initial": texte_initial,
                "texte_apres_suppression": texte_apres_suppression,
                "texte_apres_undo": texte_apres_undo
            }""",
            hints=[
                "Historique des commandes pour undo/redo",
                "Commande sauvegarde état pour annulation",
                "Position dans historique pour navigation"
            ]
        ),

        Exercise(
            id="255",
            title="State Pattern - Machine à états",
            description="Pattern State pour modéliser une machine distributrice avec différents états.",
            difficulty="difficile",
            category="POO - Design Patterns",
            test_cases=[
                {"function": "MachineDistributrice", "inputs": [2], "expected": "INIT"},
                {"function": "inserer_piece", "inputs": [], "expected": "Pièce insérée"},
                {"function": "selectionner_produit", "inputs": ["Coca"], "expected": "Produit sélectionné: Coca"},
                {"function": "distribuer", "inputs": [], "expected": "Voici votre Coca"},
                {"function": "etat_actuel", "inputs": [], "expected": "AttenteMonnaie"},
            ],
            solution_template="""from abc import ABC, abstractmethod

        class EtatMachine(ABC):
            @abstractmethod
            def inserer_piece(self, machine):
                pass
            
            @abstractmethod
            def selectionner_produit(self, machine, produit):
                pass
            
            @abstractmethod
            def distribuer(self, machine):
                pass

        class AttenteMonnaie(EtatMachine):
            def inserer_piece(self, machine):
                machine.set_etat(machine.attente_selection)
                return "Pièce insérée"
            
            def selectionner_produit(self, machine, produit):
                return "Insérez une pièce d'abord"
            
            def distribuer(self, machine):
                return "Sélectionnez un produit d'abord"

        class AttenteSelection(EtatMachine):
            def inserer_piece(self, machine):
                return "Pièce déjà insérée"
            
            def selectionner_produit(self, machine, produit):
                machine.produit_selectionne = produit
                machine.set_etat(machine.pret_distribution)
                return f"Produit sélectionné: {produit}"
            
            def distribuer(self, machine):
                return "Sélectionnez un produit d'abord"

        class PretDistribution(EtatMachine):
            def inserer_piece(self, machine):
                return "Distribution en cours"
            
            def selectionner_produit(self, machine, produit):
                return "Distribution en cours"
            
            def distribuer(self, machine):
                produit = machine.produit_selectionne
                machine.set_etat(machine.attente_monnaie)
                machine.stock -= 1
                return f"Voici votre {produit}"

        class MachineDistributrice:
            def __init__(self, stock_initial):
                self.stock = stock_initial
                self.produit_selectionne = None
                
                # États
                self.attente_monnaie = AttenteMonnaie()
                self.attente_selection = AttenteSelection()
                self.pret_distribution = PretDistribution()
                
                # État initial
                self._etat = self.attente_monnaie
            
            def set_etat(self, etat):
                self._etat = etat
            
            def inserer_piece(self):
                return self._etat.inserer_piece(self)
            
            def selectionner_produit(self, produit):
                return self._etat.selectionner_produit(self, produit)
            
            def distribuer(self):
                return self._etat.distribuer(self)
            
            @property
            def etat_actuel(self):
                return self._etat.__class__.__name__""",
            hints=[
                "État = classe avec comportement spécifique",
                "Machine change d'état selon actions",
                "Context (Machine) délègue aux états"
            ]
        ),
        
        # === RECHERCHE OPÉRATIONNELLE (256-270) ===

        Exercise(
            id="256",
            title="Programmation linéaire - Méthode graphique",
            description="Fonction `optimiser_lineaire_2d(objectif, contraintes)` qui résout un PL à 2 variables graphiquement.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "optimiser_lineaire_2d", "inputs": [{"coeffs": [3, 2], "type": "max"}, [{"coeffs": [1, 1], "op": "<=", "rhs": 4}, {"coeffs": [2, 1], "op": "<=", "rhs": 6}]], "expected": {"x": 2, "y": 2, "valeur": 10}},
                {"function": "optimiser_lineaire_2d", "inputs": [{"coeffs": [5, 3], "type": "min"}, [{"coeffs": [1, 2], "op": ">=", "rhs": 4}, {"coeffs": [3, 1], "op": ">=", "rhs": 6}]], "expected": {"x": 2, "y": 0, "valeur": 10}},
            ],
            hints=[
                "Trouvez les points d'intersection des contraintes",
                "Évaluez la fonction objectif en chaque point",
                "Solution optimale = sommet du polyèdre réalisable"
            ]
        ),

        Exercise(
            id="257",
            title="Algorithme du simplexe basique",
            description="Fonction `simplexe(c, A, b)` qui implémente l'algorithme du simplexe pour PL standard.",
            difficulty="très difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "simplexe", "inputs": [[-3, -2], [[1, 1], [2, 1]], [4, 6]], "expected": {"solution": [2, 2], "valeur": -10, "iterations": 2}},
                {"function": "simplexe", "inputs": [[-1, -1], [[1, 0], [0, 1], [1, 1]], [2, 3, 4]], "expected": {"solution": [1, 3], "valeur": -4, "iterations": 1}},
            ],
            hints=[
                "Tableau du simplexe avec variables d'écart",
                "Test de ratio pour variable sortante",
                "Pivotage de Gauss-Jordan"
            ]
        ),

        Exercise(
            id="258",
            title="Problème de transport",
            description="Fonction `resoudre_transport(offres, demandes, couts)` qui minimise les coûts de transport.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "resoudre_transport", "inputs": [[20, 30], [25, 25], [[4, 6], [8, 4]]], "expected": {"allocation": [[20, 0], [5, 25]], "cout_total": 180}},
                {"function": "resoudre_transport", "inputs": [[15, 25, 10], [20, 15, 15], [[2, 3, 4], [5, 1, 2], [3, 4, 1]]], "expected": {"allocation": "OPTIMAL_MATRIX", "cout_total": 85}},
            ],
            hints=[
                "Méthode du coin nord-ouest pour solution initiale",
                "Méthode MODI pour test d'optimalité",
                "Méthode du stepping stone pour amélioration"
            ]
        ),

        Exercise(
            id="259",
            title="Problème d'affectation (Algorithme hongrois)",
            description="Fonction `affectation_hongroise(matrice_couts)` qui trouve l'affectation optimale.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "affectation_hongroise", "inputs": [[[4, 2, 8], [4, 3, 7], [1, 2, 5]]], "expected": {"affectation": [(0, 1), (1, 2), (2, 0)], "cout_total": 9}},
                {"function": "affectation_hongroise", "inputs": [[[3, 4, 6, 8], [6, 8, 5, 4], [5, 7, 4, 3], [4, 5, 8, 6]]], "expected": {"affectation": [(0, 0), (1, 3), (2, 2), (3, 1)], "cout_total": 16}},
            ],
            hints=[
                "Soustraction ligne puis colonne",
                "Couverture minimale avec lignes/colonnes",
                "Ajustement jusqu'à solution optimale"
            ]
        ),

        Exercise(
            id="260",
            title="Plus court chemin - Algorithme de Floyd-Warshall",
            description="Fonction `floyd_warshall(graphe)` qui trouve tous les plus courts chemins.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "floyd_warshall", "inputs": [[[0, 3, float('inf'), 7], [8, 0, 2, float('inf')], [5, float('inf'), 0, 1], [2, float('inf'), float('inf'), 0]]], "expected": [[0, 3, 5, 6], [7, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]},
            ],
            hints=[
                "Programmation dynamique en 3 boucles",
                "dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])",
                "Complexité O(n³)"
            ]
        ),

        Exercise(
            id="261",
            title="Algorithme de branch and bound",
            description="Fonction `branch_and_bound(objectif, contraintes, variables_entieres)` pour PL en nombres entiers.",
            difficulty="très difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "branch_and_bound", "inputs": [{"coeffs": [3, 2], "type": "max"}, [{"coeffs": [1, 1], "op": "<=", "rhs": 4}, {"coeffs": [2, 1], "op": "<=", "rhs": 6}], [True, True]], "expected": {"solution": [2, 2], "valeur": 10, "nodes_explored": 1}},
            ],
            hints=[
                "Résolution PL continue pour borne supérieure",
                "Branchement sur variables fractionnaires",
                "Élagage si borne < meilleure solution"
            ]
        ),

        Exercise(
            id="262",
            title="Problème du voyageur de commerce (TSP)",
            description="Fonction `tsp_dynamique(distances)` qui résout TSP par programmation dynamique.",
            difficulty="très difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "tsp_dynamique", "inputs": [[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]], "expected": {"chemin": [0, 1, 3, 2, 0], "cout": 35}},
            ],
            hints=[
                "État = (ville_actuelle, ensemble_villes_visitées)",
                "Masquage de bits pour représenter ensembles",
                "Complexité O(n² * 2ⁿ)"
            ]
        ),

        Exercise(
            id="263",
            title="Problème de flot maximal - Ford-Fulkerson",
            description="Fonction `flot_maximal_ford_fulkerson(graphe, source, puits)` avec DFS.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "flot_maximal_ford_fulkerson", "inputs": [{("s", "a"): 10, ("s", "b"): 10, ("a", "t"): 10, ("b", "t"): 10, ("a", "b"): 1}, "s", "t"], "expected": {"flot_max": 20, "chemins_augmentants": [["s", "a", "t"], ["s", "b", "t"]]}},
            ],
            hints=[
                "Cherchez chemins augmentants avec DFS",
                "Capacité résiduelle = capacité - flot",
                "Arrêt quand plus de chemin augmentant"
            ]
        ),

        Exercise(
            id="264",
            title="Théorie des jeux - Équilibre de Nash",
            description="Fonction `equilibre_nash(matrice_joueur1, matrice_joueur2)` pour jeu 2x2.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "equilibre_nash", "inputs": [[[3, 0], [5, 1]], [[3, 5], [0, 1]]], "expected": {"equilibres": [(1, 1)], "type": "pur"}},
                {"function": "equilibre_nash", "inputs": [[[1, 0], [0, 1]], [[0, 1], [1, 0]]], "expected": {"equilibres": [], "mixte": {"joueur1": [0.5, 0.5], "joueur2": [0.5, 0.5]}}},
            ],
            hints=[
                "Équilibre pur : aucun joueur ne veut dévier",
                "Équilibre mixte : stratégies probabilistes",
                "Résolution par système d'équations"
            ]
        ),

        Exercise(
            id="265",
            title="Programmation dynamique - Problème du sac à dos",
            description="Fonction `sac_a_dos_dp(capacite, poids, valeurs)` avec reconstruction de solution.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "sac_a_dos_dp", "inputs": [50, [10, 20, 30], [60, 100, 120]], "expected": {"valeur_max": 220, "objets_pris": [1, 2], "poids_total": 50}},
                {"function": "sac_a_dos_dp", "inputs": [15, [12, 2, 1, 1, 4], [4, 2, 1, 2, 10]], "expected": {"valeur_max": 15, "objets_pris": [1, 2, 3, 4], "poids_total": 8}},
            ],
            hints=[
                "DP[i][w] = valeur max avec i objets et capacité w",
                "Récurrence : max(prendre, ne pas prendre)",
                "Backtrack pour trouver les objets"
            ]
        ),

        Exercise(
            id="266",
            title="Algorithme de colonies de fourmis (ACO)",
            description="Fonction `aco_tsp(distances, nb_fourmis, iterations)` pour résoudre TSP.",
            difficulty="très difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "aco_tsp", "inputs": [[[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]], 10, 100], "expected": {"meilleur_chemin": [0, 1, 3, 2, 0], "cout": 21, "convergence": 45}},
            ],
            hints=[
                "Phéromones τ et visibilité η = 1/distance",
                "Probabilité ∝ τᵅ * ηᵝ",
                "Évaporation et renforcement des phéromones"
            ]
        ),

        Exercise(
            id="267",
            title="Algorithme génétique pour optimisation",
            description="Fonction `ag_optimisation(fonction, domaine, pop_size, generations)` pour optimiser une fonction.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "ag_optimisation", "inputs": [lambda x: -(x[0]**2 + x[1]**2 - 10), [(-5, 5), (-5, 5)], 50, 100], "expected": {"meilleure_solution": [0.0, 0.0], "meilleure_fitness": 10.0, "generation_convergence": 67}},
            ],
            hints=[
                "Sélection par tournoi",
                "Croisement arithmétique pour variables réelles",
                "Mutation gaussienne"
            ]
        ),

        Exercise(
            id="268",
            title="Méthode de Monte Carlo",
            description="Fonction `monte_carlo_integration(fonction, bornes, nb_echantillons)` pour intégration numérique.",
            difficulty="moyen",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "monte_carlo_integration", "inputs": [lambda x: x**2, (0, 1), 100000], "expected": {"integrale": 0.333, "erreur_std": 0.001}},
                {"function": "monte_carlo_integration", "inputs": [lambda x: 4/(1+x**2), (0, 1), 100000], "expected": {"integrale": 3.14159, "erreur_std": 0.01}},
            ],
            hints=[
                "Échantillonnage uniforme dans le domaine",
                "Moyenne * volume du domaine",
                "Erreur ∝ 1/√n"
            ]
        ),

        Exercise(
            id="269",
            title="Simulation de Monte Carlo - Files d'attente",
            description="Fonction `simuler_file_attente(taux_arrivee, taux_service, duree_simulation)` type M/M/1.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "simuler_file_attente", "inputs": [2.0, 3.0, 1000], "expected": {"temps_attente_moyen": 0.5, "taille_queue_moyenne": 1.33, "taux_occupation": 0.67}},
                {"function": "simuler_file_attente", "inputs": [1.0, 2.0, 2000], "expected": {"temps_attente_moyen": 0.5, "taille_queue_moyenne": 0.5, "taux_occupation": 0.5}},
            ],
            hints=[
                "Processus de Poisson pour arrivées",
                "Loi exponentielle pour temps de service",
                "Statistiques sur fenêtre glissante"
            ]
        ),

        Exercise(
            id="270",
            title="Recuit simulé (Simulated Annealing)",
            description="Fonction `recuit_simule(fonction_cout, solution_initiale, temperature, refroidissement)` pour optimisation.",
            difficulty="difficile",
            category="Recherche opérationnelle",
            test_cases=[
                {"function": "recuit_simule", "inputs": [lambda x: sum(xi**2 for xi in x), [5, 5], 100, 0.95], "expected": {"solution": [0.0, 0.0], "cout": 0.0, "iterations": 523}},
                {"function": "recuit_simule", "inputs": [lambda x: abs(x[0]-2)**2 + abs(x[1]-3)**2, [0, 0], 50, 0.9], "expected": {"solution": [2.0, 3.0], "cout": 0.0, "iterations": 234}},
            ],
            hints=[
                "Acceptation : si meilleur OU si exp(-Δ/T) > rand",
                "Diminution géométrique de température",
                "Voisinage = petite perturbation aléatoire"
            ]
        ),
        
    ]),
    
    
    return exercises