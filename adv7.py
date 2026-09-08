#set operations
while True:
    set1 = set()
    set2 = set()
    n=int(input("enter the number of elements in set1: "))
    for i in range(n):
        element=input("enter the element:")
        set1.add(element)

    m=int(input("enter the number of elements in set2: "))
    for j in range(m):
        element=input("enter the element:")
        set2.add(element)

    ch=input("enter the operation you want to perform (union,intersection,difference): ").strip().lower()
    match ch:
        case "union":
            new_set=set1.union(set2)
            print("union is:",new_set)

        case "intersection":
            new_set=set1.intersection(set2)
            print("intersection is:",new_set)

        case "difference":
            new_set=set1.difference(set2)
            print("difference is:",new_set)
    choice=input("do you want to continue? (y/n): ").strip().lower()
    if choice=="y":
        continue
    else:
        print("thankyou for choosing our program (^_^ !!!! XD ❤️❤️)")
        break
    
