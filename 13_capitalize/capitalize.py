def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # return phrase.replace(phrase[0],phrase[0].upper(),1)
    # correct one but better one below

    return phrase[:1].upper()+phrase[1:]
   
    