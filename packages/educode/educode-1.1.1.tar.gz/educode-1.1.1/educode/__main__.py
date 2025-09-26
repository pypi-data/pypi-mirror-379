# educode/__main__.py (version avec authentification)
"""Point d'entrée pour l'exécution en module (python -m educode)"""

import sys
import os
import shutil
from .auth import main_authenticated  # Import du système d'authentification
from .core import EduCode

# Conserver toutes les classes Colors et fonctions utilitaires existantes
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

def get_terminal_width():
    """Obtient la largeur du terminal"""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def print_banner():
    """Affiche une bannière colorée pour EduCode"""
    width = min(get_terminal_width(), 80)
    
    # Bannière principale
    banner_lines = [
        "███████╗██████╗ ██╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗",
        "██╔════╝██╔══██╗██║   ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝",
        "█████╗  ██║  ██║██║   ██║██║     ██║   ██║██║  ██║█████╗  ",
        "██╔══╝  ██║  ██║██║   ██║██║     ██║   ██║██║  ██║██╔══╝  ",
        "███████╗██████╔╝╚██████╔╝╚██████╗╚██████╔╝██████╔╝███████╗",
        "╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝"
    ]
    
    print()
    for line in banner_lines:
        if len(line) <= width:
            padding = (width - len(line)) // 2
            colored_line = Colors.colorize(line, Colors.BRIGHT_CYAN, bold=True)
            print(" " * padding + colored_line)
    
    # Sous-titre
    subtitle = "🐍 Système d'exercices interactifs pour apprendre Python 🚀"
    if len(subtitle) <= width:
        padding = (width - len(subtitle)) // 2
        print(" " * padding + Colors.colorize(subtitle, Colors.BRIGHT_YELLOW, bold=True))
    
    print(Colors.colorize("═" * width, Colors.BRIGHT_BLUE))
    print()

def print_colored_help():
    """Affiche l'aide avec des couleurs (mise à jour avec authentification)"""
    print_banner()
    
    sections = [
        {
            "title": "📋 Usage",
            "color": Colors.BRIGHT_GREEN,
            "content": [
                ("python -m educode", "Mode interactif authentifié", Colors.CYAN),
                ("python -m educode stats", "Afficher vos statistiques (nécessite connexion)", Colors.CYAN),
                ("python -m educode certificate", "Générer certificat (utilisateurs authentifiés)", Colors.CYAN),
                ("python -m educode help", "Afficher cette aide", Colors.CYAN),
                ("python -m educode version", "Afficher la version", Colors.CYAN),
                ("python -m educode demo", "Mode démo sans authentification", Colors.BRIGHT_YELLOW)
            ]
        },
        {
            "title": "🔐 Authentification",
            "color": Colors.BRIGHT_RED,
            "content": [
                ("🛡️ Sécurisé", "Mots de passe chiffrés PBKDF2", Colors.GREEN),
                ("👤 Profils individuels", "Progression personnalisée", Colors.BLUE),
                ("🏆 Certification validée", "Certificats avec nom authentifié", Colors.CYAN),
                ("🔒 Sessions sécurisées", "Expiration automatique 24h", Colors.BRIGHT_WHITE),
                ("📊 Statistiques privées", "Données utilisateur protégées", Colors.BRIGHT_YELLOW)
            ]
        },
        {
            "title": "🏆 Système de certification",
            "color": Colors.BRIGHT_YELLOW,
            "content": [
                ("🌱 Apprenti Python", "Premiers exercices réussis", Colors.GREEN),
                ("📜 Développeur Intermédiaire", "25+ exercices, 60%+ réussite", Colors.BLUE),
                ("🥉 Développeur Confirmé", "50+ exercices, 75%+ réussite", Colors.CYAN),
                ("🥈 Développeur Avancé", "100+ exercices, 85%+ réussite", Colors.BRIGHT_WHITE),
                ("🏆 Expert Python", "150+ exercices, 95%+ réussite", Colors.BRIGHT_YELLOW)
            ]
        },
        {
            "title": "✨ Fonctionnalités",
            "color": Colors.BRIGHT_MAGENTA,
            "content": [
                ("📚 150+ exercices progressifs", "Facile → Moyen → Difficile", Colors.GREEN),
                ("🤖 Correction automatique", "Tests unitaires intégrés", Colors.GREEN),
                ("📊 Suivi personnalisé", "Progression sauvegardée par utilisateur", Colors.GREEN),
                ("🎯 Exercices ciblés", "Par catégorie et difficulté", Colors.GREEN),
                ("💡 Système d'aide", "Indices et templates inclus", Colors.GREEN)
            ]
        }
    ]
    
    for section in sections:
        print(Colors.colorize(section["title"], section["color"], bold=True))
        print(Colors.colorize("─" * 50, Colors.BRIGHT_BLACK))
        
        for item, description, color in section["content"]:
            print(f"  {Colors.colorize('•', Colors.BRIGHT_BLUE)} {Colors.colorize(item, color, bold=True)}")
            print(f"    {Colors.colorize(description, Colors.BRIGHT_BLACK)}")
        print()
    
    # Footer mis à jour
    footer_box = [
        "╭─────────────────────────────────────────────────────────────╮",
        "│              🔐 Pour commencer avec authentification        │",
        "│                                                             │",
        "│                   python -m educode                        │",
        "│                                                             │",
        "│              🎭 Pour le mode démo (sans compte)            │",
        "│                                                             │",
        "│                 python -m educode demo                     │",
        "│                                                             │",
        "│                    Bon apprentissage ! 🚀                  │",
        "╰─────────────────────────────────────────────────────────────╯"
    ]
    
    for line in footer_box:
        print(Colors.colorize(line, Colors.BRIGHT_GREEN))

