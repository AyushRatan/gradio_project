import gradio as gr

def login(username,password):
    return {"username":username,"password":password}

with gr.Blocks() as demo:
    username = gr.Textbox(label="username")
    password = gr.Textbox(label="password")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=login, inputs=[username,password], outputs=output, api_name="greet")
  

demo.launch()
print("Hello world!")