import streamlist as st

#手動建立counter_key,並設定初始值為0
if "counte" not in st.session_state:
    #st.session_state.counter=0
    st.session_state.counter += 1

st.session_state.counter += 

st.header(f"這頁網頁已經執行{st.session_state.counter} 次")
buttet_status = st. button(再執行一次",key="reset")#自動建立rest_key
st.writes(st.session_state)