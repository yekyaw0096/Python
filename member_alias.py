import importlib
import calculator

importlib.reload(calculator) #dynamic reload,
from calculator import add as sum
import calculator
print("Add as sum ", sum(10,20))