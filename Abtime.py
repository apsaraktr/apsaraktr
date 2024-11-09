def expand_string(input_str):
    output = ""
    i = 0

    while i < len(input_str):
        # Take the character
        char = input_str[i]
        i += 1
        
        # Initialize number string to capture multi-digit numbers
        num_str = ""
        
        # Extract the number that follows the character
        while i < len(input_str) and input_str[i].isdigit():
            num_str += input_str[i]
            i += 1
        
        # Convert the number string to an integer
        if num_str:
            count = int(num_str)
        else:
            count = 1  # Default to 1 if no number is found
        
        # Append the character repeated 'count' times to the output
        output += char * count

    return output

# Test the function
input_str = "a1b10"
print(expand_string(input_str))



output

abbbbbbbbbb
