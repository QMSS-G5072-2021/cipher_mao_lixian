def cipher(text, shift, encrypt=True):
  """
  Each letter is replaced by a letter some fixed number of positions down the alphabet.

  Parameters
  ----------
  text: str
    A string of text to be encrypted or decrypted.
  shift: int
    An integer incidating the digits that would be used to encrypt or decrypt.
  encrypt: boolean
    A boolean value indicating either True or False to encrypt or decrypt

  Returns
  -------
  new_text: str
    A new string of text after being encrypted or decrypted.

  Examples
  --------
  >>> from cipher_lm3598 import cipher_lm3598
  >>> a = 'l'
  >>> b = 1
  >>> cipher_lm3598.cipher(a, b)
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