full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
     """
    Creates a character profile after validating the character name
    and its statistics.

    The function validates the following:
    - The character name must be a string
    - The character name must not be empty
    - The character name must not exceed 10 characters
    - The character name must not contain spaces
    - All stats must be integers
    - All stats must be between 1 and 4 (inclusive)
    - The sum of all stats must be exactly 7

    If any validation fails, an error message is returned.
    If all validations pass, a formatted string representing the
    character and its stats is returned.

    Parameters:
        name (str): The name of the character
        strength (int): Strength stat (1 to 4)
        intelligence (int): Intelligence stat (1 to 4)
        charisma (int): Charisma stat (1 to 4)

    Returns:
        str: An error message if validation fails, otherwise a
             formatted string describing the character.
    """
    
    #name conditions
    if not isinstance(name, str):
        return ("The character name should be a string")

    if name == "":
        return ("The character should have a name")

    if len(name) > 10:
        return ("The character name is too long")

    if " " in name:
        return ("The character name should not contain spaces")

    #values conditions

    if (not isinstance(strength, int) or 
       not isinstance(intelligence, int) or 
       not isinstance(charisma, int)):
        return ("All stats should be integers")


    if strength < 1 or intelligence < 1 or charisma < 1:
        return ("All stats should be no less than 1")

    if strength > 4 or intelligence > 4 or charisma > 4:
        return ("All stats should be no more than 4")

    if strength + intelligence + charisma != 7:
        return ("The character should start with 7 points")

    result = name + "\n"
    result += f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
    result += f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
    result += f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    return result


create_character('ren', 4, 2, 1)
