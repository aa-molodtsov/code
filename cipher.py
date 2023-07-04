alphabet = {
  'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
  'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
  'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
  'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
  'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray', 'y': 'Yankee',
  'z': 'Zulu'}
def encode_word(word):
  if not word:
    return ''
  first_char = word[0].lower()
  if first_char in alphabet:
    return alphabet[first_char] + ' ' + encode_word(word[1:])
  else:
    return encode_word(word[1:])