# 🎓 EduCode - Apprendre Python par la pratique

EduCode est un système interactif de +200 exercices progressifs pour apprendre Python, avec correction automatique et suivi de progression.

## ✨ Fonctionnalités

- **200 exercices progressifs** répartis en 3 niveaux (facile, moyen, difficile)
- **Correction automatique** avec tests unitaires intégrés
- **Interface colorée** avec codes ANSI pour une meilleure expérience utilisateur
- **Suivi de progression** personnel sauvegardé localement
- **Exercices par catégorie** et par difficulté
- **Système d'indices** et templates pour vous aider
- **Installation automatique de modules** Python externes
- **Mode hors-ligne** - fonctionne sans internet une fois installé

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

## 🎯 Menu principal

Lorsque vous lancez EduCode, vous accédez à un menu interactif coloré :

```
🎯 Menu Principal
─────────────────────────────────
1. 🎲 Exercice aléatoire
   Choisir un exercice au hasard

2. 📈 Exercice par difficulté  
   Facile, Moyen ou Difficile

3. 📚 Exercice par catégorie
   Fonctions, Listes, Algorithmes...

4. 📊 Mes statistiques
   Voir votre progression

5. 🔄 Reprendre un exercice
   Continuer où vous en étiez

6. 📦 Import module
   Télécharger un module à utiliser

7. 👋 Quitter
   Fermer EduCode
```

## 📚 Catégories d'exercices

### 🟢 Niveau Facile (50 exercices)
- **Fonctions basiques** : carré, maximum, calculatrice simple
- **Chaînes de caractères** : palindromes, comptage de caractères, formatage
- **Listes basiques** : somme, min/max, recherche d'éléments
- **Boucles et conditions** : factorielle, fibonacci, tables de multiplication

### 🟡 Niveau Moyen (50 exercices)  
- **Listes et algorithmes** : tri, recherche binaire, permutations
- **Dictionnaires** : calcul de fréquences, fusion, filtrage
- **Chaînes avancées** : anagrammes, compression, expressions régulières
- **Structures de données** : piles, files, manipulation avancée

### 🔴 Niveau Difficile (100 exercices)
- **Algorithmes complexes** : QuickSort, MergeSort, algorithme de Dijkstra
- **Structures de données avancées** : arbres binaires, graphes
- **Problèmes classiques** : N-Reines, sac à dos, plus court chemin

## 🎯 Exemple d'utilisation

```
═══════════════════════════════════════════════════
🎓 Fonction carré
📚 Catégorie: Fonctions basiques
🔥 Difficulté: FACILE
─────────────────────────────────────────────────────
📝 Description:
Écrivez une fonction `carre(n)` qui retourne le carré d'un nombre.

💡 Template de solution:
def carre(n):
    # Votre code ici
    pass

✍️  Instructions:
• Écrivez votre solution ligne par ligne
• Appuyez sur Entrée avec une ligne vide pour tester
• Tapez hints pour des indices
• Tapez quit pour quitter
─────────────────────────────────────────────────────
 1>>> def carre(n):
 2...     return n * n
 3... 

🧪 Tests en cours...
─────────────────────────────────────────────────────
  Test 1: ✅ RÉUSSI
     carre(2) = 4
  Test 2: ✅ RÉUSSI
     carre(0) = 0
  Test 3: ✅ RÉUSSI
     carre(-3) = 9
  Test 4: ✅ RÉUSSI
     carre(10) = 100

═══════════════════════════════════════════════════
🎉 FÉLICITATIONS ! 🎉
Score parfait: 4/4 tests réussis
═══════════════════════════════════════════════════
```

## 📊 Suivi de progression

EduCode sauvegarde automatiquement votre progression dans `~/.educode_progress.json` :

### Statistiques affichées
- 📚 **Exercices total** : nombre total d'exercices disponibles
- ✅ **Exercices réussis** : nombre d'exercices complétés avec succès
- 📊 **Taux de complétion** : pourcentage d'exercices terminés
- 🎯 **Taux de réussite** : ratio succès/tentatives
- 🔄 **Tentatives total** : nombre total de tentatives

### Barre de progression visuelle
```
📈 Progression:
[██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 25.0%
```

### Historique des succès
```
🏆 Derniers succès:
  ✨ Fonction carré (FACILE)
  ✨ Maximum de trois nombres (FACILE)
  ✨ Palindrome (MOYEN)
```

## 🔧 Fonctionnalités avancées

