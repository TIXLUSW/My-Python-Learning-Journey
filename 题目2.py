# 数字猜谜游戏
import random
# 生成随机数字
secret_number = random.randint(1, 100)
attempts = 7  # 总尝试次数
current_attempt = 1  # 当前尝试次数
print("欢迎来到数字猜谜游戏!")
print("我已经想了一个1到100之间的数字，你有7次机会来猜中它。")
# 使用while循环控制游戏流程
while current_attempt <= attempts:
    print(f"\n第{current_attempt}次尝试，你还剩{attempts - current_attempt}次机会。")
    # 获取用户输入
    try:
        guess = int(input("请输入你猜的数字: "))
    except ValueError:
        print("请输入一个有效的整数!")
        continue
    # 判断猜测结果
    if guess == secret_number:
        print(f"恭喜你! 你在第{current_attempt}次尝试时猜中了数字 {secret_number}!")
        break
    elif guess < secret_number:
        print("你猜的数字太小了，再试试!")
    else:
        print("你猜的数字太大了，再试试!")
    current_attempt += 1
# 如果尝试次数用完仍未猜中
if current_attempt > attempts:
    print(f"\n游戏结束! 你没有在7次内猜中数字。正确答案是: {secret_number}")
