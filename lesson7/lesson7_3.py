import streamlist as st

st.title("counter Example")
count = 0

increament = st.button('每次加1')
if increament:
    count += 1

st.write('次數=',count)