import unittest
from main import ScoreManager, Snake

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        """Paruošiama aplinka prieš kiekvieną testą."""
        self.score_manager = ScoreManager()
        self.score_manager.reset_score()
        self.snake = Snake()

    def test_singleton_score_manager(self):
        """Testuojamas Singleton dizaino šablonas."""
        another_manager = ScoreManager()
        self.assertIs(self.score_manager, another_manager, "ScoreManager nėra Singleton!")

    def test_score_addition(self):
        """Testuojamas taškų pridėjimas."""
        initial_score = self.score_manager.get_score()
        self.score_manager.add_score()
        self.assertEqual(self.score_manager.get_score(), initial_score + 1)

    def test_score_reset(self):
        """Testuojamas taškų nunulinimas."""
        self.score_manager.add_score()
        self.score_manager.reset_score()
        self.assertEqual(self.score_manager.get_score(), 0)

    def test_snake_initial_direction(self):
        """Testuojama pradinė gyvatėlės kryptis."""
        self.assertEqual(self.snake.get_direction(), "stop")

    def test_snake_direction_change(self):
        """Testuojamas krypties pakeitimas ir apsauga nuo savižudybės."""
        self.snake.set_direction("up")
        self.assertEqual(self.snake.get_direction(), "up")
        
        self.snake.set_direction("down")
        self.assertNotEqual(self.snake.get_direction(), "down")
        self.assertEqual(self.snake.get_direction(), "up")

if __name__ == '__main__':
    unittest.main()
