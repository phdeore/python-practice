import json


print("--------------------------------")
# Unsafe append
def unsafe_append(value, target_list=[]):
    target_list.append(value)
    return target_list

print("Unsafe append defaults:")
print(unsafe_append.__defaults__)       # contains empty list

print("=== ❌ Testing Unsafe Behavior ===")
# First call works as expected
call_1 = unsafe_append("Apple")
print(f"Call 1 (expected ['Apple']): {call_1}")
print("\nDefault values tuple after Call 1:")
print(unsafe_append.__defaults__)  

# Second call reuses the SAME list from Call 1!
call_2 = unsafe_append("Banana")
print(f"Call 2 (expected ['Banana']): {call_2}")
print("\nDefault values tuple after Call 2:")
print("Shared list ----------------->", unsafe_append.__defaults__)  
# Explicitly passing a list still works fine
call_3 = unsafe_append("Cherry", target_list=["Date"])
print(f"Call 3 (with custom list):   {call_3}")
print("\nDefault values tuple after Call 3:")
print(unsafe_append.__defaults__)
call_4 = unsafe_append("Papaya")
print(f"Call 4 (expected ['Papaya']): {call_4}")
print("\nDefault values tuple after Call 4:")
print("Shared list ----------------->", unsafe_append.__defaults__)  

print("\n--------------------------------")

# Safe append
def safe_append(value, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(value)
    return target_list

print("Safe append defaults:", "-")
print(safe_append.__defaults__)

print("\n===  Testing Safe Behavior ===")
# First call works cleanly
safe_1 = safe_append("Apple")
print(f"Call 1 (expected ['Apple']): {safe_1}")
print("\nDefault values tuple after Call 1:")
print(safe_append.__defaults__)  
# Second call gets a brand new list
safe_2 = safe_append("Banana")
print(f"Call 2 (expected ['Banana']): {safe_2}")
print("\nDefault values tuple after Call 2:")
print(safe_append.__defaults__)  
# Third call gets a brand new list
safe_3 = safe_append("Cherry", target_list=["Date"])
print(f"Call 3 (with custom list):   {safe_3}")
print("\nDefault values tuple after Call 3:")
print(safe_append.__defaults__)
safe_4 = safe_append("Papaya")
print(f"Call 4 (expected ['Papaya']): {safe_4}")
print("\nDefault values tuple after Call 4:")
print(safe_append.__defaults__)  