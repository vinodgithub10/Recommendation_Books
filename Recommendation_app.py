import streamlit as st
import pickle


recom = pickle.load(open('recommend.pkl','rb'))
lk = pickle.load(open('like.pkl','rb'))

st.title("Book Recommendation App")
st.subheader("Enter User-ID")
unm = st.selectbox("Search",lk.keys())

if st.button("Recommend"):

    for k, v in recom.items():
        if unm == k:
            for i in v[:5]:

                st.write("{}".format(i[0]))


