<div align="center" >

# Park-to-Play: P2P

서울특별시 영등포구 주차장 예측 웹앱 서비스

</div>

## 시연 영상

<div align="center" >

https://youtu.be/JDg3364ZCEk

![GIFMaker_me (1)](https://github.com/user-attachments/assets/cd365e7e-784f-45aa-889f-729be896a587)

</div>

<br>

## 🔖 목차

- [서비스 소개](#서비스-소개)
- [서비스 제작 기간](#서비스-제작-기간)
- [멤버 및 역할](#멤버-및-역할)
- [Tech Stack](#tech-stack)
- [pipeline](#pipeline)
- [수집 데이터](#수집-데이터)
- [데이터 전처리](#데이터-전처리)
- [모델링](#모델링)
- [모델링 결과 분석](#모델링-결과-분석)

<br>

## 서비스 소개

"Park to Play(P2P)"는 주차를 더 효율적이고 스마트하게 만들기 위해 시작된 프로젝트입니다. <br> 사용자는 주차 공간을 쉽게 찾고, 실시간으로 주차 상황을 확인하며, 해당 주차장의 향후 주차량 예측을 통해 주차 관련 시간을 절약할 수 있습니다. P2P는 단순한 주차 이상의 경험을 제공하며, 주차장에서의 스트레스를 줄여 더 나은 일상으로 나아갈 수 있게 돕습니다.

<br>

브랜드 이름인 "Park to Play"는 주차(Park)를 간편하게 처리하고, 그로 인해 확보한 시간을 여유롭게 사용(Play)하자는 의미를 담고 있습니다. 즉, 주차 문제를 해결함으로써 사용자에게 더 많은 여유와 즐거움을 제공하는 것을 목표로 하는 서비스입니다.

<br>

## 서비스 제작 기간

- 2024-09-20 ~ 2024-10-25

<br>

## 멤버 및 역할

<img width="100" alt="image" src="https://github.com/user-attachments/assets/67587fcf-89ee-4399-accf-07c93fae42ca">
<img width="100" alt="image" src="https://github.com/user-attachments/assets/536c3d9a-a109-4074-94b9-348fa3707fd5">
<img width="100" alt="image" src="https://github.com/user-attachments/assets/c98c3515-c9dc-4997-befa-032d46ed00c3">
<img width="100" alt="image" src="https://github.com/user-attachments/assets/2f922f36-cbf9-488f-993d-160e89842a25">
<img width="100" alt="image" src="https://github.com/user-attachments/assets/7b7d3c2b-c409-4a80-a825-72de612f7aa3">
<img width="100" alt="image" src="https://github.com/user-attachments/assets/af5e73d5-542b-4ed1-a733-97a67b2941c3">

<br>
<br>

- [김관용](https://github.com/ToleranceKim) : 데이터 수집, 데이터 분석, 모델링
- [김윤일](https://github.com/yunilkim) : 데이터 수집, 데이터 분석
- [서동옥](https://github.com/SeoDongOk) : 데이터 수집, 서비스 구현
- [이종찬](https://github.com/qkskfka) : 데이터 수집, 서비스 구현
- [장준혁](https://github.com/JangJune) : 데이터 수집, 데이터 분석, 모델링
- [최준혁](https://github.com/kimbap918) : 데이터 수집, 데이터 분석, 모델링

<br>

## Tech Stack

- Back End

  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=ffffff"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/REST framework-009688?style=flat-square&logo=Django&logoColor=ffffff"/>

- Front End

  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=Next.js&logoColor=ffffff"/> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=Tailwind CSS&logoColor=ffffff"/>

- Cloud, Community

  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Trello-0079BF?style=flat-square&logo=Trello&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=Figma&logoColor=ffffff"/>

<br>

## Pipeline

  <img width="770" alt="Screenshot 2024-10-28 at 5 41 53 PM" src="https://github.com/user-attachments/assets/5f193e14-f49a-4709-abb7-4ef7bd0ea8e0">

  <img width="758" alt="Screenshot 2024-10-28 at 5 41 04 PM" src="https://github.com/user-attachments/assets/ca2bba2d-6ac7-44ad-be5e-81395b6cb5d3">

<br>
<br>

## 수집 데이터

<img width="1150" alt="Screenshot 2024-10-28 at 5 50 40 PM" src="https://github.com/user-attachments/assets/66dbddb1-83e0-42ca-b2b2-42943ca6d566">

<br>
<br>

## 데이터 전처리

### 주차장(tb_parking)

#### 보간 : 주차장의 점유율에 대해 선형 보간법 (Linear Interpolation) 사용 <br>

보간 목적: 100% 또는 0%로 이상치가 발생한 값을 결측값으로 처리한 후, 해당 결측값을 보간
<img width="1614" alt="Screenshot 2024-10-28 at 6 15 22 PM" src="https://github.com/user-attachments/assets/028f5a04-2920-487a-b2a5-835b2473c9b6">

<br>
<br>

#### 이상치 처리 : 축제 당일 주차장의 점유율이 140%가 넘으므로, 노이즈로 판단하고 해당 일자의 데이터는 삭제

<img width="1673" alt="Screenshot 2024-10-28 at 6 19 23 PM" src="https://github.com/user-attachments/assets/d53cfe7c-ffaa-43da-9e94-68f7b2c4bf02">

<br>
<br>

#### 데이터 수직 이동 : 수집 기간 중 현재 주차 대수의 최대치를 실제 조사 후 "최대 주차 가능 면수"로 수직 이동

<img width="1274" alt="Screenshot 2024-10-28 at 6 24 07 PM" src="https://github.com/user-attachments/assets/0f2d17f3-5378-4718-b2b2-12e19cb43155">
<img width="703" alt="Screenshot 2024-10-23 at 7 00 37 PM" src="https://github.com/user-attachments/assets/6506cb29-516f-412b-abe5-2078347f7c0b">

<br>
<br>

### 교통 현황(tb_traffic)

#### 혼잡도(confusion) : 전체적으로 규칙성이 존재하므로 현재 속도와 허용 속도를 통해 혼잡도를 계산

<img width="1659" alt="Screenshot 2024-10-28 at 6 31 02 PM" src="https://github.com/user-attachments/assets/02e9134b-af35-4199-bb2f-ce7774868576">

<br>
<br>

### 용도목적

주차장 주변 건물들의 특징을 통한 주차장 사용용도 카테고리화
<img width="1677" alt="Screenshot 2024-10-28 at 6 33 44 PM" src="https://github.com/user-attachments/assets/b83886cd-9127-49c3-a235-2e9c6d5c289c">

<br>
<br>

### GIS(tb_gis)

#### 상관 관계 : 주차율과 높은 상관 관계를 가지는 시설 추출, 주차장 반경 150m내 해당 시설 개수 사용

<img width="1626" alt="Screenshot 2024-10-28 at 6 36 08 PM" src="https://github.com/user-attachments/assets/c634d7e8-3fd8-4253-a83c-50c535e79dc1">

<br>
<br>

### Feature Importance

LightGBM에서 Split, Gain방식을 통한 상관 관계 분석, 높은 상관 관계를 가지는 요소들로 정렬하고 테스트

<img width="904" alt="image" src="https://github.com/user-attachments/assets/53fdc492-7e25-41ee-bf80-806f6eb675bc">

#### 추출된 Feature

<img width="300" height="400" alt="Screenshot 2024-10-28 at 6 38 56 PM" src="https://github.com/user-attachments/assets/6455744f-6d4c-4089-8ff7-80eb8356535b">

#### Feature 예시

<img width="1292" alt="image" src="https://github.com/user-attachments/assets/d41cfe1f-f49c-4bf2-a8f8-638a5c88ce13">

<br>
<br>

## 모델링

- 딥러닝 모델

  - LSTM

- 머신러닝 모델
  - XGBoost
  - LightGBM
  - Random Forest
  - AutoML

<img width="1670" alt="Screenshot 2024-10-28 at 6 54 34 PM" src="https://github.com/user-attachments/assets/968d59c7-90a1-4d36-b072-0db9e1714b83">
<img width="1663" alt="Screenshot 2024-10-28 at 6 55 20 PM" src="https://github.com/user-attachments/assets/c4bc4321-89c6-4af6-916e-64a7dabb89a5">
<img width="1661" alt="Screenshot 2024-10-28 at 6 55 38 PM" src="https://github.com/user-attachments/assets/77ef2cda-cb1b-4440-b2fc-8bca22179b3b">
<img width="1668" alt="Screenshot 2024-10-28 at 6 55 57 PM" src="https://github.com/user-attachments/assets/8ed82317-cff5-48d6-ad25-5be22d262835">
<img width="1655" alt="Screenshot 2024-10-28 at 6 57 12 PM" src="https://github.com/user-attachments/assets/d0194f02-2345-4d7c-9719-f15a7b3a84e2">

<br>
<br>

### AutoML

AutoML결과, Extra Tree Regressor가 가장 우수한 성능을 보였기에, 해당 모델로 테스트
<img width="1416" alt="image" src="https://github.com/user-attachments/assets/354c176c-e482-4f7c-81da-13f1234c86f6">

<img width="1655" alt="Screenshot 2024-10-28 at 6 57 12 PM" src="https://github.com/user-attachments/assets/d0194f02-2345-4d7c-9719-f15a7b3a84e2">

<br>
<br>

## 모델링 결과 분석

![image](https://github.com/user-attachments/assets/5397c802-b766-4778-8ea6-8c9406c0a529)

- LSTM

  - 시간에 따른 변화 패턴을 잘 반영하지만, 3주 간의 데이터로는 장기 의존성 활용이 어려움
  - 학습 및 예측에 시간과 메모리 소모가 커 대규모 데이터 처리에 비효율적

- XGBoost

  - 날씨, 시간대, 주말/평일, 혼잡도 등 다양한 변수를 잘 반영해 높은 예측 성능을 발휘했으나, 학습 시간이 길며 과적합이 발생하는 문제가 발생

- LightGBM

  - 빠르고 대규모 데이터 처리에 최적화되어 실시간 주차 데이터 처리에 효과적이나, 작은 데이터셋에서는 과적합 문제 존재

- Random Forest

  - 예측 안정성 및 일관성이 뛰어났으며, 튜닝 및 병렬처리 시 대규모 데이터 처리에도 효율적
  - 성능을 높일수록 속도가 느려지는 단점이 존재함

- Extra Trees
  - Random Forest보다 성능이 좋은편이나, 대규모 데이터에서는 무작위 분할특성으로 인해 분할할 후보들이 매우 많아지는 경우 계산 비용이 증가할 수 있음을 파악
