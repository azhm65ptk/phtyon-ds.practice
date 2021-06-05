def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    newStr=''
    for w in phrase:
        if w.lower()== to_swap.lower():
            if w.islower():
                newStr+=w.upper()
            else:
                newStr+=w.lower()
        else:
            newStr+=w
    return newStr