# Nelson Barahona and Mark Downs
#  password generator

# Password consists of 2 upper case letters, 4 lower case letters, 4 digits, and 2 punctuation marks.
# Each character is created randomly with the random function and then all characters are concatenated into one string
import random
import string


# randomize password characters
def shuffle(string):
    tempList = list(string)  # create list with string
    random.shuffle(tempList)  # use list shuffle function to randomize order of characters
    return ''.join(tempList)  # user list join function to return list of chars as string


# upperCase random values
upperCase1 = chr(random.randint(65, 90))
upperCase2 = chr(random.randint(65, 90))


# lowerCase random values
lowerCase1 = chr(random.randint(97,122))
lowerCase2 = chr(random.randint(97,122))
lowerCase3 = chr(random.randint(97,122))
lowerCase4 = chr(random.randint(97,122))


# Digit random values
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
digit3 = chr(random.randint(48,57))
digit4 = chr(random.randint(48,57))


# Punctuation random values
punctuation = string.punctuation  # string of all punctuation characters
punctuationSign1 = punctuation[random.randint(0, len(punctuation)-1)]
punctuationSign2 = punctuation[random.randint(0, len(punctuation)-1)]


# Create password with random values above
password = upperCase1 + upperCase2 + lowerCase1 + lowerCase2 + lowerCase3 + lowerCase4 + digit1 + digit2 + digit3 \
           + digit4 + punctuationSign1 + punctuationSign2


# Shuffle character order with shuffle function
password = shuffle(password)

print(password)