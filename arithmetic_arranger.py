# This function will receives a list of strings that are arithmetic problems and 
# returns the problems arranged vertically and side-by-side. 
# The function should optionally take a second argument. 
# When the second argument is set to True, the answers will be displayed.

def arithmetic_arranger(a,b=False):
    adet=len(a)
    mesafe=[]
    for i in range(adet):
        a[i]=a[i].split(" ")
        for ii in range(len(a[i])):
            l=len(a[i][ii])
            if len(mesafe)<=i:
                mesafe.insert(i,l)
            elif mesafe[i]<l:
                mesafe[i]=l

    for i in range (adet):
        print( a[i][0].rjust(mesafe[i]+2) ,end="    ")
    print(end="\n")
    for i in range (adet):
        print(a[i][1],a[i][2].rjust(mesafe[i]),end="    ")        
    print(end="\n")
    for i in range (adet):
        print("-"*(mesafe[i]+2),end="    ")        
    print(end="\n")

    if b==True:
        for i in range (adet):
            if a[i][1]=="+":
                Sonuc=int(a[i][0])+int(a[i][2])
            else:
                Sonuc=int(a[i][0])-int(a[i][2])
            print((str(Sonuc)).rjust(mesafe[i]+2),end="    ")        
        print(end="\n") 


# Testpart

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
