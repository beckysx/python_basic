import random
"""
1 出拳
    玩家： 手动输入
    电脑：1 固定：剪刀 2 随机
2 裁判
    玩家胜
    平局
    电脑胜
"""
player = int(input("what's your choice? 0--stone 1--scissor 2--paper : "))
computer = random.randint(0,2)
if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print("you win")
elif player == computer:
    print("平局")
else:
    print('computer wins')

