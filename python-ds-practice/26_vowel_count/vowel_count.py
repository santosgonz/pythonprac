def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_dict = {}
    vowels = ("a","e","i","o","u")
    phrase_2 = phrase.lower()
    for letters in phrase_2:
        if letters in vowels:
            vowel_dict[letters] = vowel_dict.get(letters, 0) + 1
    return vowel_dict