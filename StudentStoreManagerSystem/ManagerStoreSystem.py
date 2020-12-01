# 学生成绩管理系统
from student import *

def __init__(self):
    # 存储数据所用的列表
    self.student_store_list = []


class StoreManagerSystem(object):
    def __init__(self):
        self.student_store_list = []

    def run(self):
        self.load_store()
        while True:
            self.show_menu()
            menu_name = int(input('请输入您需要的功能序号：'))
            if menu_name == 1:
                self.print_store()
            if menu_name == 2:
                self.add_store()
            if menu_name == 3:
                self.del_store()
            if menu_name == 4:
                self.modify_store()
            if menu_name == 5:
                self.search_store()
            if menu_name == 6:
                self.count_store()
            if menu_name == 7:
                self.save_student()
            if menu_name == 8:
                exit_info = input('确定要退出吗？yes? or no?')
                if exit_info == 'yes':
                    break
                else:
                    print('输入有误')

    # 显示
    def show_menu(self):
        print('请选择如下功能：')
        print('1.显示所有显示信息')
        print('2.添加成绩')
        print('3.删除成绩')
        print('4.修改成绩')
        print('5.查询成绩')
        print('6.统计')
        print('7.保存')
        print('8.退出')

    # 显示
    def print_store(self):
        for i in self.student_store_list:
            print(f'学号：{i.num}、姓名：{i.name}、英语：{i.english}、数学：{i.math}、c语言：{i.cyy}、总分：{i.sum}、平均值：{i.avr}')

    # 添加
    def add_store(self):
        num = input('学号：')
        name = input('姓名：')
        english = int(input('英语：'))
        math = int(input('高等数学：'))
        cyy = int(input('c语言：'))
        sum = english + math + cyy
        avr = sum/3.0
        student = Student(num, name, english, math, cyy, sum, avr)
        self.student_store_list.append(student)
        print(student)

    # 删除
    def del_store(self):
        del_name = input('请输入要删除成绩的学生姓名：')
        for i in self.student_store_list:
            if i.name == del_name:
                self.student_store_list.remove(i)
                print('删除成功')
                break
        else:
            print('查无此人！')

    # 修改
    def modify_store(self):
        modify_name = input('请输入要修改成绩的学生姓名：')
        for i in self.student_store_list:
            if i.name == modify_name:
                i.english = int(input('请输入新的英语成绩：'))
                i.math = int(input('请输入新的高等数学成绩：'))
                i.cyy = int(input('请输入新的c语言成绩：'))
                i.sum = i.english + i.math + i.cyy
                i.avr = i.sum/3.0
                print(f'修改成功!学号：{i.num}、姓名：{i.name}、英语：{i.english}、高等数学：{i.math}、c语言：{i.cyy}、总分：{i.sum}、平均值：{i.avr}')
                break
        else:
            print('查无此人！')

     # 查询
    def search_store(self):
        search_name = input('请输入要查询成绩的学生姓名：')
        for i in self.student_store_list:
            if i.name == search_name:
                print('学号\t\t姓名\t\t英语\t\t高等数学\t\tc语言\t\t总分\t\t平均值')
                print(f'{i.num}\t\t{i.name}\t\t{i.english}\t\t{i.math}\t\t{i.cyy}\t\t{i.sum}\t\t{i.avr}')
                break
        else:
            print('查无此人！')

    # 排序\统计
    def count_store(self):
        sum_count = []
        english = []
        math = []
        cyy = []
        for i in self.student_store_list:
            english.append(i.english)
            math.append(i.math)
            cyy.append(i.cyy)
            sum_count.append(i.sum)
            english = sorted(english)
            english = english[::-1]
            math = sorted(math)
            math = math[::-1]
            cyy = sorted(cyy)
            cyy = cyy[::-1]
        print(f'按英语成绩从大到小排序为：')
        # print(english)
        for j in english:
            for i in self.student_store_list:
                if j == i.english:
                    print(f'学号：{i.num}、姓名：{i.name}、英语：{i.english}、数学：{i.math}、c语言：{i.cyy}、总分：{i.sum}、平均值：{i.avr}')
                    break
        print(f'按高等数学成绩从大到小排序为：')
        for j in math:
            for i in self.student_store_list:
                if j == i.math:
                    print(f'学号：{i.num}、姓名：{i.name}、英语：{i.english}、数学：{i.math}、c语言：{i.cyy}、总分：{i.sum}、平均值：{i.avr}')
                    break
        print(f'按英语成绩从大到小排序为：')
        # print(english)
        for j in cyy:
            for i in self.student_store_list:
                if j == i.cyy:
                    print(f'学号：{i.num}、姓名：{i.name}、英语：{i.english}、数学：{i.math}、c语言：{i.cyy}、总分：{i.sum}、平均值：{i.avr}')
                    break






            # math = sorted(math)
            # cyy = sorted(cyy)



    # 保存
    def save_student(self):
        # 1.打开文件
        f = open('studentstore.data', 'w')
        # 2.文件写入学员数据
        # 注：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成字符串才能文件写入数据
        # 2、1[学员对象]转换成[字典]
        new_list = [i.__dict__ for i in self.student_store_list]
        # 2、2文件写入字符串数据
        f.write(str(new_list))
        # 3.关闭文件
        f.close()

    # 加载
    def load_store(self):
        # 1、打开文件
        try:
            f = open('studentstore.data', 'r')
        except:
            f = open('studentstore.data', 'w')
        else:
            # 2、读取数据 ：文件读取的数据还原列表类型；[{}] 转换[学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_store_list = [Student(i['num'], i['name'], i['english'], i['math'], i['cyy'], i['num'], i['avr']) for i in new_list]
        finally:
            # 3.关闭文件
            f.close()
