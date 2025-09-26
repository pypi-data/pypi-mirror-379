# educode/certification.py
"""
Module de génération de certificats PDF professionnels pour EduCode
"""

import os
import subprocess
import sys
from datetime import datetime
from typing import Dict, Any, Optional

# educode/certification.py
"""
Module de génération de certificats sécurisés pour EduCode
Intégré au système d'authentification pour garantir l'authenticité
"""

class CertificationGenerator:
    """Générateur de certificats PDF professionnels pour EduCode"""
    
    def __init__(self):
        self.certificates_dir = os.path.expanduser("~/EduCode_Certificates")
        self.ensure_certificates_directory()
        self.reportlab_available = self._check_reportlab()
    
    def ensure_certificates_directory(self):
        """Crée le dossier des certificats s'il n'existe pas"""
        if not os.path.exists(self.certificates_dir):
            os.makedirs(self.certificates_dir)
    
    def _check_reportlab(self) -> bool:
        """Vérifie si reportlab est disponible"""
        try:
            import reportlab
            return True
        except ImportError:
            return False
    
    def _import_reportlab(self):
        """Importe les modules reportlab nécessaires"""
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.lib.colors import Color, black, white, grey, HexColor
            from reportlab.lib.units import inch, cm, mm
            from reportlab.platypus import Paragraph, Frame
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.graphics.shapes import Drawing, Rect, Circle
            from reportlab.graphics import renderPDF
            return canvas, A4, landscape, Color, black, white, grey, HexColor, inch, cm, mm, Paragraph, Frame, getSampleStyleSheet, ParagraphStyle, Drawing, Rect, Circle, renderPDF
        except ImportError as e:
            raise ImportError(f"Impossible d'importer reportlab: {e}")
    
    def install_reportlab(self) -> bool:
        """Installe reportlab si nécessaire"""
        if self.reportlab_available:
            return True
            
        try:
            print("📦 Installation de reportlab pour la génération de PDF...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "reportlab"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ reportlab installé avec succès !")
                self.reportlab_available = True
                return True
            else:
                print(f"❌ Échec de l'installation: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Erreur lors de l'installation: {e}")
            return False
    
    def get_certificate_level(self, stats: Dict[str, Any]) -> Dict[str, str]:
        """Détermine le niveau de certification basé sur les statistiques"""
        completion_rate = stats['completion_rate']
        success_rate = stats['success_rate']
        completed = stats['completed']
        
        if completion_rate >= 90 and success_rate >= 95 and completed >= 150:
            return {
                "level": "Expert Python",
                "level_en": "PYTHON EXPERT",
                "color": "#FFD700",  # Or
                "bg_color": "#FFF8DC",
                "description": "Maîtrise exceptionnelle de Python",
                "symbol": "★",
                "rank": "EXCELLENCE"
            }
        elif completion_rate >= 70 and success_rate >= 85 and completed >= 100:
            return {
                "level": "Développeur Python Avancé",
                "level_en": "ADVANCED PYTHON DEVELOPER",
                "color": "#C0C0C0",  # Argent
                "bg_color": "#F8F8FF",
                "description": "Excellente connaissance de Python",
                "symbol": "◆",
                "rank": "ADVANCED"
            }
        elif completion_rate >= 50 and success_rate >= 75 and completed >= 50:
            return {
                "level": "Développeur Python Confirmé",
                "level_en": "CONFIRMED PYTHON DEVELOPER",
                "color": "#CD7F32",  # Bronze
                "bg_color": "#FDF5E6",
                "description": "Bonne maîtrise des concepts Python",
                "symbol": "●",
                "rank": "CONFIRMED"
            }
        elif completion_rate >= 25 and success_rate >= 60 and completed >= 25:
            return {
                "level": "Développeur Python Intermédiaire",
                "level_en": "INTERMEDIATE PYTHON DEVELOPER",
                "color": "#4682B4",  # Bleu acier
                "bg_color": "#F0F8FF",
                "description": "Connaissance solide des bases Python",
                "symbol": "▲",
                "rank": "INTERMEDIATE"
            }
        else:
            return {
                "level": "Apprenti Python",
                "level_en": "PYTHON APPRENTICE",
                "color": "#87CEEB",  # Bleu ciel
                "bg_color": "#F0F8FF",
                "description": "",
                "symbol": "○",
                "rank": "APPRENTICE"
            }
    
    def _draw_centered_text(self, canvas_obj, x, y, text):
        """Dessine du texte centré à la position donnée"""
        text_width = canvas_obj.stringWidth(text, canvas_obj._fontname, canvas_obj._fontsize)
        canvas_obj.drawString(x - text_width / 2, y, text)
    
    def _draw_right_aligned_text(self, canvas_obj, x, y, text):
        """Dessine du texte aligné à droite"""
        text_width = canvas_obj.stringWidth(text, canvas_obj._fontname, canvas_obj._fontsize)
        canvas_obj.drawString(x - text_width, y, text)
    
    def _truncate_text_to_fit(self, canvas_obj, text, max_width, font_name, font_size):
        """Tronque le texte pour qu'il rentre dans la largeur donnée"""
        canvas_obj.setFont(font_name, font_size)
        text_width = canvas_obj.stringWidth(text, font_name, font_size)
        
        if text_width <= max_width:
            return text
        
        # Si le texte ne rentre pas, on le raccourcit
        while text_width > max_width and len(text) > 3:
            text = text[:-4] + "..."
            text_width = canvas_obj.stringWidth(text, font_name, font_size)
        
        return text
    
    def generate_certificate(self, user_name: str, stats: Dict[str, Any]) -> str:
        """Génère un certificat PDF professionnel"""
        # Installer reportlab si nécessaire
        if not self.install_reportlab():
            raise Exception("Impossible d'installer reportlab pour générer le PDF")
        
        # Importer les modules après installation
        try:
            canvas, A4, landscape, Color, black, white, grey, HexColor, inch, cm, mm, Paragraph, Frame, getSampleStyleSheet, ParagraphStyle, Drawing, Rect, Circle, renderPDF = self._import_reportlab()
        except ImportError as e:
            raise Exception(f"Erreur d'import reportlab: {e}")
        
        cert_info = self.get_certificate_level(stats)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = user_name.replace(' ', '_').replace('/', '_').replace('\\', '_')
        safe_level = cert_info['level'].replace(' ', '_').replace('/', '_')
        filename = f"EduCode_Certificate_{safe_name}_{safe_level}_{timestamp}.pdf"
        filepath = os.path.join(self.certificates_dir, filename)
        
        # Utiliser le format paysage pour plus d'espace
        page_width, page_height = landscape(A4)
        
        # Création du PDF
        c = canvas.Canvas(filepath, pagesize=landscape(A4))
        
        # Couleurs du thème
        primary_color = HexColor(cert_info['color'])
        bg_color = HexColor(cert_info['bg_color'])
        dark_grey = HexColor("#2C2C2C")
        light_grey = HexColor("#F5F5F5")
        
        # Arrière-plan avec dégradé simulé
        self._draw_background(c, page_width, page_height, bg_color, primary_color)
        
        # Bordure élégante
        self._draw_elegant_border(c, page_width, page_height, primary_color)
        
        # En-tête avec logo simulé
        self._draw_header(c, page_width, page_height, primary_color, dark_grey, white)
        
        # Titre principal (très réduit)
        c.setFont("Helvetica-Bold", 28)  # Réduit de 40 à 28
        c.setFillColor(primary_color)
        self._draw_centered_text(c, page_width/2, page_height - 145, "CERTIFICAT DE RÉUSSITE")
        
        # Sous-titre anglais (très réduit)
        c.setFont("Helvetica", 10)  # Réduit de 14 à 10
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, page_width/2, page_height - 165, "CERTIFICATE OF ACHIEVEMENT")
        
        # Séparateur décoratif (réduit)
        self._draw_decorative_line(c, page_width/2 - 100, page_height - 185, 200, primary_color)
        
        # Texte d'introduction (très réduit)
        c.setFont("Helvetica", 12)  # Réduit de 16 à 12
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, page_width/2, page_height - 210, "Cette certification atteste que M. / Mme")
        
        # Nom de l'utilisateur avec style
        self._draw_name_section(c, page_width/2, page_height - 240, user_name, primary_color)
        
        # Niveau atteint (très réduit)
        c.setFont("Helvetica", 12)  # Réduit de 16 à 12
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, page_width/2, page_height - 270, "a démontré ses compétences et obtenu le niveau")
        
        # Badge de niveau
        self._draw_level_badge(c, page_width/2, page_height - 320, cert_info, primary_color, dark_grey)
        
        # Description du niveau (très réduit)
        c.setFont("Helvetica-Oblique", 10)  # Réduit de 14 à 10
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, page_width/2, page_height - 360, cert_info['description'])
        
        # Statistiques en colonnes
        self._draw_statistics_section(c, page_width, page_height - 395, stats, primary_color, dark_grey)
        
        # Pied de page avec informations officielles
        self._draw_footer(c, page_width, page_height, primary_color, dark_grey, white, timestamp, user_name)
        
        c.save()
        return filepath
    
    def _draw_background(self, c, width, height, bg_color, primary_color):
        """Dessine un arrière-plan élégant (réduit)"""
        # Fond principal
        c.setFillColor(bg_color)
        c.rect(0, 0, width, height, fill=1, stroke=0)
        
        # Motifs décoratifs subtils dans les coins (très réduits)
        c.setFillColor(primary_color)
        c.setFillAlpha(0.05)  # Transparence réduite de 0.1 à 0.05
        
        # Coin supérieur gauche (réduit)
        c.circle(40, height - 40, 60, fill=1, stroke=0)  # Rayon réduit de 100 à 60
        # Coin inférieur droit (réduit)
        c.circle(width - 40, 40, 60, fill=1, stroke=0)  # Rayon réduit de 100 à 60
        
        c.setFillAlpha(1)  # Rétablir l'opacité
    
    def _draw_elegant_border(self, c, width, height, primary_color):
        """Dessine une bordure élégante (réduite)"""
        # Bordure principale (épaisseur réduite)
        c.setStrokeColor(primary_color)
        c.setLineWidth(2)  # Réduit de 3 à 2
        c.rect(30, 30, width - 60, height - 60, fill=0, stroke=1)  # Marges réduites
        
        # Bordure intérieure fine
        c.setStrokeColor(primary_color)
        c.setLineWidth(1)
        c.rect(35, 35, width - 70, height - 70, fill=0, stroke=1)  # Marges réduites
        
        # Coins décoratifs (très réduits)
        corner_size = 8  # Réduit de 15 à 8
        corners = [
            (45, height - 55),  # Haut gauche
            (width - 55, height - 55),  # Haut droite
            (45, 45),  # Bas gauche
            (width - 55, 45)  # Bas droite
        ]
        
        c.setFillColor(primary_color)
        for x, y in corners:
            c.rect(x, y, corner_size, corner_size, fill=1, stroke=0)
    
    def _draw_header(self, c, width, height, primary_color, dark_grey, white):
        """Dessine l'en-tête avec logo simulé (réduit)"""
        # Logo simulé (cercle avec texte) - taille réduite
        logo_x, logo_y = 80, height - 80  # Position ajustée
        c.setFillColor(primary_color)
        c.circle(logo_x, logo_y, 18, fill=1, stroke=0)  # Rayon réduit de 25 à 18
        
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 12)  # Réduit de 16 à 12
        self._draw_centered_text(c, logo_x, logo_y - 4, "E")
        
        # Nom de l'organisation (très réduit)
        c.setFont("Helvetica-Bold", 10)  # Réduit de 14 à 10
        c.setFillColor(dark_grey)
        c.drawString(logo_x + 25, logo_y + 3, "EDUCODE")  # Position ajustée
        
        c.setFont("Helvetica", 7)  # Réduit de 10 à 7
        c.drawString(logo_x + 25, logo_y - 8, "Learning Platform")  # Position ajustée
        
        # Date en haut à droite (réduite)
        date_str = datetime.now().strftime("%d/%m/%Y")
        c.setFont("Helvetica", 9)  # Réduit de 12 à 9
        c.setFillColor(dark_grey)
        self._draw_right_aligned_text(c, width - 60, height - 75, f"Délivré le {date_str}")
    
    def _draw_decorative_line(self, c, x, y, length, color):
        """Dessine une ligne décorative (réduite)"""
        c.setStrokeColor(color)
        c.setLineWidth(1)  # Réduit de 2 à 1
        c.line(x, y, x + length, y)
        
        # Points décoratifs aux extrémités (très réduits)
        c.setFillColor(color)
        c.circle(x, y, 2, fill=1, stroke=0)  # Rayon réduit de 3 à 2
        c.circle(x + length, y, 2, fill=1, stroke=0)  # Rayon réduit de 3 à 2
    
    def _draw_name_section(self, c, x, y, name, primary_color):
        """Dessine la section nom avec style (très réduite)"""
        # Dimensions du fond réduites
        name_bg_width = 320  # Réduit de 350 à 320
        name_bg_height = 30  # Réduit de 35 à 30
        
        c.setFillColor(primary_color)
        c.setFillAlpha(0.08)  # Réduit de 0.1 à 0.08
        c.rect(x - name_bg_width/2, y - name_bg_height/2, name_bg_width, name_bg_height, fill=1, stroke=0)
        c.setFillAlpha(1)
        
        # Bordure du nom (épaisseur réduite)
        c.setStrokeColor(primary_color)
        c.setLineWidth(1)  # Réduit de 2 à 1
        c.rect(x - name_bg_width/2, y - name_bg_height/2, name_bg_width, name_bg_height, fill=0, stroke=1)
        
        # Nom en gras avec vérification de la taille (très réduit)
        font_size = 20  # Réduit de 22 à 20
        max_width = name_bg_width - 12  # Marge intérieure réduite
        
        # Tronquer le nom si nécessaire
        display_name = self._truncate_text_to_fit(c, name.upper(), max_width, "Helvetica-Bold", font_size)
        
        c.setFont("Helvetica-Bold", font_size)
        c.setFillColor(primary_color)
        self._draw_centered_text(c, x, y - 5, display_name)  # Position ajustée
    
    def _draw_level_badge(self, c, x, y, cert_info, primary_color, dark_grey):
        """Dessine le badge de niveau professionnel (très réduit)"""
        # Cercle de fond pour le badge (très réduit)
        badge_radius = 30  # Réduit de 35 à 30
        c.setFillColor(primary_color)
        c.setFillAlpha(0.15)  # Légèrement augmenté pour compensation
        c.circle(x, y, badge_radius, fill=1, stroke=0)
        c.setFillAlpha(1)
        
        # Bordure du badge (épaisseur réduite)
        c.setStrokeColor(primary_color)
        c.setLineWidth(2)  # Réduit de 3 à 2
        c.circle(x, y, badge_radius, fill=0, stroke=1)
        
        # Symbole au centre (très réduit)
        c.setFont("Helvetica-Bold", 18)  # Réduit de 20 à 18
        c.setFillColor(primary_color)
        self._draw_centered_text(c, x, y - 4, cert_info['symbol'])
        
        # Nom du niveau en dessous avec ajustement dynamique (très réduit)
        level_text = cert_info['level']
        max_level_width = 220  # Réduit de 250 à 220
        
        if len(level_text) > 25:  # Si le texte est très long
            font_size = 9  # Réduit de 10 à 9
        elif len(level_text) > 20:  # Si le texte est long
            font_size = 11  # Réduit de 12 à 11
        else:
            font_size = 13  # Réduit de 14 à 13
        
        # Tronquer si nécessaire
        display_level = self._truncate_text_to_fit(c, level_text, max_level_width, "Helvetica-Bold", font_size)
        
        c.setFont("Helvetica-Bold", font_size)
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, x, y - 48, display_level)  # Réduit de -60 à -48
        
        # Rank en anglais (très réduit)
        c.setFont("Helvetica", 6)  # Réduit de 7 à 6
        c.setFillColor(primary_color)
        self._draw_centered_text(c, x, y - 60, cert_info['rank'])  # Réduit de -75 à -60
    
    def _draw_statistics_section(self, c, width, y, stats, primary_color, dark_grey):
        """Dessine les statistiques en colonnes élégantes (très réduites)"""
        # Titre de la section (très réduit)
        c.setFont("Helvetica-Bold", 9)  # Réduit de 10 à 9
        c.setFillColor(dark_grey)
        self._draw_centered_text(c, width/2, y, "PERFORMANCES ET STATISTIQUES")
        
        # Ligne sous le titre (très réduite)
        line_y = y - 8  # Espacement augmenté de -4 à -8
        c.setStrokeColor(primary_color)
        c.setLineWidth(1)
        c.line(width/2 - 50, line_y, width/2 + 50, line_y)  # Ligne encore plus courte
        
        # Colonnes de statistiques (très réduites)
        col_width = 110  # Réduit de 120 à 110
        col_height = 45  # Augmenté de 40 à 45 pour plus d'espace
        cols_y = y - 38  # Espacement augmenté de -28 à -38
        
        stats_data = [
            ("Exercices", f"{stats['completed']}", f"/{stats['total_exercises']}"),  # Labels raccourcis
            ("Réussite", f"{stats['success_rate']:.0f}%", "taux"),  # Labels raccourcis et sans décimale
            ("Progrès", f"{stats['completion_rate']:.0f}%", "fait")  # Labels raccourcis et sans décimale
        ]
        
        start_x = width/2 - (len(stats_data) * col_width / 2) + col_width/2
        
        for i, (label, value, detail) in enumerate(stats_data):
            col_x = start_x + i * col_width
            
            # Fond de colonne (marges très réduites)
            margin = 8  # Augmenté de 6 à 8 pour plus d'espace
            col_rect_width = col_width - 2*margin
            
            c.setFillColor(primary_color)
            c.setFillAlpha(0.08)  # Réduit de 0.1 à 0.08
            c.rect(col_x - col_width/2 + margin, cols_y - col_height/2, col_rect_width, col_height, fill=1, stroke=0)
            c.setFillAlpha(1)
            
            # Valeur principale (très réduite)
            c.setFont("Helvetica-Bold", 14)  # Réduit de 16 à 14
            c.setFillColor(primary_color)
            self._draw_centered_text(c, col_x, cols_y + 8, value)  # Espacement augmenté de +6 à +8
            
            # Label (très réduit)
            max_label_width = col_rect_width - 4  # Réduit de -5 à -4
            truncated_label = self._truncate_text_to_fit(c, label, max_label_width, "Helvetica-Bold", 6)
            
            c.setFont("Helvetica-Bold", 6)  # Réduit de 7 à 6
            c.setFillColor(dark_grey)
            self._draw_centered_text(c, col_x, cols_y - 2, truncated_label)  # Espacement maintenu
            
            # Détail (très réduit)
            truncated_detail = self._truncate_text_to_fit(c, detail, max_label_width, "Helvetica", 5)
            
            c.setFont("Helvetica", 5)  # Réduit de 6 à 5
            c.setFillColor(dark_grey)
            self._draw_centered_text(c, col_x, cols_y - 12, truncated_detail)  # Espacement augmenté de -9 à -12
    
    def _draw_footer(self, c, width, height, primary_color, dark_grey, white, timestamp, user_name):
        """Dessine le pied de page professionnel (très réduit)"""
        footer_y = 110  # Remonté de 100 à 110 pour plus d'espace
        
        # Ligne séparatrice
        c.setStrokeColor(primary_color)
        c.setLineWidth(1)
        c.line(60, footer_y + 35, width - 60, footer_y + 35)  # Position ajustée
        
        # Informations officielles (très réduites)
        c.setFont("Helvetica-Bold", 9)  # Réduit de 11 à 9
        c.setFillColor(dark_grey)
        c.drawString(60, footer_y + 12, "EduCode Learning Platform")  # Espacement augmenté
        
        c.setFont("Helvetica", 7)  # Réduit de 9 à 7
        c.drawString(60, footer_y + 2, "Plateforme Python interactive")  # Espacement augmenté
        c.drawString(60, footer_y - 8, "Certification continue")  # Espacement augmenté
        
        # ID du certificat et signature numérique (très réduit)
        cert_id = f"EDC-{timestamp}-{abs(hash(user_name)) % 10000:04d}"
        
        c.setFont("Helvetica", 7)  # Réduit de 9 à 7
        c.setFillColor(dark_grey)
        self._draw_right_aligned_text(c, width - 60, footer_y + 12, "Certificat vérifié")  # Espacement augmenté
        self._draw_right_aligned_text(c, width - 60, footer_y + 2, f"ID: {cert_id}")  # Espacement augmenté
        
        # QR code simulé (très réduit)
        qr_size = 25  # Réduit de 35 à 25
        qr_x, qr_y = width - 60 - qr_size, footer_y - 20  # Position ajustée pour plus d'espace
        
        c.setFillColor(dark_grey)
        c.rect(qr_x, qr_y, qr_size, qr_size, fill=1, stroke=0)
        
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 6)  # Réduit de 7 à 6
        self._draw_centered_text(c, qr_x + qr_size/2, qr_y + qr_size/2 - 1, "QR")
        
        # Cachet officiel simulé (très réduit)
        stamp_x, stamp_y = 60, footer_y - 20  # Position ajustée pour plus d'espace
        c.setStrokeColor(primary_color)
        c.setLineWidth(1)  # Réduit de 2 à 1
        c.circle(stamp_x + 12, stamp_y + 12, 10, fill=0, stroke=1)  # Taille très réduite
        
        c.setFont("Helvetica-Bold", 5)  # Réduit de 7 à 5
        c.setFillColor(primary_color)
        self._draw_centered_text(c, stamp_x + 12, stamp_y + 15, "OFFICIEL")
        self._draw_centered_text(c, stamp_x + 12, stamp_y + 9, "EDUCODE")