import gradio as gr

def f(s):
    if '0' <= s[0] <= '9':
        s = 'P' + s
    return f"[https://www.luogu.com.cn/article/_new?problem={s}](https://www.luogu.com.cn/article/_new?problem={s})"

with gr.Blocks() as app:
    id = gr.Textbox(label="洛谷题目编号")
    sub = gr.Button("生成题解模版")
    out = gr.Markdown("")
    sub.click(f, id, outputs=out)

app.launch()