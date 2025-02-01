import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
import pprint
# 1. [ 환경 변수 로드 ]
load_dotenv()
# 1. [ dotenv를 활용하여 알라딘 API 키 가져오기 ]
MY_TTBKEY = os.getenv('MY_TTBKEY')
# 2. [ 공식 문서를 참고하여 알라딘 API 검색 URL 설정하기 ]
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'


# 2. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic,page, max_results=100):
    url = ALADIN_SEARCH_URL
    # 3.1 [ API 요청에 필요한 파라미터 설정 (문서 참고하여 작성해보기) ]

    
    params = {
        "TTBKey": MY_TTBKEY,    # API 키
        "Query": topic,       # 검색 키워드
        "output": "js",         # 응답 형식
        "Version": "20131101",  # API 버전
        'start' : page,
        "MaxResults" : max_results,
    }
    # 3.2 [ HTTP 요청 보내고 응답 데이터를 JSON 형식으로 반환하기 ]
    data = requests.get(url,params).json()
    return data


# 3. '인공지능' 도서 데이터를 처리하는 함수 정의
def process_ai_books():
    # 3.1 [ '인공지능' 관련 도서 검색 ]
    # fetch_books_by_topic()을 호출하여 '인공지능' 관련 도서를 100개 수집합니다.
    ai = []
    filter_ai = []
    for i in range(2):
        ai.append(fetch_books_by_topic('인공지능',i)['item'])
    pprint.pprint(len(ai))
    # 3.2 [ 수집된 데이터에서 가격 정보가 있는 책 필터링 및 가격순 정렬 ]
    for i in range(2) :
        for j in range(50):
            if ai[i][j]['priceStandard'] != '':
                filter_ai.append(ai[i][j])
    sorted_filter_ai_desc = sorted(filter_ai, key=lambda x: x['priceStandard'], reverse=True)
    
    # 3.3 [ 상위 10개 도서 선택 ]
    top_10 = []
    for i in range(10):
        top_10.append(sorted_filter_ai_desc[i])
    

    # 3.4 [ 상위 10개 도서 정보 출력 ]
    for i in range(10):
        title = top_10[i]['title']
        price = top_10[i]['priceStandard']
        print(f'{i}. 제목: {title}, 가격: {price}')

    # 3.5 [ JSON 파일로 저장할 데이터 준비 ]
    # output/ai_top10_books.json 파일로 저장
    top_10 = {
        'top_10' : top_10
    }
    current_path = Path.cwd()
    output_folder = current_path/'pjt01'/'output'
    output_folder.mkdir(exist_ok=True)
    file_path = Path(output_folder/'ai_top10_books.json')

    ### with 문
    # 경로.open > 파일오픈 w는 쓰기모드, encoding = 인코딩 설정 as 별칭
    # json.dump > 저장할 파일, 오픈한 파일, 아스키설정 default=True(False 일 경우 한글등을 직접넣음, 한글깨짐없애기), indent=4(간격을 4칸으로해서 가독성 상승)
 
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(top_10, f, ensure_ascii=False, indent=4)
    # 3.6 [ 완료 메시지를 출력 ]
    print('ai_top10_books 파일이 생성되었습니다.')

# 함수 실행
if __name__ == '__main__':
    process_ai_books()
