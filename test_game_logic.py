import unittest
from game_logic import *

class GenerateHandTestCase(unittest.TestCase):

	def test_throws(self):
		#check if get throws works
		throws = ["rock", "paper", "scissor"]
		self.assertEqual(do_throw(throws, 0), "rock")
		self.assertEqual(do_throw(throws,1), "paper")
		self.assertEqual(do_throw(throws,2), "scissor")
		self.assertNotEqual(do_throw(throws,0), "ardvark")

	def test_check_win(self):
		#check if check win works
		loss = "You Lose!"
		win = "You Win!"
		tie = "It's a tie"
		self.assertEqual(check_win("rock", "rock"), tie)
		self.assertNotEqual(check_win("rock", "paper"), win)
		self.assertEqual(check_win("rock", "scissor"), win)
		self.assertEqual(check_win("rock", "paper"), loss)
		self.assertEqual(check_win("paper", "scissor"), loss)
		self.assertEqual(check_win("paper", "rock"), win)
		self.assertEqual(check_win("paper", "paper"), tie)
		self.assertEqual(check_win("scissor", "paper"), win)
		self.assertEqual(check_win("scissor", "scissor"), tie)
		self.assertEqual(check_win("scissor", "rock"), loss)

	def test_generate_random_throw(self):
		#check if random.randint works
		for i in range(100):
			comp_throw = generate_computer_throw(0,2)
			self.assertLessEqual(comp_throw,2)
			self.assertGreaterEqual(comp_throw,0)

if __name__ == "__main__":
	unittest.main()