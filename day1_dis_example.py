import dis

def add(a, b):
    return a + b

pi = 3.142

# Sample comment
def areaofcircle(r):
    return pi * (r ** 2)

def areaofcirclepi(r):
    return 3.142 * (r ** 2)


dis.dis(add)
print()
#dis.dis(add.__code__)

dis.dis(areaofcircle)
print()
dis.dis(areaofcirclepi)

'''
Reading dis-assembling output
First Column: 
    Source code line number. Blank spaces below it mean those instructions belong to same source line.
Second Column: 
    Byte index of the instruction in compiled code object. 
    In Python3, offsets usually increase by 2 bytes (1 byte for the opcode, 1 byte for the argument)
Third Column:
    Human-readable name of the bytecode instruction (LOAD_FAST, BINARY_OP etc.)
    What Python VM (PVM) is doing at the moment.
Fourth Column:
    The raw internal index or numeric value used by PVM.
Fifth Column:
    Human readable hint in parenthesis. The resolved name or value mapping to the raw argument.

How Python Executes This Example?
LOAD_FAST 0 (a): Pushes the value of a onto the evaluation stack.
LOAD_FAST 1 (b): Pushes the value of b onto the evaluation stack.
BINARY_OP 0 (+): Pops both values, adds them, and pushes the result back.
STORE_FAST 2 (result): Pops the result and stores it in the local variable result.
LOAD_FAST 2 (result): Pushes result back onto the stack to prepare for the return.
RETURN_VALUE: Pops the top value and returns it to the caller.

Want to optimize performance or debugging unexpected behaviour.

'''