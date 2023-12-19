def consolidate(base, length, fill = "‌",):
    """
    Returns an array of possible consolidations.

    :param str baseString: String to put fillerString within
    :param int maxLength: Max length of result string
    :param str fillerChar : Character to consolidate with base, default ZWNJ
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

def count(base, length, fill = "‌",):
    """
    Returns the total amount of consolidations possible.

    :param str baseString: String to put fillerString within
    :param int maxLength: Max length of result string
    :param str fillerString : String to put within baseString
    :return: List of combinations
    :rtype: list
    """
    fl = len(fill) #filler length
    
