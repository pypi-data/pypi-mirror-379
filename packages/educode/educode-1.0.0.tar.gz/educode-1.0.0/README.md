# README.md
# 🎓 EduCode - Apprendre Python par la pratique

EduCode est un système interactif de 100 exercices progressifs pour apprendre Python, avec correction automatique et suivi de progression.

## ✨ Fonctionnalités

- **100 exercices progressifs** répartis en 3 niveaux (facile, moyen, difficile)
- **Correction automatique** avec tests unitaires intégrés
- **Suivi de progression** personnel sauvegardé localement
- **Exercices par catégorie** et par difficulté
- **Indices et templates** pour vous aider
- **Mode hors-ligne** - fonctionne sans internet

## 🚀 Installation

```bash
pip install educode
```

## 💻 Utilisation

### Mode interactif (recommandé)
```bash
python -m educode
```

### Commandes disponibles
```bash
python -m educode stats    # Voir vos statistiques
python -m educode help     # Aide
python -m educode version  # Version
```

## 📚 Catégories d'exercices

### 🟢 Niveau Facile (40 exercices)
- **Fonctions basiques** : carré, maximum, calculatrice...
- **Chaînes de caractères** : palindromes, comptage, formatage...
- **Listes basiques** : somme, min/max, recherche...
- **Boucles et conditions** : factorielle, fibonacci, tables...

### 🟡 Niveau Moyen (40 exercices)  
- **Listes et algorithmes** : tri, recherche, permutations...
- **Dictionnaires** : fréquences, fusion, filtrage...
- **Chaînes avancées** : anagrammes, compression, regex...

### 🔴 Niveau Difficile (20 exercices)
- **Algorithmes complexes** : QuickSort, Dijkstra, N-Reines...
- **Structures de données** : arbres, graphes, tables de hachage...

## 🎯 Exemple d'utilisation

```
🎓 Bienvenue dans EduCode !

🎯 Que souhaitez-vous faire ?
1. Exercice aléatoire
2. Exercice par difficulté  
3. Exercice par catégorie
4. Voir mes statistiques
5. Continuer où j'en étais
6. Quitter

👉 Votre choix (1-6): 1

🎓 Exercice: Fonction carré
📚 Catégorie: Fonctions basiques  
🔥 Difficulté: FACILE
==================================================
Écrivez une fonction `carre(n)` qui retourne le carré d'un nombre.

📝 Écrivez votre solution:
>>> def carre(n):
...     return n * n
... 

🧪 Exécution de 4 tests...
  ✅ Test 1: carre(2) = 4
  ✅ Test 2: carre(0) = 0  
  ✅ Test 3: carre(-3) = 9
  ✅ Test 4: carre(10) = 100

📊 Résultat: 4/4 tests réussis
🎉 Félicitations ! Exercice réussi !
```

## 📊 Suivi de progression

EduCode sauvegarde automatiquement votre progression dans `~/.educode_progress.json` :

- ✅ Exercices réussis
- ❌ Exercices échoués  
- 📈 Statistiques détaillées
- 🎯 Taux de réussite

## 🛠 Développement

### Structure du projet
```
educode/
├── __init__.py          # Point d'entrée du module
├── __main__.py          # Exécution python -m educode  
├── core.py              # Logique principale
└── exercises.py         # Base de données des 100 exercices
```

### Contribuer

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Pushez (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 📝 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Support

- 🐛 **Bugs**: [GitHub Issues](https://github.com/educode-team/educode/issues)
- 📖 **Documentation**: [ReadTheDocs](https://educode.readthedocs.io/)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/educode-team/educode/discussions)

## 🏆 Pourquoi EduCode ?

- ✅ **Pratique immédiate** - Pas de théorie, que de la pratique
- ✅ **Progression guidée** - Du plus simple au plus complexe
- ✅ **Correction instantanée** - Sachez immédiatement si c'est bon
- ✅ **Hors ligne** - Apprenez n'importe où, sans connexion
- ✅ **Suivi personnel** - Voyez votre évolution
- ✅ **Open Source** - Gratuit et améliorable par tous

Commencez dès maintenant :
```bash
pip install educode && python -m educode