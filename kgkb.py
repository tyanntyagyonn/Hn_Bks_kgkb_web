import streamlit as st

#初期設定
if 'bangou' not in st.session_state and 'kurikaesi' not in st.session_state:
    st.session_state.bangou = 1





#ボタン
def ボタン():
    #if st.button("科学部文化祭"):
        #st.session_state.bangou = 0
    if st.button("工学班"):
        st.session_state.bangou = 1
    if st.button("生物班"):
        st.session_state.bangou = 2
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
st.title("科学部文化祭")
サイドバーボタン()
ボタン()
ページ移動()

import streamlit as st



        


