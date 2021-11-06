def cipher(text, shift, encrypt=True):
    """
    Each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text : str
      the original string.
    shift : int
      the fixed number of positions down the alphabet.

    Returns
    -------
    str
      the new string.

    Examples
    --------
    >>> from pypkgs import pypkgs
    >>> a = 'l'
    >>> b = 1
    >>> pypkgs.cipher(a, b)
    m
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text