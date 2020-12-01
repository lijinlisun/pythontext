"""
# 1.定义类
class A(object):
    a = 0
    def __init__(self):
        self.b = 1

aa = A()
# 返回类内部所有属性和方法定义的字典
print(aa.__dict__)
# 返回实例属性和值组成的字典
print(A.__dict__)
"""
# 导入系统管理模块
from managerSystem import *
# 启动管理系统
# 保证是当前文件运行才启动管理系统
if __name__ == '__main__':
    student_maneger = StudentManager()
    student_maneger.run()