# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    quit()
for letter in fh:
    letter= letter.rstrip()
    print(letter.lower())