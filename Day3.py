n = int(input("Type an integer : "))

if n in range(1,101):
    if n % 2 == 0:
        if n in range(2,6):
            print("Not weird")

        elif n in range(6,21):
            print("Weird")

        elif n > 20:
            print("Not weird")

    else:
        print("Weird")

        
