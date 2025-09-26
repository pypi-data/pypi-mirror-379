# tests/test_educode.py
"""Tests unitaires pour EduCode"""

import unittest
import tempfile
import os
from educode.core import EduCode, Exercise
from educode.exercises import get_all_exercises

class TestEduCode(unittest.TestCase):
    
    def setUp(self):
        """Prépare un environnement de test"""
        self.temp_progress_file = tempfile.NamedTemporaryFile(delete=False).name
        self.educode = EduCode()
        self.educode.progress_file = self.temp_progress_file
    
    def tearDown(self):
        """Nettoie après les tests"""
        if os.path.exists(self.temp_progress_file):
            os.unlink(self.temp_progress_file)
    
    def test_load_exercises(self):
        """Teste le chargement des exercices"""
        self.assertEqual(len(self.educode.exercises), 215)
        self.assertIn("001", self.educode.exercises)
        self.assertIn("215", self.educode.exercises)
    
    def test_exercise_structure(self):
        """Teste la structure des exercices"""
        ex = self.educode.exercises["001"]
        self.assertIsInstance(ex, Exercise)
        self.assertEqual(ex.title, "Fonction carré")
        self.assertEqual(ex.difficulty, "facile")
        self.assertTrue(len(ex.test_cases) > 0)
    
    def test_get_random_exercise(self):
        """Teste la sélection d'exercices aléatoires"""
        ex = self.educode.get_random_exercise(difficulty="facile")
        self.assertIsNotNone(ex)
        self.assertEqual(ex.difficulty, "facile")
    
    def test_stats(self):
        """Teste le calcul des statistiques"""
        stats = self.educode.get_stats()
        self.assertEqual(stats["total_exercises"], 215)
        self.assertEqual(stats["completed"], 0)
        self.assertEqual(stats["completion_rate"], 0.0)
    
    def test_progress_update(self):
        """Teste la mise à jour de la progression"""
        self.educode._update_progress("001", True)
        self.assertIn("001", self.educode.progress["completed"])
        
        stats = self.educode.get_stats()
        self.assertEqual(stats["completed"], 1)

class TestExercises(unittest.TestCase):
    
    def setUp(self):
        self.exercises = get_all_exercises()
    
    def test_exercise_count(self):
        """Teste qu'on a bien 215 exercices"""
        self.assertEqual(len(self.exercises), 215)
    
    def test_difficulty_distribution(self):
        """Teste la répartition des difficultés"""
        difficulties = [ex.difficulty for ex in self.exercises]
        facile_count = difficulties.count("facile")
        moyen_count = difficulties.count("moyen") 
        difficile_count = difficulties.count("difficile")
        
        self.assertEqual(facile_count, 40)
        self.assertEqual(moyen_count, 40)
        self.assertEqual(difficile_count, 20)
    
    def test_unique_ids(self):
        """Teste que tous les IDs sont uniques"""
        ids = [ex.id for ex in self.exercises]
        self.assertEqual(len(ids), len(set(ids)))
    
    def test_required_fields(self):
        """Teste que tous les exercices ont les champs requis"""
        for ex in self.exercises:
            self.assertIsNotNone(ex.id)
            self.assertIsNotNone(ex.title)
            self.assertIsNotNone(ex.description)
            self.assertIsNotNone(ex.difficulty)
            self.assertIsNotNone(ex.category)
            self.assertIsInstance(ex.test_cases, list)
            self.assertTrue(len(ex.test_cases) > 0)

if __name__ == '__main__':
    unittest.main()