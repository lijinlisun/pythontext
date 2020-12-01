class Student(object):
    def __init__(self, num, name, gender, age, tel):
        self.num = num
        self.name = name
        self.gender = gender
        self.age = age
        self.tel =tel

    def __str__(self):
        return f'学号：{self.num},姓名：{self.name},性别：{self.gender},年龄：{self.age},电话：{self.tel}'


if __name__ == '__main__':
    aa =Student(1, 'aa', '女', '16', '1111')
    print(aa)