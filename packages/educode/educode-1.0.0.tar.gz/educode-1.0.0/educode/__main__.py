# educode/__main__.py
"""Point d'entrée pour l'exécution en module (python -m educode)"""

import sys
from .core import EduCode

def main():
    """Fonction principale"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        educode = EduCode()
        
        if command == "stats":
            educode.display_stats()
        elif command == "version":
            from . import __version__
            print(f"EduCode version {__version__}")
        elif command == "help":
            print_help()
        else:
            print(f"❌ Commande inconnue: {command}")
            print_help()
    else:
        # Mode interactif par défaut
        educode = EduCode()
        educode.interactive_mode()

def print_help():
    """Affiche l'aide"""
    print("""
🎓 EduCode - Système d'exercices interactifs pour apprendre Python

Usage:
    python -m educode          # Mode interactif
    python -m educode stats    # Afficher les statistiques
    python -m educode help     # Afficher cette aide
    python -m educode version  # Afficher la version

Fonctionnalités:
    • 100 exercices progressifs (facile, moyen, difficile)
    • Correction automatique avec tests unitaires
    • Suivi de progression personnalisé
    • Exercices par catégorie et difficulté
    • Indices et templates de solution

Catégories disponibles:
    • Fonctions basiques
    • Chaînes de caractères  
    • Listes basiques
    • Boucles et conditions
    • Listes et algorithmes
    • Dictionnaires et structures
    • Chaînes avancées
    • Algorithmes complexes
    • Structures de données avancées

Pour commencer:
    python -m educode

Bon apprentissage ! 🚀
    """)

if __name__ == "__main__":
    main()