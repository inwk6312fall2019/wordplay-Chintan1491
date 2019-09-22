#prog 9.3
def avoids(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
        return True
    
fin = open('words.txt')
count = 0
forbidden_letters = input('Enter any forbidden letters: ')
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters) == True:
        count += 1
print(count)

