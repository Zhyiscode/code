import random
min_val = 1
max_val = 6

roll_again = 'yes'
while roll_again == 'yes' or roll_again == 'y':
    print('开始掷色子')
    print('色子的数值为：')

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again = input('是否继续掷色子')
