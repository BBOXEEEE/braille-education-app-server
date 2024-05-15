# 시각장애인을 위한 점자 학습 도우미
- 2024학년도 1학기 컴퓨터공학부 졸업설계 Flask 서버 저장소
- [어플리케이션 저장소 바로가기](https://github.com/BBOXEEEE/braille-education-app)


## 📌 Introduction
To be updated.

## 🖥️ Model
**모델 정보**
- YOLOv8 <br>
모델은 다음 클래스들을 탐지할 수 있습니다.
<details>
<summary style="color: orange;"><strong>80개의 클래스 목록 보기</strong></summary>

```Text
01: 사람
01: 자전거
02: 자동차
03: 오토바이
04: 비행기
05: 버스
06: 기차
07: 트럭
08: 보트
09: 신호등
10: 소화전
11: 정지 표지판
12: 주차료 징수기
13: 벤치
14: 새
15: 고양이
16: 개
17: 말
18: 양
19: 소
20: 코끼리
21: 곰
22: 얼룩말
23: 기린
24: 가방
25: 우산
26: 핸드백
27: 넥타이
28: 서류 가방
29: 원반
30: 스키
31: 스노우 보드
32: 공
33: 연
34: 야구 방망이
35: 야구 글러브
36: 스케이트 보드
37: 서핑 보드
38: 테니스 라켓
39: 병
40: 와인잔
41: 컵
42: 포크
43: 나이프
44: 숟가락
45: 그릇
46: 바나나
47: 사과
48: 샌드위치
49: 오렌지
50: 브로콜리
51: 당근
52: 핫도그
53: 피자
54: 도넛
55: 케잌
56: 의자
57: 쇼파
58: 화분
59: 침대
60: 식탁
61: 화장실
62: 티비
63: 노트북
64: 마우스
65: 리모컨
66: 키보드
67: 휴대전화
68: 전자레인지
69: 오븐
70: 토스터
71: 싱크대
72: 냉장고
73: 책
74: 시계
75: 꽃병
76: 가위
77: 곰 인형
78: 헤어 드라이기
79: 칫솔
```

</details>

## 📂 Project Structure

```
├─ apps                     : 서버가 제공하는 기능이 정의된 폴더
│  ├─ constants             : 상수를 관리하는 폴더
│  │  └─ domain.py          : 객체 탐지 모델이 분류할 수 있는 클래스 목록
│  └─ object_detection      : 객체 탐지 기능 구현 (모델 학습 완료 시 분리 예정)
│  │  ├─ __init__.py
│  │   └─ routes.py
│  └─ text_to_braille       : 텍스트를 점자로 변환하는 알고리즘
│     ├─ braille_list.py
│     └─ text_to_braille.py
├─ model                    : 객체 탐지 모델을 학습하기 위한 폴더
│  └─ test.py
├─ app.py                   : 서버 기본 코드
├─ README.md                : README
└─requirements.txt          : pip package 목록
```

## ⚙️ Installation
1. Clone this Repository

```shell
$ git clone https://github.com/BBOXEEEE/braille-education-app-server
$ cd braille-education-app-server
```

2. Install the Package List

```shell
$ pip install -r requirements.txt
```

3. Get start Flask Server

```shell
$ python app.py
```