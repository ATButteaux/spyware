#!/usr/bin/python3 

import sys

def reduce_num(digits):
  summod = 0
  for index, digit in enumerate(digits):
    summod += int(digits[index])
  return summod % 10

#
# Modulus Two Strings 
#
def mts(string1, string2):
  new_string = ""
  for index in range(len(string1)):
    if string1[index] == " ":
      new_string = new_string + " "
      continue
    new_string = new_string + str((int(string1[index]) + int(string2[index])) % 10)
  return new_string

#
# Lagging Fibonachi Modulus
#
def lfm( seed ):
  seed_len = len(seed)
  sequence = str()
  if seed_len < 1: return
  position = 1

  while position < seed_len:
    result = (int(seed[position-1]) + int(seed[position])) % 10
    sequence = sequence + str(result)
    position += 1

  result = (int(seed[0]) + int(seed[position-1])) % 10
  sequence = sequence + str(result)
  return sequence

#
# Encode letter
#
def find_letter(letter):
  found = False
  for element in dec_encoder:
    if element[0] == letter:
      found = True
      return element[1]
    continue

#
# Write out string of digits in 5 letter groups
#
def format_digits(string):
  new_string = ""
  count = 0
  for letter in string:
    new_string = new_string + letter
    if count % 5 == 4:
      new_string = new_string + " "
    count += 1
  return new_string.strip()

dec_encoder = [
  [ "A", "1"],
  [ "E", "2"],
  [ "I", "3"],
  [ "N", "4"],
  [ "O", "5"],
  [ "T", "6"],
  [ "B", "70"],
  [ "C", "71"],
  [ "D", "72"],
  [ "F", "73"],
  [ "G", "74"],
  [ "H", "75"],
  [ "J", "76"],
  [ "K", "77"],
  [ "L", "78"],
  [ "M", "79"],
  [ "P", "80"],
  [ "Q", "81"],
  [ "R", "82"],
  [ "S", "83"],
  [ "U", "84"],
  [ "V", "85"],
  [ "W", "86"],
  [ "X", "87"],
  [ "Y", "88"],
  [ "Z", "89"],
  [ "@", "90"],
  [ ":", "91"],
  [ "-", "92"],
  [ ".", "93"],
  [ "+", "94"],
  [ "#", "95"],
  [ "/", "96"],
  [ "*", "97"],
  [ " ", "98"],
  [ "0", "00"],
  [ "1", "11"],
  [ "2", "22"],
  [ "3", "33"],
  [ "4", "44"],
  [ "5", "55"],
  [ "6", "66"],
  [ "7", "77"],
  [ "8", "88"],
  [ "9", "99"]
]

user_seed_encoded = ""
user_seed = str(input("What is your seed? ")).upper()

for letter in user_seed:
  user_seed_encoded = user_seed_encoded + find_letter(letter)

# Pad seed
while len(user_seed_encoded) % 5 != 0:
  user_seed_encoded = user_seed_encoded + "9"

print("Your encoded seed: " + format_digits(user_seed_encoded))
print()

#loop(enc -> shift -> mod)
offset = int(reduce_num(user_seed_encoded[0:5]))
string1 = user_seed_encoded
string2 =lfm(user_seed_encoded[offset:] + user_seed_encoded[0:offset])
result = mts(string1, string2)
print("00001: " + format_digits(string1) + "   Encoded seed")
print("00002: " + format_digits(string2) + "   SLFM10")
print("00003: " + format_digits(result) + "   AM10", end="")
count = 3
while input("  More? ") + ".":
  count += 1
  string1 = result
  offset = int(reduce_num(string1[0:5]))
  string2 = lfm(string1[offset:] + string1[0:offset])
  result = mts(string1, string2)
  print("{:05d}".format(count) + ": " + format_digits(string2) + "   SLFM10")
  count += 1
  print("{:05d}".format(count) + ": " + format_digits(result) + "   AM10", end="")

