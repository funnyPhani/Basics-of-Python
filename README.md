# Basics-of-Python

```python
# age based shopping

name = input("enter ur name : ")
age = int(input("enter ur age :"))

if age<10:
    print("-"*50)
    print("Toys Galary".center(75))
    print("-"*50)
    total_price = 0
    while True:
        data = """

        1. a toy
        2. b toy 
        3. c toy
        4. break
        """
        print(data)
        intrest = input("enter ur chooice :")
        if intrest == "1":
            price_1 = 5
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}")
        elif intrest == "2":
            price_1 = 10
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}")
            
        elif intrest == "3":
            price_1 = 15
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty, "/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}")

        elif intrest == "4":
            print(f"ur final bill is {total_price}")
            break
        else:
            print("invaild option")
elif age>10 and age<20:
    print("-"*50)
    print("Toys Galary".center(75))
    print("-"*50)
    total_price = 0
    while True:
        data = """

        1. playstation
        2. xbox 
        3. mobile
        4. break
        """
        print(data)
        intrest = input("enter ur chooice :")
        if intrest == "1":
            price_1 = 50
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}/-")
            shop = input("do u want to comtinie ...y/n :")
            if shop == "y":
                continue
            else:
                print(f"the {name}'s bill upto date is {total_price} /-")
                break
        elif intrest == "2":
            price_1 = 100
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}/-")
            
        elif intrest == "3":
            price_1 = 150
            qty = int(input("enter the quantity: "))
            amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty, "/-")
            total_price+=(price_1*qty)
            print(f"the {name}'s bill upto date is {total_price}/-")

        elif intrest == "4":
            print(f"ur final bill is {total_price}")
            break
        else:
            print("invaild option")
    


```

```python

# overall shopping.

name = input("enter ur name : ")
age = int(input("enter ur age :"))
total_price = 0
while True:
    main = """
    
    1. kids
    2. teens
    3. adults
    4. exit
    
    """
    print(main)
    btn = input("entrerur dataaaaa :")

    if btn == "1":
        print("-"*50)
        print("Toys Galary".center(75))
        print("-"*50)
        
        while True:
            data = """

            1. a toy
            2. b toy 
            3. c toy
            4. break
            """
            print(data)
            intrest = input("enter ur chooice :")
            if intrest == "1":
                price_1 = 5
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}")
            elif intrest == "2":
                price_1 = 10
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}")

            elif intrest == "3":
                price_1 = 15
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty, "/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}")

            elif intrest == "4":
                print(f"ur final bill is {total_price}")
                break
            else:
                print("invaild option")
    elif btn == "2":
        print("-"*50)
        print("Toys Galary".center(75))
        print("-"*50)
        
        while True:
            data = """

            1. playstation
            2. xbox 
            3. mobile
            4. break
            """
            print(data)
            intrest = input("enter ur chooice :")
            if intrest == "1":
                price_1 = 50
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")
                shop = input("do u want to comtinie ...y/n :")
                if shop == "y":
                    continue
                else:
                    print(f"the {name}'s bill upto date is {total_price} /-")
                    break
            elif intrest == "2":
                price_1 = 100
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")

            elif intrest == "3":
                brand = input("enter ur brand ")
                price_1 = 150
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty, "/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")

            elif intrest == "4":
                print(f"ur final bill is {total_price}")
                break
            else:
                print("invaild option")
    elif btn == "3":
        print("-"*50)
        print("Toys Galary".center(75))
        print("-"*50)
        
        while True:
            data = """

            1. lapi
            2. mouse 
            3. ipad
            4. break
            """
            print(data)
            intrest = input("enter ur chooice :")
            if intrest == "1":
                price_1 = 50
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")
                shop = input("do u want to comtinie ...y/n :")
                if shop == "y":
                    continue
                else:
                    print(f"the {name}'s bill upto date is {total_price} /-")
                    break
            elif intrest == "2":
                price_1 = 100
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty ,"/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")

            elif intrest == "3":
                price_1 = 150
                qty = int(input("enter the quantity: "))
                amnt = print(f"the amnt is option :{intrest} qty : {qty}:",price_1*qty, "/-")
                total_price+=(price_1*qty)
                print(f"the {name}'s bill upto date is {total_price}/-")

            elif intrest == "4":
                print(f"ur final bill is {total_price}")
                break
            else:
                print("invaild option")
                
    elif btn == "4":
        print(f"ur {name}'s final bill is {total_price}/-")
        break
    else:
        print("Inavild optin")
    


```
