#Prog 9.1
my_file=open("words.txt")
for line in my_file:
    word=line.strip()
    if len(word)>20:
        print(word)
#print(my_file.read())
my_file.close()

