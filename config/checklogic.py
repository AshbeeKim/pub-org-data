# argparser가 익숙해지면 사용하게 될 듯
class CheckUps:
    def __init__(self):
        self.purpose = None

    def details(checkups):
        while True: # 값 비교, 추가 확인 등의 데이터 세부 내용 확인이 필요한 경우
            checkups = input("세부 내용을 확인하겠습니까?(True: 1, False: 0)\t")
            
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
                from config.define.kr_unq import kr_codes
                col_num = int(input("확인할 항목 번호를 입력하세요.\t"))
                print(kr_codes(value=fdata.iloc[:,col_num]).unqs)
                continue