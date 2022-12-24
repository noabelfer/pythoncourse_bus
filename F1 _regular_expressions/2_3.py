#1
# import re
#
# cap = input("write here")
# pattern = "[A-Z][a-z]"
# result = re.match(pattern, cap)
# print(result)

# Given a string that represents DNA,
# check whether a given DNA string contain a TATA-box-like pattern.
#
# TATA-box-like pattern has the following structure:
# “TATAA” followed by 3 nucleotides and ends with “TT”
# Nucleotide is one of: A, C, G, T
#
# Examples of TATA-box-like DNA:
# "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
# "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
# import re
#
# dna = input("write here")
# pattern = "[TATAA]+[A or C or G or T]{3}+[TT]"
# result = re.search(pattern, dna)
# print(result)

import re
#
# dna = input("write here")
# pattern = "[TATAA]+[A or C or G or T]{3}+[T]{2}"
# result = re.match(pattern, dna)
# print(result)

#5
# Check whether the given string contains at least two TATA-lke patterns
# dna = input("write here")
# pattern = "([TATAA][A or C or G or T]{3}[T]){2}"
# result = re.search(pattern, dna)
# print(result)

# #6
# Maximum 2 TATA-like patterns

# dna = input("write here")
# pattern = "([TATAA][A or C or G or T]{3}[T]){0,2}"
# result = re.search(pattern, dna)
# print(result)

#7
# Write a regular expression to look for 3 digits, possibly separated by whitespace.
exp = input("write here")
pattern = "([0-9][\s]*){3}"
result = re.match(pattern, exp)
print(result)

#8
# Find all the israeli cell phone numbers in the text.
# In this exercise, israeli cell phone number answers the following:
# format: <000-0000000>
# starts from 05

exp = input("write here")
pattern = "([0][5][0-9]-[0-9]{7}"
result = re.match(pattern, exp)
print(result)