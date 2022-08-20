import random
n = 7
l = ['--'] * (n ** 2)
blocks = [5, 6, 7, 15, 16, 17, 20, 21, 29, 32, 33, 34, 35, 43, 44, 45]
win = False
dice = [1,2,3,4,5,6]
dice_num = 0
playerA_pos = 0
playerB_pos = 0
playerA_point =0
playerB_point =0

def display(playerA,playerB):
    for i in range(len(l)):
        if i % n == 0:
            print()
        if i+1 in blocks:
            l[i]="**"
            print("**",end="\t")
        elif i==playerA == playerB == 0:
            l[i]="AB"
            print("AB",end="\t")
        elif i == playerA:
            l[i] = "A_"
            print("A_",end="\t")
        elif i == playerB:
            l[i] = "_B"
            print("_B",end="\t")
        elif i== n*n-1:
            l[i] ="Go"
            print("Go", end="\t")
        else:
            l[i] = "--"
            print("--", end="\t")
    l[n ** 2 - 1] = ""

    print()


def move(direction, dice_num, playerPos):
    if direction == "8" and playerPos - dice_num * n >=0 and l[playerPos - dice_num * n]!="**":
        playerPos = playerPos - dice_num * n
        return  playerPos
    elif direction == "2" and playerPos + dice_num * n <= n*n-1 and l[playerPos + dice_num * n]!="**":
        playerPos += dice_num * n
        return playerPos
    elif direction == "4" and (playerPos-dice_num+1) - (playerPos//n)*n >= 0 and l[playerPos - dice_num ]!="**":
        playerPos -= dice_num
        return playerPos
    elif direction == "6" and (playerPos+dice_num+1) - (playerPos//n)*n <= n and l[playerPos + dice_num ]!="**":
        playerPos += dice_num
        return playerPos
    else:
        return  playerPos

display(playerA_pos,playerB_pos)
tmp = 0
while not win:

#playerA
    direction = str(input("You are the player A,Type a direction or press enter to skip \n"))
    print("rolling dice....")
    dice_num =random.choice(dice)
    print("your dice number is :{}".format(dice_num))
    tmp = playerA_pos
    playerA_pos = move(direction, dice_num,playerA_pos)
    if playerA_pos == tmp:
        print("invalid dice number , player unable to move")
    if playerA_pos == playerB_pos!=0:
        playerB_pos = 0
        print("playerA get one point")
        playerA_point+=1
#    print(playerA_pos,playerB_pos)
    display(playerA_pos,playerB_pos)
    if playerA_pos == n * n - 1:
        win = True
        print("PlayerA wins the game, congrats!")
        print("total points got: ")
        print("playerA: ",playerA_point)
        print("playerB: ",playerB_point)
        break
#    print(l)
#playerB
    direction = str(input("You are the player B,Type a direction or press enter to skip \n"))
    print("rolling dice....")
    dice_num =random.choice(dice)
    print("your dice number is :{}".format(dice_num))
    tmp = playerB_pos
    playerB_pos=move(direction, dice_num,playerB_pos)
    if playerB_pos == tmp:
        print("invalid dice number , player unable to move")
    if playerB_pos == playerA_pos!=0:
        playerA_pos = 0
        print("playerB get one point")
        playerB_point+=1
#    print(playerA_pos,playerB_pos)

    display(playerA_pos,playerB_pos)
    if playerB_pos == n * n - 1:
        win = True
        print("PlayerB wins the game, congrats!")
        print("total points got: ")
        print("playerA: ",playerA_point)
        print("playerB: ",playerB_point)
        break
#    print(l)

