from datetime import datetime

name = input("Enter your name:")

#List of Items
list_of_items = '''
Rice        Rs 50/kg
Sugar       Rs 40/kg
Salt        Rs 20/kg
Oil         Rs 80/kg
Panner      Rs 110/kg
Maggi       Rs 50/kg
Boost       Rs 90/kg
Daal        Rs 110/kg
Colgate     Rs 90/each

'''

#Decleration 
price = 0
pricelist =[]
totalprice = 0
finalprice= 0
ilist=[]
qlist=[]
plist=[]

#Rates for items
items ={"rice":50,
        "sugar":40,
        "salt":20,
        "oil":80,
        "panner":110,
        "maggi":50,
        "boost":90,
        "daal":110,
        "colgate":90}
option = int(input("For list of items available in the shop press 1:"))
if option == 1:
    print(list_of_items)
    
for i in range(len(items)):
    inp1 = int(input("if you want buy press 1 or 2 for exit:"))
    if inp1 == 2:
        break
    if inp1==1:
        item = input("Enter your items:")
        quantity = int(input("Enter Quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            GST = (totalprice*5)/100
            finalamount = GST+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("Can i bill the items Yes or No:")
    if inp == "yes":
        pass
        if finalamount != 0:
            print(75*" ")
            print("="*33,"S Mart","="*34)
            print(30*" ","Visakhapatnam")
            print(75*" ")
            print("Name:",name,28*" ","Date:",datetime.now())
            print(75*"-")
            print("S.No",10*" ","Items",6*" ","Quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],9*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:",totalprice,"Rs")
            print("GST",59*" ",GST,"Rs")
            print(75*"-")
            print(50*" ","FinalAmount:",finalamount,"Rs")
            print(75*"-")
            print(23*" ","Thankyou and visit again")
            print(75*"-")
      
        
            
            