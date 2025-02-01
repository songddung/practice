import os
import requests
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 1. [ 환경 변수 로드 ]
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# 1. [ dotenv를 활용하여 알라딘 API 키 가져오기 ]
MY_TTBKEY = os.getenv('MY_TTBKEY')
# 2. [ 공식 문서를 참고하여 알라딘 API 검색 URL 설정하기 ]
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'


# 2. OpenAI API 클라이언트 초기화
client = OpenAI(api_key=OPENAI_API_KEY)


# 3. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic, max_results=100):
    url = ALADIN_SEARCH_URL
    params = {
        "TTBKey": MY_TTBKEY,    # API 키
        "Query": topic,       # 검색 키워드
        "output": "js",         # 응답 형식
        "Version": "20131101",  # API 버전
        "MaxResults" : max_results,
    }
    data = requests.get(url,params).json()
    return data

# 4. 책 데이터를 ChatGPT로 분류하는 함수 정의 (습관, 시간관리, 독서법, 기타)
def classify_books_with_gpt(books):
    # 4.1 [ 분류할 책 제목들을 전달하기 편한 문자열로 취합 ]
    title = []
    for i in range(len(books)):
        title.append(books[i]['title'])

    # 4.2 [ ChatGPT 대화 메시지 설정 (프롬프트 작성) ]
    # 습관, 시간관리, 독서법, 기타 로 분류
    conversation_history = [
        {"role": "system", "content": "당신은 사용자 질문에 답변하는 챗봇입니다."},      # 페르소나 작성
        {"role": "user", "content": "답변은 사용자가 읽기 쉽도록 마크다운 형태로 정리해서 출력해줘."}         # 요청 프롬프트 작성
    ]

    # 4.3 [ 생성형 AI에 분류 요청 보내기 ]
    # client.chat.completions.create() 호출 (example 코드 참고)
    conversation_history.append(
        {
            "role": "user",
            "content": "도서를 습관, 시간관리, 독서법, 기타로 분류해줘",
        }
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",            # 사용하려는 모델 (필수 지정)
        messages=conversation_history,  # 대화 메시지 목록 (필수 지정)
        max_tokens=500,                 # 생성될 응답의 최대 토큰 수 (값의 범위: 1~모델 마다 최대값 ex> gpt-4o-mini: 16,385 tokens)
        temperature=1.0,                # 확률 분포 조정을 통한 응답의 다양성 제어 (값의 범위: 0~2)
        top_p=1.0,                      # 누적 확률 값을 통한 응답의 다양성 제어 (값의 범위: 0~1)
        n=1,                            # 생성할 응답 수 (1이상의 값)
        seed=1000                       # 랜덤 씨드 값 (설정하는 경우 일관된 답변을 얻을 수 있음)
    )
    # 4.4 [ ChatGPT의 응답을 가져와 JSON 으로 추출 ]
    # ! 주의. JSON 형태로 프롬프팅을 하지 못하면 파싱에서 에러가 발생할 수 있습니다.
    for response in response.choices :
        print(f"Assistant: {response.message.content}")  # 응답에서 JSON 데이터를 추출하고 파싱

    return response.response.choices[0].message['content']   # 분류 정보 반환


# 5. [ 데이터를 JSON 파일로 저장하는 함수 정의 ]
def save_to_json(data, filename):
    data = {
        'data' : data
    }
    current_path = Path.cwd()
    output_folder = current_path/'pjt01'/'output'
    output_folder.mkdir(exist_ok=True)
    file_path = output_folder/filename
    with filename.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 6. '독서' 도서 데이터를 처리하는 함수 정의
def process_reading_books():
    # 6.1 [ '독서'와 관련된 도서 검색 (100개) ]
    # fetch_books_by_topic() 호출
    books = fetch_books_by_topic('독서')['item']

    # 6.2 [ 생성형 AI를 이용해 책 분류 ]
    # classify_books_with_gpt() 호출
    data = classify_books_with_gpt(books)
    # 6.3 [ 분류된 책 정보를 JSON 파일로 저장 ]
    # output/reading_habits.json 으로 저장하기
    # save_to_json() 호출
    save_to_json(data,'reading_habits.json')

    # 완료 메시지 출력
    print("'output/reading_habits.json' 파일이 생성되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_reading_books()
