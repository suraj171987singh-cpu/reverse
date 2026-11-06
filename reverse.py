user_input = (input("Enter a number:")).strip()
if user_input.startswith('-'):
    user_input = user_input[:1]

digit_count = len(user_input)
print(f"Total number of digits:{digit_count}")