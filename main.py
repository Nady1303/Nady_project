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
    <width>760</width>
    <height>567</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>691</width>
      <height>441</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="tab_1">
     <attribute name="title">
      <string>Tab 1</string>
     </attribute>
     <widget class="QPushButton" name="diap">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>40</y>
        <width>121</width>
        <height>31</height>
       </rect>
      </property>
      <property name="text">
       <string>Введите диапазон</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_1">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>110</y>
        <width>141</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>  ОТ</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_2">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>240</y>
        <width>141</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;ДО&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>110</y>
        <width>131</width>
        <height>121</height>
       </rect>
      </property>
      <property name="text">
       <string>Получить 
число</string>
      </property>
     </widget>
     <widget class="QLabel" name="label">
      <property name="geometry">
       <rect>
        <x>490</x>
        <y>100</y>
        <width>121</width>
        <height>131</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_2">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
     <widget class="QPushButton" name="lang_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>20</y>
        <width>91</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>Выбрать язык</string>
      </property>
     </widget>
     <widget class="QPushButton" name="noun_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>80</y>
        <width>141</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Существительное </string>
      </property>
     </widget>
     <widget class="QPushButton" name="verb_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>150</y>
        <width>141</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Глагол </string>
      </property>
     </widget>
     <widget class="QPushButton" name="adj_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>220</y>
        <width>141</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Прилагательное</string>
      </property>
     </widget>
     <widget class="QPushButton" name="all_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>290</y>
        <width>141</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Все</string>
      </property>
     </widget>
     <widget class="QPushButton" name="translate_but">
      <property name="geometry">
       <rect>
        <x>420</x>
        <y>160</y>
        <width>151</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>Перевести слово</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_3">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>60</y>
        <width>181</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_4">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>250</y>
        <width>181</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_3">
     <attribute name="title">
      <string>Tab 2</string>
     </attribute>
     <widget class="QLabel" name="element">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>40</y>
        <width>181</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="add_but">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>110</y>
        <width>171</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Добавить элемент</string>
      </property>
     </widget>
     <widget class="QPushButton" name="del_but">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>190</y>
        <width>171</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Удалить элемент</string>
      </property>
     </widget>
     <widget class="QPushButton" name="clear_but">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>270</y>
        <width>171</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Заново</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_2">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>40</y>
        <width>211</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>Выбрать элемент</string>
      </property>
     </widget>
     <widget class="QLabel" name="choice">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>170</y>
        <width>201</width>
        <height>101</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_4">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
     <widget class="QPushButton" name="pushButton_3">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>60</y>
        <width>201</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>Предсказание</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_4">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>60</y>
        <width>201</width>
        <height>71</height>
       </rect>
      </property>
      <property name="text">
       <string>Совет</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_5">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>210</y>
        <width>441</width>
        <height>101</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:16pt; font-weight:600;&quot;&gt;Предсказание или совет&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_5">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
     <widget class="QPushButton" name="cub_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>50</y>
        <width>201</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>Бросить кости</string>
      </property>
     </widget>
     <widget class="QPushButton" name="coin_but">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>50</y>
        <width>201</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>Бросить монетку</string>
      </property>
     </widget>
     <widget class="QLabel" name="cub1">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>160</y>
        <width>81</width>
        <height>81</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="cub2">
      <property name="geometry">
       <rect>
        <x>150</x>
        <y>250</y>
        <width>81</width>
        <height>81</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="coin">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>160</y>
        <width>191</width>
        <height>171</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_6">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
     <widget class="QTableWidget" name="tableWidget">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>90</y>
        <width>231</width>
        <height>192</height>
       </rect>
      </property>
     </widget>
     <widget class="QTableWidget" name="tableWidget_2">
      <property name="geometry">
       <rect>
        <x>380</x>
        <y>90</y>
        <width>231</width>
        <height>192</height>
       </rect>
      </property>
     </widget>
     <widget class="QLabel" name="label_6">
      <property name="geometry">
       <rect>
        <x>70</x>
        <y>30</y>
        <width>121</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Смотрел&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_7">
      <property name="geometry">
       <rect>
        <x>420</x>
        <y>30</y>
        <width>131</width>
        <height>41</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Буду смотреть&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_5">
      <property name="geometry">
       <rect>
        <x>150</x>
        <y>310</y>
        <width>331</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>ВЫБРАТЬ ФИЛЬМ</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_7">
     <attribute name="title">
      <string>Страница</string>
     </attribute>
     <widget class="QPushButton" name="rules_but">
      <property name="geometry">
       <rect>
        <x>40</x>
        <y>30</y>
        <width>191</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>ПРАВИЛА</string>
      </property>
     </widget>
     <widget class="QPushButton" name="itog_but">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>30</y>
        <width>191</width>
        <height>61</height>
       </rect>
      </property>
      <property name="text">
       <string>ИСТОРИЯ</string>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox">
      <property name="geometry">
       <rect>
        <x>60</x>
        <y>170</y>
        <width>81</width>
        <height>71</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_2">
      <property name="geometry">
       <rect>
        <x>220</x>
        <y>170</y>
        <width>81</width>
        <height>71</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_3">
      <property name="geometry">
       <rect>
        <x>390</x>
        <y>170</y>
        <width>81</width>
        <height>71</height>
       </rect>
      </property>
     </widget>
     <widget class="QSpinBox" name="spinBox_4">
      <property name="geometry">
       <rect>
        <x>550</x>
        <y>170</y>
        <width>81</width>
        <height>71</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_6">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>340</y>
        <width>441</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>НАЧАТЬ/СБРОСИТЬ</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_7">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>270</y>
        <width>441</width>
        <height>51</height>
       </rect>
      </property>
      <property name="text">
       <string>ПРОВЕРИТЬ</string>
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
     <width>760</width>
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
        self.color1 = (170, 200, 255)
        self.color2 = (170, 170, 255)
        self.color3 = (170, 230, 255)
        if color == 1:
            self.color1 = (204, 255, 204)
            self.color2 = (255, 153, 204)
            self.color3 = (234, 255, 203)
        if color == 2:
            self.color1 = (255, 159, 172)
            self.color2 = (255, 185, 135)
            self.color3 = (255, 189, 183)
        if color == 3:
            self.color1 = (170, 200, 255)
            self.color2 = (170, 170, 255)
        if color == 4:
            self.color1 = (255, 255, 153)
            self.color2 = (255, 198, 85)
            self.color3 = (255, 255, 183)
        self.setStyleSheet(f"background-color: rgb{self.color3}")
        self.tabWidget.setStyleSheet(f"background-color: rgb{self.color1}")
        self.tab_1.setStyleSheet(f"background-color: rgb{self.color1}")
        self.tab_7.setStyleSheet(f"background-color: rgb{self.color1}")
        self.diap.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_1.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_2.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton.setStyleSheet(f"background-color: rgb{self.color2}")
        self.lang_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.noun_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.verb_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.adj_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.all_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.translate_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.element.setStyleSheet(f"background-color: rgb{self.color2}")
        self.add_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.del_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.clear_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_2.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_3.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_4.setStyleSheet(f"background-color: rgb{self.color2}")
        self.cub_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.coin_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_6.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_7.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_5.setStyleSheet(f"background-color: rgb{self.color2}")
        self.rules_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.itog_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_7.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_6.setStyleSheet(f"background-color: rgb{self.color2}")
        self.tabWidget.setTabText(0, 'Число')
        self.tabWidget.setTabText(1, 'Слово')
        self.tabWidget.setTabText(2, 'Элемент списка')
        self.tabWidget.setTabText(3, 'Будущее')
        self.tabWidget.setTabText(4, 'Выбор')
        self.tabWidget.setTabText(5, 'Что посмотреть')
        self.tabWidget.setTabText(6, 'Угадай чило')
        self.n1, self.n2 = 'от', 'до'
        self.diap.clicked.connect(self.run1)
        self.label_1.setText('  ОТ ')
        self.label_2.setText('  ДО ')
        self.pushButton.clicked.connect(self.r)

    def run1(self):
        self.n1, ok_pressed1 = QInputDialog.getText(self, "Введите число", "От:")
        self.n2, ok_pressed2 = QInputDialog.getText(self, "Введите число", "До:")
        if ok_pressed1:
            self.label_1.setText('  ОТ ' + self.n1)
            self.label_1.setStyleSheet(
                "background-color: rgb(170, 200, 255)")
        if ok_pressed2:
            self.label_2.setText('  ДО ' + self.n2)
            self.label_2.setStyleSheet(
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
            self.label.setText('   ' + str(n))
            self.label.setStyleSheet(
                f"background-color: rgb{self.color2}")
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
