# ----------------------------- Cách 1: chạy uvicorn trực tiếp --------------------------------
'''from fastapi import FastAPI
# Name app
app = FastAPI()'''

# ----------------------------- Cách 2: cách 2 chạy theo cách truyền thống python file.py --------------------------------

'''from fastapi import FastAPI
import uvicorn

app = FastAPI()
print('First')
# Tại sao phải định nghĩa đoạn này - vì khi import file trong file khác thì  chỉ các đoạn code
# ngoài main mới được chạy các đoạn code trong main chỉ khi chính file này chạy mới được chạy
if __name__ == "__main__":
    #print('second')
    uvicorn.run(app)'''

# ------------------------------ First API ----------------------------------

# Ví dụ về decorator
#------------ Ứng dụng 1: Thêm chức năng cho hàm nhưng không muốn sửa hàm gốc
#VD: giờ ta có hàm chào mà cần xây dựng hàm GreatName mà không muốn sửa trong hàm great

def great():
    return "Hello"

def Great_Name(func):
    def SayHello():
        return func() +"Chiến"
    return SayHello

# Nhận đầu vào là hàm great -> trả về hàm mới có tên GreatName
# Cách code 1:
'''GreatName = Great_Name(great) # Nhận lại hàm có tên là GreatName
print(GreatName())'''

# Cách code 2: với cách viết như này hàm great() được sử dụng như một hàm mới
'''@Great_Name
def great():
    return "Hello "

print(great())
'''

#----------------------------- Ứng dụng 2: được sử dụng tái sử dụng code

 
'''@Great_Name
def chao():
    return "Chào "
print(chao())'''



from fastapi import FastAPI
app = FastAPI()

# @-decorator - khái niệm hàm chồng hàm trong python

# Trong đoạn code này @app.get('/') là một decorator của FastAPI được tái sử dụng cho hàm
# root() mà người dùng định nghĩa

'''
@app.get('/') # '/' đường dẫn trang chủ
def root():
    return "hello world"
'''

# ---------------------------------- Path operations --------------------------------------

#---------------------- Query parameter : Các tham số truy vấn 
data = [
    {
        'id': 0,
        'name': 'Chiến'
    },
    {
        'id':1,
        'name': 'Thư'
    }
]
'''
# Phương thức get: lấy ra thông tin gì đó của API
# ở đây user_id được định nghĩa là tham số truy vấn 
@app.get('/get_user') # Đường dẫn .../get_user cho phép sử dụng phương thức get của API 
def get_user(user_id: int):
    return data[user_id]


# Phương thức post: Tạo thông tin gì đó trong API
# user_name làm một tham số truy vấn  
@app.post('/post_user')# Đường dẫn .../post_user cho phép sử dụng phương thức post của API
def post_user(user_name : str):
    new_user = {
        'id' : len(data),
        'name': user_name
    }
    data.append(new_user)
    return data[new_user['id']]


# Phương thức Put của API: Cập nhật thông tin gì đó trong API
# id_user là tham số truy vấn 
@app.put('/put_user') # .../put_user là đường dẫn cho phép sử dụng phương thức PUT của API
def put_user(id_user:int, name: str):
    data[id_user]['id'] = id_user
    data[id_user]['name'] = name
    return data[id_user]


# Phương thức delete của API: Xóa thông tin nào đó trong API
@app.delete('/delete_user') #.../delete_use - đường dẫn cho phép sử dụng phương thức delete của API
def delete_user(id_user:int):
    data.remove(data[id_user])
    return {"message": "user is deleted successfull"}

'''
# --------------------------------- Path parameter

'''
@app.get('/get_user/{user_id}') # Đây là path parameter
def get_user(user_id:int):
    return data[user_id]

@app.put('/put_user/{user_id}') # path parameter and query parameter
def put_user(user_id:int, name:str):
    data[user_id]['name'] = name
    return data[user_id]
'''

# ------------------------------ Request body 

# Để sử dụng Request body cần tải gói pydantic

from pydantic import BaseModel

