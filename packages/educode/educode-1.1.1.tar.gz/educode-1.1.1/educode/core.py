# educode/core.py (version mise à jour avec authentification)
import json
import os
import sys
import random
import importlib.util
import tempfile
import traceback
import shutil
from typing import Dict, List, Any, Callable, Optional
from datetime import datetime

class Colors:
    """Classe pour gérer les couleurs dans le terminal"""
    
    # Codes ANSI pour les couleurs
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Couleurs de texte
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Couleurs de texte vives
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Couleurs de fond
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    @classmethod
    def is_supported(cls):
        """Vérifie si les couleurs ANSI sont supportées"""
        return (
            hasattr(sys.stdout, 'isatty') and sys.stdout.isatty() and
            os.getenv('TERM') != 'dumb' and
            os.getenv('NO_COLOR') is None
        )
    
    @classmethod
    def colorize(cls, text, color, bold=False, bg_color=None):
        """Applique une couleur au texte si supportée"""
        if not cls.is_supported():
            return text
        
        codes = []
        if bold:
            codes.append(cls.BOLD)
        if bg_color:
            codes.append(bg_color)
        codes.append(color)
        
        return ''.join(codes) + text + cls.RESET

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
    """Classe principale du système EduCode (version avec support authentification)"""
    
    def __init__(self, progress_file: str = None):
        """
        Initialise EduCode avec un fichier de progression optionnel
        
        Args:
            progress_file: Chemin personnalisé vers le fichier de progression
                          (utilisé par le système d'authentification)
        """
        self.exercises = {}
        self.progress_file = progress_file or os.path.expanduser("~/.educode_progress.json")
        self.progress = self._load_progress()
        self._load_exercises()
        
        # Indicateur si c'est une session authentifiée
        self.is_authenticated = progress_file is not None
    
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
            if self.is_authenticated:
                print(f"{Colors.colorize('❌', Colors.BRIGHT_RED)} Erreur lors de la sauvegarde: {e}")
            else:
                print(f"{Colors.colorize('⚠️ ', Colors.BRIGHT_YELLOW)} Mode démo: progression non sauvegardée")
    
    def _get_terminal_width(self):
        """Obtient la largeur du terminal"""
        try:
            return shutil.get_terminal_size().columns
        except:
            return 80
    
    def _print_separator(self, char="═", color=Colors.BRIGHT_BLUE):
        """Affiche une ligne de séparation colorée"""
        width = min(self._get_terminal_width(), 80)
        print(Colors.colorize(char * width, color))
    
    def _print_box(self, text, color=Colors.BRIGHT_CYAN, padding=1):
        """Affiche du texte dans une boîte colorée"""
        width = min(self._get_terminal_width(), 80)
        text_width = len(text)
        
        if text_width + 4 + (padding * 2) > width:
            # Texte trop long, on l'affiche simplement
            print(Colors.colorize(text, color, bold=True))
            return
        
        box_width = text_width + (padding * 2) + 2
        top_line = "╭" + "─" * (box_width - 2) + "╮"
        text_line = "│" + " " * padding + text + " " * padding + "│"
        bottom_line = "╰" + "─" * (box_width - 2) + "╯"
        
        print(Colors.colorize(top_line, color))
        print(Colors.colorize(text_line, color, bold=True))
        print(Colors.colorize(bottom_line, color))
    
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
        """Affiche les statistiques avec couleurs et avertissements pour mode démo"""
        stats = self.get_stats()
        
        print()
        
        # Avertissement pour mode démo
        if not self.is_authenticated:
            print(Colors.colorize("⚠️  MODE DÉMO - PROGRESSION NON SAUVEGARDÉE", Colors.BRIGHT_YELLOW, bold=True))
            print(Colors.colorize("Pour sauvegarder vos progrès, créez un compte avec: python -m educode", Colors.BRIGHT_CYAN))
            self._print_separator("─", Colors.BRIGHT_BLACK)
            print()
        
        # Statistiques principales
        stats_data = [
            ("📚 Exercices total", stats['total_exercises'], Colors.BRIGHT_BLUE),
            ("✅ Exercices réussis", stats['completed'], Colors.BRIGHT_GREEN),
            ("📊 Taux de complétion", f"{stats['completion_rate']:.1f}%", Colors.BRIGHT_CYAN),
            ("🎯 Taux de réussite", f"{stats['success_rate']:.1f}%", Colors.BRIGHT_YELLOW),
            ("🔄 Tentatives total", stats['total_attempts'], Colors.BRIGHT_MAGENTA)
        ]
        
        # Affichage en colonnes colorées
        for label, value, color in stats_data:
            print(f"{Colors.colorize(label + ':', Colors.BRIGHT_WHITE, bold=True)} {Colors.colorize(str(value), color, bold=True)}")
        
        # Barre de progression
        if stats['total_exercises'] > 0:
            progress_percent = stats['completion_rate']
            bar_width = 50
            filled_width = int((progress_percent / 100) * bar_width)
            empty_width = bar_width - filled_width
            
            progress_bar = (
                Colors.colorize("█" * filled_width, Colors.BRIGHT_GREEN) + 
                Colors.colorize("░" * empty_width, Colors.BRIGHT_BLACK)
            )
            
            print(f"\n{Colors.colorize('📈 Progression:', Colors.BRIGHT_WHITE, bold=True)}")
            print(f"[{progress_bar}] {Colors.colorize(f'{progress_percent:.1f}%', Colors.BRIGHT_CYAN, bold=True)}")
        
        # Exercices récents
        if self.progress["completed"]:
            print(f"\n{Colors.colorize('🏆 Derniers succès:', Colors.BRIGHT_YELLOW, bold=True)}")
            for ex_id in self.progress["completed"][-5:]:
                if ex_id in self.exercises:
                    ex = self.exercises[ex_id]
                    difficulty_colors = {
                        "facile": Colors.BRIGHT_GREEN,
                        "moyen": Colors.BRIGHT_YELLOW,
                        "difficile": Colors.BRIGHT_RED
                    }
                    diff_color = difficulty_colors.get(ex.difficulty, Colors.BRIGHT_WHITE)
                    
                    print(f"  {Colors.colorize('✨', Colors.BRIGHT_YELLOW)} "
                          f"{Colors.colorize(ex.title, Colors.BRIGHT_WHITE, bold=True)} "
                          f"({Colors.colorize(ex.difficulty.upper(), diff_color, bold=True)})")
        
        # Encouragement basé sur les stats
        if stats['completed'] == 0:
            encouragement = "🚀 Prêt à commencer votre aventure Python ?"
            color = Colors.BRIGHT_CYAN
        elif stats['completion_rate'] < 25:
            encouragement = "💪 Bon début ! Continuez sur cette lancée !"
            color = Colors.BRIGHT_GREEN
        elif stats['completion_rate'] < 50:
            encouragement = "🔥 Excellent progrès ! Vous maîtrisez bien !"
            color = Colors.BRIGHT_YELLOW
        elif stats['completion_rate'] < 75:
            encouragement = "⭐ Impressionnant ! Vous êtes un expert !"
            color = Colors.BRIGHT_MAGENTA
        else:
            encouragement = "🏆 Maître Python ! Félicitations !"
            color = Colors.BRIGHT_YELLOW
        
        print(f"\n{Colors.colorize(encouragement, color, bold=True)}")
        
        # Message spécial pour mode démo
        if not self.is_authenticated and stats['completed'] > 0:
            print()
            print(Colors.colorize("💡 Astuce:", Colors.BRIGHT_BLUE, bold=True))
            print(Colors.colorize("Créez un compte pour obtenir un certificat de vos accomplissements !", Colors.BRIGHT_CYAN))
        print()
    
    def generate_certificate_pdf(self, user_name: str = None):
        """Génère un certificat PDF pour l'utilisateur authentifié"""
        try:
            # Import de la classe CertificationGenerator
            from .certification import CertificationGenerator
            
            # Récupérer automatiquement le nom de l'utilisateur authentifié
            if not user_name:
                user_stats = self.auth_manager.get_user_stats()
                user_name = user_stats['name']
            
            # Récupérer les statistiques pour le certificat
            stats = self.get_stats()
            
            # Vérifier que l'utilisateur a au moins quelques exercices réussis
            if stats['completed'] < 3:
                certificate_title = "📋 CERTIFICAT EDUCODE"
                print(f"\n{Colors.colorize(certificate_title, Colors.BRIGHT_YELLOW, bold=True)}")
                print(Colors.colorize("─" * 30, Colors.BRIGHT_BLACK))
                warning_message = "⚠️  Certificat non disponible"
                print(f"{Colors.colorize(warning_message, Colors.BRIGHT_YELLOW, bold=True)}")
                requirement_text = "Vous devez réussir au moins 3 exercices pour obtenir un certificat."
                print(f"{Colors.colorize(requirement_text, Colors.BRIGHT_WHITE)}")
                progress_text = f"Progression actuelle: {stats['completed']} exercice(s) réussi(s)"
                print(f"{Colors.colorize(progress_text, Colors.BRIGHT_CYAN)}")
                encouragement = "💪 Continuez vos exercices et revenez ensuite !"
                print(f"\n{Colors.colorize(encouragement, Colors.BRIGHT_GREEN, bold=True)}")
                return
            
            # Créer une instance du générateur de certificats
            cert_generator = CertificationGenerator()
            
            # Générer le certificat PDF
            pdf_path = cert_generator.generate_certificate(user_name, stats)
            
            if pdf_path:
                success_title = "🏆 CERTIFICAT GÉNÉRÉ AVEC SUCCÈS !"
                print(f"\n{Colors.colorize(success_title, Colors.BRIGHT_GREEN, bold=True)}")
                print(Colors.colorize("─" * 40, Colors.BRIGHT_BLACK))
                
                congrats_text = f"✨ Félicitations {user_name} !"
                print(f"{Colors.colorize(congrats_text, Colors.BRIGHT_YELLOW, bold=True)}")
                
                location_text = "📄 Votre certificat EduCode a été créé dans ~/EduCode_Certificates/"
                print(f"{Colors.colorize(location_text, Colors.BRIGHT_CYAN)}")
                
                file_text = f"📁 Fichier: {os.path.basename(pdf_path)}"
                print(f"{Colors.colorize(file_text, Colors.BRIGHT_WHITE)}")
                
                auth_text = "🔒 Certificat authentifié et personnalisé"
                print(f"{Colors.colorize(auth_text, Colors.BRIGHT_GREEN)}")
                
                accomplishments_title = "📊 Vos accomplissements:"
                print(f"\n{Colors.colorize(accomplishments_title, Colors.BRIGHT_WHITE, bold=True)}")
                
                completed_text = f"   • {stats['completed']} exercices réussis"
                print(f"{Colors.colorize(completed_text, Colors.BRIGHT_GREEN)}")
                
                success_rate_text = f"   • {stats['success_rate']:.1f}% de taux de réussite"
                print(f"{Colors.colorize(success_rate_text, Colors.BRIGHT_YELLOW)}")
                
                attempts_text = f"   • {stats['total_attempts']} tentatives au total"
                print(f"{Colors.colorize(attempts_text, Colors.BRIGHT_BLUE)}")
            else:
                error_message = "❌ Erreur lors de la génération du certificat"
                print(f"\n{Colors.colorize(error_message, Colors.BRIGHT_RED, bold=True)}")
                retry_message = "Veuillez réessayer plus tard."
                print(f"{Colors.colorize(retry_message, Colors.BRIGHT_WHITE)}")
            
        except ImportError:
            cert_title = "📋 GÉNÉRATION DE CERTIFICAT"
            print(f"\n{Colors.colorize(cert_title, Colors.BRIGHT_YELLOW, bold=True)}")
            print(Colors.colorize("─" * 40, Colors.BRIGHT_BLACK))
            
            unavailable_msg = "❌ Module de certification non disponible"
            print(f"{Colors.colorize(unavailable_msg, Colors.BRIGHT_RED, bold=True)}")
            
            temp_unavailable = "Le système de certificats est temporairement indisponible."
            print(f"{Colors.colorize(temp_unavailable, Colors.BRIGHT_WHITE)}")
            
            # Afficher un certificat textuel en attendant
            user_stats = self.auth_manager.get_user_stats()
            stats = self.get_stats()
            
            temp_cert_title = "📜 CERTIFICAT TEMPORAIRE (format texte)"
            print(f"\n{Colors.colorize(temp_cert_title, Colors.BRIGHT_CYAN, bold=True)}")
            print(Colors.colorize("═" * 60, Colors.BRIGHT_BLUE))
            
            educode_cert = "🎓 CERTIFICAT EDUCODE"
            print(f"\n{Colors.colorize(educode_cert, Colors.BRIGHT_YELLOW, bold=True)}")
            
            cert_intro = "Ce certificat atteste que"
            print(f"\n{Colors.colorize(cert_intro, Colors.BRIGHT_WHITE)}")
            print(f"{Colors.colorize(user_stats['name'], Colors.BRIGHT_GREEN, bold=True)}")
            
            completion_text = "a complété avec succès"
            print(f"{Colors.colorize(completion_text, Colors.BRIGHT_WHITE)}")
            
            exercises_text = f"{stats['completed']} exercices Python"
            print(f"{Colors.colorize(exercises_text, Colors.BRIGHT_CYAN, bold=True)}")
            
            platform_text = "sur la plateforme EduCode"
            print(f"{Colors.colorize(platform_text, Colors.BRIGHT_WHITE)}")
            
            performance_title = "📊 Performances:"
            print(f"\n{Colors.colorize(performance_title, Colors.BRIGHT_WHITE, bold=True)}")
            
            success_rate_display = f"   • Taux de réussite: {stats['success_rate']:.1f}%"
            print(f"{Colors.colorize(success_rate_display, Colors.BRIGHT_YELLOW, bold=True)}")
            
            attempts_display = f"   • Tentatives totales: {stats['total_attempts']}"
            print(f"{Colors.colorize(attempts_display, Colors.BRIGHT_BLUE, bold=True)}")
            
            member_since = f"   • Membre depuis: {user_stats['member_since']}"
            print(f"{Colors.colorize(member_since, Colors.BRIGHT_MAGENTA, bold=True)}")
            
            issued_text = f"Délivré le: {datetime.now().strftime('%d/%m/%Y')}"
            print(f"\n{Colors.colorize(issued_text, Colors.BRIGHT_GREEN, bold=True)}")
            
            identifier_text = f"Identifiant: {user_stats['email']}"
            print(f"{Colors.colorize(identifier_text, Colors.BRIGHT_BLACK)}")
            
            final_congrats = "🏆 Félicitations pour vos accomplissements !"
            print(f"\n{Colors.colorize(final_congrats, Colors.BRIGHT_YELLOW, bold=True)}")
            print(Colors.colorize("═" * 60, Colors.BRIGHT_BLUE))
            
        except Exception as e:
            system_error = f"❌ Erreur système: {str(e)}"
            print(f"\n{Colors.colorize(system_error, Colors.BRIGHT_RED, bold=True)}")

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
        """Lance un exercice interactif avec affichage coloré"""
        print()
        self._print_separator("═", Colors.BRIGHT_CYAN)
        
        # Avertissement mode démo
        if not self.is_authenticated:
            print(Colors.colorize("⚠️  MODE DÉMO - Progression non sauvegardée", Colors.BRIGHT_YELLOW, bold=True))
            self._print_separator("─", Colors.BRIGHT_BLACK)
        
        # En-tête de l'exercice
        title_text = f"🎓 {exercise.title}"
        print(Colors.colorize(title_text, Colors.BRIGHT_CYAN, bold=True))
        
        # Informations sur l'exercice
        category_text = f"📚 Catégorie: {exercise.category}"
        print(Colors.colorize(category_text, Colors.BRIGHT_BLUE))
        
        difficulty_colors = {
            "facile": Colors.BRIGHT_GREEN,
            "moyen": Colors.BRIGHT_YELLOW,
            "difficile": Colors.BRIGHT_RED
        }
        diff_color = difficulty_colors.get(exercise.difficulty, Colors.BRIGHT_WHITE)
        difficulty_text = f"🔥 Difficulté: {exercise.difficulty.upper()}"
        print(Colors.colorize(difficulty_text, diff_color, bold=True))
        
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        # Description
        print(Colors.colorize("📝 Description:", Colors.BRIGHT_WHITE, bold=True))
        print(exercise.description)
        
        # Template de solution si disponible
        if exercise.solution_template:
            print(f"\n{Colors.colorize('💡 Template de solution:', Colors.BRIGHT_YELLOW, bold=True)}")
            print(Colors.colorize(exercise.solution_template, Colors.BRIGHT_BLACK, bg_color=Colors.BG_WHITE))
        
        # Instructions
        print(f"\n{Colors.colorize('✍️  Instructions:', Colors.BRIGHT_GREEN, bold=True)}")
        print(f"• {Colors.colorize('Écrivez votre solution ligne par ligne', Colors.BRIGHT_WHITE)}")
        print(f"• {Colors.colorize('Appuyez sur Entrée avec une ligne vide pour tester', Colors.BRIGHT_WHITE)}")
        print(f"• {Colors.colorize('Tapez', Colors.BRIGHT_WHITE)} {Colors.colorize('hints', Colors.BRIGHT_CYAN, bold=True)} {Colors.colorize('pour des indices', Colors.BRIGHT_WHITE)}")
        print(f"• {Colors.colorize('Tapez', Colors.BRIGHT_WHITE)} {Colors.colorize('quit', Colors.BRIGHT_RED, bold=True)} {Colors.colorize('pour quitter', Colors.BRIGHT_WHITE)}")
        
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        user_code = []
        line_number = 1
        
        while True:
            try:
                prompt = Colors.colorize(f"{line_number:2d}>>> " if not user_code else f"{line_number:2d}... ", Colors.BRIGHT_BLUE, bold=True)
                line = input(prompt)
                
                if line.strip() == "quit":
                    print(f"\n{Colors.colorize('👋 À bientôt !', Colors.BRIGHT_YELLOW, bold=True)}")
                    return False
                elif line.strip() == "hints":
                    self._show_hints(exercise)
                    continue
                elif line.strip() == "modules":
                    self._show_popular_modules()
                    continue
                elif line.strip() == "test" and user_code:
                    # Tester immédiatement sans valider
                    code = "\n".join(user_code)
                    print("\n🧪 Test rapide...")
                    self._quick_test(exercise, code)
                    continue
                elif line.strip() == "" and user_code:
                    # Code terminé, on teste
                    code = "\n".join(user_code)
                    success = self._test_solution(exercise, code)
                    self._update_progress(exercise.id, success)
                    return success
                else:
                    user_code.append(line)
                    line_number += 1
                    
            except KeyboardInterrupt:
                print(f"\n\n{Colors.colorize('👋 Au revoir !', Colors.BRIGHT_YELLOW, bold=True)}")
                return False
            except EOFError:
                break
        
        return False
    
    def _show_hints(self, exercise: Exercise):
        """Affiche les indices avec couleurs"""
        if not exercise.hints:
            print(f"\n{Colors.colorize('💡', Colors.BRIGHT_YELLOW)} {Colors.colorize('Aucun indice disponible pour cet exercice.', Colors.BRIGHT_WHITE)}")
            return
        
        print(f"\n{Colors.colorize('💡 Indices:', Colors.BRIGHT_YELLOW, bold=True)}")
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        for i, hint in enumerate(exercise.hints, 1):
            print(f"  {Colors.colorize(f'{i}.', Colors.BRIGHT_CYAN, bold=True)} {Colors.colorize(hint, Colors.BRIGHT_WHITE)}")
        
        self._print_separator("─", Colors.BRIGHT_BLACK)
        print()
    
    def _test_solution(self, exercise: Exercise, user_code: str) -> bool:
        """Teste la solution utilisateur avec installation préalable des modules"""
        import importlib
        import importlib.util
        import tempfile
        import os
        import time
        
        try:
            # Installer les modules requis d'abord
            required_modules = self._extract_imports(user_code)
            
            # Installer tous les modules requis d'abord
            all_installed = True
            for module_name in required_modules:
                if not self._install_module(module_name):
                    print(f"⚠️  Module '{module_name}' non disponible. Tentative de continuer...")
                    all_installed = False
            
            # Invalider les caches après toutes les installations
            if required_modules:
                importlib.invalidate_caches()
                # Attendre un court instant pour que les modules soient disponibles
                time.sleep(0.1)
                    
            # Créer un fichier temporaire avec le code utilisateur
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(user_code)
                temp_file = f.name
            
            # Charger le module utilisateur
            spec = importlib.util.spec_from_file_location("user_solution", temp_file)
            user_module = importlib.util.module_from_spec(spec)
            
            # Exécuter dans un try/catch spécifique pour les imports
            try:
                spec.loader.exec_module(user_module)
            except ImportError as e:
                print(f"❌ Erreur d'import: {e}")
                print("💡 Essayez de redémarrer EduCode si le problème persiste.")
                os.unlink(temp_file)
                return False
            
            # Tests
            passed_tests = 0
            total_tests = len(exercise.test_cases)
            
            print(f"\n{Colors.colorize('🧪 Tests en cours...', Colors.BRIGHT_BLUE, bold=True)}")
            self._print_separator("─", Colors.BRIGHT_BLACK)
            
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
                    if self._compare_results(result, expected):
                        test_status = Colors.colorize("✅ RÉUSSI", Colors.BRIGHT_GREEN, bold=True)
                        print(f"  {Colors.colorize(f'Test {i}:', Colors.BRIGHT_WHITE, bold=True)} {test_status}")
                        print(f"     {Colors.colorize(f'{func_name}({inputs}) = {result}', Colors.BRIGHT_GREEN)}")
                        passed_tests += 1
                    else:
                        test_status = Colors.colorize("❌ ÉCHEC", Colors.BRIGHT_RED, bold=True)
                        print(f"  {Colors.colorize(f'Test {i}:', Colors.BRIGHT_WHITE, bold=True)} {test_status}")
                        print(f"     {Colors.colorize(f'{func_name}({inputs}) = {result}', Colors.BRIGHT_RED)}")
                        print(f"     {Colors.colorize(f'Attendu: {expected}', Colors.BRIGHT_YELLOW)}")
                        
                except Exception as e:
                    test_status = Colors.colorize("💥 ERREUR", Colors.BRIGHT_RED, bold=True)
                    print(f"  {Colors.colorize(f'Test {i}:', Colors.BRIGHT_WHITE, bold=True)} {test_status}")
                    print(f"     {Colors.colorize(f'Erreur: {str(e)}', Colors.BRIGHT_RED)}")
            
            # Nettoyer
            os.unlink(temp_file)
            
            # Résultat final
            success = passed_tests == total_tests
            
            self._print_separator("═", Colors.BRIGHT_BLUE)
            
            if success:
                result_text = f"🎉 FÉLICITATIONS ! 🎉"
                score_text = f"Score parfait: {passed_tests}/{total_tests} tests réussis"
                print(Colors.colorize(result_text, Colors.BRIGHT_GREEN, bold=True))
                print(Colors.colorize(score_text, Colors.BRIGHT_GREEN, bold=True))
                
                # Message spécial pour mode démo
                if not self.is_authenticated:
                    print(Colors.colorize("💡 Créez un compte pour sauvegarder cette réussite !", Colors.BRIGHT_CYAN))
            else:
                result_text = f"💪 Presque réussi ! Continuez vos efforts !"
                score_text = f"Score: {passed_tests}/{total_tests} tests réussis"
                print(Colors.colorize(result_text, Colors.BRIGHT_YELLOW, bold=True))
                print(Colors.colorize(score_text, Colors.BRIGHT_YELLOW, bold=True))
            
            self._print_separator("═", Colors.BRIGHT_BLUE)
            return success
            
        except Exception as e:
            print(f"\n{Colors.colorize('💥 ERREUR SYSTÈME', Colors.BRIGHT_RED, bold=True)}")
            error_msg = Colors.colorize('Erreur lors de l\'exécution:', Colors.BRIGHT_RED)
            print(f"{error_msg} {str(e)}")
            return False
    
    def _update_progress(self, exercise_id: str, success: bool):
        """Met à jour la progression (avec gestion du mode démo)"""
        if not self.is_authenticated:
            # En mode démo, on met à jour en mémoire mais pas sur disque
            pass
            
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
        
        # Sauvegarder seulement si authentifié
        if self.is_authenticated:
            self._save_progress()
    
    def _install_module(self, module_name: str) -> bool:
        """Installe un module externe si nécessaire avec validation post-installation"""
        import subprocess
        import sys
        import importlib
        
        try:
            # Vérifier si le module est déjà installé
            try:
                __import__(module_name)
                return True
            except ImportError:
                pass
            
            print(f"📦 Module '{module_name}' non trouvé. Installation en cours...")
            
            # Installer le module
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", module_name
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                # Invalider le cache d'imports et tester l'import réel
                importlib.invalidate_caches()
                
                try:
                    # Tenter l'import réel pour validation
                    __import__(module_name)
                    print(f"✅ Module '{module_name}' installé et validé avec succès !")
                    return True
                except ImportError as e:
                    print(f"❌ Module '{module_name}' installé mais non importable: {e}")
                    return False
            else:
                print(f"❌ Échec de l'installation de '{module_name}': {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erreur lors de l'installation de '{module_name}': {e}")
            return False

    def _extract_imports(self, code: str) -> List[str]:
        """Extrait les modules importés du code utilisateur"""
        imports = []
        lines = code.split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('import '):
                # import module ou import module as alias
                parts = line.replace('import ', '').split(' as ')[0].split(',')
                for part in parts:
                    module = part.strip().split('.')[0]  # Prendre le module racine
                    if module and module not in ['os', 'sys', 'json', 'tempfile', 'importlib']:
                        imports.append(module)
            elif line.startswith('from '):
                # from module import something
                try:
                    module = line.split(' ')[1]
                    if module and module not in ['os', 'sys', 'json', 'tempfile', 'importlib']:
                        imports.append(module)
                except IndexError:
                    pass
        
        return list(set(imports))  # Supprimer les doublons
    
    def _compare_results(self, result, expected):
        """Compare les résultats avec gestion des types spéciaux"""
        try:
            # Gestion spéciale pour pandas DataFrame/Series
            if hasattr(result, 'equals') and hasattr(expected, 'equals'):
                return result.equals(expected)
            
            # Gestion spéciale pour numpy arrays
            if hasattr(result, 'shape') and hasattr(expected, 'shape'):
                try:
                    import numpy as np
                    return np.array_equal(result, expected)
                except ImportError:
                    pass
            
            # Gestion des listes/arrays avec tolérance numérique
            if isinstance(result, (list, tuple)) and isinstance(expected, (list, tuple)):
                if len(result) != len(expected):
                    return False
                for r, e in zip(result, expected):
                    if isinstance(r, float) and isinstance(e, float):
                        if abs(r - e) > 1e-9:  # Tolérance pour les flottants
                            return False
                    elif r != e:
                        return False
                return True
            
            # Comparaison avec tolérance pour les flottants
            if isinstance(result, float) and isinstance(expected, float):
                return abs(result - expected) < 1e-9
            
            # Comparaison standard
            return result == expected
            
        except Exception:
            # Fallback sur comparaison standard
            return result == expected
        
    def _show_popular_modules(self):
        """Affiche une liste de modules populaires"""
        modules = {
            "📊 Data Science": ["pandas", "numpy", "matplotlib", "seaborn", "scipy", "sklearn"],
            "🌐 Web & APIs": ["requests", "beautifulsoup4", "flask", "fastapi", "urllib3"],
            "📁 Fichiers & Formats": ["openpyxl", "pillow", "PyPDF2", "python-docx"],
            "🔢 Mathématiques": ["sympy", "statistics", "decimal", "fractions"],
            "📅 Date & Temps": ["datetime", "dateutil", "pytz"],
            "🎨 Interface utilisateur": ["tkinter", "pygame", "rich", "colorama"],
            "🔧 Utilitaires": ["itertools", "collections", "functools", "operator"]
        }
        
        print("\n🐍 Modules Python populaires (exemples):")
        for category, mods in modules.items():
            print(f"\n{category}:")
            for mod in mods:
                print(f"  import {mod}")
        print("\n💡 Vous pouvez importer n'importe quel module disponible sur PyPI !")
        print("   Exemple: import pandas as pd\n")

    def _quick_test(self, exercise: Exercise, user_code: str):
        """Effectue un test rapide sans validation complète"""
        try:
            # Test de syntaxe seulement
            compile(user_code, '<string>', 'exec')
            print("✅ Syntaxe Python valide !")
            
            # Vérifier les imports
            required_modules = self._extract_imports(user_code)
            if required_modules:
                print(f"📦 Modules détectés: {', '.join(required_modules)}")
                
        except SyntaxError as e:
            print(f"❌ Erreur de syntaxe: {e}")
        except Exception as e:
            print(f"⚠️  Attention: {e}")
    
    def interactive_mode(self):
        """Mode interactif principal avec interface colorée (version avec support demo)"""
        print(Colors.colorize("Système d'exercices interactifs pour apprendre Python", Colors.BRIGHT_CYAN))
        
        # Afficher le statut d'authentification
        if not self.is_authenticated:
            print(Colors.colorize("⚠️  MODE DÉMO - Progression non sauvegardée", Colors.BRIGHT_YELLOW, bold=True))
            print(Colors.colorize("Pour l'expérience complète, créez un compte avec: python -m educode", Colors.BRIGHT_CYAN))
        
        self._print_separator("═", Colors.BRIGHT_BLUE)
        
        # Affichage du menu principal adapté
        while True:
            try:
                print(f"\n{Colors.colorize('🎯 Menu Principal', Colors.BRIGHT_MAGENTA, bold=True)}")
                self._print_separator("─", Colors.BRIGHT_BLACK)
                
                menu_options = [
                    ("1", "🎲 Exercice aléatoire", "Choisir un exercice au hasard", Colors.BRIGHT_GREEN),
                    ("2", "📈 Exercice par difficulté", "Facile, Moyen ou Difficile", Colors.BRIGHT_YELLOW),
                    ("3", "📚 Exercice par catégorie", "Fonctions, Listes, Algorithmes...", Colors.BRIGHT_CYAN),
                    ("4", "📊 Statistiques", "Voir vos performances", Colors.BRIGHT_BLUE),
                    ("5", "🔄 Reprendre un exercice", "Continuer où vous en étiez", Colors.BRIGHT_MAGENTA),
                    ("6", "📦 Test d'import module", "Télécharger un module à utiliser", Colors.BRIGHT_WHITE)
                ]
                
                # Ajouter des options selon le mode
                if self.is_authenticated:
                    menu_options.append(("7", "🏆 Générer certificat", "Créer votre certificat PDF", Colors.BRIGHT_YELLOW))
                    menu_options.append(("8", "👋 Quitter", "Fermer EduCode", Colors.BRIGHT_RED))
                else:
                    menu_options.append(("7", "🔐 Créer un compte", "Pour sauvegarder votre progression", Colors.BRIGHT_GREEN))
                    menu_options.append(("8", "👋 Quitter", "Fermer EduCode", Colors.BRIGHT_RED))
                
                for number, title, description, color in menu_options:
                    print(f"  {Colors.colorize(number + '.', color, bold=True)} "
                          f"{Colors.colorize(title, Colors.BRIGHT_WHITE, bold=True)}")
                    print(f"     {Colors.colorize(description, Colors.BRIGHT_BLACK)}")
                
                self._print_separator("─", Colors.BRIGHT_BLACK)
                max_choice = len(menu_options)
                choice = input(f"{Colors.colorize(f'👉 Votre choix (1-{max_choice}):', Colors.BRIGHT_CYAN, bold=True)} ").strip()
                
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
                    self._test_module_import()
                elif choice == "7":
                    if self.is_authenticated:
                        self.generate_certificate_pdf()
                    else:
                        self._show_account_creation_info()
                elif choice == "8":
                    goodbye_msg = Colors.colorize('👋 Merci d\'avoir utilisé EduCode !', Colors.BRIGHT_YELLOW, bold=True)
                    continue_msg = Colors.colorize('🚀 Continuez à coder et à apprendre !', Colors.BRIGHT_CYAN)
                    print(f"\n{goodbye_msg}")
                    print(f"{continue_msg}")
                    break
                else:
                    print(f"{Colors.colorize('❌', Colors.BRIGHT_RED)} {Colors.colorize('Choix invalide.', Colors.BRIGHT_RED)} "
                          f"{Colors.colorize(f'Veuillez entrer un nombre entre 1 et {max_choice}.', Colors.BRIGHT_WHITE)}")
                    
            except KeyboardInterrupt:
                print(f"\n\n{Colors.colorize('👋 Au revoir !', Colors.BRIGHT_YELLOW, bold=True)}")
                break
    
    def _show_account_creation_info(self):
        """Affiche les informations pour créer un compte"""
        print(f"\n{Colors.colorize('🔐 CRÉER UN COMPTE EDUCODE', Colors.BRIGHT_GREEN, bold=True)}")
        self._print_separator("─", Colors.BRIGHT_BLACK)
        print()
        print(Colors.colorize("Avantages d'un compte EduCode:", Colors.BRIGHT_WHITE, bold=True))
        print(f"  ✅ {Colors.colorize('Sauvegarde automatique de votre progression', Colors.BRIGHT_GREEN)}")
        print(f"  🏆 {Colors.colorize('Certificats PDF personnalisés et authentifiés', Colors.BRIGHT_YELLOW)}")
        print(f"  📊 {Colors.colorize('Statistiques détaillées et historique', Colors.BRIGHT_BLUE)}")
        print(f"  🔒 {Colors.colorize('Profil sécurisé et données protégées', Colors.BRIGHT_MAGENTA)}")
        print()
        print(Colors.colorize("Pour créer votre compte:", Colors.BRIGHT_CYAN, bold=True))
        print(f"  {Colors.colorize('python -m educode', Colors.BRIGHT_WHITE, bold=True)}")
        print()
    
    # Méthodes communes aux deux versions (inchangées)
    def _run_random_exercise(self):
        """Lance un exercice aléatoire"""
        exercise = self.get_random_exercise()
        if not exercise:
            self._print_box("🎉 Félicitations ! Vous avez terminé tous les exercices ! 🎉", Colors.BRIGHT_GREEN)
            print(f"\n{Colors.colorize('🏆 Vous êtes maintenant un maître Python !', Colors.BRIGHT_YELLOW, bold=True)}")
            return
        
        print(f"\n{Colors.colorize('🎲 Exercice choisi aléatoirement...', Colors.BRIGHT_GREEN, bold=True)}")
        self.run_exercise(exercise)
    
    def _run_by_difficulty(self):
        """Lance un exercice par difficulté avec interface colorée"""
        print(f"\n{Colors.colorize('📈 Choisissez votre niveau de difficulté:', Colors.BRIGHT_MAGENTA, bold=True)}")
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        difficulties = [
            ("1", "🟢 Facile", "Parfait pour débuter", Colors.BRIGHT_GREEN, "facile"),
            ("2", "🟡 Moyen", "Pour approfondir vos connaissances", Colors.BRIGHT_YELLOW, "moyen"),
            ("3", "🔴 Difficile", "Défiez-vous avec des algorithmes complexes", Colors.BRIGHT_RED, "difficile")
        ]
        
        for number, title, description, color, _ in difficulties:
            # Compter les exercices disponibles pour cette difficulté
            available = len([ex for ex in self.exercises.values() 
                           if ex.difficulty == difficulties[int(number)-1][4] and ex.id not in self.progress["completed"]])
            completed = len([ex for ex in self.exercises.values() 
                           if ex.difficulty == difficulties[int(number)-1][4] and ex.id in self.progress["completed"]])
            total = len([ex for ex in self.exercises.values() if ex.difficulty == difficulties[int(number)-1][4]])
            
            print(f"  {Colors.colorize(number + '.', color, bold=True)} "
                  f"{Colors.colorize(title, Colors.BRIGHT_WHITE, bold=True)} "
                  f"{Colors.colorize(f'({completed}/{total})', Colors.BRIGHT_BLACK)}")
            print(f"     {Colors.colorize(description, Colors.BRIGHT_BLACK)}")
            if available == 0:
                print(f"     {Colors.colorize('✨ Tous les exercices terminés !', Colors.BRIGHT_GREEN)}")
        
        self._print_separator("─", Colors.BRIGHT_BLACK)
        choice = input(f"{Colors.colorize('👉 Votre choix (1-3):', Colors.BRIGHT_CYAN, bold=True)} ").strip()
        
        difficulty_map = {"1": "facile", "2": "moyen", "3": "difficile"}
        
        if choice in difficulty_map:
            difficulty = difficulty_map[choice]
            exercise = self.get_random_exercise(difficulty=difficulty)
            if exercise:
                print(f"\n{Colors.colorize(f'📈 Exercice de niveau {difficulty.upper()} sélectionné...', Colors.BRIGHT_BLUE, bold=True)}")
                self.run_exercise(exercise)
            else:
                self._print_box(f"🎉 Tous les exercices de niveau {difficulty.upper()} sont terminés ! 🎉", Colors.BRIGHT_GREEN)
        else:
            print(f"{Colors.colorize('❌ Choix invalide.', Colors.BRIGHT_RED)}")
    
    def _run_by_category(self):
        """Lance un exercice par catégorie avec interface colorée"""
        categories = set(ex.category for ex in self.exercises.values())
        categories = sorted(categories)
        
        print(f"\n{Colors.colorize('📚 Choisissez une catégorie:', Colors.BRIGHT_CYAN, bold=True)}")
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        category_colors = [Colors.BRIGHT_BLUE, Colors.BRIGHT_GREEN, Colors.BRIGHT_YELLOW, 
                          Colors.BRIGHT_MAGENTA, Colors.BRIGHT_CYAN, Colors.BRIGHT_RED,
                          Colors.BRIGHT_WHITE, Colors.GREEN, Colors.YELLOW]
        
        for i, cat in enumerate(categories, 1):
            total = len([ex for ex in self.exercises.values() if ex.category == cat])
            completed = len([ex for ex in self.exercises.values() 
                           if ex.category == cat and ex.id in self.progress["completed"]])
            available = total - completed
            
            color = category_colors[i % len(category_colors)]
            progress_bar = "█" * (completed * 10 // total) + "░" * (10 - (completed * 10 // total))
            
            print(f"  {Colors.colorize(f'{i}.', color, bold=True)} "
                  f"{Colors.colorize(cat, Colors.BRIGHT_WHITE, bold=True)} "
                  f"{Colors.colorize(f'({completed}/{total})', Colors.BRIGHT_BLACK)}")
            print(f"     [{Colors.colorize(progress_bar, color)}] "
                  f"{Colors.colorize(f'{available} disponible(s)', Colors.BRIGHT_BLACK if available > 0 else Colors.BRIGHT_GREEN)}")
        
        self._print_separator("─", Colors.BRIGHT_BLACK)
        
        try:
            choice = int(input(f"{Colors.colorize('👉 Votre choix:', Colors.BRIGHT_CYAN, bold=True)} ").strip()) - 1
            if 0 <= choice < len(categories):
                category = categories[choice]
                available = [ex for ex in self.exercises.values() 
                           if ex.category == category and ex.id not in self.progress["completed"]]
                if available:
                    exercise = random.choice(available)
                    print(f"\n{Colors.colorize(f'📚 Exercice de la catégorie {category} sélectionné...', Colors.BRIGHT_CYAN, bold=True)}")
                    self.run_exercise(exercise)
                else:
                    self._print_box(f"🎉 Tous les exercices de la catégorie {category} sont terminés ! 🎉", Colors.BRIGHT_GREEN)
            else:
                print(f"{Colors.colorize('❌ Choix invalide.', Colors.BRIGHT_RED)}")
        except ValueError:
            print(f"{Colors.colorize('❌ Veuillez entrer un nombre.', Colors.BRIGHT_RED)}")
    
    def _continue_progress(self):
        """Continue là où l'utilisateur s'était arrêté"""
        failed_exercises = [self.exercises[ex_id] for ex_id in self.progress["failed"] 
                          if ex_id in self.exercises]
        
        if failed_exercises:
            print(f"\n{Colors.colorize('💪 Reprise de vos exercices en cours...', Colors.BRIGHT_MAGENTA, bold=True)}")
            print(f"{Colors.colorize(f'Vous avez {len(failed_exercises)} exercice(s) à reprendre.', Colors.BRIGHT_YELLOW)}")
            
            # Afficher les exercices en attente
            print(f"\n{Colors.colorize('📋 Exercices à reprendre:', Colors.BRIGHT_BLUE, bold=True)}")
            for i, ex in enumerate(failed_exercises[:5], 1):  # Montrer max 5
                difficulty_colors = {
                    "facile": Colors.BRIGHT_GREEN,
                    "moyen": Colors.BRIGHT_YELLOW,
                    "difficile": Colors.BRIGHT_RED
                }
                diff_color = difficulty_colors.get(ex.difficulty, Colors.BRIGHT_WHITE)
                print(f"  {Colors.colorize(f'{i}.', Colors.BRIGHT_CYAN)} "
                      f"{Colors.colorize(ex.title, Colors.BRIGHT_WHITE)} "
                      f"({Colors.colorize(ex.difficulty.upper(), diff_color)})")
            
            if len(failed_exercises) > 5:
                print(f"  {Colors.colorize(f'... et {len(failed_exercises) - 5} autre(s)', Colors.BRIGHT_BLACK)}")
            
            exercise = random.choice(failed_exercises)
            resume_msg = Colors.colorize('🔄 Reprise d\'un exercice...', Colors.BRIGHT_BLUE, bold=True)
            print(f"\n{resume_msg}")
            self.run_exercise(exercise)
        else:
            success_msg = Colors.colorize('✨ Aucun exercice en attente !', Colors.BRIGHT_GREEN, bold=True)
            new_exercise_msg = Colors.colorize('Prenons un nouvel exercice à la place.', Colors.BRIGHT_CYAN)
            print(f"\n{success_msg}")
            print(f"{new_exercise_msg}")
            self._run_random_exercise()
    
    def _test_module_import(self):
        """Permet de tester l'import d'un module"""
        print("\n🧪 Test d'import de module")
        module_name = input("Nom du module à tester: ").strip()
        
        if not module_name:
            return
        
        print(f"\n📦 Test d'import de '{module_name}'...")
        
        try:
            # Essayer d'importer le module
            __import__(module_name)
            print(f"✅ Module '{module_name}' déjà disponible !")
        except ImportError:
            print(f"❌ Module '{module_name}' non trouvé.")
            install = input("Voulez-vous l'installer ? (o/n): ").strip().lower()
            
            if install in ['o', 'oui', 'y', 'yes']:
                if self._install_module(module_name):
                    print("🎉 Module installé avec succès ! Vous pouvez maintenant l'utiliser dans vos exercices.")
                else:
                    print("❌ Échec de l'installation.")
            else:
                print("ℹ️  Installation annulée.")
        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")