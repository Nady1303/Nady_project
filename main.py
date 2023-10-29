import io
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

t = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>755</width>
    <height>502</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>20</y>
      <width>471</width>
      <height>371</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>3</number>
    </property>
    <widget class="QWidget" name="tab">
     <attribute name="title">
      <string>Tab 1</string>
     </attribute>
    </widget>
    <widget class="QWidget" name="tab_2">
     <attribute name="title">
      <string>Tab 2</string>
     </attribute>
    </widget>
    <widget class="QWidget" name="tab_3">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
    </widget>
    <widget class="QWidget" name="tab_4">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>755</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>603</width>
    <height>554</height>
   </rect>
  </property>
  <property name="palette">
   <palette>
    <active>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>200</red>
        <green>105</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
    </active>
    <inactive>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>200</red>
        <green>105</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
    </inactive>
    <disabled>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>120</red>
        <green>120</green>
        <blue>120</blue>
       </color>
      </brush>
     </colorrole>
    </disabled>
   </palette>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>541</width>
      <height>281</height>
     </rect>
    </property>
    <property name="palette">
     <palette>
      <active>
       <colorrole role="WindowText">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>0</green>
          <blue>127</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Button">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Base">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Window">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Highlight">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>210</red>
          <green>255</green>
          <blue>224</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="LinkVisited">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>255</red>
          <green>121</green>
          <blue>208</blue>
         </color>
        </brush>
       </colorrole>
      </active>
      <inactive>
       <colorrole role="WindowText">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>0</green>
          <blue>127</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Button">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Base">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Window">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Highlight">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>210</red>
          <green>255</green>
          <blue>224</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="LinkVisited">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>255</red>
          <green>121</green>
          <blue>208</blue>
         </color>
        </brush>
       </colorrole>
      </inactive>
      <disabled>
       <colorrole role="WindowText">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>120</red>
          <green>120</green>
          <blue>120</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Button">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Base">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Window">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>170</red>
          <green>170</green>
          <blue>255</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="Highlight">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>210</red>
          <green>255</green>
          <blue>224</blue>
         </color>
        </brush>
       </colorrole>
       <colorrole role="LinkVisited">
        <brush brushstyle="SolidPattern">
         <color alpha="255">
          <red>255</red>
          <green>121</green>
          <blue>208</blue>
         </color>
        </brush>
       </colorrole>
      </disabled>
     </palette>
    </property>
    
    <property name="currentIndex">
     <number>5</number>
    </property>
    <property name="elideMode">
     <enum>Qt::ElideLeft</enum>
    </property>
    <widget class="QWidget" name="tabWidgetPage1" native="true">
     <attribute name="title">
      <string>Число</string>
     </attribute>
     <widget class="QPushButton" name="pushButton">
      <property name="geometry">
       <rect>
        <x>200</x>
        <y>90</y>
        <width>101</width>
        <height>71</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">QPushButton{
	
	;
	background-color: rgb(170, 255, 255);
}</string>
      </property>
      <property name="text">
       <string>Получить
число</string>
      </property>
     </widget>
     <widget class="QPushButton" name="diap">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>30</y>
        <width>101</width>
        <height>21</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <property name="text">
       <string>Выбрать диапазон</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_3">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>90</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#aaffff;&quot;&gt;от&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_4">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>150</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#aaffff;&quot;&gt;до&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label">
      <property name="geometry">
       <rect>
        <x>380</x>
        <y>90</y>
        <width>111</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:16pt; color:#aaffff;&quot;&gt;0&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tabWidgetPage2" native="true">
     <attribute name="title">
      <string>Слово</string>
     </attribute>
     <widget class="QPushButton" name="nounBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>30</y>
        <width>131</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Существительное</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_5">
      <property name="geometry">
       <rect>
        <x>280</x>
        <y>90</y>
        <width>141</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QPushButton" name="verbBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>80</y>
        <width>131</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Глагол</string>
      </property>
     </widget>
     <widget class="QPushButton" name="adjBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>130</y>
        <width>131</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Прилагательное</string>
      </property>
     </widget>
     <widget class="QPushButton" name="allBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>180</y>
        <width>131</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Все</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tabWidgetPage3" native="true">
     <attribute name="title">
      <string>Элемент списка</string>
     </attribute>
     <widget class="QTextEdit" name="elem">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>40</y>
        <width>161</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
     </widget>
     <widget class="QPushButton" name="addBut">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>90</y>
        <width>141</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>Добавить элемент</string>
      </property>
     </widget>
     <widget class="QPushButton" name="delBut">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>140</y>
        <width>141</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>Удалить элемент</string>
      </property>
     </widget>
     <widget class="QPushButton" name="one_elem">
      <property name="geometry">
       <rect>
        <x>250</x>
        <y>40</y>
        <width>101</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Выбрать 
