
def add_time(saat,ekle,gun=False):
    Hafta=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    g=9
    if gun:
        gun=gun.capitalize()
        g=Hafta.index(gun)

    saat=saat.upper()
    AM=0
    if saat.endswith("AM"):
        AM=1
        saat=saat.rstrip("AM")
    else:
        saat=saat.rstrip("PM")
    saat=saat.split(":")
    ekle=ekle.split(":")

    d=int(saat[1])+int(ekle[1])
    s=int(saat[0])+int(ekle[0])+int(d/60)
    dd=str(d%60)
    ss=s%12
    if ss==0: ss=str(12)
    else: ss=str(ss)
    gg=int(s/24)
    if AM==0 and (AM+int(s/12))%2==1:
        gg +=1
    AM=(AM+int(s/12))%2

    AMPM=["PM","AM"]
    zaman=ss.rjust(2," ")+":"+dd.rjust(2,"0")

    print("# Returns: ",zaman,  AMPM[AM], end=" ")
    if g!=9 :   print( "," , Hafta[(g+gg)%7], end=" ")
    if gg>=2:   print("(",gg ,"days later)" , end=" ")
    elif gg==1: print("(next day)" , end=" ")
    print(end="\n") 

     
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
