input_list =  eval(input("Enter the list:"))

vowels = "AEUOIYaeuoiy"
consonants = "BCDFGHKLMNPQRSTVWQXYZbcdfghjklmnpqrstvwxyz"
symbols = ",. ;:"

list_vow = []
list_con = []
list_sym = []

print(input_list)
for char, count in input_list:
    if char in vowels:
     list_vow.append((char, count))
    elif char in consonants:
     list_con.append((char, count))
    elif char in symbols:
     list_sym.append((char, count))


print(list_vow)
print(list_con)
print(list_sym)