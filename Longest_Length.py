def max_len_same_char(input_string):
    if not input_string:
        return 0, None

    max_len = 1
    curr_len = 1
    max_char = input_string[0]

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
                max_char = input_string[i - 1]
            curr_len = 1

    # Check the last substring
    if curr_len > max_len:
        max_length = curr_len
        max_char = input_string[-1]

    return max_len, max_char

# Input a string
input_str = input("Enter a string: ")

length, character = max_len_same_char(input_str)

if length > 1:
    print(f"The longest char: {character}")
    print(f" length is:  {length}.")
else:
    print("No repeating characters found.")