
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
uploaded_file = st.file_uploader("HR 데이터를 업로드하세요 (Excel 파일)", type=["xlsx"])

if uploaded_file:
    # 엑셀 파일을 DataFrame으로 읽기
    df = pd.read_excel(uploaded_file)
    
    # 기본 데이터프레임 정보 표시
    st.write("### 업로드한 데이터 미리보기")
    st.dataframe(df)

    # 부서별 인원 구성 시각화
    st.write("## 부서별 인원 구성")
    department_count = df['부서'].value_counts()
    fig, ax = plt.subplots()
    department_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('부서')
    ax.set_ylabel('인원 수')
    ax.set_title('부서별 인원 구성')
    st.pyplot(fig)

    # 성별 비율 분석
    st.write("## 성별 비율 분석")
    gender_count = df['성별'].value_counts()
    fig, ax = plt.subplots()
    gender_count.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    ax.set_title('성별 비율')
    st.pyplot(fig)

    # 연령 분포 분석
    st.write("## 연령 분포 분석")
    df['연령'] = pd.to_datetime('today').year - pd.to_datetime(df['생년월일']).dt.year
    fig, ax = plt.subplots()
    df['연령'].plot(kind='hist', bins=10, ax=ax)
    ax.set_xlabel('연령')
    ax.set_title('직원 연령 분포')
    st.pyplot(fig)

    # 근속 연수 분석
    st.write("## 직원별 근속 연수 분석")
    df['근속연수'] = pd.to_datetime('today').year - pd.to_datetime(df['입사일']).dt.year
    st.write("평균 근속연수:", round(df['근속연수'].mean(), 2), "년")
    fig, ax = plt.subplots()
    df['근속연수'].plot(kind='hist', bins=10, ax=ax)
    ax.set_xlabel('근속 연수')
    ax.set_title('직원 근속 연수 분포')
    st.pyplot(fig)
else:
    st.write("업로드된 파일이 없습니다. HR 데이터를 업로드하여 분석을 시작하세요.")
