import streamlist as st

if 'key' not in st.session_state:
    print('上面的')
    st.session_state['key'] = 'value'

if 'key' not in st.session_state:
    print('下面的')
    st.session_state['key'] = 'value'


    