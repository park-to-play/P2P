# 깃허브 룰북

## 브랜치 전략

<b style="color: red"> 절대 동일한 기능을 여러명이 구현하려 하면 안됩니다! </b>

- main: 서비스 제공 분기점
  |
  | - dev: 작업들 병합 및 개발자 코드리뷰
  |
  | - features: 작업 위치
  |
  | - ex) login
  |
  | - ex) data_crawling
  |
  | - ex) traffic

## 커밋 메시지 양식

- @add 추가된 기능
- @fix 수정 내용
- @remove 삭제된 내용
- @error 에러

외에는 비슷한 양식으로 작성

## PR 요청 방식

- 요청 제목은 유지할것
- 요청 내용 필수사항
  - 기능설명
  - 변동된 내용

## 코드리뷰 코멘트 참고

https://hidekuma.github.io/github/abbreviation/abbreviation/

주로 쓰는것

- LGTM: Looking Good To Me
- AFAIK: As Far As I Know

## 이슈

- 특이사항 모두 업로드

### ex

- 제목: @Error 간략한 내용, 커밋 위치

- 내용: 에러 로그
