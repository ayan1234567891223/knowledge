import streamlit as st
st.title("Maths")

value = st.slider(label="Value", min_value=0, max_value=100)
st.write("Value: " , value)
st.write("Value square: " , value * value)
st.write("Value cube: " , value * value * value)

st.title("Cube")
cubel = st.slider(label="Cube length", min_value=0, max_value=100)
st.write("Volume: ", cubel * cubel * cubel)

st.title("Cuboid")
cuboidl = st.slider(label="Cuboid length", min_value=0, max_value=100)
cuboidb = st.slider(label="Cuboid breadth", min_value=0, max_value=100)
cuboidh = st.slider(label="Cuboid height", min_value=0, max_value=100)
st.write("Volume: " , cuboidl * cuboidb * cuboidh)

st.title("Cylinder")
cylinderh = st.slider(label="Cuboid Height", min_value=0, max_value=100)
cylinderr = st.slider(label="Cuboid Radius", min_value=0, max_value=100)
st.write("Volume: " , 22/7 * cylinderr * cylinderr * cylinderh)

st.title("Sphere")
spherer = st.slider(label="Sphere Radius", min_value=0, max_value=100)
st.write("Volume: " , 4/3 * 22/7 * spherer * spherer * spherer)

st.latex('''
(a+b)^2=a^2+2ab+b^2
''')
st.latex('''
(a-b)^2=a^2-2ab+b^2
''')
st.latex('''
a^2-b^2=(a+b)(a-b)
''')
st.latex('''
(x+a)(x+b)=x^2+ax+bx+ab
''')
