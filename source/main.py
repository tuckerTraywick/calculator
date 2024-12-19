from tkinter import *
from tkinter import ttk

class Calculator:
	def __init__(self, root):
		root.title("Calculator")

		self.answer = "0"

		self.resultText = StringVar(value="")

		self.frame = ttk.Frame(root)
		self.result = ttk.Label(self.frame, textvariable=self.resultText, font="Menlo 15", justify="right").grid(column=0, row=0, columnspan=5, sticky="e")

		self.buttonLeftParenthesis = ttk.Button(self.frame, text="(", command=lambda: self.appendToResult("(")).grid(column=0, row=1, sticky="nsew")
		self.buttonRightParenthesis = ttk.Button(self.frame, text=")", command=lambda: self.appendToResult(")")).grid(column=1, row=1, sticky="nsew")
		self.buttonRightParenthesis = ttk.Button(self.frame, text="%", command=lambda: self.appendToResult("%")).grid(column=2, row=1, sticky="nsew")

		self.button7 = ttk.Button(self.frame, text="7", command=lambda: self.appendToResult("7")).grid(column=0, row=2, sticky="nsew")
		self.button8 = ttk.Button(self.frame, text="8", command=lambda: self.appendToResult("8")).grid(column=1, row=2, sticky="nsew")
		self.button9 = ttk.Button(self.frame, text="9", command=lambda: self.appendToResult("9")).grid(column=2, row=2, sticky="nsew")
		self.button4 = ttk.Button(self.frame, text="4", command=lambda: self.appendToResult("4")).grid(column=0, row=3, sticky="nsew")
		self.button5 = ttk.Button(self.frame, text="5", command=lambda: self.appendToResult("5")).grid(column=1, row=3, sticky="nsew")
		self.button6 = ttk.Button(self.frame, text="6", command=lambda: self.appendToResult("6")).grid(column=2, row=3, sticky="nsew")
		self.button1 = ttk.Button(self.frame, text="1", command=lambda: self.appendToResult("1")).grid(column=0, row=4, sticky="nsew")
		self.button2 = ttk.Button(self.frame, text="2", command=lambda: self.appendToResult("2")).grid(column=1, row=4, sticky="nsew")
		self.button3 = ttk.Button(self.frame, text="3", command=lambda: self.appendToResult("3")).grid(column=2, row=4, sticky="nsew")
		self.button0 = ttk.Button(self.frame, text="0", command=lambda: self.appendToResult("0")).grid(column=1, row=5, sticky="nsew")
		self.buttonScientific = ttk.Button(self.frame, text="e", command=lambda: self.appendToResult("e")).grid(column=0, row=5, sticky="nsew")
		self.buttonDecimal = ttk.Button(self.frame, text=".", command=lambda: self.appendToResult(".")).grid(column=2, row=5, sticky="nsew")

		self.buttonPower = ttk.Button(self.frame, text="^", command=lambda: self.appendToResult("^")).grid(column=3, row=1, sticky="nsew")
		self.buttonDivide = ttk.Button(self.frame, text="/", command=lambda: self.appendToResult("/")).grid(column=3, row=2, sticky="nsew")
		self.buttonTimes = ttk.Button(self.frame, text="*", command=lambda: self.appendToResult("*")).grid(column=3, row=3, sticky="nsew")
		self.buttonMinus = ttk.Button(self.frame, text="-", command=lambda: self.appendToResult("-")).grid(column=3, row=4, sticky="nsew")
		self.buttonPlus = ttk.Button(self.frame, text="+", command=lambda: self.appendToResult("+")).grid(column=3, row=5, sticky="nsew")

		self.buttonAllClear = ttk.Button(self.frame, text="ac", command=self.clearAll).grid(column=4, row=1, sticky="nsew")
		self.buttonClear = ttk.Button(self.frame, text="c", command=self.clearResult).grid(column=4, row=2, sticky="nsew")
		self.buttonDelete = ttk.Button(self.frame, text="del", command=self.delete).grid(column=4, row=3, sticky="nsew")
		self.buttonAnswer = ttk.Button(self.frame, text="ans", command=self.appendAnswer).grid(column=4, row=4, sticky="nsew")
		self.buttonEquals = ttk.Button(self.frame, text="=", command=self.evaluate, default="active").grid(column=4, row=5, sticky="nsew")

		for widget in self.frame.winfo_children():
			widget.grid_configure(padx=2, pady=0)

		self.frame.grid()

	def appendToResult(self, button):
		self.resultText.set(self.resultText.get() + button)

	def clearAll(self):
		self.clearResult()
		self.answer = "0"

	def clearResult(self):
		self.resultText.set("")

	def delete(self):
		if self.resultText.get():
			self.resultText.set(self.resultText.get()[:-1])

	def appendAnswer(self):
		if not self.resultText.get() or (not self.resultText.get()[-1].isnumeric() and self.resultText.get()[-1] != "."):
			self.appendToResult(self.answer)

	def evaluate(self):
		if self.resultText.get():
			self.answer = str(eval(self.resultText.get()))
			self.resultText.set(self.answer)

root = Tk()
calculator = Calculator(root)
root.mainloop()
