import tkinter as tk
import players as pla

class MainView():
	def __init__(self, root, control):
		self.control = control
		self.root = root 
		self.root.geometry('250x250')
		self.menubar = tk.Menu(self.root)

		#Menu bar:
		self.menubar.add_command(label="Make a bet", command=self.control.createBet)
		self.menubar.add_command(label="Nominees", command=self.control.printNominees)
		self.menubar.add_command(label="Data", command=self.control.printData)
		self.menubar.add_command(label="Register Winners", command=self.control.registerWin)
		self.menubar.add_command(label="Save and close", command=self.control.closeProg)

		self.root.config(menu=self.menubar)

class MainControl:
	def __init__(self):
		self.root = tk.Tk()

		self.ctrlPlayer = pla.CtrlPlayer(self)

		self.view = MainView(self.root, self)

		self.root.title("Oscar 2023")

		self.root.mainloop()

	def createBet(self):
		self.ctrlPlayer.createBet()

	def printNominees(self):
		self.ctrlPlayer.printNominees()

	def printData(self):
		self.ctrlPlayer.printData()

	def registerWin(self):
		self.ctrlPlayer.registerWin()

	def closeProg(self):
		self.root.destroy()

if __name__ == '__main__':
	c = MainControl()