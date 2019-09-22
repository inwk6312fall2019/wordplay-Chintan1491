#prog 9.4
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

my_file = open('words.txt')
count = 0
for line in my_file:
    word = line.strip()
    if uses_only(word, 'acefhlo') == True:
        print(word)
        count += 1
print(count)
