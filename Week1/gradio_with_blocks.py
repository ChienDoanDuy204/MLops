import gradio as gr
def greeting(name,age):
    return 'Hello, '+ name + f"-{age}"

# strating => Mặc định bố cục mỗi thành phần là 1 hàng

'''with gr.Blocks() as demo:
    input = gr.Textbox(label='Name')
    age = gr.Number(label='age')
    btn = gr.Button('Send')
    output = gr.Textbox(label='greeting')
    # Định nghĩa even khi click button
    btn.click(fn=greeting,inputs=[input,age],outputs=output)'''

# Chia theo bố cục ngang
with gr.Blocks() as demo:
    # Bố cục với hàng
    with gr.Row():
        # Hai phần tử trên cùng một hàng
        input = gr.Textbox(label='Name')
        age = gr.Number(label='age')
    btn = gr.Button('Send')
    output = gr.Textbox(label='greeting')
    # Định nghĩa even khi click button
    btn.click(fn=greeting,inputs=[input,age],outputs=output)
demo.launch()