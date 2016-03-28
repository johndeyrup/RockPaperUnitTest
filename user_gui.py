from Tkinter import *
from game_logic import *

class Frm(Frame):
	#Creates a Frame

	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()

	def get_result(self, throw):
		comp_throw, result = play_computer(throw)
		self.compThrow['text'] = comp_throw.capitalize()
		self.resultThrow['text'] = result

	def initUI(self):
		self.parent.title("Rock Paper Scissors")
		self.grid()

		self.chooseThrow = Lbl(self, "Choose a throw", 0, 0)
		self.rockButton = Btn(self, "Rock", lambda: self.get_result("rock"), 1, 0)
		self.paperButton = Btn(self, "Paper", lambda: self.get_result("paper"), 2, 0)
		self.scissorButton = Btn(self, "Scissor", lambda: self.get_result("scissor"), 3, 0)
		self.computerLabel = Lbl(self, "Computer Throw", 0, 1)
		self.compThrow = Lbl(self, "None", 1, 1)
		self.quitButton = Btn(self, "Quit", self.quit, 4, 1)
		self.resultLabel = Lbl(self, "Result Throw", 0, 2)
		self.resultThrow = Lbl(self, "None", 1, 2)


class Btn(Button):
	#Create a button
	def __init__(self, parent, text, command, row, column):
		Button.__init__(self, parent, text = text, command = command)
		self.grid(row=row, column=column, padx=10, pady=10)

class Lbl(Label):
    '''
    Creates a label with specified text, size, and location
    '''
    def __init__(self, parent, text, row, column):
        Label.__init__(self, parent, text=text)
        self.grid(row=row, column=column, padx=10, pady=10)

def main():


	root = Tk()
	root.geometry("400x400+300+300")
	app = Frm(root)
	root.mainloop()

if __name__ == "__main__":
	main()