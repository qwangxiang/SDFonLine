import streamlit as st
from PIL import Image
from d3 import *
import xml.etree.ElementTree as ET
import vtk

st.set_page_config(
    page_title="SDFonLine by Axiang",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# st.balloons()
# st.snow()

# stl预览
def view():
    # create data mannualy
    # cylinder = vtk.vtkCylinderSource()
    # cylinder.SetHeight(3.0) # 设置柱体的高
    # cylinder.SetRadius(1.0) #  设置柱体横截面的半径
    # cylinder.SetResolution(6) # 设置柱体横截面的等边多边形的边数
 
    # Read from file
    stlreader = vtk.vtkSTLReader()
    stlreader.SetFileName("out.stl")
 
    cylinderMapper = vtk.vtkPolyDataMapper() # 渲染多边形几何数据
    cylinderMapper.SetInputConnection(stlreader.GetOutputPort()) # VTK可视化管线的输入数据接口 ，对应的可视化管线输出数据的接口为GetOutputPort()；
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper) # 设置生成几何图元的Mapper。即连接一个Actor到可视化管线的末端(可视化管线的末端就是Mapper)。
    renderer = vtk.vtkRenderer() # 负责管理场景的渲染过程
    renderer.AddActor(cylinderActor)
    renderer.SetBackground(0.1, 0.2, 0.4)
    renWin = vtk.vtkRenderWindow() # 将操作系统与VTK渲染引擎连接到一起。
    renWin.AddRenderer(renderer)
    renWin.SetSize(300, 300)
    iren = vtk.vtkRenderWindowInteractor() # 提供平台独立的响应鼠标、键盘和时钟事件的交互机制
    iren.SetRenderWindow(renWin)
 
    # 交互器样式的一种，该样式下，用户是通过控制相机对物体作旋转、放大、缩小等操作
    style = vtk.vtkInteractorStyleTrackballCamera()
 
    iren.SetInteractorStyle(style)
    iren.Initialize()
 
    iren.Start()
 
    # Clean up
    # del cylinder
    del stlreader
    del cylinderMapper
    del cylinderActor
    del renderer
    del renWin
    del iren

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
        if st.button('View', help='Click to view the stl file.'):
            view()
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

    if st.button('View', help='Click to view the stl file.'):
        view()
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
        if st.button('View', help='Click to view the stl file.'):
            view()
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