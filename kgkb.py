import streamlit as st

#初期設定
if 'bangou' not in st.session_state and 'kurikaesi' not in st.session_state:
    st.session_state.bangou = 0
    st.session_state.kurikaesi  = False



#ボタン
def ボタン():
    if st.button("科学部文化祭"):
        st.session_state.bangou = 0
        st.session_state.kurikaesi = True
    if st.button("工学班"):
        st.session_state.bangou = 1
        st.session_state.kurikaesi = True
    if st.button("生物班"):
        st.session_state.bangou = 2
        st.session_state.kurikaesi = True
    if st.button("化学班"):
        st.session_state.bangou = 3
        st.session_state.kurikaesi = True



#サイドバーボタン
def サイドバーボタン():
    if st.sidebar.button("科学部文化祭 "):
        st.session_state.bangou = 0
        st.session_state.kurikaesi = True
    if st.sidebar.button("工学班 "):
        st.session_state.bangou = 1
        st.session_state.kurikaesi = True
    if st.sidebar.button("生物班 "):
        st.session_state.bangou = 2
        st.session_state.kurikaesi = True
    if st.sidebar.button("化学班 "):
        st.session_state.bangou = 3
        st.session_state.kurikaesi = True



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
    ページ移動()
    サイドバーボタン()
    ボタン()



        


