
# Translation and Text Summarization
It is difficult for us  to understand the contents of newspaper article which is in different languages like chinese,arabic,french etc, this model helps us to translate these contents of different languages to our desired language. Along with the contents of webpage it also tells us the title of the webpage, authors, date and time when this web page was published.

This model expects the url of the newpaper article that we need to translate, by using newspaper library we scrap the contents of the webpage then we use nltk to process the text. goslate library is used for text translation, this automtically detects the language of the web page, we have few options to select the languages to translate.

There are numerous articles that we read on a daily basis. As a result, there is a lot of data moving about, largely in the form of text. If we need to learn something about an article, we must read the entire piece to understand it, and many times those articles become excessively long. So, in order to receive the useful information, we must read the entire article, which is a complete waste of time, and if we need to read several articles like that for work purposes, it will take a long time, resulting in a loss of work hour. The goal of text summarizing is to see if we can come up with a method that employs natural language processing to do so. By using hugging face transformers we summarise the contents. This method will not only save time in comprehending a text, but it will also allow someone to read multiple texts in a short period of time





## Requirements
Libraries used are 

* Newspaper : Newspaper is a Python module used for extracting and parsing newspaper articles. Newspaper use advance algorithms with web scraping to extract all the useful text from a website. It works amazingly well on online newspapers websites. Since it use web scraping too many request to a newspaper website may lead to blocking, so use it accordingly.
  
  Installation :
  ```bash
  pip install newspaper3k
  ```
* nltk : NLTK is a standard python library with prebuilt functions and utilities for the ease of use and implementation. It is one of the most used libraries for natural language processing and computational linguistics.

  Installation :
  ```bash
  pip install nltk
  ```
* Goslate :  provides you free python API to google translation service by querying google translation website.

  It is:

  Free: get translation through public google web site without fee

  Fast: batch, cache and concurrently fetch

  Simple: single file module, just Goslate().translate('Hi!', 'zh')

  Installation :
  ```bash
  pip install goslate
  ```
* Hugging face - transformers : Hugging Face Transformer uses the Abstractive Summarization approach where the model develops new sentences in a new form, exactly like people do, and produces a whole distinct text that is shorter than the original.
    Installation :
  ```bash
  pip install transformers
  ```
## Deployment

Deployment is done using Streamlit
( refer : https://docs.streamlit.io/ )

To deploy this project run

```bash
  streamlit run translate.py
```

