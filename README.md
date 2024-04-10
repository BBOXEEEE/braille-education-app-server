# 시각장애인을 위한 점자 학습 도우미
- 2024학년도 1학기 컴퓨터공학부 졸업설계 Flask 서버 저장소
- [어플리케이션 저장소 바로가기](https://github.com/BBOXEEEE/braille-education-app)


## 📌 Introduction
To be updated.

## 📁 Project Structure

```
├─ apps                 : 서버가 제공하는 기능이 정의된 폴더
│  ├─ constants         : 상수를 관리하는 폴더
│  │  └─ domain.py      : 객체 탐지 모델이 분류할 수 있는 클래스 목록
│  └─ object_detection  : 객체 탐지 기능 구현 (모델 학습 완료 시 분리 예정)
│     ├─ __init__.py
│     └─ routes.py
├─ model                : 객체 탐지 모델을 학습하기 위한 폴더
│  └─ test.py
├─ app.py               : 서버 기본 코드
├─ README.md            : README
└─requirements.txt      : pip package 목록
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
