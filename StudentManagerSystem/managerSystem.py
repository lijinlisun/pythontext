from student import *
class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一、程序入口函数
    def run(self):
        # 1.加载学员信息
         self.load_student()
         while True:
            #  2.显示功能菜单
                self.show_menu()
                # 3.用户输入目标功能序号
                menu_name = int(input('请输入您需要的功能序号：'))
                # 4.根据用户输入的序号执行不同的功能
                if menu_name == 1:
                    self.add_student()
                elif menu_name == 2:
                    self.del_student()
                elif menu_name == 3:
                    self.modify_student()
                elif menu_name == 4:
                    self.search_student()
                elif menu_name == 5:
                    self.print_student()
                elif menu_name == 6:
                    self.save_student()
                elif menu_name == 7:
                    exit_info = input('确定要退出吗？yes? or no ?')
                    if exit_info == 'yes':
                        break
                    else:
                        print('输入有误')

    # 二、系统功能函数
    # 2.1显示
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员')
        print('4.查询学员')
        print('5.显示学员')
        print('6.保存学员')
        print('7.退出系统')

    # 2.2添加
    def add_student(self):
        num  = input('学号：')
        name = input('姓名：')
        sex = input('性别：')
        age = input('年龄：')
        tel = input('电话：')
        student = Student(num, name, sex, age, tel)
        self.student_list.append(student)
        print(student)
    # 2.3删除
    def del_student(self):
        del_name = input('请输入要删除学生的姓名：')
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print('删除成功')
                break
        else:
            print('查无此人！')

    # 2.4修改
    def modify_student(self):
        modify_name = input('请输入要修改信息学生的姓名：')
        for i in self.student_list:
            if i.name == modify_name:
                i.num = input('请输入新的学号：')
                i.name = input('请输入新的姓名：')
                i.sex = input('请输入新的性别：')
                i.tel = input('请输入新的手机号：')
                print(f'修改该学员信息成功！学号：{i.num},姓名：{i.name},性别：{i.gender},年龄：{i.age},电话：{i.tel}')
                break
        else:
            print('查无此人！')

    # 2.5查询
    def search_student(self):
        search_name = input('请输入要查询信息学生的姓名：')
        for i in self.student_list:
            if i.name == search_name:
                print(f'查询成功！学号：{i.num},姓名：{i.name},性别：{i.gender},年龄：{i.age},电话：{i.tel}')
                break
            else:
                print('查无此人！')

    # 2.6显示
    def print_student(self):
        for i in self.student_list:
                print('学号\t姓名\t性别\t年龄\t电话')
                print(f'{i.num}\t{i.name}\t{i.gender}\t{i.age}\t{i.tel}')
                break

    # 2.7保存
    def save_student(self):
        # 1.打开文件
        f = open('student.data', 'w')
        # 2.文件写入学员数据
        # 注：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成字符串才能文件写入数据
        # 2、1[学员对象]转换成[字典]
        new_list = [i.__dict__ for i in self.student_list]
        # 2、2文件写入字符串数据
        f.write(str(new_list))
        # 3.关闭文件
        f.close()

    # 2.8加载

    def load_student(self):
        # 1、打开文件
        try:
            f = open('student.data', 'r')
        except:
            f =open('student.data', 'w')
        else:
            # 2、读取数据 ：文件读取的数据还原列表类型；[{}] 转换[学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['num'], i['name'], i['gender'], i['age'], i['tel']) for i in new_list]
        finally:
            # 3.关闭文件
            f.close()