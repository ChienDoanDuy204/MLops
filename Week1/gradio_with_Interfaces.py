import gradio as gr
import cv2
import numpy as np
import matplotlib.pyplot as plt
def greet(name):
    img = cv2.imread("Thu.jpg")
    return "Hello " + name, img[:,:,::-1]
demo = gr.Interface(
    fn= greet, # Hàm thực hiện chức năng gì đó -> Chứa model
    inputs=["text"],
    outputs=["text","image"]
)
demo.launch(share=True)
