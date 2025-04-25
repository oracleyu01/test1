import plotly.express as px
import plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 폰트 설정 부분 제거 또는 수정
# Streamlit Cloud에서는 다음과 같이 기본 폰트 사용
import matplotlib as mpl
mpl.rcParams['font.family'] = 'DejaVu Sans'  # 리눅스 환경에서 기본적으로 제공되는 폰트

# 데이터 로드 - 상대 경로 사용
money = pd.read_csv("money_data7.csv")  # 파일이 코드와 같은 디렉토리에 있다고 가정

# 년도 선택 박스 넣기
option = st.selectbox(
    'How would you like to choice year ?',
    ('2020', '2021', '2022'))

option2 = int(option)

st.write('You selected:', option)

money = money[:] [money['A_YEAR']== option2]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(list(money['A_MONTH']), list(money['A_RATE']), color='red', marker='o')
plt.xticks(tuple(money['A_MONTH']))
plt.title('미국금리')

plt.subplot(222)
plt.plot(list(money['A_MONTH']), list(money['K_RATE']), color='blue', marker='o')
plt.xticks(tuple(money['A_MONTH']))
plt.title('한국금리')

plt.subplot(223)
plt.plot(list(money['A_MONTH']), list(money['KOSPI']), color='green', marker='o')
plt.xticks(tuple(money['A_MONTH']))
plt.title('코스피 지수')

plt.subplot(224)
plt.plot(list(money['A_MONTH']), list(money['HOUSE_PRICE']), color='yellow', marker='o')
plt.xticks(tuple(money['A_MONTH']))
plt.title('집값')

st.pyplot(fig)
