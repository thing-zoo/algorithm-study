# 🧸 algorithm-study 💛
취업을 위한 알고리즘 스터디

- 기간: 2022년 3월~
- 정기 회의: 토요일 오후 8시
- 참고 사이트: [프로그래머스](https://programmers.co.kr/learn/challenges), [백준](https://www.acmicpc.net/)
- 언어: 파이썬

## 📚 스터디 규칙 

#### 📍문제 풀이

1. 주마다 문제를 선정해서 문제 풀이를 진행함. 회의 시간에는 각자 1문제 풀이 설명.
   1. 개념+알고리즘+풀이 방식 자세하게 설명하기. 
   2. 만약 상대가 이해 못하면 이해할 때까지 설명해야 함.
2. 깃허브 활용해서 Pull Request로 코드 리뷰 진행함.
   1. 서로에 대한 코드 리뷰는 토요일까지 완료하기.
   2. 반드시 코드 리뷰 후에 main branch로 merge.
   3. 기본적으로 올릴 때는 각자 이름으로 된 branch에 올림.
3. 코드 리뷰 받은 것에 대해서는 다음 회의 전까지 수정해서 다시 깃허브에 올리기.

#### 📍설명 방식

1. 적용 알고리즘 개념 간단하게 설명하기
2. 문제 풀이를 위한 접근 방식(or 개념) 설명
3. 기본 코드에 대한 설명
4. 추가적으로 개선한 코드에 대한 설명
5. 시간 복잡도, 공간 복잡도 계산 => 어려우면 실행 시간 캡처로 대체
6. 사용 라이브러리 정리
7. 기타(문제 풀이에 어려웠던 점, 구현하고자 했는데 실패한 방식)

#### 📍진행 방식

- 만약 주차에 해당하는 문제 풀이가 미완료 시, 회의 당일에 직접 문제 풀이 진행해야 함.
- 끝날 때까지 회의는 끝나지 않음.....

#### 📍참여 방법
1. 이 저장소를 fork 한다.
2. 생성된 원격 저장소에 이름 혹은 github ID로 폴더를 생성한다.
3. 생성된 폴더에 자신의 소스코드를 업로드 한다.
4. 이때 commit 규칙을 지키도록한다!
5. 원본 저장소로 Pull Request를 한다.
6. 다른 사람들의 PR을 보고 자유롭게 코드리뷰를 한다.

## 💬 PR 및 Commit Message 규칙

#### Pull Request
- PR 제목: 이름 / 주차 / 몇 문제
-  ```thing-zoo / 3월 1주차 / 4문제 ```
-  comment는 이번주에 풀었던 문제의 알고리즘 분류가 어떻게 되는지, <br> 어떤 문제가 어려웠는지 회고를 작성


#### Commit Message Rule
- commit 메세지: [문제 출처(플랫폼)] 문제이름(번호) / 난이도 / 걸린시간 
- description: 문제 주소 (option)
- 터미널에서 작성법: 
```
git commit -m "[BOJ] Hello World / 브론즈5 / 1분" -m "https://www.acmicpc.net/problem/2557"
```
- type: 
   - [BOJ] : 백준 
   - [PGS] : 프로그래머스
   - [ADD] : 문제 풀이 파일이나 부수적인 코드 추가
   - [MOD] : 코드 및 내부 파일 수정
   - [DEL] : 쓸모없는 코드나 파일 삭제
   - [CORRECT] : 문법 오류 해결, 타입 변경, 이름 변경 등의 작은 수정
   - [DOCS] : README 등의 문서 개정
   - [MOVE] : 프로젝트 파일 및 코드 이동
   - [RENAME] : 파일 이름 변경
   - [MERGE] : 다른 브랜치와의 충돌 해결 후 Merge
   - [REFACTOR] : 전면 수정

## 📁 파일 및 폴더 구조

#### 프로그래머스

- PGS/이름/폴더명/문제명.py

#### 백준

- BOJ/이름/폴더명/문제번호_문제명.py

## 🗓️ 일정표

[바킹독 알고리즘 문제집](https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog)

| **주차** | **내용** | **진행 현황** |
| -------- | ------------------------------------------------------------ | ------------- |
| 1주차     | [기초 문제](https://www.acmicpc.net/workbook/view/7306), [배열](https://www.acmicpc.net/workbook/view/7307), [연결리스트](https://www.acmicpc.net/workbook/view/7308)|               |

## 참고
https://github.com/soo5717/2021-Algorithm-Study/ <br>
https://github.com/ellynhan/challenge100-codingtest-study
