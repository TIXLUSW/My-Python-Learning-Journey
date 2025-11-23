# 学生成绩管理系统
# 初始化变量
students = []  # 存储学生信息的列表
grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}  # 等级统计字典
# 输入2名学生的信息
for i in range(2):
    print(f"请输入第{i + 1}名学生的信息:")
    name = input("姓名: ")
    chinese = float(input("语文成绩: "))
    math = float(input("数学成绩: "))
    english = float(input("英语成绩: "))
    # 计算总分和平均分
    total = chinese + math + english
    average = total / 3
    # 根据平均分确定等级
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    # 更新等级统计
    grade_count[grade] += 1
    # 将学生信息添加到列表
    students.append((name, chinese, math, english, total, average, grade))
# 输出结果
print("\n学生成绩统计结果:")
print("姓名\t语文\t数学\t英语\t总分\t平均分\t等级")
for student in students:
    print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]:.2f}\t{student[6]}")
