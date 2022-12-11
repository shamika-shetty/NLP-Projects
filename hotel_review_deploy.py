import streamlit as st
import numpy as np
import pandas as pd
import pickle
import altair as alt
import emoji

pipe_lr=pickle.load(open('Hotel_model.pkl', 'rb'))

#function to read the emotion
def predict_rating(docx):
    results=pipe_lr.predict([docx] )
    return results

def get_prediction_proba(docx):
    results=pipe_lr.predict_proba([docx] )
    return results

def main():
    st.title('Hotel Rating Classifier App')
    menu=["Home", "About"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home-rating in text")

        with st.form(key='rating_clf_form'):
            raw_text = st.text_area("Please enter your review")
            submit_text = st.form_submit_button(label="Submit")

        if submit_text:
            col1,col2 = st.columns(2)
            prediction=predict_rating(raw_text)
            probability=get_prediction_proba(raw_text)
            with col1:
                st.success('Original text')
                st.write(raw_text)
                st.success("Prediction")
                if prediction[0] == 0:
                    st.write(emoji.emojize(":frowning_face:"))
                else:
                    st.write(emoji.emojize(":star-struck:"))
                st.write("Confidence: {}".format(np.max(probability)))

            with col2:
                st.success('Prediction Probability')
                st.write(probability)
                proba_df=pd.DataFrame(probability,columns=pipe_lr.classes_)
                st.write(proba_df.transpose())
                proba_df_clean=proba_df.transpose().reset_index()
                proba_df_clean.columns=["rating","probability"]

            fig=alt.Chart(proba_df_clean).mark_bar().encode(x='rating', y='probability',color='rating')
            st.altair_chart(fig,use_container_width=True)
                

    elif choice == "Monitor":
        st.subheader("Monitor App")
    else:
        st.subheader("About")
        st.write("This is an NLP powered webapp that can predict emotion from text recognition with 89.73%  accuracy, Many python libraries like Numpy, Pandas, Seaborn, Scikit-learn, Joblib,  altair, streamlit was used. Streamlit was mainly used for the front-end development, Linear regression model from the scikit-learn library was used to train a dataset containing speeches and their respective emotions.")
        st.caption('Created by: Shamika Shetty')

if __name__ == "__main__":
    main()