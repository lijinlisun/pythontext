class Student(object):
    def __init__(self, num, name, english, math, cyy, sum, avr):
        self.num =num
        self.name = name
        self.english = english
        self.math = math
        self.cyy = cyy
        self.sum = sum
        self.avr = avr

    def __str__(self):
        return f'学号：{self.num}、姓名：{self.name}、英语：{self.english}、数学：{self.math}、c语言：{self.cyy}、总分：{self.sum}、平均值：{self.avr}'



if __name__ == '__main__':
    aa = Student(1,'aa',74,96,78)
    print(aa)