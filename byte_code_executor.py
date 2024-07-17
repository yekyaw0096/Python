import dis

a = 11
b = 40
c = 30
d = a + b * c

print("Globals ",globals())#variables outside functions are global variables

variables = globals()

execution_stack = []
byte_codes = [("LOAD_GLOBAL","a"),#op_code = LOAD_GLOBAL, operand = 10
              ("LOAD_GLOBAL","b"),#op_code = LOAD_GLOBAL, operand = 20
              ("LOAD_GLOBAL","c"),#op_code = LOAD_GLOBAL, operand = 30
              ("BINARY_MULTIPLY",),
              ("BINARY_ADD",),
              ]
#print("byte codes ", byte_codes)

for byte_code in byte_codes:
    print("byte codes ", byte_code)
    op_code = byte_code[0]
    print("Opcode ", op_code)
    
    if op_code == "LOAD_GLOBAL":
        var_name = byte_code[1]
        operand = variables[var_name]
        execution_stack.append(operand)
    
    elif op_code == "BINARY_MULTIPLY":
        op_two = execution_stack.pop()
        op_one = execution_stack.pop()
        execution_stack.append((op_one*op_two))
        
    elif op_code == "BINARY_ADD":
        op_two = execution_stack.pop()
        op_one = execution_stack.pop()
        execution_stack.append((op_one+op_two))
        
    else:
        print("unknown opcode")
print("Result ", execution_stack.pop())
print("D is ",d)