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
print(f"\n\n\t{'+'*70}\t\n")

if __name__ == '__main__':
    # os.getcwd=='/Volumes/WORK/OpenData'
    while True:
        task_name = input('Task : ')
        if task_name=='compare':    # 비교 업무 진행 시, # script로 생성한 파일 옮겨야 함.
            from config import compare
            # import script.config.repeatContents as IC

        elif task_name == 'define': # 정의 업무 진행 시
            print(f"\n\n\t {'='*30} define {'='*30}\t\n\n")
            from config import define
            # import define만 해도 바로 조회가 가능하도록, config.define.__init__.py 작성
            # 우선 각 테이블로 다를 수 있을 것 같아서, 세부 내용을 확인하겠냐는 질문을 
            # ./config/define/__init__.py에 작성했으나, 내용을 자세히 확인할 경우도 가정하기
            
            while True: # 값 비교, 추가 확인 등의 데이터 세부 내용 확인이 필요한 경우
                # checkups가 script, scraping에서도 반복된다면, 그냥 ./config/checkups.py로 만들기
                # 우선은 보류
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
                    # 어떤 경우에 내용을 자세히 확인해야 했던가를 더 고려해서 작성해야할 듯
                    
            print(f"\n\n\t{'='*30} finished {'='*30}\t\n\n")
        # another_check = input(f"추가적으로 확인할 사항이 있습니까?\t")
        # if another_check  
        # script랑 연결할 때 사용, script가 아니더라도 define에서 단어의 용례를 검색하는 것에 활용해도 좋을 듯?
        break