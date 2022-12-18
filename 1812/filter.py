


vowels = ['a','e','i','o','u']



c= "fwesf"
l= filter(lambda letter: letter.lower() not in vowels, c )
print("".join(l))