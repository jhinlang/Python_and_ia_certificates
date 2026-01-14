def caesar(text, shift, encrypt=True):
  """
    Applies a Caesar cipher to a given text.

    This function shifts each alphabetical character in the input text by a
    specified number of positions in the alphabet. By default, the function
    encrypts the text. If encrypt is set to False, the function decrypts the text.

    Parameters:
        text (str): The text to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        encrypt (bool, optional): If True, the text is encrypted.
                                 If False, the text is decrypted.
                                 Default is True.

    Returns:
        str: The encrypted or decrypted text.

    Example:
        caesar("hello", 3)            -> "khoor"
        caesar("khoor", 3, False)     -> "hello"
    """

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
