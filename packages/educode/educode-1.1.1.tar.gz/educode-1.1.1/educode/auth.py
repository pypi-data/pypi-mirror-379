# educode/auth.py
import json
import os
import hashlib
import secrets
import re
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
from .core import Colors

class AuthenticationManager:
    """Gestionnaire d'authentification sécurisé pour EduCode"""
    
    def __init__(self):
        self.users_file = os.path.expanduser("~/.educode_users.json")
        self.session_file = os.path.expanduser("~/.educode_session.json")
        self.users_data = self._load_users()
        self.current_user = None
        
        # Politiques de sécurité
        self.min_password_length = 8
        self.session_duration = timedelta(hours=24)  # Session expire après 24h
        self.max_failed_attempts = 3
        self.lockout_duration = timedelta(minutes=3)
    
    def _load_users(self) -> Dict:
        """Charge la base de données des utilisateurs"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        return {
            "users": {},
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    
    def _save_users(self):
        """Sauvegarde la base de données des utilisateurs"""
        try:
            # Créer une sauvegarde avant modification
            if os.path.exists(self.users_file):
                backup_file = f"{self.users_file}.backup"
                import shutil
                shutil.copy2(self.users_file, backup_file)
            
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"{Colors.colorize('❌', Colors.BRIGHT_RED)} Erreur de sauvegarde: {e}")
    
    def _hash_password(self, password: str, salt: str = None) -> Tuple[str, str]:
        """Hash un mot de passe avec salt"""
        if salt is None:
            salt = secrets.token_hex(32)
        
        # Utilisation de PBKDF2 avec SHA-256 (plus sécurisé que SHA simple)
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 100k iterations
        )
        
        return password_hash.hex(), salt
    
    def _validate_email(self, email: str) -> bool:
        """Valide le format d'un email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _validate_password_strength(self, password: str) -> Tuple[bool, str]:
        """Valide la force d'un mot de passe"""
        if len(password) < self.min_password_length:
            return False, f"Le mot de passe doit contenir au moins {self.min_password_length} caractères"
        
        checks = {
            "majuscule": any(c.isupper() for c in password),
            "minuscule": any(c.islower() for c in password),
            "chiffre": any(c.isdigit() for c in password),
            "caractère spécial": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        }
        
        missing = [name for name, present in checks.items() if not present]
        
        if len(missing) > 1:
            return False, f"Le mot de passe doit contenir : {', '.join(missing)}"
        
        return True, "Mot de passe valide"
    
    def _is_user_locked(self, email: str) -> bool:
        """Vérifie si un utilisateur est temporairement bloqué"""
        if email not in self.users_data["users"]:
            return False
        
        user = self.users_data["users"][email]
        failed_attempts = user.get("failed_attempts", 0)
        last_failed = user.get("last_failed_attempt")
        
        if failed_attempts >= self.max_failed_attempts and last_failed:
            last_failed_time = datetime.fromisoformat(last_failed)
            if datetime.now() - last_failed_time < self.lockout_duration:
                return True
        
        return False
    
    def _reset_failed_attempts(self, email: str):
        """Remet à zéro les tentatives échouées"""
        if email in self.users_data["users"]:
            self.users_data["users"][email]["failed_attempts"] = 0
            self.users_data["users"][email].pop("last_failed_attempt", None)
    
    def _increment_failed_attempts(self, email: str):
        """Incrémente les tentatives échouées"""
        if email not in self.users_data["users"]:
            return
        
        user = self.users_data["users"][email]
        user["failed_attempts"] = user.get("failed_attempts", 0) + 1
        user["last_failed_attempt"] = datetime.now().isoformat()
    
    def register_user(self, email: str, password: str, full_name: str) -> Tuple[bool, str]:
        """Inscription d'un nouvel utilisateur"""
        
        # Validation email
        if not self._validate_email(email):
            return False, "Format d'email invalide"
        
        # Vérifier si l'utilisateur existe déjà
        if email.lower() in self.users_data["users"]:
            return False, "Un compte existe déjà avec cet email"
        
        # Validation du mot de passe
        is_valid, message = self._validate_password_strength(password)
        if not is_valid:
            return False, message
        
        # Validation du nom complet
        if not full_name.strip() or len(full_name.strip()) < 2:
            return False, "Le nom complet doit contenir au moins 2 caractères"
        
        # Hash du mot de passe
        password_hash, salt = self._hash_password(password)
        
        # Création du profil utilisateur
        user_profile = {
            "email": email.lower(),
            "full_name": full_name.strip(),
            "password_hash": password_hash,
            "salt": salt,
            "created_at": datetime.now().isoformat(),
            "last_login": None,
            "failed_attempts": 0,
            "is_active": True,
            "progress_file": os.path.expanduser(f"~/.educode_progress_{hashlib.md5(email.lower().encode()).hexdigest()}.json")
        }
        
        # Sauvegarde
        self.users_data["users"][email.lower()] = user_profile
        self._save_users()
        
        return True, "Compte créé avec succès"
    
    def login_user(self, email: str, password: str) -> Tuple[bool, str]:
        """Connexion utilisateur"""

        import time

        email = email.lower()

        # Vérifier si l'utilisateur est bloqué
        if self._is_user_locked(email):
            last_failed = datetime.fromisoformat(self.users_data["users"][email]["last_failed_attempt"])
            remaining = self.lockout_duration - (datetime.now() - last_failed)
            remaining_seconds = int(remaining.total_seconds())

            print(Colors.colorize("⚠️ Compte temporairement bloqué. Chronomètre de déblocage :", Colors.BRIGHT_RED, bold=True))
            while remaining_seconds > 0:
                mins, secs = divmod(remaining_seconds, 60)
                timer_text = f"\r⏱ Réessayez dans {mins:02d}:{secs:02d}"
                print(Colors.colorize(timer_text, Colors.BRIGHT_RED, bold=True), end="")
                time.sleep(1)
                remaining_seconds -= 1
            print("\nVous pouvez maintenant réessayer de vous connecter.")
            return False, "Compte débloqué, veuillez réessayer"

        # Vérifier si l'utilisateur existe
        if email not in self.users_data["users"]:
            return False, "Email ou mot de passe incorrect"

        user = self.users_data["users"][email]

        # Vérifier si le compte est actif
        if not user.get("is_active", True):
            return False, "Compte désactivé"

        # Vérifier le mot de passe
        password_hash, _ = self._hash_password(password, user["salt"])

        if password_hash == user["password_hash"]:
            # Connexion réussie
            user["last_login"] = datetime.now().isoformat()
            self._reset_failed_attempts(email)
            self.current_user = user
            self._create_session(email)
            self._save_users()
            return True, "Connexion réussie"
        else:
            # Échec de connexion
            self._increment_failed_attempts(email)
            self._save_users()
            return False, "Email ou mot de passe incorrect"

    
    def _create_session(self, email: str):
        """Crée une session utilisateur"""
        session_data = {
            "email": email,
            "login_time": datetime.now().isoformat(),
            "expires_at": (datetime.now() + self.session_duration).isoformat(),
            "session_token": secrets.token_urlsafe(32)
        }
        
        try:
            with open(self.session_file, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2)
        except Exception as e:
            print(f"Erreur lors de la création de session: {e}")
    
    def check_session(self) -> bool:
        """Vérifie si une session valide existe"""
        if not os.path.exists(self.session_file):
            return False
        
        try:
            with open(self.session_file, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            expires_at = datetime.fromisoformat(session_data["expires_at"])
            
            if datetime.now() > expires_at:
                # Session expirée
                os.remove(self.session_file)
                return False
            
            # Charger l'utilisateur de la session
            email = session_data["email"]
            if email in self.users_data["users"]:
                self.current_user = self.users_data["users"][email]
                return True
            
        except (json.JSONDecodeError, KeyError, ValueError):
            # Session corrompue
            try:
                os.remove(self.session_file)
            except:
                pass
        
        return False
    
    def logout_user(self):
        """Déconnexion utilisateur"""
        self.current_user = None
        try:
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
        except:
            pass
    
    def get_current_user(self) -> Optional[Dict]:
        """Retourne l'utilisateur actuellement connecté"""
        return self.current_user
    
    def get_user_progress_file(self) -> str:
        """Retourne le chemin du fichier de progression de l'utilisateur connecté"""
        if self.current_user:
            return self.current_user["progress_file"]
        return os.path.expanduser("~/.educode_progress.json")  # Fallback
    
    def change_password(self, current_password: str, new_password: str) -> Tuple[bool, str]:
        """Change le mot de passe de l'utilisateur connecté"""
        if not self.current_user:
            return False, "Aucun utilisateur connecté"
        
        # Vérifier l'ancien mot de passe
        password_hash, _ = self._hash_password(current_password, self.current_user["salt"])
        if password_hash != self.current_user["password_hash"]:
            return False, "Mot de passe actuel incorrect"
        
        # Valider le nouveau mot de passe
        is_valid, message = self._validate_password_strength(new_password)
        if not is_valid:
            return False, message
        
        # Hash du nouveau mot de passe
        new_password_hash, new_salt = self._hash_password(new_password)
        
        # Mise à jour
        email = self.current_user["email"]
        self.users_data["users"][email]["password_hash"] = new_password_hash
        self.users_data["users"][email]["salt"] = new_salt
        self.current_user = self.users_data["users"][email]
        self._save_users()
        
        return True, "Mot de passe changé avec succès"
    
    def get_user_stats(self) -> Dict:
        """Retourne les statistiques de l'utilisateur connecté"""
        if not self.current_user:
            return {}
        
        return {
            "name": self.current_user["full_name"],
            "email": self.current_user["email"],
            "member_since": datetime.fromisoformat(self.current_user["created_at"]).strftime("%d/%m/%Y"),
            "last_login": datetime.fromisoformat(self.current_user["last_login"]).strftime("%d/%m/%Y à %H:%M") if self.current_user["last_login"] else "Jamais"
        }

class AuthenticatedEduCode:
    """Interface d'authentification pour EduCode"""
    
    def __init__(self):
        self.auth = AuthenticationManager()
        self.educode_instance = None
    
    def show_welcome_screen(self):
        """Écran de bienvenue avec options d'authentification"""
        print()
        print(Colors.colorize("🔐 SYSTÈME D'AUTHENTIFICATION EDUCODE", Colors.BRIGHT_CYAN, bold=True))
        print(Colors.colorize("═" * 50, Colors.BRIGHT_BLUE))
        print()
        print(Colors.colorize("🎓 Bienvenue dans EduCode !", Colors.BRIGHT_YELLOW, bold=True))
        print(Colors.colorize("   Votre plateforme d'apprentissage Python sécurisée", Colors.BRIGHT_WHITE))
        print()
        
        # Vérifier s'il y a une session active
        if self.auth.check_session():
            user = self.auth.get_current_user()
            print(Colors.colorize(f"👋 Bon retour, {user['full_name']} !", Colors.BRIGHT_GREEN, bold=True))
            print(Colors.colorize(f"📧 Connecté en tant que: {user['email']}", Colors.BRIGHT_BLACK))
            
            choice = input(f"\n{Colors.colorize('Continuer avec ce compte ? (o/n):', Colors.BRIGHT_CYAN, bold=True)} ").strip().lower()
            
            if choice in ['o', 'oui', 'y', 'yes', '']:
                return self._start_educode_session()
            else:
                self.auth.logout_user()
        
        # Menu principal d'authentification
        while True:
            self._show_auth_menu()
            choice = input(f"\n{Colors.colorize('👉 Votre choix (1-4):', Colors.BRIGHT_CYAN, bold=True)} ").strip()
            
            if choice == "1":
                if self._handle_login():
                    return self._start_educode_session()
            elif choice == "2":
                self._handle_registration()
            elif choice == "3":
                self._show_help()
            elif choice == "4":
                print(f"\n{Colors.colorize('👋 Au revoir !', Colors.BRIGHT_YELLOW, bold=True)}")
                return False
            else:
                print(f"\n{Colors.colorize('❌ Choix invalide. Veuillez entrer 1, 2, 3 ou 4.', Colors.BRIGHT_RED)}")
    
    def _show_auth_menu(self):
        """Affiche le menu d'authentification"""
        print(f"\n{Colors.colorize('🔑 Authentification', Colors.BRIGHT_MAGENTA, bold=True)}")
        print(Colors.colorize("─" * 30, Colors.BRIGHT_BLACK))
        
        menu_options = [
            ("1", "🔓 Se connecter", "Accéder à votre compte", Colors.BRIGHT_GREEN),
            ("2", "📝 S'inscrire", "Créer un nouveau compte", Colors.BRIGHT_BLUE),
            ("3", "❓ Aide", "Informations et support", Colors.BRIGHT_YELLOW),
            ("4", "🚪 Quitter", "Fermer l'application", Colors.BRIGHT_RED)
        ]
        
        for number, title, description, color in menu_options:
            print(f"  {Colors.colorize(number + '.', color, bold=True)} "
                  f"{Colors.colorize(title, Colors.BRIGHT_WHITE, bold=True)}")
            print(f"     {Colors.colorize(description, Colors.BRIGHT_BLACK)}")
    
    def _handle_login(self) -> bool:
        """Gère la connexion utilisateur"""
        print(f"\n{Colors.colorize('🔓 CONNEXION', Colors.BRIGHT_GREEN, bold=True)}")
        print(Colors.colorize("─" * 20, Colors.BRIGHT_BLACK))
        
        try:
            email = input(f"{Colors.colorize('📧 Email:', Colors.BRIGHT_CYAN)} ").strip()
            if not email:
                print(f"{Colors.colorize('❌ Email requis', Colors.BRIGHT_RED)}")
                return False
            
            # Masquer le mot de passe (simulation - en réalité utiliser getpass)
            import getpass
            try:
                password = getpass.getpass(f"{Colors.colorize('🔑 Mot de passe:', Colors.BRIGHT_CYAN)} ")
            except KeyboardInterrupt:
                print(f"\n{Colors.colorize('❌ Connexion annulée', Colors.BRIGHT_YELLOW)}")
                return False
            
            if not password:
                print(f"{Colors.colorize('❌ Mot de passe requis', Colors.BRIGHT_RED)}")
                return False
            
            success, message = self.auth.login_user(email, password)
            
            if success:
                user = self.auth.get_current_user()
                print(f"\n{Colors.colorize('✅ ' + message, Colors.BRIGHT_GREEN, bold=True)}")
                print(Colors.colorize(f"👋 Bienvenue, {user['full_name']} !", Colors.BRIGHT_YELLOW, bold=True))
                return True
            else:
                print(f"\n{Colors.colorize('❌ ' + message, Colors.BRIGHT_RED, bold=True)}")
                return False
                
        except KeyboardInterrupt:
            print(f"\n{Colors.colorize('❌ Connexion annulée', Colors.BRIGHT_YELLOW)}")
            return False
    
    def _handle_registration(self):
        """Gère l'inscription utilisateur"""
        print(f"\n{Colors.colorize('📝 INSCRIPTION', Colors.BRIGHT_BLUE, bold=True)}")
        print(Colors.colorize("─" * 25, Colors.BRIGHT_BLACK))
        print(f"{Colors.colorize('✨ Créons votre compte EduCode !', Colors.BRIGHT_CYAN)}")
        print()
        
        try:
            # Nom complet
            full_name = input(f"{Colors.colorize('👤 Nom complet:', Colors.BRIGHT_CYAN)} ").strip()
            if not full_name:
                print(f"{Colors.colorize('❌ Nom requis', Colors.BRIGHT_RED)}")
                return
            
            # Email
            email = input(f"{Colors.colorize('📧 Email:', Colors.BRIGHT_CYAN)} ").strip()
            if not email:
                print(f"{Colors.colorize('❌ Email requis', Colors.BRIGHT_RED)}")
                return
            
            # Mot de passe avec confirmation
            import getpass
            print(f"\n{Colors.colorize('🔒 Sécurité du mot de passe:', Colors.BRIGHT_YELLOW)}")
            print(f"• {Colors.colorize('Au moins 8 caractères', Colors.BRIGHT_WHITE)}")
            print(f"• {Colors.colorize('Majuscules et minuscules', Colors.BRIGHT_WHITE)}")
            print(f"• {Colors.colorize('Au moins un chiffre', Colors.BRIGHT_WHITE)}")
            print(f"• {Colors.colorize('Au moins un caractère spécial', Colors.BRIGHT_WHITE)}")
            
            password = getpass.getpass(f"\n{Colors.colorize('🔑 Mot de passe:', Colors.BRIGHT_CYAN)} ")
            if not password:
                print(f"{Colors.colorize('❌ Mot de passe requis', Colors.BRIGHT_RED)}")
                return
            
            password_confirm = getpass.getpass(f"{Colors.colorize('🔑 Confirmez le mot de passe:', Colors.BRIGHT_CYAN)} ")
            
            if password != password_confirm:
                print(f"\n{Colors.colorize('❌ Les mots de passe ne correspondent pas', Colors.BRIGHT_RED)}")
                return
            
            # Inscription
            success, message = self.auth.register_user(email, password, full_name)
            
            if success:
                print(f"\n{Colors.colorize('🎉 ' + message, Colors.BRIGHT_GREEN, bold=True)}")
                print(f"{Colors.colorize('💡 Vous pouvez maintenant vous connecter avec vos identifiants', Colors.BRIGHT_CYAN)}")
            else:
                print(f"\n{Colors.colorize('❌ ' + message, Colors.BRIGHT_RED, bold=True)}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.colorize('❌ Inscription annulée', Colors.BRIGHT_YELLOW)}")
    
    def _show_help(self):
        """Affiche l'aide du système d'authentification"""
        print(f"\n{Colors.colorize('❓ AIDE EDUCODE', Colors.BRIGHT_YELLOW, bold=True)}")
        print(Colors.colorize("═" * 40, Colors.BRIGHT_BLUE))
        
        help_sections = [
            {
                "title": "🔐 Sécurité",
                "items": [
                    "Vos mots de passe sont chiffrés avec PBKDF2",
                    "Sessions automatiquement expirées après 24h",
                    "Protection contre les attaques par force brute",
                    "Fichiers de progression individuels sécurisés"
                ]
            },
            {
                "title": "📝 Inscription",
                "items": [
                    "Email valide requis (sera votre identifiant)",
                    "Mot de passe fort obligatoire (8+ caractères)",
                    "Nom complet pour vos certificats",
                    "Création automatique de votre profil de progression"
                ]
            },
            {
                "title": "🔓 Connexion",
                "items": [
                    "Utilisez votre email et mot de passe",
                    "3 tentatives maximum avant blocage temporaire",
                    "Session sauvegardée pour reconnexion automatique",
                    "Déconnexion automatique après 24h d'inactivité"
                ]
            },
            {
                "title": "🏆 Certification",
                "items": [
                    "Seuls les utilisateurs authentifiés peuvent obtenir des certificats",
                    "Certificats personnalisés avec votre nom complet",
                    "Horodatage sécurisé de vos accomplissements",
                    "Validation de l'identité pour les employeurs"
                ]
            }
        ]
        
        for section in help_sections:
            print(f"\n{Colors.colorize(section['title'], Colors.BRIGHT_MAGENTA, bold=True)}")
            for item in section['items']:
                print(f"  • {Colors.colorize(item, Colors.BRIGHT_WHITE)}")
        
        print(f"\n{Colors.colorize('💌 Support:', Colors.BRIGHT_CYAN, bold=True)} contact@educode.dev")
        print(f"{Colors.colorize('🌐 Site web:', Colors.BRIGHT_CYAN, bold=True)} https://educode.dev")
    
    def _start_educode_session(self):
        """Démarre une session EduCode authentifiée"""
        from .core import EduCode
        
        # Modifier la classe EduCode pour utiliser le fichier de progression spécifique à l'utilisateur
        class AuthenticatedEduCodeSession(EduCode):
            def __init__(self, auth_manager):
                self.auth_manager = auth_manager
                self.exercises = {}
                self.progress_file = auth_manager.get_user_progress_file()
                self.progress = self._load_progress()
                self.is_authenticated = True  # Toujours vrai puisque l'utilisateur est authentifié
                self._load_exercises()
            
            def display_stats(self):
                # Afficher les infos utilisateur d'abord
                user_stats = self.auth_manager.get_user_stats()
                
                print(f"\n{Colors.colorize('👤 PROFIL UTILISATEUR', Colors.BRIGHT_CYAN, bold=True)}")
                print(Colors.colorize("─" * 30, Colors.BRIGHT_BLACK))
                print(f"{Colors.colorize('Nom:', Colors.BRIGHT_WHITE, bold=True)} {Colors.colorize(user_stats['name'], Colors.BRIGHT_GREEN, bold=True)}")
                print(f"{Colors.colorize('Email:', Colors.BRIGHT_WHITE, bold=True)} {Colors.colorize(user_stats['email'], Colors.BRIGHT_CYAN)}")
                print(f"{Colors.colorize('Membre depuis:', Colors.BRIGHT_WHITE, bold=True)} {Colors.colorize(user_stats['member_since'], Colors.BRIGHT_YELLOW)}")
                print(f"{Colors.colorize('Dernière connexion:', Colors.BRIGHT_WHITE, bold=True)} {Colors.colorize(user_stats['last_login'], Colors.BRIGHT_MAGENTA)}")
                
                # Afficher les stats de progression normales
                super().display_stats()
            
            def generate_certificate_pdf(self, user_name: str = None):
                # Utiliser automatiquement le nom de l'utilisateur authentifié
                if not user_name:
                    user_stats = self.auth_manager.get_user_stats()
                    user_name = user_stats['name']
                
                super().generate_certificate_pdf(user_name)
            
            def interactive_mode(self):
                # Ajouter des options d'authentification au menu
                original_interactive_mode = super().interactive_mode
                
                print(Colors.colorize("Système d'exercices interactifs pour apprendre Python", Colors.BRIGHT_CYAN))
                user = self.auth_manager.get_current_user()
                print(f"{Colors.colorize('👤 Connecté:', Colors.BRIGHT_GREEN)} {Colors.colorize(user['full_name'], Colors.BRIGHT_WHITE, bold=True)}")
                self._print_separator("═", Colors.BRIGHT_BLUE)
                
                while True:
                    try:
                        print(f"\n{Colors.colorize('🎯 Menu Principal', Colors.BRIGHT_MAGENTA, bold=True)}")
                        self._print_separator("─", Colors.BRIGHT_BLACK)
                        
                        menu_options = [
                            ("1", "🎲 Exercice aléatoire", "Choisir un exercice au hasard", Colors.BRIGHT_GREEN),
                            ("2", "📈 Exercice par difficulté", "Facile, Moyen ou Difficile", Colors.BRIGHT_YELLOW),
                            ("3", "📚 Exercice par catégorie", "Fonctions, Listes, Algorithmes...", Colors.BRIGHT_CYAN),
                            ("4", "📊 Mes statistiques", "Voir votre progression", Colors.BRIGHT_BLUE),
                            ("5", "🔄 Reprendre un exercice", "Continuer où vous en étiez", Colors.BRIGHT_MAGENTA),
                            ("6", "🏆 Générer certificat", "Créer votre certificat PDF", Colors.BRIGHT_YELLOW),
                            ("7", "🔧 Paramètres compte", "Gérer votre compte", Colors.BRIGHT_WHITE),
                            ("8", "🚪 Se déconnecter", "Fermer votre session", Colors.BRIGHT_RED),
                            ("9", "👋 Quitter", "Fermer EduCode", Colors.BRIGHT_RED)
                        ]
                        
                        for number, title, description, color in menu_options:
                            print(f"  {Colors.colorize(number + '.', color, bold=True)} "
                                  f"{Colors.colorize(title, Colors.BRIGHT_WHITE, bold=True)}")
                            print(f"     {Colors.colorize(description, Colors.BRIGHT_BLACK)}")
                        
                        self._print_separator("─", Colors.BRIGHT_BLACK)
                        choice = input(f"{Colors.colorize('👉 Votre choix (1-9):', Colors.BRIGHT_CYAN, bold=True)} ").strip()
                        
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
                            self.generate_certificate_pdf()
                        elif choice == "7":
                            self._account_settings()
                        elif choice == "8":
                            print(f"\n{Colors.colorize('🔓 Déconnexion...', Colors.BRIGHT_YELLOW, bold=True)}")
                            self.auth_manager.logout_user()
                            print(f"{Colors.colorize('✅ Déconnexion réussie', Colors.BRIGHT_GREEN)}")
                            return False
                        elif choice == "9":
                            goodbye_msg = Colors.colorize('👋 Merci d\'avoir utilisé EduCode !', Colors.BRIGHT_YELLOW, bold=True)
                            continue_msg = Colors.colorize('🚀 Continuez à coder et à apprendre !', Colors.BRIGHT_CYAN)
                            print(f"\n{goodbye_msg}")
                            print(f"{continue_msg}")
                            return True
                        else:
                            print(f"{Colors.colorize('❌', Colors.BRIGHT_RED)} {Colors.colorize('Choix invalide.', Colors.BRIGHT_RED)} "
                                  f"{Colors.colorize('Veuillez entrer un nombre entre 1 et 9.', Colors.BRIGHT_WHITE)}")
                            
                    except KeyboardInterrupt:
                        print(f"\n\n{Colors.colorize('👋 Au revoir !', Colors.BRIGHT_YELLOW, bold=True)}")
                        return True
            
            def _account_settings(self):
                """Menu de gestion du compte utilisateur"""
                while True:
                    user_stats = self.auth_manager.get_user_stats()
                    
                    print(f"\n{Colors.colorize('🔧 PARAMÈTRES DU COMPTE', Colors.BRIGHT_WHITE, bold=True)}")
                    self._print_separator("─", Colors.BRIGHT_BLACK)
                    
                    print(f"{Colors.colorize('👤 Profil actuel:', Colors.BRIGHT_CYAN, bold=True)}")
                    print(f"   Nom: {Colors.colorize(user_stats['name'], Colors.BRIGHT_WHITE, bold=True)}")
                    print(f"   Email: {Colors.colorize(user_stats['email'], Colors.BRIGHT_CYAN)}")
                    print(f"   Membre depuis: {Colors.colorize(user_stats['member_since'], Colors.BRIGHT_YELLOW)}")
                    
                    print(f"\n{Colors.colorize('Options disponibles:', Colors.BRIGHT_MAGENTA, bold=True)}")
                    settings_options = [
                        ("1", "🔑 Changer le mot de passe", Colors.BRIGHT_YELLOW),
                        ("2", "📊 Exporter les données", Colors.BRIGHT_BLUE),
                        ("3", "🔄 Réinitialiser la progression", Colors.BRIGHT_RED),
                        ("4", "↩️  Retour au menu principal", Colors.BRIGHT_GREEN)
                    ]
                    
                    for number, title, color in settings_options:
                        print(f"  {Colors.colorize(number + '.', color, bold=True)} "
                              f"{Colors.colorize(title, Colors.BRIGHT_WHITE, bold=True)}")
                    
                    self._print_separator("─", Colors.BRIGHT_BLACK)
                    choice = input(f"{Colors.colorize('👉 Votre choix (1-4):', Colors.BRIGHT_CYAN, bold=True)} ").strip()
                    
                    if choice == "1":
                        self._change_password()
                    elif choice == "2":
                        self._export_data()
                    elif choice == "3":
                        self._reset_progress()
                    elif choice == "4":
                        break
                    else:
                        print(f"{Colors.colorize('❌ Choix invalide.', Colors.BRIGHT_RED)}")
            
            def _change_password(self):
                """Interface pour changer le mot de passe"""
                print(f"\n{Colors.colorize('🔑 CHANGEMENT DE MOT DE PASSE', Colors.BRIGHT_YELLOW, bold=True)}")
                self._print_separator("─", Colors.BRIGHT_BLACK)
                
                try:
                    import getpass
                    
                    current_password = getpass.getpass(f"{Colors.colorize('🔒 Mot de passe actuel:', Colors.BRIGHT_CYAN)} ")
                    if not current_password:
                        print(f"{Colors.colorize('❌ Operation annulée', Colors.BRIGHT_RED)}")
                        return
                    
                    new_password = getpass.getpass(f"{Colors.colorize('🆕 Nouveau mot de passe:', Colors.BRIGHT_CYAN)} ")
                    if not new_password:
                        print(f"{Colors.colorize('❌ Operation annulée', Colors.BRIGHT_RED)}")
                        return
                    
                    confirm_password = getpass.getpass(f"{Colors.colorize('✅ Confirmez le nouveau mot de passe:', Colors.BRIGHT_CYAN)} ")
                    
                    if new_password != confirm_password:
                        print(f"\n{Colors.colorize('❌ Les mots de passe ne correspondent pas', Colors.BRIGHT_RED)}")
                        return
                    
                    success, message = self.auth_manager.change_password(current_password, new_password)
                    
                    if success:
                        print(f"\n{Colors.colorize('✅ ' + message, Colors.BRIGHT_GREEN, bold=True)}")
                        print(f"{Colors.colorize('🔐 Votre compte est maintenant plus sécurisé !', Colors.BRIGHT_CYAN)}")
                    else:
                        print(f"\n{Colors.colorize('❌ ' + message, Colors.BRIGHT_RED, bold=True)}")
                        
                except KeyboardInterrupt:
                    print(f"\n{Colors.colorize('❌ Changement annulé', Colors.BRIGHT_YELLOW)}")
            
            def _export_data(self):
                """Exporte les données utilisateur"""
                print(f"\n{Colors.colorize('📊 EXPORT DES DONNÉES', Colors.BRIGHT_BLUE, bold=True)}")
                self._print_separator("─", Colors.BRIGHT_BLACK)
                
                try:
                    import json
                    from datetime import datetime
                    
                    # Compiler toutes les données utilisateur
                    user_stats = self.auth_manager.get_user_stats()
                    exercise_stats = self.get_stats()
                    
                    export_data = {
                        "user_info": user_stats,
                        "progress_stats": exercise_stats,
                        "completed_exercises": self.progress["completed"],
                        "failed_exercises": self.progress["failed"],
                        "export_date": datetime.now().isoformat(),
                        "export_version": "1.0"
                    }
                    
                    # Créer le nom de fichier
                    safe_email = user_stats['email'].replace('@', '_').replace('.', '_')
                    filename = f"educode_export_{safe_email}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    filepath = os.path.expanduser(f"~/Desktop/{filename}")
                    
                    # Sauvegarder
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(export_data, f, indent=2, ensure_ascii=False)
                    
                    print(f"✅ {Colors.colorize('Export réussi !', Colors.BRIGHT_GREEN, bold=True)}")
                    print(f"📁 {Colors.colorize('Fichier créé:', Colors.BRIGHT_WHITE)} {filepath}")
                    print(f"📊 {Colors.colorize('Contient:', Colors.BRIGHT_CYAN)} Profil, progression, exercices réussis")
                    
                except Exception as e:
                    error_msg = "Erreur lors de l'export:"
                    print(f"❌ {Colors.colorize(error_msg, Colors.BRIGHT_RED)} {str(e)}")
            
            def _reset_progress(self):
                """Réinitialise la progression avec confirmation multiple"""
                print(f"\n{Colors.colorize('🔄 RÉINITIALISATION DE LA PROGRESSION', Colors.BRIGHT_RED, bold=True)}")
                self._print_separator("─", Colors.BRIGHT_BLACK)
                
                print(f"{Colors.colorize('⚠️  ATTENTION:', Colors.BRIGHT_YELLOW, bold=True)} Cette action est irréversible !")
                print(f"{Colors.colorize('Toute votre progression sera perdue définitivement.', Colors.BRIGHT_RED)}")
                
                stats = self.get_stats()
                print(f"\n{Colors.colorize('📊 Progression actuelle:', Colors.BRIGHT_WHITE, bold=True)}")
                print(f"   • {stats['completed']} exercices réussis")
                print(f"   • {stats['total_attempts']} tentatives au total")
                print(f"   • {stats['success_rate']:.1f}% de taux de réussite")
                
                # Triple confirmation
                confirmations = [
                    "Êtes-vous absolument certain de vouloir réinitialiser votre progression ?",
                    "Cette action supprimera TOUS vos exercices réussis. Continuez ?",
                    "Dernière chance : confirmez-vous la réinitialisation complète ?"
                ]
                
                for i, question in enumerate(confirmations, 1):
                    print(f"\n{Colors.colorize(f'Confirmation {i}/3:', Colors.BRIGHT_YELLOW, bold=True)}")
                    answer = input(f"{Colors.colorize(question + ' (oui/non):', Colors.BRIGHT_RED)} ").strip().lower()
                    
                    if answer not in ['oui', 'yes']:
                        print(f"{Colors.colorize('✅ Réinitialisation annulée. Vos données sont préservées.', Colors.BRIGHT_GREEN, bold=True)}")
                        return
                
                # Réinitialisation effective
                try:
                    self.progress = {
                        "completed": [],
                        "failed": [],
                        "total_attempts": 0,
                        "total_success": 0,
                        "start_date": datetime.now().isoformat()
                    }
                    self._save_progress()
                    
                    print(f"\n{Colors.colorize('🔄 Progression réinitialisée avec succès', Colors.BRIGHT_GREEN, bold=True)}")
                    learning_message = "🚀 Vous pouvez recommencer votre parcours d'apprentissage !"
                    print(f"{Colors.colorize(learning_message, Colors.BRIGHT_CYAN)}")
                    
                except Exception as e:
                    print(f"\n{Colors.colorize('❌ Erreur lors de la réinitialisation:', Colors.BRIGHT_RED)} {str(e)}")
        
        # Créer et lancer la session authentifiée
        self.educode_instance = AuthenticatedEduCodeSession(self.auth)
        return self.educode_instance.interactive_mode()

def main_authenticated():
    """Point d'entrée principal avec authentification"""
    try:
        auth_system = AuthenticatedEduCode()
        success = auth_system.show_welcome_screen()
        return 0 if success else 1
    except KeyboardInterrupt:
        print(f"\n{Colors.colorize('👋 Au revoir !', Colors.BRIGHT_YELLOW, bold=True)}")
        return 0
    except Exception as e:
        print(f"{Colors.colorize('❌ Erreur système:', Colors.BRIGHT_RED)} {str(e)}")
        return 1