#!/bin/python3

import glob
import random
import sys

if len(sys.argv) != 2:
  rows_requested = int(input("How many rows of numbers do you need? "))
else:
  rows_requested=int(sys.argv[1])

# Read in codebook, unique, and sort
codebook = []
for codebook_file in glob.glob('codebook*.txt'):
  print("opening: " + codebook_file)
  codebook_fh = open(codebook_file, "r")
  for line in codebook_fh:
    codebook.append(line.upper().strip())
  codebook_fh.close()

# Strip, unique, and sort array
for index,code in enumerate(codebook):
  codebook[index] = codebook[index].upper()
  codebook[index] = codebook[index].strip()
codebook = list(set(codebook))
codebook.sort()

line_styles = [ 
  [31,"--"], 
  [32,"--"], 
  [48,"--"], 
  [49,"--"], 
  [76,"--"], 
  [77,"--"], 
  [93,"--"], 
  [94,"--"], 
  [110,"---"], 
  [111,"---"], 
  [138,"---"], 
  [139,"---"], 
  [155,"---"], 
  [156,"---"], 
  [172,"---"], 
  [173,"---"], 
  [200,"---"], 
  [201,"---"], 
  [217,"---"], 
  [218,"---"], 
  [234,"---"], 
  [235,"---"], 
  [262,"---"], 
  [263,"---"], 
  [279,"---"], 
  [280,"---"],
  [296,"---"],
  [297,"---"],
  [324,"---"], 
  [325,"---"], 
  [341,"---"], 
  [342,"---"], 
  [358,"---"], 
  [359,"---"], 
  [386,"---"], 
  [387,"---"], 
  [403,"---"], 
  [404,"---"], 
  [420,"---"], 
  [421,"---"], 
  [448,"---"], 
  [449,"---"], 
  [465,"---"], 
  [466,"---"], 
  [482,"---"], 
  [483,"---"], 
  [510,"---"], 
  [511,"---"], 
  [527,"---"], 
  [528,"---"], 
  [544,"---"], 
  [545,"---"] 
]

def find_line_style(line):
  found = False
  for row in line_styles:
    if row[0] == line:
      found = True
      style = row[1]
      break

  if found:
    return style
  else:
    return "#"

print("""CODE |  A E I N O T
 A   |  1 2 3 4 5 6
 B  C  D  F  G  H  J  K  L  M
70 71 72 73 74 75 76 77 78 79
 P  Q  R  S  U  V  W  X  Y  Z
80 81 82 83 74 85 86 87 88 89
 @  :  -  .  +  #  /  *  _ CC
90 91 92 93 94 95 96 97 98 99
0   1  2  3  4  5  6  7  8  9
00 11 22 33 44 55 66 77 88 99





0  1  2  3  4  5  6  7  8  9
1  2  3  4  5  6  7  8  9  0
2  3  4  5  6  7  8  9  0  1
3  4  5  6  7  8  9  0  1  2
4  5  6  7  8  9  0  1  2  3
5  6  7  8  9  0  1  2  3  4
6  7  8  9  0  1  2  3  4  5
7  8  9  0  1  2  3  4  5  6
8  9  0  1  2  3  4  5  6  7
9  0  1  2  3  4  5  6  7  8""")

      
# Print CodeBook
current_line=26

#for line in range(current_line,186*3):
#  print(line)
#sys.exit(0)
  
for index, code in enumerate(codebook):
  #print("codebook index: " + str(index) + " " + code.upper())
  while find_line_style(current_line) != "#":
    print(find_line_style(current_line))
    current_line = current_line + 1
  print(str("{:03d}".format(index+1)) + " " + code.upper())
  current_line = current_line + 1

#  style=find_line_style(current_line)
#  if style == "#":
#    print(str("{:03d}".format(index+1)) + " " + code.upper())
#  else:
#    print(style)
#  current_line = current_line + 1

#sys.exit(0)  

# Print OTP
for row in range(0,rows_requested):
  style = find_line_style(current_line)
  if style == "#":
    data = str("{:05d}".format(random.randint(0,99999))) + " "
    data = data + str("{:05d}".format(random.randint(0,99999))) + " "
    data = data + str("{:05d}".format(random.randint(0,99999))) + " "
    data = data + str("{:05d}".format(random.randint(0,99999))) + " "
    data = data + str("{:05d}".format(random.randint(0,99999)))
    print(data)
  else:
    print(style)
  current_line = current_line + 1

sys.exit(0)
