#prog 9.2
def has_no_e_word():
    my_file=open("words.txt")
    word=line.strip()
    for letter in word:
        if letter =='e':
            return False
    return True

print(has_no_e_word())  

my_file=open("words.txt")
total_words=0
count_of_e=0
for letter in my_file:
    total_words+=1
    word=letter.strip()
    if word.find('e') == -1:
        print(word)
        count_of_e+=1
    percent_of_e_words=(count_of_e/total_words)*100
    print(percent_of_words)        
my_file.close()

