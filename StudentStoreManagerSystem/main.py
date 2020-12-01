# 导入系统管理模块
from ManagerStoreSystem import *
# 启动管理系统
# 保证是当前文件运行才启动管理系统
if __name__ == '__main__':
    student_maneger = StoreManagerSystem()
    student_maneger.run()