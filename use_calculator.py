#from calculator import add,mul #*
import calculator as c
import dis

print("add ",c.add(10,20))  
print("multiply ",c.mul(10,20))
print("disassembly ",dis.dis(c.mul))