def print_stats_header():
    """Affiche un en-tête coloré pour les statistiques"""
    print()
    header = "📊 VOS STATISTIQUES EDUCODE (AUTHENTIFICATION REQUISE)"
    width = get_terminal_width()
    
    print(Colors.colorize("╭" + "─" * (width - 2) + "╮", Colors.BRIGHT_CYAN))
    padding = max(0, (width - len(header) - 2) // 2)
    print(Colors.colorize("│" + " " * padding + header + " " * (width - len(header) - padding - 2) + "│", Colors.BRIGHT_CYAN, bold=True))
    print(Colors.colorize("╰" + "─" * (width - 2) + "╯", Colors.BRIGHT_CYAN))

def print_version():
    """Affiche la version avec style"""
    try:
        from . import __version__
        version = __version__
    except ImportError:
        version = "dev"
    
    print()
    version_art = [
        "██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗",
        "██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║",
        "██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║",
        "╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║",
        " ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║",
        "  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝"
    ]
    
    for line in version_art:
        print(Colors.colorize(line, Colors.BRIGHT_MAGENTA))
    
    print()
    print(Colors.colorize(f"🚀 EduCode version ", Colors.BRIGHT_WHITE, bold=True) + 
          Colors.colorize(version, Colors.BRIGHT_YELLOW, bold=True))
    print(Colors.colorize("🐍 Système d'apprentissage Python sécurisé", Colors.BRIGHT_CYAN))
    print(Colors.colorize("🔐 Avec authentification et certification validée", Colors.BRIGHT_GREEN))
    print()

def print_error(message):
    """Affiche un message d'erreur coloré"""
    error_symbol = Colors.colorize("❌", Colors.BRIGHT_RED)
    error_text = Colors.colorize("Erreur: ", Colors.BRIGHT_RED, bold=True)
    print(f"\n{error_symbol} {error_text}{message}")

def print_unknown_command(command):
    """Affiche un message pour une commande inconnue"""
    print()
    print(Colors.colorize("⚠️", Colors.BRIGHT_YELLOW) + 
          Colors.colorize(" Commande inconnue: ", Colors.BRIGHT_YELLOW, bold=True) + 
          Colors.colorize(command, Colors.BRIGHT_RED, bold=True))
    print()
    print(Colors.colorize("💡 Commandes disponibles:", Colors.BRIGHT_BLUE, bold=True))
    print(f"  • {Colors.colorize('python -m educode', Colors.BRIGHT_CYAN)} - Mode authentifié")
    print(f"  • {Colors.colorize('python -m educode stats', Colors.BRIGHT_CYAN)} - Statistiques (connexion requise)")  
    print(f"  • {Colors.colorize('python -m educode certificate', Colors.BRIGHT_CYAN)} - Certificat (connexion requise)")
    print(f"  • {Colors.colorize('python -m educode demo', Colors.BRIGHT_CYAN)} - Mode démo")
    print(f"  • {Colors.colorize('python -m educode help', Colors.BRIGHT_CYAN)} - Aide complète")
    print(f"  • {Colors.colorize('python -m educode version', Colors.BRIGHT_CYAN)} - Version")
    print()

def print_certificate_header():
    """Affiche un en-tête coloré pour la génération de certificat"""
    print()
    header = "🏆 GÉNÉRATION DE CERTIFICAT EDUCODE (AUTHENTIFICATION REQUISE)"
    width = get_terminal_width()
    
    print(Colors.colorize("╭" + "─" * (width - 2) + "╮", Colors.BRIGHT_YELLOW))
    padding = max(0, (width - len(header) - 2) // 2)
    print(Colors.colorize("│" + " " * padding + header + " " * (width - len(header) - padding - 2) + "│", Colors.BRIGHT_YELLOW, bold=True))
    print(Colors.colorize("╰" + "─" * (width - 2) + "╯", Colors.BRIGHT_YELLOW))

def run_demo_mode():
    """Mode démo sans authentification (fonctionnalité limitée)"""
    print()
    print(Colors.colorize("🎭 MODE DÉMO EDUCODE", Colors.BRIGHT_MAGENTA, bold=True))
    print(Colors.colorize("═" * 50, Colors.BRIGHT_BLUE))
    print()
    print(Colors.colorize("⚠️  ATTENTION:", Colors.BRIGHT_YELLOW, bold=True))
    print(Colors.colorize("• Progression non sauvegardée", Colors.BRIGHT_RED))
    print(Colors.colorize("• Certificats non disponibles", Colors.BRIGHT_RED))
    print(Colors.colorize("• Fonctionnalités limitées", Colors.BRIGHT_RED))
    print()
    print(Colors.colorize("💡 Pour l'expérience complète, créez un compte avec:", Colors.BRIGHT_CYAN))
    print(Colors.colorize("   python -m educode", Colors.BRIGHT_WHITE, bold=True))
    print()
    
    # Lancer EduCode en mode basique
    educode = EduCode()
    educode.interactive_mode()

def require_authentication():
    """Informe que l'authentification est requise"""
    print()
    print(Colors.colorize("🔐 AUTHENTIFICATION REQUISE", Colors.BRIGHT_RED, bold=True))
    print(Colors.colorize("═" * 40, Colors.BRIGHT_BLUE))
    print()
    print(Colors.colorize("Cette fonctionnalité nécessite une connexion.", Colors.BRIGHT_WHITE))
    print(Colors.colorize("Veuillez vous connecter pour accéder à:", Colors.BRIGHT_CYAN))
    print()
    print(f"  • {Colors.colorize('Statistiques personnalisées', Colors.BRIGHT_GREEN)}")
    print(f"  • {Colors.colorize('Certificats nominatifs', Colors.BRIGHT_YELLOW)}")
    print(f"  • {Colors.colorize('Sauvegarde de progression', Colors.BRIGHT_BLUE)}")
    print(f"  • {Colors.colorize('Profil utilisateur sécurisé', Colors.BRIGHT_MAGENTA)}")
    print()
    print(Colors.colorize("🚀 Pour vous connecter:", Colors.BRIGHT_WHITE, bold=True))
    print(f"   {Colors.colorize('python -m educode', Colors.BRIGHT_CYAN, bold=True)}")
    print()
    print(Colors.colorize("🎭 Pour tester sans compte (limité):", Colors.BRIGHT_BLACK))
    print(f"   {Colors.colorize('python -m educode demo', Colors.BRIGHT_BLACK)}")
    print()

def main():
    """Fonction principale avec gestion de l'authentification"""
    try:
        if len(sys.argv) > 1:
            command = sys.argv[1].lower()
            
            if command == "stats":
                require_authentication()
                return 1
                
            elif command == "certificate":
                require_authentication()
                return 1
                
            elif command == "version":
                print_version()
                
            elif command in ["help", "--help", "-h"]:
                print_colored_help()
                
            elif command == "demo":
                run_demo_mode()
                
            else:
                print_unknown_command(command)
                return 1
        else:
            # Mode authentifié par défaut
            if Colors.is_supported():
                print_banner()
                print(Colors.colorize("🔐 Lancement du système d'authentification...", Colors.BRIGHT_CYAN))
            else:
                print("🎓 EduCode - Système d'exercices Python avec authentification")
                print("=" * 60)
            
            return main_authenticated()
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.colorize('👋', Colors.BRIGHT_YELLOW)} " + 
              f"{Colors.colorize('Au revoir !', Colors.BRIGHT_WHITE, bold=True)}")
        return 0
    except Exception as e:
        print_error(f"Une erreur inattendue s'est produite: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())