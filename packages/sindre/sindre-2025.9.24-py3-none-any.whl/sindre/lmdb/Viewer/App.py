# -*- coding: UTF-8 -*-
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@path   ：ToothSegData -> 3D_Lmdb_Viewer.py
@IDE    ：PyCharm
@Author ：sindre
@Email  ：yx@mviai.com
@Date   ：2023/9/1 13:30
@Version: V0.1
@License: (C)Copyright 2021-2023 , UP3D
@Reference: 
@History:
- 2023/9/1 :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(一)本代码的质量保证期（简称“质保期”）为上线内 1个月，质保期内乙方对所代码实行包修改服务。
(二)本代码提供三包服务（包阅读、包编译、包运行）不包熟
(三)本代码所有解释权归权归神兽所有，禁止未开光盲目上线
(四)请严格按照保养手册对代码进行保养，本代码特点：
      i. 运行在风电、水电的机器上
     ii. 机器机头朝东，比较喜欢太阳的照射
    iii. 集成此代码的人员，应拒绝黄赌毒，容易诱发本代码性能越来越弱
声明：未履行将视为自主放弃质保期，本人不承担对此产生的一切法律后果
如有问题，热线: 114

"""
__author__ = 'sindre'

import numpy as np
# You may need to uncomment these lines on some systems:
import vtk.qt
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (QFileDialog, QInputDialog, QMessageBox, QLineEdit, 
                            QDialog, QVBoxLayout, QComboBox, QLabel, QPushButton,
                            QDialogButtonBox, QGroupBox)

vtk.qt.QVTKRWIBase = "QGLWidget"
import vtk
import os
import vedo
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidgetItem
from PyQt5 import QtWidgets, QtCore
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vedo import Plotter, Points
from UI.View_UI import Ui_Form,DataConfigDialog
import qdarkstyle
from sindre.lmdb import Reader,Writer
from sindre.utils3d  import labels2colors
import configparser

class config_thread(QtCore.QThread):
    progress_int = QtCore.pyqtSignal(int)

    def __init__(self, db_path, config_parser, name_key, start_idx, end_idx):
        super().__init__()
        self.config_parser = config_parser
        self.db_path = db_path
        self.name_key = name_key
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.len_idx = end_idx - start_idx

    def run(self):
        self.progress_int.emit(0)
        
        # 确保有INDEX_MAPPING节
        if not self.config_parser.has_section('INDEX_MAPPING'):
            self.config_parser.add_section('INDEX_MAPPING')
        
        for i in range(self.start_idx, self.end_idx):
            with Reader(self.db_path) as db:
                data = db[i]
            k = str(i)
            v =data.get(self.name_key, "unknown")
            if np.issubdtype(v.dtype,np.str_) or isinstance(v,str) :
                v = str(v)
                if len(v)>34:
                    v=f"*{v[-34:]}"
            else:
                v = f"numpy_{k}_{v.shape}"
            
            # 使用configparser存储映射
            self.config_parser.set('INDEX_MAPPING', k, v)
            self.config_parser.set('INDEX_MAPPING', v, k)
            
            self.progress_int.emit(int(i * 99 / self.len_idx))
            
        self.progress_int.emit(100)

class LMDB_Viewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.app_ui = Ui_Form()
        self.app_ui.setupUi(self)
    
        # 基础变量
        self.vp = None
        self.count = 0
        self.max_count = 0
        self.current_mesh = None
        self.db_path = None
        self.fileName = None
        self.page_size = 15
        self.current_page = 1
        
        # 使用configparser作为缓存
        self.config_parser = configparser.ConfigParser()
        self.config_file = "viewer_config.ini"
        
        # 加载现有配置或创建新配置
        if os.path.exists(self.config_file):
            self.config_parser.read(self.config_file, encoding='utf-8')
            # 加载缓存的路径信息
            if self.config_parser.has_option('DATA_CONFIG', 'db_path'):
                self.db_path = self.config_parser.get('DATA_CONFIG', 'db_path')
                self.app_ui.path_label.setText(self.db_path)
        else:
            # 创建默认配置
            self.config_parser.add_section('DATA_CONFIG')
            self.config_parser.set('DATA_CONFIG', 'data_type', '网格(Mesh)')
            self.config_parser.set('DATA_CONFIG', 'vertex_key', 'mesh_vertices')
            self.config_parser.set('DATA_CONFIG', 'vertex_label_key', 'vertex_labels')
            self.config_parser.set('DATA_CONFIG', 'face_key', 'mesh_faces')
            self.config_parser.set('DATA_CONFIG', 'face_label_key', 'face_labels')
            self.config_parser.set('DATA_CONFIG', 'name_key', 'name')
            # 创建STATE节
            self.config_parser.add_section('STATE')
            self.config_parser.add_section('INDEX_MAPPING')
            self.save_config()
        
        # 从配置加载数据设置
        self.data_config = {
            "data_type": self.config_parser.get('DATA_CONFIG', 'data_type'),
            "vertex_key": self.config_parser.get('DATA_CONFIG', 'vertex_key'),
            "vertex_label_key": self.config_parser.get('DATA_CONFIG', 'vertex_label_key'),
            "face_key": self.config_parser.get('DATA_CONFIG', 'face_key'),
            "face_label_key": self.config_parser.get('DATA_CONFIG', 'face_label_key'),
            "name_key": self.config_parser.get('DATA_CONFIG', 'name_key')
        }

        # 信息视图
        self.app_ui.treeWidget.setHeaderLabels(["键名", "类型", "大小"])
        self.app_ui.treeWidget.setColumnCount(3)
        self.app_ui.treeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        # 按钮绑定 
        self.app_ui.openmdbBt.clicked.connect(self.OpenFile)
        self.app_ui.NextButton.clicked.connect(self.NextFile)
        self.app_ui.PreButton.clicked.connect(self.PreFile)
        self.app_ui.JumpButton.clicked.connect(self.JumpCount)
        self.app_ui.SearchButton.clicked.connect(self.search)
        self.app_ui.NameView.clicked.connect(self.show_selected_value)
        self.app_ui.state_bt.clicked.connect(self.SetState)
        self.app_ui.Pre_view_Button.clicked.connect(self.Previous_Page)
        self.app_ui.Next_view_Button.clicked.connect(self.Next_Page)
        self.app_ui.functionButton.clicked.connect(self.ExportMesh)
        

        # 3D界面 
        self.vtkWidget = QVTKRenderWindowInteractor(self)
        self.app_ui.horizontalLayout.addWidget(self.vtkWidget)
        self.vp = Plotter(N=1, qt_widget=self.vtkWidget)
        self.vp.show(bg="black")
        
        # 确保有INDEX_MAPPING && STATE 节点
        if not self.config_parser.has_section('INDEX_MAPPING'):
            self.config_parser.add_section('INDEX_MAPPING')
            self.save_config()
        if not self.config_parser.has_section('STATE'):
            self.config_parser.add_section('STATE')
            self.save_config()


   
    
    def pre_processing(self):
        self.UpdateDisplay()
        self.load_view_data()

    ###############################按钮逻辑#######################################

    def ExportMesh(self):
        """导出当前视图中的网格为PLY文件"""
        try:
            # 确保有可导出的对象
            if self.current_mesh is None:
                QMessageBox.warning(self, "导出失败", "没有可导出的网格对象！")
                return
                
            # 弹出文件保存对话框
            file_path, _ = QFileDialog.getSaveFileName(
                self, 
                "保存网格文件",
                os.path.join(os.path.expanduser("~"), "Desktop", f"mesh_{self.count}.ply"),  # 默认保存到桌面
                "PLY文件 (*.ply);;所有文件 (*)"
            )
            # 如果用户取消选择，则返回
            if not file_path:
                return
            # 确保文件有正确的扩展名
            if not file_path.lower().endswith('.ply'):
                file_path += '.ply'
            # 使用vedo导出网格
            vedo.write(self.current_mesh, file_path)
            QMessageBox.information(self, "导出成功", f"网格已成功导出到:\n{file_path}")
            
        except Exception as e:
            # 捕获并显示任何错误
            error_msg = f"导出网格时出错:\n{str(e)}"
            QMessageBox.critical(self, "导出错误", error_msg)
        
    def change_state_bt_color(self, color=QColor(255, 0, 0)):
        palette = self.app_ui.state_bt.palette()
        palette.setColor(QPalette.Button, color)
        self.app_ui.state_bt.setAutoFillBackground(True)
        self.app_ui.state_bt.setPalette(palette)
        self.app_ui.state_bt.update()

    def SetState(self):
        # 从INI文件中获取当前状态
        current_state = ""
        if self.config_parser.has_option('STATE', str(self.count)):
            current_state = self.config_parser.get('STATE', str(self.count))
        else:
            current_state = "这个数据有以下问题:\n"

        text, ok = QInputDialog.getMultiLineText(self, "输入状态", "请输入需要记录文本:", text=current_state)
        if ok:
            # 保存状态到INI文件
            self.config_parser.set('STATE', str(self.count), text)
            self.save_config()
            self.ShowState()

    def ShowState(self):
        """显示当前状态"""
        if self.config_parser.has_option('STATE', str(self.count)):
            self.app_ui.state_bt.setText("已记录")
            self.change_state_bt_color(color=QColor(0, 255, 0))
        else:
            self.app_ui.state_bt.setText("未记录")
            self.change_state_bt_color(color=QColor(255, 0, 0))

    def JumpCount(self):
        number, ok = QInputDialog.getInt(self, "输入跳转到的序号", f"请输入0-{self.max_count}之间的数值:", min=0,
                                         max=self.max_count)
        if ok:
            if number < 0 or number > self.max_count:
                QMessageBox.critical(self, "错误", "输入的数值超出范围！")
            else:
                self.count = number
                self.UpdateDisplay()

    def NextFile(self):
        if self.count < self.max_count - 1:
            self.count += 1
            self.UpdateDisplay()

    def PreFile(self):
        if 0 < self.count < self.max_count - 1:
            self.count -= 1
            self.UpdateDisplay()

    ###############################按钮逻辑#######################################

    ###############################资源视图#######################################

    def load_view_data(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = self.current_page * self.page_size
        
        # 防止用户快速点击视图按钮
        self.app_ui.Next_view_Button.setEnabled(False)
        self.app_ui.Pre_view_Button.setEnabled(False)
        
        # 启动写入配置线程
        self.write_thread = config_thread(
            self.db_path,
            self.config_parser, 
            self.data_config["name_key"], 
            start_index,
            end_index
        )
        self.write_thread.progress_int.connect(self.app_ui.fun_progressBar.setValue)
        self.write_thread.finished.connect(self.update_view_data)
        self.write_thread.start()

    def update_view_data(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = self.current_page * self.page_size
        
        # 保存配置
        self.save_config()
        
        # 渲染视图
        data = []
        for i in range(start_index, end_index):
            if self.config_parser.has_option('INDEX_MAPPING', str(i)):
                data.append(self.config_parser.get('INDEX_MAPPING', str(i)))
            else:
                data.append(f"unknown_{i}")
        
        self.model = QStringListModel()
        self.model.setStringList(data)
        self.app_ui.NameView.setModel(self.model)
        
        # 重新启用按钮
        self.app_ui.Next_view_Button.setEnabled(True)
        self.app_ui.Pre_view_Button.setEnabled(True)

    def Next_Page(self):
        self.current_page += 1
        self.load_view_data()

    def Previous_Page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.load_view_data()

    def search(self):
        keyword = self.app_ui.search_edit.text().lower()
        filtered_options = []
        
        # 从配置中获取所有选项
        all_options = []
        for option in self.config_parser.options('INDEX_MAPPING'):
            # 只添加值，不添加键
            if option.isdigit():
                all_options.append(self.config_parser.get('INDEX_MAPPING', option))
        
        for option in all_options:
            if keyword in option.lower():
                filtered_options.append(option)
        self.model.setStringList(filtered_options)

    def show_selected_value(self, index):
        selected_option = index.data()
        
        # 从配置中查找对应的索引
        count = None
        for key in self.config_parser.options('INDEX_MAPPING'):
            if self.config_parser.get('INDEX_MAPPING', key) == selected_option and key.isdigit():
                count = int(key)
                break
        
        if count is None:
            QMessageBox.warning(self, "警告", "未找到对应的索引!")
            return
        
        ok_ = QMessageBox.question(self, "提示", f"你选择了{selected_option}-->对应序号为{count}的数据",
                                   QMessageBox.Yes | QMessageBox.No)
        if ok_ == QMessageBox.Yes:
            self.count = count
            self.UpdateDisplay()

    ###############################资源视图#######################################


    def _labels_flag(self, mesh_vd, labels,is_points=True):
        fss = []
        for i in np.unique(labels):
            if is_points:
                vertices =np.array( mesh_vd.vertices)
                v_i =vertices[labels == i]
            else:
                faces = np.array(mesh_vd.cells)
                faces_indices = np.unique(faces[labels == i])
                v_i = mesh_vd.vertices[faces_indices]
            if len(v_i) > 0:
                cent = np.mean(v_i, axis=0)
                fs = mesh_vd.flagpost(f"{i}", cent)
                fss.append(fs)
        return fss

    def UpdateDisplay(self):
        self.ShowState()
        self.app_ui.treeWidget.clear()
        self.vp.clear(deep=True)
        
        if self.db_path is None:
            QMessageBox.warning(self, "警告", "数据库未打开!")
            return
        with Reader(self.db_path) as db:
            data = db[self.count]
            self.max_count = len(db) - 1
        
        try:
            if self.data_config["data_type"] == "网格(Mesh)":
                vertices = np.array(data[self.data_config["vertex_key"]][...,:3])
                faces = np.array(data[self.data_config["face_key"]][...,:3])
                mesh = vedo.Mesh([vertices, faces])
                fss = []
                
                if self.data_config["vertex_label_key"] and self.data_config["vertex_label_key"] in data:
                    labels =data[self.data_config["vertex_label_key"]].ravel()
                    fss = self._labels_flag(mesh, labels,is_points=True)
                    mesh.pointcolors = labels2colors(labels)
                
                if self.data_config["face_label_key"] and self.data_config["face_label_key"] in data:
                    labels = data[self.data_config["face_label_key"]].ravel()
                    fss = self._labels_flag(mesh, labels,is_points=False)
                    mesh.cellcolors = labels2colors(labels)
                    
                fss.append(mesh)
                self.vp.show(fss, axes=3)
                self.current_mesh = mesh
            else:
                points = np.array(data[self.data_config["vertex_key"]][...,:3])
                pc = Points(points)
                fss = []
                
                if self.data_config["vertex_label_key"] and self.data_config["vertex_label_key"] in data:
                    labels =data[self.data_config["vertex_label_key"]].ravel()
                    pc.pointcolors = labels2colors(labels)
                    fss = self._labels_flag(pc,labels,is_points=True)
                fss.append(pc)
                self.vp.show(fss, axes=3)
                self.current_mesh = pc
            
        except KeyError as e:
            QMessageBox.critical(self, "键名错误", f"未找到配置的键名: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "渲染错误", f"渲染数据时出错: {str(e)}")
        
        with Reader(self.db_path) as db:
            spec = db.get_data_specification(0)
            keys = db.get_data_keys(0)

        for key in keys:
            k = str(key)
            t = str(spec[key]["dtype"])
            s = str(spec[key]["shape"])
            if "<U" in t or "str" in t or "bool" in t:
                s = str(data[key])
            QtWidgets.QTreeWidgetItem(self.app_ui.treeWidget, [k, t, s])

        self.app_ui.NowNumber.display(str(self.count))
        self.app_ui.MaxNumber.display(str(self.max_count))
        self.vp.render()


    def save_config(self):
        """保存配置到文件"""
        if self.db_path:
            self.config_parser.set('DATA_CONFIG', 'db_path', self.db_path)
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config_parser.write(configfile)

    def onClose(self):
        """保存配置到文件"""
        self.save_config()
        self.vtkWidget.close()

    def OpenFile(self):
        user_path = self.app_ui.path_label.text()
        if user_path != "":
            ok_ = QMessageBox.information(self, "提示", f"将打开{user_path}!", QMessageBox.Yes | QMessageBox.No)
            if ok_ == QMessageBox.Yes:
                self.fileName = user_path
            else:
                self.fileName = QFileDialog.getOpenFileName(self, "选取LMDB数据库文件", "./")[0]
        else:
            self.fileName = QFileDialog.getOpenFileName(self, "选取LMDB数据库文件", "./")[0]

        if os.path.exists(self.fileName):
            self.db_path = self.fileName
            self.app_ui.path_label.setText(self.fileName)
            try:
                with Reader(self.db_path) as db:
                    data = db[0]
                    len_db = len(db)
                keys = list(data.keys())

                dialog = DataConfigDialog(keys,self.data_config, self)
                if dialog.exec_() == QDialog.Accepted:
                    self.data_config = dialog.get_config()
                    
                    # 保存新配置
                    self.config_parser.set('DATA_CONFIG', 'data_type', self.data_config["data_type"])
                    self.config_parser.set('DATA_CONFIG', 'vertex_key', self.data_config["vertex_key"])
                    self.config_parser.set('DATA_CONFIG', 'vertex_label_key', self.data_config["vertex_label_key"] or "")
                    self.config_parser.set('DATA_CONFIG', 'face_key', self.data_config["face_key"] or "")
                    self.config_parser.set('DATA_CONFIG', 'face_label_key', self.data_config["face_label_key"] or "")
                    self.config_parser.set('DATA_CONFIG', 'name_key', self.data_config["name_key"])
                    self.save_config()
                    
                    # 清除旧的索引映射
                    if self.config_parser.has_section('INDEX_MAPPING'):
                        self.config_parser.remove_section('INDEX_MAPPING')
                    self.config_parser.add_section('INDEX_MAPPING')
                    self.save_config()
                    
                    self.max_count = len_db
                    self.pre_processing()
                else:
                    QMessageBox.warning(self, "警告", "未完成配置，数据库未加载!")

            except Exception as e:
                QMessageBox.critical(self, "错误", f"打开数据库失败:{e}")


        else:
            QMessageBox.warning(self, "警告", "未找到LMDB数据库文件!")


def main():
    # 适应高分辨率
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) 
    app = QtWidgets.QApplication(sys.argv)
    
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette()))
    window = LMDB_Viewer()
    window.show()
    app.aboutToQuit.connect(window.onClose)
    app.exec_()


if __name__ == "__main__":
    main()

