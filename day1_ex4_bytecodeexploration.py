import dis

def slow():
    total = 0
    for i in range(1000):
        total = total + i
    return total

def fast():
    return sum(range(1000))
    # push loops into builtins and the standard library, they run in C
    '''
        LOAD_GLOBAL   sum
        LOAD_GLOBAL   range
        LOAD_CONST    1000
        CALL          1       ← calls range(1000)
        CALL          1       ← calls sum(...)
        RETURN_VALUE

        The primary difference between LOAD_FAST and LOAD_GLOBAL is how and where they look up variables in memory. 
        LOAD_FAST retrieves local variables directly from a fixed-size array by index, making it exceptionally quick. 
        In contrast, LOAD_GLOBAL looks up variables by name through a dynamic dictionary search, which carries higher computational overhead.
    '''

dis.dis(slow)
print("=======")
dis.dis(fast)