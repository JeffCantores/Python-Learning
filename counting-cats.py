print('How many cats do you have?')
numCats = input()
if(numCats[0]) == "-":
    print("Invalid Input.")
else:    
    try:
        if int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('That is not a lot of cats.')
    except ValueError:
        print('Invalid input.')
        
