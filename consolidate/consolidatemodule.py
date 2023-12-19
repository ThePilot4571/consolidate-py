def consolidate(base, length, fill = "‌",):
    """
    Generate a list of possible combinations where .

    :param str baseString: String to put fillerString within
    :param int maxLength: Max length of result string
    :param str fillerString : String to put within baseString
    :return: List of combinations
    :rtype: list
    """
    # maybe add a "must match max length" bool as an input if user requires exact length, no less
    if(length - len(base) < 0):
        raise ValueError("Maximum length can't be less than length of base string")
    output = []
    d = length - len(base)
    output.append(base)
    for i in range(1, d+1):
        output.append(fill * i + base)
    return output
        
print(consolidate("hey", 3, "X")) 