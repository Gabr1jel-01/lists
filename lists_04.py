


numbers = []

# numbers.append(1)
# numbers.append(2)

# numbers[2] = 3 JOS NEMA indexa sa brojem 2 tako da ga ne mozemo zamjenit niti mu pridodat vrijednost

print(numbers)


# dodaj brojeve od 1 do 100
for i in range(1, 101):
    numbers.append(i) #-> tu cu napunit listu od 1 do 100
    
#for i in range(1,101,2):
    #numbers.append(i)  #-> tu cu napunit listu sa svakim drugim brojem 2..4..6..8..
    
for number in numbers:
    print(number)
    

    
