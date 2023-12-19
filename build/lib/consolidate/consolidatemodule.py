def consolidate(base, fill, len):
    output = []
    
    """
    Generate a list of possible combinations where .

    :param str baseString: String to put fillerString within
    :param str fillerString : String to put within baseString
    :param int maxLength: Max length of result string
    :return: List of combinations
    :rtype: list
    """
    # maybe add a "must match max length" bool as an input if user requires exact length, no less

def generate_combinations(s, length):
    result = []
    n = len(s)

    # Loop through each position to insert '*'
    for i in range(n + 1):
        for j in range(length + 1):
            new_str = s[:i] + '*' * j + s[i:]
            
            # Ensure the length of the new string is not greater than specified
            if len(new_str) <= length:
                result.append(new_str)

    return result

# Example usage:
input_string = "hello"
max_length = 10
combinations = generate_combinations(input_string, max_length)

for combination in combinations:
    print(combination)