# Định nghĩa một kiểu DL User
'''
class User(BaseModel):
    id: int | None = None # Trường giá trị của id có thể int hoặc None và giá trị mặc định =None
    user_name : str

# Phương thức get lấy thông tin gì đó từ API -> sử dụng path parameter
@app.get('/get_user/{user_id}')
def get_user(user_id:int):
    return data[user_id]


# Phương thức Post tạo một thông tin gì đó trong API
@app.post('/post_user')
def post_user(user: User): # Biến user có kiểu DL là User được định nghĩa -> request body 
    # do kiểu DL của user là trường tự định nghĩa -> request body
    user.id = len(data)
    data.append(user)
    return user


# Phương thức put cập nhật thông tin nào đó trong API
@app.put('/put_user/{user_id}') # kết hợp query parameter, path parameter và request body
def put_user(user_id:int, user:User):
    data[user_id]['name'] = user.user_name
    return data[user_id]


# Phương thức delete xóa thông tin gì đó trong API
@app.delete('/delete_user/{user_id}')
def delete_user(user_id:int):
    data.remove(data[user_id])
    return{
        'messeage': 'user is deleted successfully '
    }
'''
# => Với Request body dữ liệu truyền vào API sẽ được bảo mật hơn.


# ---------------------------------- Return type: định nghĩa chặt chẽ kiểu DL mà API chả về
'''
class Item(BaseModel):
    name: str # Định nghĩa trường name có kiểu DL str
    price: float
    describe: str| None = None

@app.get('/get_item')
def get_item() -> list[Item]:
    return [
        Item(name="Iphone 17 Pro Max",price=1000),
        Item(name="Macbook ari M1", price=2000)
    ] 
'''

# -------------------------------- Annotated and Field
'''
from fastapi import Query
from pydantic import Field
from typing import Annotated

Items = [
    {
        'name': 'Iphone',
        'price': 1000,
        'describe': 'smartphone'
    },
    {
        'name': 'Macbook',
        'price':2000,
        'describe': 'laptop'
    }
]


# Sử dụng Field -> đặt các yêu cầu, các ràng buộc của trường. -> Đây là cách định nghĩa sâu hơn về
# các ràng buộc của các trường DL được định nghĩa các tham số truyền vào của hàm 
class Item(BaseModel):
    name:str = Field(..., min_length=1,max_length=30)
    price: float = Field(..., gt=0, description='price of items')
    describe : str|None = Field(
        None, max_length=500, description='info of item'
    )


@app.get('/get_items')
async def get_item(
    query_text: Annotated[str, Query(min_length=3, description="text to query")],
    max_price: Annotated[float|None, Query(gt=0, description='price of items')] = None
    # do hai tham số query_text và max_price đều là query parameter nên dùng hàm Query để ràng buộc
    # các yêu cầu các ràng buộc của tham số. Với các kiểu truyền DL trong API khác như path parameter
    # hoặc request body hàm Query có thể được thay thế bằng các hàm khác 
): 
    result = [item for item in Items if query_text.lower() in item['name'].lower() and item['price']<= max_price]
    return result


@app.post('/post_item')
async def post_item(item: Item):
    Items.append(item)
    return item
'''

# ----------------------------------File and Upload file
'''
from fastapi import File, UploadFile
from typing import Annotated

@app.post('/file')
def file(file: Annotated[bytes,File()]):
    return {
        'file_size': len(file)
    }
'''
'''
@app.post('/upload_file')
def upload_file(file: UploadFile):
    return {
        'file_name': file.filename,
        'content_type': file.content_type
    }
'''
'''
# upload nhiều file 
@app.post('/upload_file')
def upload_file(file: list[ UploadFile]):
    return [{
        'file_name': f.filename,
        'content_type': f.content_type} for f in file] 
'''
#---------------------------- Middelware -> thường được dùng để phân quyền cho
# phép/ Chặn domain gọi API của mình  -> Cơ chế bảo mật

'''
from fastapi.middleware.cors import CORSMiddleware

origins = [
    'http://127.0.0.1:8000'
]

# add_middelware là một phương thức của API
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, #  Cho phép web nào gọi đến API của mình
    allow_credentials=True, # Cho phép gửi cookie, token
    allow_methods=["*"],# Cho phép sử dụng method  nào
    allow_headers=["*"], # Cho phép những header nào 
)

@app.get('/')
def get_info():
    return {'message' : 'hello'}
'''

# -------------------------------- SaticFiles:
# => gắn foler tĩnh vào đường dẫn Path Url -> giúp cho client truy cập cách trực tiếp 
from fastapi.staticfiles import StaticFiles

@app.get('/')
def get_info():
    return {
        'message' :'Hello !'
    }

app.mount('/static',StaticFiles(directory='static'),name='static')
# -> truy cập http://127.0.0.1:8000/static/Me.jpg