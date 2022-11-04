# pip install matplotlib opencv-python
import matplotlib.pyplot as plt
import cv2
Total = 0
while True:
    a = """
    
    1.fruits and vegtables
    2.home needs
    3.NonVeg
    4.snacks
    5.break
    
    """
    print(a)
    data = int(input("enter ur chooice :"))
    if data == 1:
        vf = cv2.imread("vf.jpg")
        vf = cv2.cvtColor(vf,cv2.COLOR_BGR2RGB)
        plt.imshow(vf)
    #     plt.axes("off")
        plt.show()
        
        b = """
        
        1. fruits
        2. vegtables
        3. dryfruits
        4. break
        
        """
        print(b)
        c = int(input("enter ur f/v/d :"))
        if c == 1:
            fv = cv2.imread("fv.jpg")
            fv = cv2.cvtColor(fv,cv2.COLOR_BGR2RGB)
            plt.imshow(fv)
            plt.show()
            print("fruits")
            print("-"*19)
           
            d = """
            
            1.apple
            2.banana
            3.exit
            
            """ 
            print(d)
            e  = int(input("enter fruit."))
            if e == 1:
                fv = cv2.imread("apple.jpeg")
                fv = cv2.cvtColor(fv,cv2.COLOR_BGR2RGB)
                plt.imshow(fv)
                plt.show()
                print("Price of 1 kg of Apples ",100,"/-")
                p_a = 100
                qty = int(input("enter ur qty for apple :"))
                Price = p_a*qty
                Total+=Price  # total = total+price
                shop = """
                1. shopping continue
                2. end shopping
                """
                print(shop)
                f = int(input("enter shop."))
                if f == 1:
                    print(b)
                    print(c)
                elif f == 2:
                    print("Total :",Total)
                    break
                    
            elif e == 2:
                pass
            elif e == 3:
                break
            else:
                print("invalid option")
                    
        elif c == 2:
            pass
        elif c == 3:
            pass
        elif c == 4:
            break
        else:
            print("Invalid input.")
    
    
    
    
    
    elif data == 5:
        break
        
