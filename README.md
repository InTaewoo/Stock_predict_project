# 뉴스 기사 및 유튜브 텍스트의 감성분석과 딥러닝을 이용한 주가등락 예측 서비스 구현
            


- 주제 : **뉴스 기사 및 유튜브 텍스트의 감성분석과 딥러닝을 이용한 주가 등락 예측 서비스 구현**
- 목적 : **미디어 키워드 분석으로 업종별 이슈가 한국 주식에 미치는 영향을 파악하고, 웹페이지 대시보드로 구현**

- 기간 : 8/25 ~ 10/8
- 멘토링 일정 : 8/28,9/11,10/4
- 중간 발표 : 9/11
- 최종 발표: 10/8
- 나머지 일정 WBS 참조

- DS - DE 역할 분담![image-20210827230959954](/image-20210827230959954.png)

- data : youtube, 뉴스 기사 크롤링, FinanceDataReader(한국거래소 자료)

- 개요 : 
  > 1. 데이터 수집
  >
  >    1.  크롤링으로 유튜브 스크립트, 언론 보도 이슈 수집
  >
  >       - 유튜브의 경우 ( 구독자수 기준 ) : 금융 유튜브 채널 상위 5개
  >
  >       - 언론보도 자료 ( 유료부수 구독자 수 기준 ) : 매일경제, 머니투데이     
  >
  >       - 매일 업로드 되는 자료에 대한 스크립트 추출 예정
  >
  >         - 크롤링 : 헤드라인, 자막, 말, 스크립트
  >
  >           \- 슈카월드
  >
  >           \- 삼프로TV
  >
  >           \- 한국경제TV
  >
  >    2. FinanceDataReader 라이브러리로 주식가격 데이터 수집 ( 한국거래소 자료 ) 
  >
  >       - 매일 실시간 종가 데이터 수집      
  >       - 추후 업종 및 종목을 선택 예정
  >
  > 2. 데이터 전처리
  >
  >    1. 유튜브 스크립트 & 언론 보도 이슈   
  >       - 텍스트 마이닝
  >    2. 주식가격
  >       - 종목마다의 가격 차이를 고려하여 MinMaxScaler 적용
  >
  > 3.  데이터 분석
  >
  >    1. 유튜브 스크립트 & 언론 보도 이슈      
  >       - 주가 등락 예측을 위한 감성 분석(목적성)
  >
  >    2. 주식 가격     
  >       -   LSTM으로 주식 가격 시계열 예측(분석 방법 비교) 
  >    3. Label
  >       - ①+② 분석을 종합하여 주식가격의 상승/정체/하락 예측
    
  >
  > 4. 데이터 시각화
  >
  >    1. 일별 이슈 키워드를 나타낸 워드 클라우드로   
  >    2. 키워드 간의 연관성(긍정/부정)   
  >    3. 주가의 시계열 그래프 
  >
  > 5. 웹 페이지 구현
  >
  >    1. 이슈로 예측한 주식가격 예측 결과를 한 눈에 볼 수 있도록 웹 페이지 구현   
  >    2. 해당 회사의 주식 그래프(전날 종가) 및 예측 등락   
  >    3. 유튜브 이슈 워드 클라우드   
  >    4. 보도 이슈 워드 클라우드 

![image](https://user-images.githubusercontent.com/81672260/136681768-c1cc669f-50f9-4cb7-bbb5-fbb697684763.png)

![image](https://user-images.githubusercontent.com/81672260/136681779-e1794278-3638-4e29-b676-3280215532d3.png)

![image](https://user-images.githubusercontent.com/81672260/136681786-667f4890-f04f-40ea-af66-afe7faa64b7f.png)


![image](https://user-images.githubusercontent.com/81672260/136681801-b3fcbe24-c4f3-49f8-a66c-559762d58218.png)

![image](https://user-images.githubusercontent.com/81672260/136681806-7a1d5055-403c-4346-8a9d-2c1553d146df.png)

![image](https://user-images.githubusercontent.com/81672260/136681821-ddceb911-a971-47cb-b965-388b99928eff.png)

![image](https://user-images.githubusercontent.com/81672260/136681856-6d5b0762-449e-411e-afef-58336fa1b4c2.png)

![image](https://user-images.githubusercontent.com/81672260/136681875-27adce7c-2bbd-4884-b57b-da9702839d66.png)

![image](https://user-images.githubusercontent.com/81672260/136681893-e1aba86e-8f57-4d11-ad22-1ac811699d53.png)

![image](https://user-images.githubusercontent.com/81672260/136681896-5743d689-beed-4c7a-bf45-e113a5c7eb60.png)

![image](https://user-images.githubusercontent.com/81672260/136681898-ec676fd4-e7b9-4a37-9782-7f538c70a0cc.png)

![image](https://user-images.githubusercontent.com/81672260/136681899-3b916d9f-d96c-4218-9cc1-62ef2347dd78.png)

![image](https://user-images.githubusercontent.com/81672260/136681905-b7142dc9-0f98-4956-94e9-96f34a6127a6.png)

![image](https://user-images.githubusercontent.com/81672260/136681910-fcdf8be0-b9e0-4c82-8f48-a1d6adb38ef9.png)

![image](https://user-images.githubusercontent.com/81672260/136681917-b996bfc1-b2a8-4f18-bd40-5466996ebae3.png)

![image](https://user-images.githubusercontent.com/81672260/136681921-8cd6694a-2172-4bab-94a3-67cfb1eb24cf.png)

![image](https://user-images.githubusercontent.com/81672260/136681928-c07754a4-a2a2-4bd9-9c76-c8be13781cf6.png)

![image](https://user-images.githubusercontent.com/81672260/136681941-e2b2dda9-1017-47a4-867a-a5b5d21aad16.png)

![image](https://user-images.githubusercontent.com/81672260/136681954-6e8f4b6b-b368-4184-b08e-8004e49bb717.png)

![image](https://user-images.githubusercontent.com/81672260/136681960-ca1d6f9c-12ae-45ef-a92d-e1a7d26d9857.png)

![image](https://user-images.githubusercontent.com/81672260/136681967-bcf07009-3de0-4da3-9ac9-79e056e42764.png)

![image](https://user-images.githubusercontent.com/81672260/136954983-f2390084-32ca-4c61-a2f6-a0779467d726.png)








