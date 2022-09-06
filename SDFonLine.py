import streamlit as st
from PIL import Image
from d3 import *
import xml.etree.ElementTree as ET
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SDFonLine by Axiang",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

components.iframe('https://www.viewstl.com/?embedded')

# components.html(
#     <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded" style="border:0;margin:0;width:100%;height:100%;"></iframe>
# )
# st.balloons()
# st.snow()

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
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
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
def xml_paser():
    global length
    # xml_file = st.file_uploader("Choose a file")
    # if xml_file is not None:
    #     tr = ET.parse(xml_file)
    #     root = tr.getroot()
    #     length = len(root)
    # 节点的类别鉴定
    # '''
    # 0 ---->None
    # 1 ----> Object:sphere, box...
    # 2 ----> Sign:Cut...
    # 3 ----> Panel
    # '''
    Object = ['Sphere', 'Box', 'Rounded_box', 'Wireframe_box', 'Torus', 'Capsule', 'Cylinder']
    Sign = ['Cut']
    def get_which(name):
        for i in Object:
            if name==i:
                return 1
        for i in Sign:
            if name==i:
                return 2
        if name=='Panel':
            return 3
        return 0


    # 获得节点的名字及其对应关系
    Name = []
    Id =[]
    tree = []
    for i in range(length):
        num = len(root[i])
        Id.append([])
        tree.append([])
        Id[i].append([])
        Id[i].append([])
        Name.append(root[i][1].text)
        for j in range(num):
            if root[i][j].tag=='Output':
                Id[i][0].append(root[i][j][0].text)
            if root[i][j].tag=='Input':
                Id[i][1].append(root[i][j][2].text)
                for ii in range(length):
                    num1 = len(root[ii])
                    for jj in range(num1):
                        if root[ii][jj].tag=='Output' and root[ii][jj][0].text==root[i][j][2].text:
                            tree[i].append(ii)
                

    # 找到最高层对应的序号
    def in_Name(name):
        for i in range(length):
            if Name[i] == name:
                return True
        return False
    def find_root():
        for i in range(length):
            num = len(root[i])
            count = 0
            for j in range(num):
                if root[i][j].tag == 'Output' and in_Name(root[i][j][1].text):
                    count +=1
            if count==0:
                return i


    # 建模部分
    def get_model(index):
        flag = get_which(Name[index])
        if flag==3:
            return (int(root[index][2][1].text))/100
        if flag==1:
            num = len(root[index])
            if Name[index]=='Cylinder':
                r = get_model(tree[index][0])
                h = get_model(tree[index][1])
                return capped_cylinder(-Z, Z, r)
            if Name[index]=='Box':
                l = get_model(tree[index][0])
                w = get_model(tree[index][1])
                h = get_model(tree[index][2])
                return box((l, w, h))
        if flag==2:
            f = []
            num = len(tree[index])
            for i in range(num):
                f.append(get_model(tree[index][i]))
            if Name[index]=='Cut':
                temp = f[0] - f[1]
                return temp
        pass
    
    # 测试区
    top = find_root()
    f = get_model(top)
    f.save('out.stl')

if my_select=="From xml files":
    """On this page, you can get sample models from xml files made from Grasshopper's ghx files.\n
---
    """
    xml_file = st.file_uploader("Choose a file")
    if xml_file is not None:
        tr = ET.parse(xml_file)
        root = tr.getroot()
        length = len(root)
        xml_paser()
        file = open('out.stl', "rb")
        st.download_button(label="Download", data=file, mime='application/vnd.ms-pkistl', file_name="out.stl", help="Click to download the stl file")
    pass


# aphorism
"""
&nbsp;\n
&nbsp;\n
&nbsp;\n
> &emsp;&emsp;&emsp;&emsp;"*All things are difficult before they are easy.*"
"""