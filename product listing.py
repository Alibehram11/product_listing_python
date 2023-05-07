product = {
    "name":"",
    "price":"",
    "Number of products":"",
}

s = 0

while s < 6:
    if s == 0:
        name = str(input("what is the name of the product:"))
        product["name"]=name
        s+=1
    if s == 1:
        price = str(input("Enter the price of the product:"))
        product["price"]=price
        s+=1
    if s == 2:
        number = str(input("Enter the number of products:"))
        product["Number of products"]=number
        s+=1
    if s == 3:
        change = int(input("If there is a structure you want to change, press 1, otherwise press 2:"))    
        if change == 1:
            Which = int(input("which product you will change (1 e if you will change the name) (2 e if you will change the price) (press 3 if you will change the number of products):"))
            if Which == 1:
                print(product["name"])
                name1 = str(input("what would you replace it with:"))
                product["name"]=name1
            if Which == 2:
                print(product["price"])
                price1 = str(input("what would you replace it with:"))
                product["price"]=price1
            if Which == 3:
                print(product["Number of products"])
                number1 = str(input("what would you replace it with:"))
                product["Number of products"]=number1
    if change == 2:
        s+=1      
    if  s == 4:
        add = int(input("If you want to add a category, press 1, if not, press 2:"))
        if add == 1:
            category = str(input("The name of the category you want to add:"))
            category1 = str(input("What you want to add to the category:"))
            product[category]=category
    if add == 2:
        s+=1
        break

s+1
print(product)
