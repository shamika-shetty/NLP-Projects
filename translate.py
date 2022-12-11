from newspaper import Article
import nltk
import goslate
from transformers import pipeline
import streamlit as st
from datetime import datetime

nltk.download('punkt')
gs = goslate.Goslate()

st.title('TRANSLATION AND SUMMARIZATION OF ARTICLE')

st.header('ENTER THE URL OF THE ARTICLE YOU WISH TO TRANSALTE AND SUMMARISE')

with st.form(key='url_form'):
            url = st.text_area("URL")
            submit_text = st.form_submit_button(label="Submit")
if submit_text :
	article = Article(url)
	article.download()
	article.parse()
	article.nlp()
	date = article.publish_date
	title = article.title
	language = st.selectbox("Choose the language to translate",('en - English','hi - Himdi','kn - Kannada','te - Telugu','la - Latin','fr - French'))
	lang = (language.split("-"))[0]
	corpus = article.text
	
	translatedtext = gs.translate(corpus,lang)
	trans_title = gs.translate(title,lang)
	st.write("Title :  ", title) 
	st.write("Translated  article ")
	st.write(translatedtext)
	st.write("Authors : ", article.authors)
	st.write("Published Date : ",date.strftime("%d-%m-%y"))
	st.write("Summarization : \n")
	summarizer = pipeline("summarization")
	summarized = summarizer(translatedtext, min_length=60, max_length=500)
	st.write(summarized)
else:
	st.write("Please provide the valid URL")
