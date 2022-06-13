from curses import use_default_colors
import streamlit as st
from PIL import Image

#初期設定
if 'bangou' not in st.session_state and 'kurikaesi' not in st.session_state:
    st.session_state.bangou = 1





#ボタン
def 工学班ボタン():
    if st.button("工学班"):
        st.session_state.bangou = 1
def 生物班ボタン():
    if st.button("生物班"):
        st.session_state.bangou = 2
def 化学班ボタン():
    if st.button("化学班"):
        st.session_state.bangou = 3



#サイドバーボタン
def サイドバーボタン():
    #if st.sidebar.button("科学部文化祭 "):
        #st.session_state.bangou = 0
    if st.sidebar.button("工学班 "):
        st.session_state.bangou = 1
    if st.sidebar.button("生物班 "):
        st.session_state.bangou = 2

    if st.sidebar.button("化学班 "):
        st.session_state.bangou = 3



#それぞれのページ設定
def 科学部文化祭():
    st.title("科学部文化祭")
def 工学班():
    st.title("工学班")
def 生物班():
    st.title("生物班")
def 化学班():
    st.title("化学班")



#ページ移動
def ページ移動():
    if st.session_state.bangou == 0:
        科学部文化祭()
    elif st.session_state.bangou == 1:
        工学班()
    elif st.session_state.bangou == 2:
        生物班()
    else:
        化学班()



#処理

horizon = Image.open("horizon fw 0.jpg")
Image.open(horizon , use_column_width=True)

st.title("科学部文化祭")

サイドバーボタン()

kougakuhan, seibutuhan, kagakuhan  = st.beta_columns(3)
kougakuhan = 工学班ボタン()
seibutuhan = 生物班ボタン()
kagakuhan = 化学班ボタン()

ページ移動()




        


