from math import *
from tkinter import *
from tkinter import ttk

cbrt = lambda x: x**(1/3)
log = log10

class Calculator:
	def __init__(self, root):
		root.title("Calculator")

		self.resultText = StringVar(value="")
		self.answer = "0"

		self.frame = ttk.Frame(root)
		self.result = ttk.Label(self.frame, textvariable=self.resultText, font="Menlo 15", justify="right").grid(column=0, row=0, columnspan=6, sticky="e")

		# Define the button layout.
		self.buttonNames = [
			["(", ")", "%", "^", "ac"],
			["7", "8", "9", "/", "c"],
			["4", "5", "6", "*", "del"],
			["1", "2", "3", "-", "ans"],
			[".", "0", "E", "+", "="],
		]
		self.buttonCommands = {
			"ac": self.clearAll,
			"c": self.clearResult,
			"del": self.delete,
			"ans": self.appendAnswer,
			"=": self.evaluate,
		}
		self.substitutions = [
			("^", "**"),
			("%", "*0.01"),
			("E", "*10**"),
		]
		self.buttons = []

		# Setup the buttons.
		for row in range(len(self.buttonNames)):
			self.buttons.append([])
			for column, name in enumerate(self.buttonNames[row]):
				# Nested lambda to capture just the current value of `name`.
				command = (lambda x: lambda: self.appendToResult(x))(name)
				self.buttons[row].append(ttk.Button(self.frame, text=name, command=self.buttonCommands.get(name, command)))
				self.buttons[row][-1].grid(row=row + 1, column=column, padx=2, pady=0, sticky="nsew")
		self.buttons[-1][-1]["default"] = "active"

		self.frame.grid()

	def appendToResult(self, button):
		if self.resultText.get() == "error":
			self.resultText.set(button)
		else:
			self.resultText.set(self.resultText.get() + button)

	def clearAll(self):
		self.clearResult()
		self.answer = "0"

	def clearResult(self):
		self.resultText.set("")

	def delete(self):
		if self.resultText.get() == "error":
			self.resultText.set("")
		elif self.resultText.get():
			self.resultText.set(self.resultText.get()[:-1])

	def appendAnswer(self):
		if not self.resultText.get() or (not self.resultText.get()[-1].isnumeric() and self.resultText.get()[-1] != "."):
			self.appendToResult(self.answer)

	def evaluate(self):
		if self.resultText.get() == "error":
			self.resultText.set("")
		elif self.resultText.get():
			text = self.resultText.get()
			for find, replace in self.substitutions:
				text = text.replace(find, replace)

			try:
				self.answer = str(eval(text))
				self.resultText.set(self.answer)
			except:
				self.resultText.set("error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
