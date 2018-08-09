# Tkinter-Useful-Instance
这个仓库主要是用来... 记录一些经典 Tkinter-GUI 的代码模板，方便以后不记得 API 的时候来查一查。

## 一，各种组件

下面是在 Tkinter 中 10 中常用的部件，包括 Label, RadioButton 等以及它们的布局方式。


### 1-label&button 
显示静态的标签([1-static_label.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/1-label%26button/1-static_label.py))；用相应事件的按钮显示动态变化的标签([2-dynamic-lbl](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/1-label%26button/2-dynamic-lbl.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/1-label%26button/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/1-label%26button/photos/2.png"/>

### 2-Entry&Text
显示文本输入框(由掩码保护)、文本框和两个输入(即时，插尾)按钮([1-entry_text.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/2-Entry%26Text/1-entry_text.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/2-Entry%26Text/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/2-Entry%26Text/photos/2.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/2-Entry%26Text/photos/3.png"/>

### 3-Listbox 列表
创建一个复选框，每次按下按钮后，将框中所选字符串打印到标签上([1-listbox.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/3-Listbox/1-listbox.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/3-Listbox/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/3-Listbox/photos/2.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/3-Listbox/photos/3.png"/>

### 4-RadioButton
显示一个复项单选框。有多个选项，但是每次只能选择一个栏目，然后打印到标签上([1-radio.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/4-RadioButton/1-radio.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/4-RadioButton/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/4-RadioButton/photos/2.png"/>

### 5-Scale 尺度
显示一个可相应事件的拖动栏, 并将拖动条所处的位置实时打印到 label 上([scale.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/5-Scale/scale.py)).

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/5-Scale/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/5-Scale/photos/2.png"/>

### 6-Checkbutton
显示一个复项复选框，并通过相应事件将对应变量的值打印到标签上([check.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/6-Checkbutton/check.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/6-Checkbutton/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/6-Checkbutton/photos/2.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/6-Checkbutton/photos/3.png"/>

### 7-Canvas 画布
在窗口类 **Tk** 的基础上镶嵌一块画布类 Canvas，支持画直线，椭圆，显示图像等操作([7-Canvas](https://github.com/LiePleased/Tkinter-Useful-Instance/tree/master/instance/7-Canvas))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/7-Canvas/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/7-Canvas/photos/2.png"/>

### 8-Menu 菜单栏
显示一个窗口的可相应事件的菜单栏，类似于大部分 APP 应用的桌面设计([menubar.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/8-Menubar/menubar.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/8-Menubar/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/8-Menubar/photos/2.png"/>

### 9-Frame 框架
通过部件 Frame 管理 Tkinter 的布局，而且 Frame 之间是可叠加的，pack 可控制方位([frame.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/9-Frame/frame.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/9-Frame/photos/1.png"/>


### 10-Messagebox
通过按钮控制弹窗 messagebox。在 tkinter 中大概有 6 中不同的弹窗种类([message.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/10-Messagebox/message.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/10-Messagebox/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/10-Messagebox/photos/2.png"/>

### 11-Pack-Place
pack, grid 和 place 是 tkinter 中三种不同指定放置部件的方法，其中 place 放置的最精确([pack-grid.py](https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/11-Pack-Grid/pack-grid.py))。

<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/11-Pack-Grid/photos/1.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/11-Pack-Grid/photos/2.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/11-Pack-Grid/photos/3.png"/>
<img width="200" height="200" 
src="https://github.com/LiePleased/Tkinter-Useful-Instance/blob/master/instance/11-Pack-Grid/photos/4.png"/>

## 二，经典实例



