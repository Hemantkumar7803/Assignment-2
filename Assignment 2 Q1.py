# Assignment-2
input = "Python is a case sensitive language"
# a
print("Length of the input string is",len(input))
# b
Reverse_order = input[35::-1]
print( "the reverse order is'", Reverse_order ,"'")
# c
phrase = input[10:26]
print('''the sliced string is "''', phrase,'''"''')
# d
New_input = input.replace("a case sensitive","object oriented")
print('''Updated string is "''',New_input,'''"''')
# e
index_of_a = input.find("a")
print("The index of 'a' is",index_of_a)
# f
updated_input = input.replace(" ","")
print("The new string is '",updated_input,"'")
