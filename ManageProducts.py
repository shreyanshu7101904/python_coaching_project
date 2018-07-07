import json
import random



ProductsTblDict = dict()
with open("products.json", mode="r") as fp1:
    ProductsTblDict = json.load(fp1)

edt_products = ProductsTblDict.keys()
product_attr = list(ProductsTblDict['R1'].keys())



def update_file():
    """Function for Updating Product.Json file"""
    with open("products.json", mode="w") as fp1:
         json.dump(ProductsTblDict, fp1, indent=2)


def display():
    """Function for displaying the product name"""
    for i in edt_products:
        print(ProductsTblDict[i]["ProductName"])


def validity_check(name):
    """Checks for the product name exist in the dictionary"""
    for i in edt_products:
         if ProductsTblDict[i]["ProductName"] == name:
            return i
    return ""


def edit_products(pname):
    """Function for Editing the product"""
    for i in product_attr:
        print("value before editing", i, ProductsTblDict[pname][i])
        print("Enter new value else Press Enter")
        a = input()
        if a != '':
            ProductsTblDict[pname][i] = a
    update_file()


def add_product(name):
    """This function adds new product"""
    dummy_dict = dict()

    R = list(edt_products)[0]+str(random.randint(2,100))
    print("please fill out the product details")
    for i in product_attr:
        if i == "ProductName":
            dummy_dict[i]=name
        else:
            print("enter", i, ":")
            x = input()
            dummy_dict[i] = x
    ProductsTblDict[R] = dict()
    ProductsTblDict[R].update(dummy_dict)
    update_file()


def delete(x):
    """This function deletes the product"""
    del ProductsTblDict[x]
    print("Product Deleted sucessfully")
    update_file()




while 1:
    ch = input(
    '''Choose
    1=display
    2=edit
    3=add
    4=delete
    0=stop
    ''')
    if ch == '0' :
        break
    elif ch == '1':
        print("*"*5,'All products',"*"*5)
        display()
    elif ch == '2':

        print("*"*5,'Edit a product',"*"*5)
        print('Enter product Name.:')
        in1 = input()
        y = validity_check(in1)
        if y != "":
            edit_products(y)
        else:
            print("product is not there")
    elif ch == '3':
        print("*"*5, 'Add a new product', "*"*5)
        print('Enter Product Name')
        while 1:
            z = input()
            if z != "":
                if validity_check(z) != "":
                    print("Product is already there")
                    break
                else:
                    add_product(z)
                    break
            else:
                print("Please Enter Proper Name")
    elif ch == '4':
        print("*"*5, 'Delete a product', "*"*5)
        a = input("enter a product name to delete")
        if validity_check(a) != "":
            d = validity_check(a)
            delete(d)
        else:
            print("Product Doesn't Exist")

    else:
        print('Enter only 0 - 4 to access features')