один элемент</string>
      </property>
     </widget>
     <widget class="QPushButton" name="clearBut">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>190</y>
        <width>141</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>Очистить</string>
      </property>
     </widget>
     <widget class="QPushButton" name="two_elem">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>40</y>
        <width>101</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(170, 255, 255);</string>
      </property>
      <property name="text">
       <string>Выбрать
 два элемента</string>
      </property>
     </widget>
     <widget class="QLabel" name="elem_res">
      <property name="geometry">
       <rect>
        <x>290</x>
        <y>120</y>
        <width>161</width>
        <height>81</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab">
     <attribute name="title">
      <string>Кости</string>
     </attribute>
     <widget class="QPushButton" name="cubBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>20</y>
        <width>171</width>
        <height>51</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 255, 255);</string>
      </property>
      <property name="text">
       <string>Бросить кости</string>
      </property>
     </widget>
     <widget class="QPushButton" name="coinBut">
      <property name="geometry">
       <rect>
        <x>300</x>
        <y>20</y>
        <width>171</width>
        <height>51</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 255, 255);</string>
      </property>
      <property name="text">
       <string>Бросить монетку</string>
      </property>
     </widget>
     <widget class="QLabel" name="cub1">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>100</y>
        <width>61</width>
        <height>61</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(0, 170, 255);</string>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QLabel" name="cub2">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>160</y>
        <width>61</width>
        <height>61</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 85, 127);</string>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QLabel" name="coin">
      <property name="geometry">
       <rect>
        <x>306</x>
        <y>100</y>
        <width>161</width>
        <height>111</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tabWidgetPage4" native="true">
     <attribute name="title">
      <string>Предсказание</string>
     </attribute>
     <widget class="QLabel" name="label_6">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>100</y>
        <width>461</width>
        <height>111</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:14pt; font-weight:600; color:#00ffff;&quot;&gt;Ваше предсказание&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_2">
      <property name="geometry">
       <rect>
        <x>110</x>
        <y>40</y>
        <width>291</width>
        <height>51</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 255, 255);</string>
      </property>
      <property name="text">
       <string>Получить предсказание</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_3">
     <attribute name="title">
      <string>Игра</string>
     </attribute>
     <widget class="QLabel" name="label_7">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>20</y>
        <width>461</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600; color:#55ffff;&quot;&gt;Было загадано четыре цифры (от 0 до 9)&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600; color:#55ffff;&quot;&gt;Ваша задача: угадать числа. Ниже будут даны подсказки &amp;gt;, &amp;lt;, =&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_1">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>110</y>
        <width>61</width>
        <height>51</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_2">
      <property name="geometry">
       <rect>
        <x>150</x>
        <y>110</y>
        <width>61</width>
        <height>51</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_3">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>110</y>
        <width>61</width>
        <height>51</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_4">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>110</y>
        <width>61</width>
        <height>51</height>
       </rect>
      </property>
     </widget>
     <widget class="QLabel" name="num1">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>180</y>
        <width>47</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QLabel" name="num2">
      <property name="geometry">
       <rect>
        <x>150</x>
        <y>180</y>
        <width>47</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="num3">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>180</y>
        <width>47</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QLabel" name="num4">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>180</y>
        <width>47</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QPushButton" name="checkBut">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>220</y>
        <width>451</width>
        <height>23</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 255, 255);</string>
      </property>
      <property name="text">
       <string>Проверить</string>
      </property>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>603</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <tabstops>
  <tabstop>tabWidget</tabstop>
  <tabstop>pushButton</tabstop>
 </tabstops>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup"/>
 </buttongroups>
</ui>
 """
template2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>559</width>
    <height>384</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(85, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QRadioButton" name="radioButton_1">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>50</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(170, 170, 255);
</string>
    </property>
    <property name="text">
     <string>Зелёный + розовый</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_2">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>120</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(170, 170, 255);
</string>
    </property>
    <property name="text">
     <string>Розовый + персиковый</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_3">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>190</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(170, 170, 255);
</string>
    </property>
    <property name="text">
     <string>Голубой + сиреневый</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_4">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>260</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(85, 255, 0);
background-color: rgb(170, 170, 255);
</string>
    </property>
    <property name="text">
     <string>Жёлтый + оранжевый</string>
    </property>
   </widget>
   <widget class="QPushButton" name="start_but">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>110</y>
      <width>161</width>
      <height>121</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(170, 170, 255);
;
</string>
    </property>
    <property name="text">
     <string>НАЧАТЬ</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>559</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

"""

color = 1


class Type1Error(Exception):
    pass


class Type2Error(Exception):
    pass


class Type3Error(Exception):
    pass


class Type4Error(Exception):
    pass


class Type5Error(Exception):
    pass


class Type6Error(Exception):
    pass


