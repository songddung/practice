import os
import requests
from pathlib import Path
from gtts import gTTS
from dotenv import load_dotenv
import pprint
# 1. [ 환경 변수 로드 ]
load_dotenv()

MY_TTBKEY = os.getenv('MY_TTBKEY')
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'


# 2. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic, max_results=100):
    url = ALADIN_SEARCH_URL
    params = {
        "TTBKey": MY_TTBKEY,    # API 키
        "Query": topic,       # 검색 키워드
        "output": "js",         # 응답 형식
        "Version": "20131101",  # API 버전
        "MaxResults" : max_results,
    }
    # 3.2 [ HTTP 요청 보내고 응답 데이터를 JSON 형식으로 반환하기 ]
    data = requests.get(url,params).json()
    return data

current_path = Path.cwd()
output_folder = current_path/'pjt01'/'output'
output_folder.mkdir(exist_ok=True)

# 3. [ 도서 정보를 텍스트 파일로 저장하는 함수 정의 ]
# 책 정보를 "제목, 저자, 소개" 형식으로 변환하여 txt 파일로 저장
def save_books_info(books, filename):
    book_info = []
    for i in range(len(books)) :
        my_dict = {
            'title' : books[i]['title'],
            'author' : books[i]['author'],
            'description' : books[i]['description']
        }
        book_info.append(my_dict)
    



    file_path = output_folder / filename    # 저장될 파일명 및 경로로
    text_file = '\n'.join(
        f"Title: {book['title']}\nAuthor: {book['author']}\nDescription: {book['description']}\n"
        for book in book_info
    )

    file_path.write_text(text_file, encoding='utf-8')
    
    print(f"{filename} 파일이 생성되었습니다.")
    return text_file


# 5. [ 텍스트 파일을 오디오 파일로 변환하는 함수 정의 ]
def create_audio_file(text_file, audio_file):
    tts = gTTS(text=text_file, lang = 'ko', slow = False)
    tts.save(output_folder/audio_file)  # 음성 파일 저장

    print(f"{audio_file} 파일이 생성되었습니다.")


# 6. [ 음악 관련 도서 데이터를 처리하는 함수 정의 ]
def process_music_books():
    # 6.1 [ '음악' 주제의 도서 데이터 수집 ]
    music = fetch_books_by_topic('음악',10)
    # 6.2 [ 도서 정보를 텍스트 파일로 저장 ]
    text_file = save_books_info(music['item'], 'music_books_info.txt')

    # 6.3 [ 텍스트 파일을 오디오 파일로 변환 ]
    create_audio_file(text_file, 'music_books.mp3')

    print("모든 작업이 완료되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_music_books()
