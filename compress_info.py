from collections import defaultdict
from math import log2

char_dict = defaultdict(int)
entropy_dict = defaultdict(float)
prob_dict = defaultdict(float)
MESSAGE = """i ate a banana on the mississippi, you ate a banana on 
             the mullum mullum"""

# Tally up frequency of each character in the message
for char in MESSAGE:
	char_dict[char] += 1

# Calculate whole length of message
msg_len = len(MESSAGE)

# Get probability of character symbols in message
for char in char_dict:
	prob_dict[char] = char_dict[char]/msg_len

# Convert values into entropy
for char in char_dict:
	entropy_dict[char] = -log2(char_dict[char]/msg_len)

# Calculate H, the optimal average number of bits per symbol
H = 0.0
for char in char_dict:
	H += (prob_dict[char] * entropy_dict[char])
print("H = {:.3f}".format(H))

# Calculate L, the minimum length of the compressed message
L = 0.0
for char in char_dict:
	L += (char_dict[char] * entropy_dict[char])
print("L = {:.3f}".format(L))