class Notebook2(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template2)
        uic.loadUi(f, self)
        self.radioButton_1.clicked.connect(self.change)
        self.radioButton_2.clicked.connect(self.change)
        self.radioButton_3.clicked.connect(self.change)
        self.radioButton_4.clicked.connect(self.change)
        self.start_but.clicked.connect(self.open_second_form)
        self.setStyleSheet("background-color: rgb(170, 200, 255)")

    def change(self):
        global color
        if self.sender() == self.radioButton_1:
            color = 1
            self.setStyleSheet("QMainWindow { background-color: rgb(204, 255, 204)}")
            self.start_but.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 153, 204)")
        if self.sender() == self.radioButton_2:
            color = 2
            self.setStyleSheet("QMainWindow { background-color: rgb(255, 159, 172) }")
            self.start_but.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 185, 135)")
        if self.sender() == self.radioButton_3:
            color = 3
            self.setStyleSheet("QMainWindow { background-color: rgb(170, 200, 255) }")
            self.start_but.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_1.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_2.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_3.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_4.setStyleSheet("background-color: rgb(170, 170, 255)")
        if self.sender() == self.radioButton_4:
            color = 4
            self.setStyleSheet("QMainWindow { background-color: rgb(255, 255, 153) }")
            self.start_but.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 198, 85)")

    def open_second_form(self):
        self.second_form = Notebook1()
        self.second_form.show()


class Notebook1(Notebook2):

    def __init__(self):
        super().__init__()
        f1 = io.StringIO(template1)
        uic.loadUi(f1, self)
        global color

        if color == 1:
            self.setStyleSheet("background-color: rgb(204, 255, 204)")
            self.tabWidget.setStyleSheet("background-color: rgb(204, 255, 204)")
            self.tabWidgetPage1.setStyleSheet("background-color: rgb(204, 255, 204)")
            self.tab_3.setStyleSheet("background-color: rgb(204, 255, 204)")
        if color == 2:
            self.setStyleSheet("background-color: rgb(255, 159, 172)")
            self.tabWidget.setStyleSheet("background-color: rgb(255, 159, 172)")
            self.tabWidgetPage1.setStyleSheet("background-color: rgb(255, 159, 172)")
            self.tab_3.setStyleSheet("background-color: rgb(255, 159, 172)")
        if color == 3:
            self.setStyleSheet("background-color: rgb(170, 200, 255)")
            self.tabWidget.setStyleSheet("background-color: rgb(170, 200, 255)")
            self.tabWidgetPage1.setStyleSheet("background-color: rgb(170, 200, 255)")
            self.tab_3.setStyleSheet("background-color: rgb(170, 200, 255)")
        if color == 4:
            self.setStyleSheet("background-color: rgb(255, 255, 153)")
            self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 153)")
            self.tabWidgetPage1.setStyleSheet("background-color: rgb(255, 255, 153)")
            self.tab_3.setStyleSheet("background-color: rgb(255, 255, 153)")
        self.n1, self.n2 = 'от', 'до'
        self.diap.clicked.connect(self.run1)
        self.pushButton.clicked.connect(self.r)

    def run1(self):
        self.n1, ok_pressed1 = QInputDialog.getText(self, "Введите число", "От:")
        self.n2, ok_pressed2 = QInputDialog.getText(self, "Введите число", "До:")
        if ok_pressed1:
            self.label_3.setText('oт ' + self.n1)
            self.label_3.setStyleSheet(
                "background-color: rgb(170, 200, 255)")
        if ok_pressed2:
            self.label_4.setText('до ' + self.n2)
            self.label_4.setStyleSheet(
                "background-color: rgb(170, 200, 255)")

    def r(self):
        try:
            if self.n1 == 'от':
                raise Type6Error
            if not self.n1.isdigit() and self.n2.isdigit():
                raise Type1Error
            if not self.n2.isdigit() and self.n1.isdigit():
                raise Type2Error
            if not self.n1.isdigit() and not self.n2.isdigit():
                raise Type3Error
            if int(self.n1) == int(self.n2):
                raise Type4Error
            if int(self.n1) > int(self.n2):
                raise Type5Error
            n = random.randrange(int(self.n1), int(self.n2) + 1)
            self.label.setText(str(n))
            self.label.setStyleSheet(
                "background-color: rgb(170, 200, 255)")
        except Type1Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Поменяйте первый\n элемент на число')
        except Type2Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Поменяйте второй\n элемент на число')
        except Type3Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Смените элементы \nдиапазона на числа')
        except Type4Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Числа диапазона не\nдолжны быть равны')
        except Type5Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('Второе число должно\nбыть больше первого')
        except Type6Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('      Введите числа\n        диапазона')
        except Exception:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('       Поменяйте числа\n    диапазона')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook2()
    ex.show()
    sys.exit(app.exec_())

