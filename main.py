import streamlit as st
import pandas as pd

# with st.echo():

st.title('Streamlit Demo')
st.write('Hello World')

code = '''
  def hello():
    print('Hello, Streamlit!')
'''



btn_show_code = st.button('Show Code', type='secondary')

if btn_show_code:
  st.code(code, language='python')


cols = st.columns(2)
with cols[0]:
  age = st.number_input('Input Your Age')
  st.markdown(f'Your Age is {round(age, 2)}')

with cols[1]:
  # st.markdown('# NLP Task')
  str = st.text_input('Input Your String')
  word_tokenize = '-'.join(str.split())
  st.markdown(f'Your String is {word_tokenize}')


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.markdown('## Data Frame')
st.dataframe(df)

st.markdown('## Line Chart')
btn_show_chart = st.button('Show Graph')
if btn_show_chart:
  st.line_chart(df, x='first column', y='second column', x_label='Order', y_label='Value')