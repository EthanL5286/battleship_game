import random
game=input("Do you want to play against someone else or the computer,solo or co-op")
if game=="solo":
    ship1=random.randint(1,5)
    ship4=random.randint(1,5)
    if ship1==1:
        ship1Cords1="b3"
        ship1Cords2="b4"
        ship1Cords3="b5"
    
        ship2Cords1="c5"
        ship2Cords2="d6"
        ship2Cords3="e7"

        ship3Cords1="j1"
        ship3Cords2="j2"
        ship3Cords3="j3"
        ship3Cords4="j4"
    elif ship1==2:
        ship1Cords1="d3"
        ship1Cords2="d4"
        ship1Cords3="d5"
    
        ship2Cords1="a1"
        ship2Cords2="b1"
        ship2Cords3="c1"

        ship3Cords1="i6"
        ship3Cords2="i7"
        ship3Cords3="i8"
        ship3Cords4="i9"
        
