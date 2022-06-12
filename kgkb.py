import streamlit as st

#初期設定
if 'bangou' not in st.session_state:
    st.session_state.bangou = 0





#ボタン
def ボタン():
    if st.button("科学部文化祭"):
        st.session_state.bangou = 0
        ページ移動()
    if st.button("工学班"):
        st.session_state.bangou = 1
        ページ移動()
    if st.button("生物班"):
        st.session_state.bangou = 2
        ページ移動()
    if st.button("化学班"):
        st.session_state.bangou = 3
        ページ移動()



#サイドバーボタン
def サイドバーボタン():
    if st.sidebar.button("科学部文化祭 "):
        st.session_state.bangou = 0
        ページ移動()
    if st.sidebar.button("工学班 "):
        st.session_state.bangou = 1
        ページ移動()
    if st.sidebar.button("生物班 "):
        st.session_state.bangou = 2
        ページ移動()
    if st.sidebar.button("化学班 "):
        st.session_state.bangou = 3
        ページ移動()



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
        サイドバーボタン()
        ボタン()
    elif st.session_state.bangou == 1:
        工学班()
        サイドバーボタン()
        ボタン()
    elif st.session_state.bangou == 2:
        生物班()
        サイドバーボタン()
        ボタン()
    else:
        化学班()
        サイドバーボタン()
        ボタン()



if 'syokigamen' not in st.session_state:
    ページ移動()




        


