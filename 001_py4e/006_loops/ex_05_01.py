switch = None
while True:
    switch = input("Enter a number: ")
    try: 
        print("your input was a number", float(switch) )      
    except:
        print("Invalid input")
    if switch == "done":
        break
print(switch)