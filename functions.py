import tkinter as tk


def add(a: float, b: float) -> str:
	return str(a+b)

def substract(a: float, b: float) -> str:
	return str(a-b)

def multiply(a: float, b: float) -> str:
	return str(a*b)

def divide(a: float, b: float) -> str:
	try:
		return round((a/b), 2)

	except ZeroDivisionError as e:
		return "Can't divide by zero!"



def equate(exp : str) -> str:
	try:

		i = 0
		while(i < len(exp)):
			if exp[i] == "X":
				exp = exp[:i] + "*" + exp[i+1:]

			if (exp[i] == "%"):
				if (i+1<len(exp) and exp[i+1].isnumeric()):
					exp = exp[:i] + "*0.01*" + exp[i+1:]
					i+=5
				else:
					exp = exp[:i] + "*0.01" + exp[i+1:]
					i+=4

			i+=1


				
		return str(eval(exp))

	except:
		return "Invalid expression!"

def equate_OP(entry):
	exp = entry.get()

	entry.delete(0, tk.END)
	entry.insert(0, equate(exp))



if __name__ == "__main__":
	print("This is Functions.py")