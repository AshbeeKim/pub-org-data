import os
import sys
import pandas as pd

'''
# pub_org_data
#     ├ scrap
#     ├ define
#     ├ compare
# ~~~~~~~~~~~~~
반복 작업의 구간을 각 모듈별로 처리되도록 하려면,
'''
print('+'*50, '\n\n\n')

if __name__ == '__main__':
    while True:
        task_name = input('Task : ')
        if task_name=='compare':    # 비교 업무 진행 시, # script로 생성한 파일 옮겨야 함.
            # from config.compare import Compare
            # 바로 이어지고 받아지도록 하려면, Compare 안에도 main.py가 있어야 함.
            # os.getcwd=='/Volumes/WORK/OpenData'
            # import script.config.repeatContents as IC
            print(IC.NessFromJSON(f'{os.getcwd()}/{task_name}')[0])

        elif task_name == 'define': # 정의 업무 진행 시
            print(f"\n\n{'='*50} define {'='*50}\n\n")
            from config import define
            # import define만 해도 바로 조회가 가능하도록, config.define.__init__.py 작성
            
            while True: # 값 비교, 추가 확인 등의 데이터 세부 내용 확인이 필요한 경우
                checkups = input("내용을 자세히 확인하겠습니까?(True: 1, False: 0)\t")
                
                try:
                    int(checkups)
                except:
                    checkups = checkups.lower()
                    if (checkups=='t') or (checkups=='true'):
                        checkups = 1
                    elif (checkups=='f') or (checkups=='false'):
                        break
                    else:
                        print('"True/False" 로 된 값을 입력해주세요.')
                        continue
                
                if checkups:
                    from config.define import kr_lens
                    from config.define import kr_unqs
                    
            print(f"\n\n{'='*50} finished {'='*50}\n\n")
        
        # another_check = input(f"추가적으로 확인할 사항이 있습니까?\t")    # script랑 연결할 때 사용
        break