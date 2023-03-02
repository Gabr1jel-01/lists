words = []
number_of_words = int(input('Koliko rijeci zelite upisati? '))

for i in range(number_of_words):
    word = input(f'Upisite {i + 1}. rijec: ')
    words.append(word)

words.append('Algebra')
    
#print(words)
print()
print(f'Ispis rijeci iz "words({len(words)})" s brojem znakova/slova.')
print()
# Rijec "Python" ima 6 znakova/slova.
message = f'Rijec "{word}" ima {len(word)} znakova/slova.'

for word in words:
    message = f'Rijec "{word}" ima {len(word)} znakova/slova.'
    print(message)
    
