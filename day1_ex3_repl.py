def parse_input(inp):
    parts = inp.split()
    if len(parts) != 3:
        return("Error: expected 'number operator number'")

    left, operator, right = parts

    try:
        left_num = int(left)
        right_num = int(right)
    except ValueError:
        return("Error: The specified input is not a number.")

    match operator:
        case "+": return left_num + right_num
        case "-": return left_num - right_num
        case "*": return left_num * right_num
        case "/": 
            if right_num == 0:
                return "Error: division by zero"
            return left_num / right_num
        case _: return f"Error: Invalid operator '{operator}'"


if __name__ == "__main__":
    while True:
        inp = input("> ")
        if inp == "quit" or inp == "exit":
            print("Bye!")
            break
        print(parse_input(inp))
