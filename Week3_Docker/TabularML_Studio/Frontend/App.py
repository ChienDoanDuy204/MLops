# -------------------------------- Home Page -------------------------------
import streamlit as st
import requests
import pandas as pd
st.set_page_config(layout="wide") # Xét chiều rộng của page

#----------------------- Navigation bar ------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def switch_page(page):
    st.session_state.current_page = page

def navbar():
    st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button {
            background-color: None!important;
            color: black !important;
            font-weight: 600 !important;
            padding: 10px 22px !important;
            border-radius: 8px !important;
            border: none !important;
        }

        div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button:hover {
            background-color: #d73c3c !important;
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

        cols = st.columns(4)
        with cols[0]:
            if st.button("Home"):
                switch_page("Home")
        with cols[1]:
            if st.button("Upload & Train"):
                switch_page("Upload_Train")
        with cols[2]:
            if st.button("Predict"):
                switch_page("Predict")
        with cols[3]:
            if st.button("About"):
                switch_page("About")

        st.markdown('</div>', unsafe_allow_html=True)

#======================================================= pages =================================================


########## Pages Home ###########
def Home():
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.markdown(
                "<h1 style = 'font-size:100px;'>Welcome To TabularML Studio</h1>",
                unsafe_allow_html=True
            )
            Paragraphs = "A web application is developed to apply Machine Learning for predict tarbular dataset."
            st.header(Paragraphs,anchor=False)
            #------ button------
            get_start_button = st.button(label="Get Started",width=200,type="primary")
            #---------------------
        with col2:
            st.image(image='assets/tarbular_data.png',width=450)
        if get_start_button:
            switch_page("Upload_Train")



############ Page Upload & Train ############
def get_DataUploaded(file_upload):
    url = 'http://backend_container:8000/upload_csv'
    files = {
        "file": (file_upload.name,file_upload.getvalue(),'text/csv')
    }
    response = requests.post(url=url,files=files)
    if response.status_code == 200:
        Json = response.json()
        return Json
def get_name_Columns():
    url = 'http://backend_container:8000/get_name_column_df'
    json_get_name_cols = requests.get(url=url)
    if json_get_name_cols.status_code == 200:
        options_features = json_get_name_cols.json()['name_cols']
        return options_features
# Hàm Hiển thị dữ liệu đã được upload lên()
def display_data_uploaded(placeholder_df,placeholder_describe):
    if st.session_state.df is not None and st.session_state.df_describe is not None:
        placeholder_df.dataframe(st.session_state.df)
        placeholder_describe.dataframe(st.session_state.df_describe)
    else:
        st.warning("⚠️ you must upload your data before click Submit!")
# Hàm hiển thị box chọn feature huấn luyện và biến mục tiêu của mô hình.
def display_box_select_feature(placeholder_features_train, placeholder_target):
    if st.session_state.option_features is not None:
        selected_feature = placeholder_features_train.multiselect(label="Select Features:",options=st.session_state.option_features, key = 'feature_selected',max_selections = len(st.session_state.option_features)-1)
        selected_target = placeholder_target.selectbox(label="Select Target:",options=st.session_state.option_features,key = 'target_selected')
def Upload_Train():
    with st.container():
        st.subheader("Upload your file.csv", anchor=False)
        file_upload = st.file_uploader(label="Upload file.csv",type=['csv'])
        st.button(label='Submit',type="primary",key = "bt_submit")
        # Tạo khoảng trống để hiển thi DL chưa được hiển thị
        placeholder_df = st.empty()
        st.subheader("📊 Info of your Tabular Data",anchor=False)
        placeholder_describe = st.empty()
        if 'df' not in st.session_state:
            st.session_state.df = None
        if 'df_describe' not in st.session_state:
            st.session_state.df_describe = None
        if st.session_state.bt_submit:
            if file_upload is not None:
                Json_Response = get_DataUploaded(file_upload)
                st.session_state.df = pd.DataFrame(Json_Response['data'])
                st.session_state.df_describe = pd.DataFrame(Json_Response['describe']['data'],columns=Json_Response['describe']['columns'],index=Json_Response['describe']['index'])
        # show tabular_data is uploaded
        display_data_uploaded(placeholder_df, placeholder_describe)
    with st.container(border=True):
        st.subheader("⚙️ Configuration Model",anchor=False)
        Model = st.selectbox(label="1.Select Model ML",
                                options=["KNN", "Decision Tree", "Random Forest", "Adaboost", "GradientBoost", "Linear Regression"], key = "Model_selected"
                                )
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("2. Select Feature")
            if "option_features" not in st.session_state:
                st.session_state.option_features = None
            placeholder_features_train = st.empty()
            placeholder_target = st.empty()
            if file_upload is None:
                placeholder_features_train.warning("⚠️ you must upload your data to select feature!")
            else:
                if st.session_state.bt_submit:
                    st.session_state.option_features = get_name_Columns()
            display_box_select_feature(placeholder_features_train, placeholder_target)
        with col3:
            st.text("4. ⚡Enable Auto-Tuning")
            enable_auto_tuning = st.toggle(label="OFF / ON",key = "enable_auto_tuning")
        with col2:
            st.text("3. Select Parameters")
            with st.container(border=True,width=400):
                if Model == "KNN":
                    n_neighbors = st.slider(label="1.Select number of Neighbors:",
                    min_value=1, max_value=20,step=1,disabled=st.session_state.enable_auto_tuning)
                    weights = st.pills(label="2.Selection weights:",
                                    options=["uniform","distance"],selection_mode="single",disabled=st.session_state.enable_auto_tuning)
                    metric = st.pills("3.metric:",options=["euclidean","manhattan","minkowski"],
                                    selection_mode="single",disabled=st.session_state.enable_auto_tuning)
                    model_info = {
                        "n_neighbors": n_neighbors,
                        "weights":weights,
                        "metric":metric,
                    }

                elif Model == "Decision Tree":
                    criterion = st.pills(label="1.criterion:",
                                            options=["squared_error","absolute_error"],disabled=st.session_state.enable_auto_tuning)
                    max_depth = st.slider(label="2.max_depth:",min_value=1,max_value=30,step=1,disabled=st.session_state.enable_auto_tuning)
                    min_samples_split = st.slider(label="3.min_samples_split:",min_value=2,max_value=10,step=1,disabled=st.session_state.enable_auto_tuning)
                    min_samples_leaf = st.slider(label="4.min_samples_leaf:",min_value=1, max_value=30, step=1,disabled=st.session_state.enable_auto_tuning)
                elif Model == "Random Forest":
                    pass
                elif Model =="Adaboost":
                    pass
                elif Model =="GradientBoost":
                    pass
                elif Model =="Linear Regression":
                    pass
        Training_button = st.button(label="🚀 START TRAINING",width="stretch",type="primary")
        if Training_button:
            if Model == "KNN":
                url = "http://backend_container:8000/post_KNN_trained"
                response = requests.post(url=url,json=model_info)
                if response.status_code == 200:
                    JsonKNN_reponse = response.json()
                    st.success(JsonKNN_reponse["Message"])
#------------------------------------------------------------------------------------
def render_page():
    page = st.session_state.current_page

    if page == "Home":
            Home()
    elif page == "Upload_Train":
        Upload_Train()
    elif page == "Predict":
        pass

navbar()
render_page()