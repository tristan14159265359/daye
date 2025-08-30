import streamlit as st
import numpy as np
import math

# 设置页面标题和描述
st.title("泰勒级数演示器")
st.write("使用简单的多项式来逼近复杂的函数。")

# 左侧侧边栏，用于参数调整
st.sidebar.header("参数调整")

# 选择函数
function_name = st.sidebar.selectbox(
    "选择函数",
    ("e^x", "sin(x)")
)

# 多项式项数
n_terms = st.sidebar.slider(
    "多项式项数 n",
    0, 10, 0
)

# 核心计算逻辑
x = np.linspace(-5, 5, 400)

if function_name == 'e^x':
    y_original = np.exp(x)
    y_taylor = np.zeros_like(x)
    for i in range(n_terms + 1):
        y_taylor += (x**i) / math.factorial(i)
    
    title_text = f"eˣ 的泰勒级数逼近 (n={n_terms})"
    
elif function_name == 'sin(x)':
    y_original = np.sin(x)
    y_taylor = np.zeros_like(x)
    for i in range(n_terms + 1):
        if i % 2 == 1:
            term = (x**i) / math.factorial(i)
            if (i - 1) % 4 == 2:
                y_taylor -= term
            else:
                y_taylor += term
    
    title_text = f"sin(x) 的泰勒级数逼近 (n={n_terms})"

# 在主页面上显示图表
st.header(title_text)
st.line_chart(y_original, use_container_width=True)
st.line_chart(y_taylor, use_container_width=True)

st.write("注：上图是原始函数，下图是泰勒多项式逼近。")