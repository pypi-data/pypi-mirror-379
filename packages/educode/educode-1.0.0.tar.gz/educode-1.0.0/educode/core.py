# educode/core.py
import json
import os
import sys
import random
import importlib.util
import tempfile
import traceback
from typing import Dict, List, Any, Callable, Optional
from datetime import datetime

class Exercise:
    """Classe représentant un exercice de programmation"""
    
    def __init__(self, id: str, title: str, description: str, difficulty: str, 
                 category: str, test_cases: List[Dict], solution_template: str = "",
                 hints: List[str] = None):
        self.id = id
        self.title = title
        self.description = description
        self.difficulty = difficulty  # "facile", "moyen", "difficile"
        self.category = category
        self.test_cases = test_cases
        self.solution_template = solution_template
        self.hints = hints or []
    
    def __repr__(self):
        return f"Exercise({self.id}: {self.title})"

class EduCode:
    """Classe principale du système EduCode"""
    
    def __init__(self):
        self.exercises = {}
        self.progress_file = os.path.expanduser("~/.educode_progress.json")
        self.progress = self._load_progress()
        self._load_exercises()
    
    def _load_exercises(self):
        """Charge tous les exercices disponibles"""
        from .exercises import get_all_exercises
        exercises_list = get_all_exercises()
        for ex in exercises_list:
            self.exercises[ex.id] = ex
    
    def _load_progress(self) -> Dict:
        """Charge la progression depuis le fichier"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {
            "completed": [],
            "failed": [],
            "total_attempts": 0,
            "total_success": 0,
            "start_date": datetime.now().isoformat()
        }
    
    def _save_progress(self):
        """Sauvegarde la progression"""
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
    
    def get_stats(self):
        """Retourne les statistiques de progression"""
        total_exercises = len(self.exercises)
        completed = len(self.progress["completed"])
        failed = len(self.progress["failed"])
        success_rate = (self.progress["total_success"] / max(1, self.progress["total_attempts"])) * 100
        
        return {
            "total_exercises": total_exercises,
            "completed": completed,
            "failed": failed,
            "completion_rate": (completed / total_exercises) * 100,
            "success_rate": success_rate,
            "total_attempts": self.progress["total_attempts"]
        }
    
    def display_stats(self):
        """Affiche les statistiques"""
        stats = self.get_stats()
        print("\n📊 Statistiques EduCode")
        print("=" * 30)
        print(f"Exercices total: {stats['total_exercises']}")
        print(f"Exercices réussis: {stats['completed']}")
        print(f"Taux de complétion: {stats['completion_rate']:.1f}%")
        print(f"Taux de réussite: {stats['success_rate']:.1f}%")
        print(f"Tentatives total: {stats['total_attempts']}")
        
        if self.progress["completed"]:
            print(f"\n🎯 Derniers exercices réussis:")
            for ex_id in self.progress["completed"][-5:]:
                if ex_id in self.exercises:
                    ex = self.exercises[ex_id]
                    print(f"  ✅ {ex.title} ({ex.difficulty})")
    
    def get_random_exercise(self, difficulty: Optional[str] = None, 
                          exclude_completed: bool = True) -> Optional[Exercise]:
        """Retourne un exercice aléatoire"""
        available = []
        for ex in self.exercises.values():
            if exclude_completed and ex.id in self.progress["completed"]:
                continue
            if difficulty and ex.difficulty != difficulty:
                continue
            available.append(ex)
        
        if not available:
            return None
        return random.choice(available)
    
    def run_exercise(self, exercise: Exercise) -> bool:
        """Lance un exercice interactif"""
        print(f"\n🎓 Exercice: {exercise.title}")
        print(f"📚 Catégorie: {exercise.category}")
        print(f"🔥 Difficulté: {exercise.difficulty.upper()}")
        print("=" * 50)
        print(exercise.description)
        
        if exercise.solution_template:
            print(f"\n💡 Template de solution:")
            print(exercise.solution_template)
        
        print("\n📝 Écrivez votre solution (tapez 'hints' pour des indices, 'quit' pour quitter):")
        
        user_code = []
        while True:
            try:
                line = input(">>> " if not user_code else "... ")
                
                if line.strip() == "quit":
                    return False
                elif line.strip() == "hints":
                    self._show_hints(exercise)
                    continue
                elif line.strip() == "" and user_code:
                    # Code terminé, on teste
                    code = "\n".join(user_code)
                    success = self._test_solution(exercise, code)
                    self._update_progress(exercise.id, success)
                    return success
                else:
                    user_code.append(line)
                    
            except KeyboardInterrupt:
                print("\n\n👋 À bientôt !")
                return False
            except EOFError:
                break
        
        return False
    
    def _show_hints(self, exercise: Exercise):
        """Affiche les indices pour l'exercice"""
        if not exercise.hints:
            print("💡 Aucun indice disponible pour cet exercice.")
            return
        
        print("\n💡 Indices:")
        for i, hint in enumerate(exercise.hints, 1):
            print(f"  {i}. {hint}")
        print()
    
    def _test_solution(self, exercise: Exercise, user_code: str) -> bool:
        """Teste la solution utilisateur"""
        try:
            # Créer un fichier temporaire avec le code utilisateur
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(user_code)
                temp_file = f.name
            
            # Charger le module utilisateur
            spec = importlib.util.spec_from_file_location("user_solution", temp_file)
            user_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(user_module)
            
            # Tester tous les cas
            passed_tests = 0
            total_tests = len(exercise.test_cases)
            
            print(f"\n🧪 Exécution de {total_tests} tests...")
            
            for i, test_case in enumerate(exercise.test_cases, 1):
                try:
                    func_name = test_case["function"]
                    inputs = test_case["inputs"]
                    expected = test_case["expected"]
                    
                    # Récupérer la fonction utilisateur
                    user_func = getattr(user_module, func_name)
                    
                    # Exécuter la fonction
                    if isinstance(inputs, list):
                        result = user_func(*inputs)
                    else:
                        result = user_func(inputs)
                    
                    # Vérifier le résultat
                    if result == expected:
                        print(f"  ✅ Test {i}: {func_name}({inputs}) = {result}")
                        passed_tests += 1
                    else:
                        print(f"  ❌ Test {i}: {func_name}({inputs}) = {result}, attendu {expected}")
                        
                except Exception as e:
                    print(f"  ❌ Test {i}: Erreur - {str(e)}")
            
            # Nettoyer
            os.unlink(temp_file)
            
            # Résultat final
            success = passed_tests == total_tests
            print(f"\n📊 Résultat: {passed_tests}/{total_tests} tests réussis")
            
            if success:
                print("🎉 Félicitations ! Exercice réussi !")
            else:
                print("💪 Continuez vos efforts ! Réessayez.")
            
            return success
            
        except Exception as e:
            print(f"❌ Erreur lors de l'exécution: {str(e)}")
            traceback.print_exc()
            return False
    
    def _update_progress(self, exercise_id: str, success: bool):
        """Met à jour la progression"""
        self.progress["total_attempts"] += 1
        
        if success:
            self.progress["total_success"] += 1
            if exercise_id not in self.progress["completed"]:
                self.progress["completed"].append(exercise_id)
            # Retirer des échecs si c'était là
            if exercise_id in self.progress["failed"]:
                self.progress["failed"].remove(exercise_id)
        else:
            if exercise_id not in self.progress["failed"] and exercise_id not in self.progress["completed"]:
                self.progress["failed"].append(exercise_id)
        
        self._save_progress()
    
    def interactive_mode(self):
        """Mode interactif principal"""
        print("🎓 Bienvenue dans EduCode !")
        print("Système d'exercices interactifs pour apprendre Python")
        print("=" * 50)
        
        while True:
            try:
                print("\n🎯 Que souhaitez-vous faire ?")
                print("1. Exercice aléatoire")
                print("2. Exercice par difficulté")
                print("3. Exercice par catégorie")
                print("4. Voir mes statistiques")
                print("5. Continuer où j'en étais")
                print("6. Quitter")
                
                choice = input("\n👉 Votre choix (1-6): ").strip()
                
                if choice == "1":
                    self._run_random_exercise()
                elif choice == "2":
                    self._run_by_difficulty()
                elif choice == "3":
                    self._run_by_category()
                elif choice == "4":
                    self.display_stats()
                elif choice == "5":
                    self._continue_progress()
                elif choice == "6":
                    print("\n👋 Merci d'avoir utilisé EduCode ! À bientôt !")
                    break
                else:
                    print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Au revoir !")
                break
    
    def _run_random_exercise(self):
        """Lance un exercice aléatoire"""
        exercise = self.get_random_exercise()
        if not exercise:
            print("🎉 Félicitations ! Vous avez terminé tous les exercices !")
            return
        self.run_exercise(exercise)
    
    def _run_by_difficulty(self):
        """Lance un exercice par difficulté"""
        print("\n📈 Choisissez la difficulté:")
        print("1. Facile")
        print("2. Moyen") 
        print("3. Difficile")
        
        choice = input("👉 Votre choix (1-3): ").strip()
        difficulty_map = {"1": "facile", "2": "moyen", "3": "difficile"}
        
        if choice in difficulty_map:
            difficulty = difficulty_map[choice]
            exercise = self.get_random_exercise(difficulty=difficulty)
            if exercise:
                self.run_exercise(exercise)
            else:
                print(f"🎉 Tous les exercices de niveau {difficulty} sont terminés !")
        else:
            print("❌ Choix invalide.")
    
    def _run_by_category(self):
        """Lance un exercice par catégorie"""
        categories = set(ex.category for ex in self.exercises.values())
        categories = sorted(categories)
        
        print("\n📚 Choisissez une catégorie:")
        for i, cat in enumerate(categories, 1):
            count = len([ex for ex in self.exercises.values() if ex.category == cat])
            completed = len([ex for ex in self.exercises.values() 
                           if ex.category == cat and ex.id in self.progress["completed"]])
            print(f"{i}. {cat} ({completed}/{count})")
        
        try:
            choice = int(input("👉 Votre choix: ").strip()) - 1
            if 0 <= choice < len(categories):
                category = categories[choice]
                available = [ex for ex in self.exercises.values() 
                           if ex.category == category and ex.id not in self.progress["completed"]]
                if available:
                    exercise = random.choice(available)
                    self.run_exercise(exercise)
                else:
                    print(f"🎉 Tous les exercices de la catégorie {category} sont terminés !")
            else:
                print("❌ Choix invalide.")
        except ValueError:
            print("❌ Veuillez entrer un nombre.")
    
    def _continue_progress(self):
        """Continue là où l'utilisateur s'était arrêté"""
        failed_exercises = [self.exercises[ex_id] for ex_id in self.progress["failed"] 
                          if ex_id in self.exercises]
        
        if failed_exercises:
            print(f"\n💪 Vous avez {len(failed_exercises)} exercice(s) à reprendre.")
            exercise = random.choice(failed_exercises)
            self.run_exercise(exercise)
        else:
            print("\n✨ Aucun exercice en attente ! Prenons-en un nouveau.")
            self._run_random_exercise()