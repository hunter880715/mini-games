# 猜数字游戏

number = 7
guess = 9

print('猜数字游戏开始！\n')
while guess != number:
    guess = int(input('请输入你猜测的数字： '))
    if guess == number:
        print('恭喜你，答对了！\n')
    elif guess > number:
        print('猜的字数大了……\n')
    elif guess < number:
        print('猜的字数小了……\n')
