import json
import pickle

def dict2json(dict_object, json_path, option='write'):
    option = option.lower()
    if option == 'write':
        with open(json_path, 'w') as f:
            json.dump(dict_object, f)
    elif option == 'read':
        with open(json_path, 'r') as f:
            data = json.load(f)
        print(f"{type(data)} : \n{data}")
    else:
        with open(json_path, 'a') as f:
            json.dump(dict_object, f)

def dict2pickle(dict_object, json_path, option='write'):
    option = option.lower()
    if option == 'write':
        with open(json_path, 'wb') as f:
            pickle.dump(dict_object, f)
    elif option == 'read':
        with open(json_path, 'rb') as f:
            data = pickle.load(f)
        print(f"{type(data)} : \n{data}")
    else:
        with open(json_path, 'ab') as f:
            pickle.dump(dict_object, f)
            
# data = pd.read_excel("./day2/개별 데이터 포털 비교업무_ 실습과제_20211102_10개.xlsx")

# site_url = [url.split(' ')[-1] for url in data['사이트명']]
# data_id = [str(id) for id in data['데이터목록ID'].values]
# data_name = [name.rstrip().lstrip() for name in data['파일 목록명'].values]

# from config.save_json import dict2pickle

# INFO = {'urls':site_url,\
#         'ids':data_id,\
#         'name':data_name}
# print(INFO)

# dict2pickle(INFO, 'search_list.json')

# dict2pickle(INFO, 'search_list.json', 'read')
# LIST = '/Volumes/WORK/OpenData/script/개별 데이터 포털 비교업무_ 파일 목록 리스트_20211027_통합본.xlsx'
