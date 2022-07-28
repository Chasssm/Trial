import time
import random
red_win = 0
blue_win = 0

for i in range(3):
    red_Blood = random.randint(200,300)
    blue_Blood = random.randint(200,300)
    red_Attack = random.randint(50,100)
    blue_Attack = random.randint(50,100)
    
    print('****************Now is Turn '+str(i+1)+'***************')
    print('[Red Side]\n'+'Blood:'+str(red_Blood)+'\nAttack:'+str(red_Attack))
    #time.sleep(1.5)
    print('\n[Blue Side]\n'+'Blood:'+str(blue_Blood)+'\nAttack:'+str(blue_Attack))
    print('======================================')
    #time.sleep(1.5)

    while(red_Blood>=0) and (blue_Blood>=0):
        red_Blood = red_Blood - blue_Attack
        blue_Blood = blue_Blood - red_Attack

        print('Red attack Blue,[Red] remaining '+str(red_Blood))
        print('Blue defends, [Blue] remaining ' + str(blue_Blood))
        print('======================================')
        #time.sleep(1.5)

    if (red_Blood > blue_Blood) and (red_Blood >= 0):
        red_win = red_win + 1
        print('Red Wins! Number of red winning is '+str(red_win)+'\n')
    elif (red_Blood<blue_Blood) and (blue_Blood >= 0):
        blue_win = blue_win + 1
        print('Blue Wins! Number of blue winning is '+str(blue_win)+'\n')
    else:
        print('Equal!\n')

print('**********************Now is the OUTPUT********************')
print('Red wins '+str(red_win)+' times')
print('Blue wins '+str(blue_win)+' times')
if red_win == blue_win:
    print('Even!')
elif red_win > blue_win:
    print('RED WINS!')
else:
    print('BLUE WINS!')


# Note: How to formatted
# a = 1000
# b = 2000
# print('Number a is %d and number b is %d' % (a, b))