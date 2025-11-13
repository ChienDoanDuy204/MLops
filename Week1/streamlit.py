import streamlit as st
import cv2
from PIL import Image
import time
import numpy as np
#---------------------------- Hiển thị text ------------------------------

# Hiển thị tiêu đề của website
st.title("Trang web đầu tiên")
# Hiển thị đoạn text trên trang
st.text("streamlit is easy")


# Hiển thị header + các thay đổi màu sắc
st.header(":blue[Đây là header]")


# Hiển thị mardown giống như trong colab
pragraphs = """
**Đây là đoạn văn bản mardown giống như trong gooogle colab**
"""
st.markdown(pragraphs)

# hiển thị đoạn code
code = """
def compute_add(a,b):
    return a+b
"""
st.code(code,language='python')


#-------------------------------- Các đối tượng input ---------------------------------

# Tạo khung nhập text
name = st.text_input(label="write your name")

# Tạo khung nhập số
age = st.number_input(
    label="write your age ",
    value=0,# Giá trị mặc định khi không nhập gì
    step=1,# bước nhảy mỗi giá trị
    format="%d", # Định dạng kiểu nhập
    min_value=0, # giá trị min được nhập
    max_value=100 # giá trị max được nhập
)

# Hiển thị các thông tin đã nhập
st.write(f"your name input: {name}")
st.write(f"your age input: {age}")


# Tạo thanh trượt nhập các giá trị

lr = st.slider(label="hyper parameter",min_value=-1.0,max_value=1.0)

# Tạo check box
check = st.checkbox("agree show hyper parameter?")
if check:
    # Hiển thị hyper parameter đã chọn
    st.write(f"your hyper parameter is selected by you: {lr}")

# Tạo selectbox hộp chọn các giá trị được quy trước
lg = st.selectbox("your languge you use",
             ('python','c++','java') # các option để lựa chọn
             )

# Tạo lựa chọn radio
sys = st.radio(label="Your system",
         options=('ubuntu','window','ios')
)

# Tạo button input
bt = st.button("submit")
if bt: 
    st.write(f"your languge: {lg}")
    st.write(f"your system: {sys}")

# Tạo upload_file

file = st.file_uploader(label="chose your image",
                             type=['jpg','png'])
print(f"file:{file} ")
# Hiển thị ảnh
if file:
    img = Image.open(file)
    st.image(img)


#--------------------------- Các đối tượng media -----------------------------------------

# đọc và hiển thị video

video_file = open('D:\Deployment\Introduction to Regularization - YouTube.webm','rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Đối tượng audio

#---------------------------- Đối tượng bố cục: layout element ----------------------------

# Hiển thị dưới dạng các cột
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Cột 1")
with col2:
    st.subheader("Cột 2")
with col3:
    st.subheader("Cột 3")

# Hiển thị khung đóng gọi sử dụng st.container
with st.container(width=500,height=400):
    st.subheader("Login")
    st.text_input("name login")
    st.text_input("your password",type='password')
    st.button(":blue[login]")


#--------------------------- các đối tượng trạng thái status -------------------------

email = st.text_input(label="write your email")
bt = st.button(label="Submit")
if bt:
    if '@' not in email:
        # Thông báo lỗi
        st.error("please input correct type of email",icon="🐥") 
    else:
        # Thông báo thành công
        st.success("you submit correct",icon="💩")


# trạng thái chờ đợi

def load_model():
    # Hiển thị trạng thái quay
    with st.spinner("Model is loading ....."):
        time.sleep(5)
    is_loaded = np.random.choice([True,False])
    return is_loaded

model_load = load_model()
if model_load:
    st.success("model is loaded",icon="🐷")
else: st.error("model is failed",icon="🐽")