### Gestion automatique des modules
EduCode peut installer automatiquement les modules Python nécessaires :
- Détection automatique des `import` dans votre code
- Installation via `pip` si le module n'est pas trouvé
- Validation post-installation pour s'assurer que le module fonctionne

### Commandes spéciales durant les exercices
- `hints` : Affiche les indices de l'exercice
- `test` : Effectue un test rapide de syntaxe
- `modules` : Liste les modules Python populaires
- `quit` : Quitte l'exercice actuel

### Interface colorée
- **Codes ANSI** pour une interface terminal attrayante
- **Détection automatique** du support des couleurs
- **Fallback** vers du texte simple si les couleurs ne sont pas supportées

## 🛠 Structure technique

### Architecture du projet
```
educode/
├── __init__.py          # Point d'entrée du module
├── __main__.py          # Exécution python -m educode  
├── core.py              # Logique principale et interface
└── exercises.py         # Base de données des 100 exercices
```

### Classes principales

#### `Colors`
Gère l'affichage coloré dans le terminal :
- Support des codes ANSI
- Détection automatique de la compatibilité terminal
- Méthodes utilitaires pour coloriser le texte

#### `Exercise`  
Représente un exercice individuel :
- Métadonnées (titre, description, difficulté, catégorie)
- Cas de test avec entrées/sorties attendues
- Template de solution optionnel
- Système d'indices

#### `EduCode`
Classe principale du système :
- Gestion des exercices et de la progression
- Interface utilisateur interactive
- Système de test automatique
- Sauvegarde/chargement de la progression

### Système de test
- **Exécution isolée** : chaque solution est testée dans un environnement temporaire
- **Gestion des erreurs** : capture et affichage des erreurs de syntaxe et d'exécution
- **Comparaison intelligente** : support des types complexes (pandas, numpy)
- **Tolérance numérique** : gestion des erreurs de précision flottante

## 🧪 Développement et contribution

### Installation en mode développement
```bash
git clone https://github.com/educode-team/educode.git
cd educode
pip install -e .
```

### Ajouter de nouveaux exercices
Les exercices sont définis dans `exercises.py` avec la structure :
```python
Exercise(
    id="unique_id",
    title="Titre de l'exercice",
    description="Description détaillée",
    difficulty="facile|moyen|difficile",
    category="Catégorie",
    test_cases=[
        {
            "function": "nom_fonction",
            "inputs": [param1, param2],
            "expected": resultat_attendu
        }
    ],
    solution_template="def fonction():\n    pass",
    hints=["Indice 1", "Indice 2"]
)
```

### Standards de contribution
1. **Fork** le projet sur GitHub
2. **Créez** une branche pour votre fonctionnalité
3. **Testez** vos modifications avec plusieurs exercices
4. **Documentez** les nouvelles fonctionnalités
5. **Soumettez** une Pull Request avec description détaillée

## 📝 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Support et communauté

- 🐛 **Rapporter des bugs** : [GitHub Issues](https://github.com/educode-team/educode/issues)
- 📖 **Documentation complète** : [ReadTheDocs](https://educode.readthedocs.io/)
- 💬 **Discussions et aide** : [GitHub Discussions](https://github.com/educode-team/educode/discussions)
- 🌟 **Suggérer des améliorations** : [Feature Requests](https://github.com/educode-team/educode/issues/new?template=feature_request.md)

## 🏆 Pourquoi choisir EduCode ?

### ✅ Avantages pédagogiques
- **Apprentissage actif** : pas de théorie passive, que de la pratique
- **Feedback immédiat** : correction instantanée de votre code
- **Progression mesurable** : statistiques détaillées de votre évolution
- **Difficulté progressive** : du niveau débutant à expert

### ✅ Avantages techniques  
- **Zero configuration** : fonctionne immédiatement après installation
- **Mode hors-ligne** : apprenez sans connexion internet
- **Multi-plateforme** : Windows, macOS, Linux
- **Installation automatique** : gère les dépendances pour vous

### ✅ Avantages pratiques
- **Interface intuitive** : navigation simple et claire
- **Sauvegarde automatique** : reprenez où vous vous êtes arrêtés
- **Exercices variés** : couvre tous les aspects fondamentaux de Python
- **Code source ouvert** : transparent et améliorable par la communauté

## 🚀 Démarrage rapide

Prêt à commencer votre apprentissage Python ?

```bash
# Installation
pip install educode

# Lancement
python -m educode

# C'est parti ! 🎉
```

---

**EduCode** - Parce que la meilleure façon d'apprendre Python, c'est de coder ! 🐍