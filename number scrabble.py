#this is number scrabble game 
#we'll start with a list of 1 to 9 numbers 
# each player will choose a number 
# if one of the players choose three numbers their sum is 15 then the player wins
print("<<welcome to number scrabble>>")
def players() :
    #p1=the first player,p2=the second player,li=the list.
    p1 = input("enter your name player1 : ")
    p2 = input("enter your  name player2 : ")
    li = [1,2,3,4,5,6,7,8,9,]
    print(li)
#players choises
    n1 = int(input(p1+" choose a number from the list : "))
    while n1>=10 or n1<=0 :
        n1 =int(input("choose another number :")) 
    li.remove(n1)
    print(li)

    m1= int(input(p2+ " choose a number from the list : "))
    while m1==n1 or m1>=10 or m1<=0 :
        m1=int(input("choose another number :"))
    li.remove(m1)
    print(li)   

    n2=int(input(p1+" choose a number from the list : "))
    while n2==n1 or n2==m1 or n2>=10 or n2<=0 :
        n2=int(input("choose another number :"))
    li.remove(n2)    
    print(li)

    m2=int(input(p2+" choose a number from the list : "))
    while m2==n1 or m2==m1 or m2==n2 or m2>=10 or m2<=0 :
        m2=int(input("choose another number :"))
    li.remove(m2)
    print(li) 

    n3=int(input(p1+" choose a number from the list : "))
    while n3==n1 or n3==m1 or n3==n2 or n3==m2 or n3>=10 or n3<=0 :
        n3=int(input("choose another number :"))
    li.remove(n3)
    print(li)
    if (n1+n2+n3)==15:
        print(p1+" wins")

    else:    
        m3=int(input(p2+" choose a number from the list : "))
        while m3==n1 or m3==m1 or m3==n2 or m3==m2 or m3==n3 or m3 >=10 or m3<=0 :
            m3=int(input("choose another number : "))
        li.remove(m3)
        print(li)    
        if (m1+m2+m3)==15:
             print(p2+" wins")

        else:
            n4=int(input(p1+" choose a number from the list: "))
            while n4==n1 or n4==m1 or n4==n2 or n4==m2 or n4==n3 or n4==m3 or n4>=10 or n4<=0:
                n4=int(input("choose another number :"))
            li.remove(n4)
            print(li)    
            if(n1+n2+n4)==15 or (n1+n3+n4)==15 or (n2+n3+n4)==15:
                print(p1+" wins")

            else:
                m4=int(input(p2+" choose a number from the list :"))
                while m4==n1 or m4==m1 or m4==n2 or m4==m2 or m4==n3 or m4==m3 or m4==n4 or m4>=10 or m4<=0:
                    m4=int(input("choose another number: "))
                li.remove(m4)
                print(li)
                if (m1+m2+m4)==15 or (m1+m3+m4)==15 or (m2+m3+m4)==15 :
                    print(p2+" wins")

                else:
                    n5=int(input(p1+"choose a number from the list" ))
                    while n5==n1 or n5==m1 or n5==n2 or n5==m2 or n5==n3 or n5==m3 or n5==n4 or n5==m4 or n5>=10 or n5<=0:
                        n5=int(input("choose another number:"))
                    li.remove(n5)
                    print(li)
                    if (n1+n2+n5)==15 or (n1+n3+n5)==15 or (n1+n4+n5)==15 or (n2+n3+n5)==15 or (n2+n4+n5)==15 or (n3+n4+n5)==15:
                        print(p1+" wins")

                    else:
                        print("draw")    
players()                        








