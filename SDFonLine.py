import streamlit as st
from PIL import Image
from d3 import *

# st.balloons()
 
# sidebar
st.sidebar.write("&emsp;&emsp;\"*We will begin a fantastic journey.*\"")
my_select = "Welcome"
my_select = st.sidebar.selectbox("Please select:", ("Homepage", "What is SDF", "Basic models", "Combined models","From xml files"))

# homepage
if my_select=="Homepage":
    c1, c2 = st.columns([3,1])
    with c1:
        """
        # Welcom to SDFonLine!  
        &emsp;&emsp;On this website you can model online and download the *.stl* files.\n
        &emsp;&emsp;From the **sidebar** you can learn about what SDF is and **download**\n
        &emsp;&emsp;some models created by SDF.
        """
    with c2:
        st.image(Image.open('pictures/081001.jpg'))
    """
    ---\n
    &emsp;&emsp;*Some of the models are listed as follows* 
    """ 
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image(Image.open('pictures/080901.png'))
    with c2:
        st.image(Image.open('pictures/080902.png'))
    with c3:
        st.image(Image.open('pictures/080903.png'))
    
# what is sdf
if my_select=="What is SDF":
    """
    # **What** is *SDF*?
    ---
    &emsp;&emsp;SDF, standing for **Signed Distance Function**, uses codes and the Marching Cubes algorithm to generate a mesh. The goal is to provide a simple, fun, and easy-to-use API for generating 3D models in our favorite language Python!  

    &emsp;&emsp;Click the box below to view a demo.
    """
    c1, c2 = st.columns([1,1])
    with c1:
        with st.expander("INPUT", False):
            """``` python
from sdf import * \n
f = sphere(1) & box(1.5) \n
c = cylinder(0.5) \n
f -= c.orient(X) | c.orient(Y) | \n
c.orient(Z) \n
f.save('out.stl') \n
            """  #这个对齐真的很怪~
    with c2:
        with st.expander("OUTPUT", False):
            st.image(Image.open('pictures/080802.png'), width=300, caption="model")
    f = sphere(1) & box(1.5)
    c = cylinder(0.5)
    f -= c.orient(X) | c.orient(Y) | c.orient(Z)
    f.save('out.stl')
    file = open('out.stl', "rb")
    st.download_button(label="Download", data=file, mime='application/vnd.ms-pkistl', file_name="out.stl", help="Click to download the stl file")
    """
    Click [here](https://github.com/fogleman/sdf) to learn more.
    """

# basic models
if my_select=="Basic models":
    """**Notice**: For basic, single models, their **geometry center** is at (0,0,0) by default when they are born."""
    c1, c2 = st.columns([2, 1])
    with c1:
        basic_select = st.selectbox("Please choose the model you want to download.", ("sphere", "box", "rounded_box", "wireframe_box","torus"))
    if basic_select=="sphere":
        c1, c2 = st.columns([2, 1])
        with c1:
            radius = st.number_input('Please select a radius:', 0.0, 100.0, 1.0, 0.1)
        with c2:
            st.image(Image.open('pictures/081002.png'))
        f = sphere(radius)
        f.save('out.stl')
    if basic_select=="box":
        c1, c2 = st.columns([2, 1])
        with c1:
            length = st.number_input('Please set the length:', 0.0, 100.0, 1.0, 0.1)
            width = st.number_input('Please set the width:', 0.0, 100.0, 1.0, 0.1)
            height = st.number_input('Please set the height:', 0.0, 100.0, 1.0, 0.1)
        with c2:
            st.image(Image.open('pictures/081004.png'))
        f = box(length, width, height)
        f.save('out.stl')
    if basic_select=="rounded_box":
        c1, c2 = st.columns([2, 1])
        with c1:
            length = st.number_input('Please set the length:', 0.0, 100.0, 1.0, 0.1)
            width = st.number_input('Please set the width:', 0.0, 100.0, 1.0, 0.1)
            height = st.number_input('Please set the height:', 0.0, 100.0, 1.0, 0.1)
            radius = st.number_input('Please set a radius:', 0.0, 10.0, 0.1,  0.01)
        with c2:
            st.image(Image.open('pictures/081003.png'))
        f = rounded_box((length, width, height), radius)
        f.save('out.stl')
    if basic_select=="wireframe_box":
        c1, c2 = st.columns([2, 1])
        with c1:
            length = st.number_input('Please set the length:', 0.0, 100.0, 1.0, 0.1)
            width = st.number_input('Please set the width:', 0.0, 100.0, 1.0, 0.1)
            height = st.number_input('Please set the height:', 0.0, 100.0, 1.0, 0.1)
            thickness = st.number_input('Please set a thickness:', 0.0, 10.0, 0.1,  0.01)
        with c2:
            st.image(Image.open('pictures/081005.png'))
        f = wireframe_box((length, width, height), thickness)
        f.save('out.stl')
    if basic_select=="torus":
        c1, c2 = st.columns([2, 1])
        with c1:
            r1 = st.number_input('Please set r1:', 0.0, 100.0, 1.0, 0.01)
            r2 = st.number_input('Please set r2:', 0.0, 100.0, 1.0, 0.01)
        with c2:
            st.image(Image.open('pictures/081006.png'))
        f = torus(r1, r2)
        f.save('out.stl')

    file = open('out.stl', "rb")
    st.download_button(label="Download", data=file, mime='application/vnd.ms-pkistl', file_name="out.stl", help="Click to download the stl file")

# comboned models
if my_select=="Combined models":
    """gugugu~~~"""
    
# From xml files
if my_select=="From xml files":
    """On this page, you can get sample models from xml files made from Grasshopper's ghx files.
       
    ---
    """
    pass



# aphorism
"""
&nbsp;\n
&nbsp;\n
&nbsp;\n
> &emsp;&emsp;&emsp;&emsp;"*All things are difficult before they are easy.*"
"""