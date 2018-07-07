x = ['st','nd','rd','th']
print("Enter Date in this format: '2 nd JUN 2018' ")
d = str(input("Enter date :"))
m = str(input("Enter month :"))
y = str(input("Enter Year :"))


def valdiate(day,month):
    if (int(day) >0 and int(day) <32):
        if (int(month) > 0 and int(month) < 13):
            return print(dat_subscript(d,m,y))
        else:
            return print("Enter proper month")
    print("Enter proper Date")



def dat_subscript(day,month,year):
    if int(day) == 1:
        return (str(day) + x[0] +" "+month+" "+year)
    elif int(day) == 2:
        return (str(day)+x[1]+" "+month+" "+year)
    elif int(day) == 3:
        return (str(day) + x[2]+" "+month+" "+year)
    else:
        return (str(day)+x[3]+" "+month+" "+year)

valdiate(d,m)
'''
val=str(input())
val=val.split(" ")
for i in range(1,5):
    print(i,x[i-1])
print(val)'''