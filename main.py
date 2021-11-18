import os
import sys
# from config.kr_csv import WIN_CSV

# WIN_CSV(4, 0).print_kr_csv()
print(os.getcwd())
# print(os.name(__name__))
print('+'*50, '\n\n\n')
if __name__ == '__main__':
    task_name = input('Task : ')
    if task_name=='script':
        # os.getcwd=='/Volumes/WORK/OpenData'
        import script.config.repeatContents as IC
        # 바로 이어지고 받아지도록 하려면, script 안에도 main.py가 있어야 함.
        print(IC.NessFromJSON(f'{os.getcwd()}/{task_name}')[0])
        # if __name__ == '__main__':
        # print(os.name(__name__)) 