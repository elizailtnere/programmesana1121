def rezultats(sk1, sk2): 
    if sk1<6 and sk2<6: 
        rez = sk1*sk2
    else: 
        rez = sk1+sk2
    return rez

for skaitlis in range(1, 11, 2): #range - funkcija, kas saista skaitļus
    for otrs in range(2, 10, 2): 
        print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts:", rezultats(skaitlis, otrs))


skaitlis1 = 7
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1, "otrais skailtis:", skaitlis2, "rezultats:", rezultats(skaitlis1,skaitlis2) )



pirmais = "6"

print(pirmais)

vards2="nē"

print(pirmais + vards2)


def zvaigznites1(skaits):
    for rindasNr in range(1, skaits+1):
        for zvaigzne in range(rindasNr):
            print("*", end="")
        print("")
    
zvaigznites1(5)

def zvaigznites2(skaits):
    for rindasNr in range(1, skaits+1):
        print("*"*rindasNr)

zvaigznites2(3)