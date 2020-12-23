# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
data = open("average.txt")
count = 0
average = 0

for line in data:
    if not line.startswith("X-DSPAM-Confidence:"): continue

    average += float(line[19:])
    count = count + 1


print("Average spam confidence:", (average / count))