import streamlit as st
import time


st.title('Streamlit 超入門')

st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'進捗率{i+1}')
    bar.progress(i+1)
    time.sleep(0.2)

'Done'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('右カラム')

question = st.expander('ですか？')
question.write('そうです')
question = st.expander('ですか？')
question.write('そうです')
question = st.expander('ですか？')
question.write('そうです')



# hobby = st.text_input('あなたの趣味は？')
# 'あなたの趣味は', hobby

# stress = st.slider("あなたのストレスは？", 0, 10, 5)
# 'あなたのストレス度', stress

# number = st.selectbox("あなたが好きな数字を教えて", list(range(1, 11)))
# 'あなたが好きな数字:', number , 'です'

# if st.checkbox("Show Image"):
#     img = Image.open('sample.png')
#     st.image(img, caption="chess board", use_column_width=True)




# 仮想環境でつながるのなぜ

# st.title('Streamlit 超入門')

# st.write('Display Image')

# img = Image.open('sample.png')
# st.image(img, caption="chess board", use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
#     })

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.1,140],
#     columns=["lat", "lon"]
# )


# st.table(df)

# st.line_chart(df)

# st.map(df)

# """
# # 章
# ## 節
# ### 項
# ''' python
# st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
#     })

# st.table(df)
# '''
# """
