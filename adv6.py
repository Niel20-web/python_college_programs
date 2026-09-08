# weekday program checker
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
while True:
    try:
        day = input("enter a day: ").strip().lower()
        if day in days:
            if day != "saturday" and day != "sunday":
                print(day,"is a weekday")
            else:
                print(day,"is a weekend")
        else:
            print("invalid day")
    finally:
        ch = input("do you want to continue? (y/n): ").strip().lower()
        if ch == "y":
            continue
        else:
            print("thankyou for choosing our program (^_^ !!!! XD ❤️❤️)")
            break
        
