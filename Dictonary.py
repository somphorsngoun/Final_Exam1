#2
numbers = eval(input())
odd = []
even = []
for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print("Odd numbers:"+"\n"+str(odd))
print("Even numbers:"+"\n"+str(even))
        
#3
studentsData = eval(input())
name = ""
X = 0
if len(studentsData) == 0:
    print("No result")
else:
    Z = studentsData[0]["score"]
    for dic in studentsData:
        if len(studentsData) == 1 or (dic["score"] > 75 and dic["score"] > Z):
            name += dic["name"]
            Z = dic["score"]

        if dic["score"] >= 75:
            X += 1

    print("The best student is",name)
    if X == len(studentsData):
        print("All students have more than 75")

#4
# Enter your code here. Read input from STDIN. Print output to STDOUT
X = True
numberLess = 0
while X:
    number = int(input())
    if number <= 10:
        numberLess += number
    if numberLess == 20:
        print("WIN")
        X = False
    if numberLess > 20:
        print("LOST")
        X = False 
#5
personsInRoom = eval(input())      # it's an array 2D !
newPersonRow = int(input())        # row of the new person to add
newPersonColumn = int(input())     # column of the new person to add
number = 0
letter = personsInRoom[0][-1]==1 and (personsInRoom[1][-1]==personsInRoom[2][-1])
for row in range(len(personsInRoom)):
    for col in range(len(personsInRoom[row])):
        if row == newPersonRow and col == newPersonColumn:
            if personsInRoom[row][col] == 0:
                if letter:
                    print("CANNOT ADD")
                else:
                    print("CAN ADD")
            else:
                print("CANNOT ADD")
            
            