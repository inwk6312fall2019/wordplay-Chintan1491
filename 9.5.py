#Prog 9.5

def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

my_file = open('words.txt')
count = 0
for line in my_file:
    word = line.strip()
    if uses_all(word, 'aeiouy') == True:
        print(word)
        count += 1
print(count)
