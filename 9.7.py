#prog 9.7
def three_consecutive(s):
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1

my_file = open('words.txt')
count = 0
for word in my_file:
    word = word.strip()
    if three_consecutive(word) == True:
        print(word)
        count += 1
print(count)
