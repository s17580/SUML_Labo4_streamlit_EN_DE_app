import streamlit as st
import pandas as pd
import matplotlib as plt
import os
from transformers import pipeline


# Streamlit configuration

st.set_page_config(page_title="Lab04 Translator", page_icon=":memo:", layout="centered")
st.title('Streamlit - Analiza Emocji i Tłumacz EN-DE')
st.image("translator.png", width=520)
st.info('Aplikacja uruchomiona poprawnie')
st.header('Opis aplikacji:')
st.write('Moja aplikacja ma dwa główne zastosowania:')
st.write('Pierwszym z nich jest ocena wydźwięku emocjonalnego tekstu. Pozwala ona na analizę, czy podane słowo jest negatywne, pozytywne czy neutralne.')
st.write('Drugim zastosowaniem jest tłumaczenie z języka angielskiego na niemiecki. Wystarczy wpisać dowolną frazę, a aplikacja dokona jej przekładu.')
st.write('Zapraszam do korzystania z aplikacji i cieszenia się jej funkcjonalnością!')

st.header('Instrukcja użytkowania')
st.write('1. Wybierz odpowiednią opcję z rozwijanego menu.')
st.write('2. Wprowadź tekst w odpowiednim polu tekstowym.')
st.write('3. Kliknij przycisk "Tłumacz" lub "Analizuj" i poczekaj na wyniki.')
st.write('4. Aby wyczyścić tekst, kliknij przycisk "Wyczyść tekst".')

st.header('Przetwarzanie języka naturalnego')

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu (eng->de)",
    ],
)

# Sentiment Analysis
if option == "Wydźwięk emocjonalny tekstu (eng)":
    if "sentiment_text" not in st.session_state:
        st.session_state.sentiment_text = ""

    if st.button("Wyczyść tekst"):
        st.session_state.sentiment_text = ""

    text = st.text_area(label="Wpisz tekst", key="sentiment_text")
    
    if st.button("Analizuj"):
        if text:
            classifier = pipeline("sentiment-analysis")
            with st.spinner('Analizuję...'):
                answer = classifier(text)
            st.success('Gotowe!')
            st.write(answer)
        else:
            st.warning('Proszę wpisać tekst do analizy.')
    

# Text Translation
elif option == "Tłumaczenie tekstu (eng->de)":
    if "translation_text" not in st.session_state:
        st.session_state.translation_text = ""

    if st.button("Wyczyść tekst"):
        st.session_state.translation_text = ""

    text = st.text_area(label="Wpisz tekst po angielsku", key="translation_text")

    if st.button("Tłumacz"):
        if text:
            translator = pipeline("translation_en_to_de")
            with st.spinner('Tłumaczę...'):
                translation = translator(text)
            st.success('Poprawnie przetłumaczono')
            st.write(translation[0]['translation_text'])
            st.balloons()
            
        else:
            st.warning('Proszę wpisać tekst do tłumaczenia.')

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Hugging Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Hugging Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')

st.header('Numer indeksu: s17580')