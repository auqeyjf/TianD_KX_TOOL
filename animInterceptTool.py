#coding:utf-8
'''
Created on 2015/7/8

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: check animtion file

@Declaration: It's free for everybody and welcome to point out mistakes.
'''
import os

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import PyQt4.uic as uic

import pymel.core as pm
import uiTool
import kxTool
reload(kxTool)
reload(uiTool)

import playblasterUI

uiPath = uiTool.getUIPath("TianD_KX_TOOL")
form_class, base_class = uic.loadUiType('%s/animInterceptWindow_all.ui' %uiPath)
class ANIMInterceptTool(form_class, base_class):
    
    def __init__(self, parent = uiTool.getMayaWindow()):
                
        super(ANIMInterceptTool, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setMaximumHeight(376)
        self.setMaximumWidth(203)
        
        self.setWindowIcon(QtGui.QIcon("%s/bullet_deny.png" %uiPath))
        
        for btn in self.findChildren(QtGui.QPushButton, QtCore.QRegExp("check\d+Btn")):
            btn.setIcon(QtGui.QIcon("%s/question.png" %uiPath))
            btn.setStyleSheet('border-image:url(%s/question.png);' %uiPath)
        
        self.anim = ANIMIntercept()
        
        self.check0Btn.clicked.connect(self.checkSceneName)               #文件命名
        self.check1Btn.clicked.connect(self.getAnimCamera)                #相机命名
        self.check2Btn.clicked.connect(self.camLock)                      #相机锁定
        self.check3Btn.clicked.connect(self.camScale1)                    #相机缩放
        self.check4Btn.clicked.connect(self.getNeedlessCamera)            #多余相机
        self.check5Btn.clicked.connect(self.framesIntercept)              #整理帧数范围
        self.check6Btn.clicked.connect(self.displayLayerIntercept)        #删除norender以外的层
        self.check7Btn.clicked.connect(self.clearUpOutliner)              #整理大纲
        self.check9Btn.clicked.connect(self.checkExt)                     #检查后缀名
        self.check10Btn.clicked.connect(self.checkResolution)             #检查分辨率
        #self.check8Btn.clicked.connect(self.anim.)                       #删除空组
        
        self.checkAllBtn.clicked.connect(self.checkAll)
        self.skipAllBtn.clicked.connect(self.skipAll)
        
        self.flag0 = None
        self.flag1 = None
        self.flag2 = None
        self.flag3 = None
        self.flag4 = None
        self.flag5 = None
        self.flag6 = None
        self.flag7 = None
        self.flag8 = None
        self.flag9 = None
        self.flag10 = None
        
        self.checkAll()
    
    def checkExt(self):
        flag = self.anim.checkExt()
        if flag :
            self.check9Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
            self.check9Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
            self.flag9 = True
        else :
            self.check9Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check9Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag9 = False
        if self.flag9 is True:
            pass
        else :
            pass   
            
    def checkSceneName(self):
        flag = self.anim.checkSceneName()
        if flag :
            self.check0Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
            self.check0Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
            self.flag0 = True
        else :
            self.check0Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check0Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag0 = False
        if self.flag0 is True:
            pass
        else :
            pass
        
    def getAnimCamera(self):
        flag = self.anim.getAnimCamera()
        if flag :
            self.check1Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
            self.check1Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
            self.flag1 = True
        else :
            self.check1Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check1Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag1 = False
        if self.flag1 is True:
            pm.select(self.anim.camera)
        else :
            pass
    
    def camLock(self):
        if self.flag1 is None:
            pass
        elif self.flag2 is None and self.flag1 is True :
            flag = self.anim.camLock()
            if flag :
                self.check2Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check2Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag2 = True
            else :
                self.check2Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check2Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag2 = False
        elif self.flag2 is True:
            pass
        elif self.flag1 is False:
            self.check2Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check2Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag2 = False
        elif self.flag2 is False and self.flag1 is True:
            pm.select(self.anim.camera)
        else :pass
    
    def camScale1(self):
        if self.flag1 is None:
            pass
        elif self.flag3 is None and self.flag1 is True:
            flag = self.anim.camScale1()
            if flag :
                self.check3Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check3Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag3 = True
            else :
                self.check3Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check3Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag3 = False
        elif self.flag3 is True:
            pass
        elif self.flag1 is False:
            self.check3Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check3Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag3 = False
        elif self.flag3 is False and self.flag1 is True:
            pm.select(self.anim.camera)
        else :
            pass
            
    def getNeedlessCamera(self):
        if self.flag1 is None:
            pass
        elif self.flag4 is None and self.flag1 is True:
            flag = self.anim.getNeedlessCamera()
            if flag :
                self.check4Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check4Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag4 = True
            else :
                self.check4Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check4Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag4 = False
        elif self.flag4 is True:
            pass
        elif self.flag1 is False:
            self.check4Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check4Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag4 = False
        elif self.flag4 is False and self.flag1 is True:
            pm.select(self.anim.needlessCamera)
        else :
            pass
        
    def framesIntercept(self):
        if self.flag5 is None:
            flag = self.anim.framesIntercept()
            if flag :
                self.check5Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check5Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag5 = True
            else :
                self.check5Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check5Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag5 = False
        elif self.flag5 is True:
            pass
        else:
            pass
    
    def displayLayerIntercept(self):
        if self.flag6 is None:
            flag = self.anim.displayLayerIntercept()
            if flag :
                self.check6Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check6Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag6 = True
            else :
                self.check6Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check6Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag6 = False
        elif self.flag6 is True:
            pass
        else:
            pm.select(self.anim.needlessDisLayers)
    
    def clearUpOutliner(self):
        if self.flag1 is None:
            pass
        elif self.flag7 is None and self.flag1 is True:
            flag = self.anim.clearUpOutliner()
            if flag :
                self.check7Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
                self.check7Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
                self.flag7 = True
            else :
                self.check7Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
                self.check7Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
                self.flag7 = False
        elif self.flag7 is True:
            pass
        elif self.flag1 is False:
            self.check7Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check7Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag7 = False
        elif self.flag7 is False and self.flag1 is True:
            pm.select(self.anim.needlessTop)
        else :
            pass
                                           
    def checkResolution(self):
        flag = self.anim.checkResolution()
        if flag :
            self.check10Btn.setIcon(QtGui.QIcon("%s/ok.png" %uiPath))
            self.check10Btn.setStyleSheet("border-image:url(%s/ok.png);" %uiPath)
            self.flag10 = True
        else :
            self.check10Btn.setIcon(QtGui.QIcon("%s/cancel.png" %uiPath))
            self.check10Btn.setStyleSheet("border-image:url(%s/cancel.png);" %uiPath)
            self.flag10 = False
        if self.flag10 is True:
            pass
        else :
            pass
            
    def checkAll(self):
        self.anim.getSceneName()
        self.anim.analyzeSceneName()
        if not self.skip9.checkState() :
            self.flag9 = None
            self.checkExt()
        if not self.skip0.checkState():
            self.flag0 = None
            self.checkSceneName()
        if not self.skip1.checkState() :
            self.flag1 = None
            self.getAnimCamera()
        if not self.skip2.checkState() :
            self.flag2 = None
            self.camLock()
        if not self.skip3.checkState() :
            self.flag3 = None
            self.camScale1()
        if not self.skip4.checkState() :
            self.flag4 = None
            self.getNeedlessCamera()
        if not self.skip5.checkState() :
            self.flag5 = None
            self.framesIntercept()
        if not self.skip6.checkState() :
            self.flag6 = None
            self.displayLayerIntercept()
        if not self.skip7.checkState() :
            self.flag7 = None
            self.clearUpOutliner()
        if not self.skip10.checkState():
            self.flag10 = None
            self.checkResolution()
        if not self.skip8.checkState() :
            pass
        
            
        if (self.flag1 or self.skip1.checkState()) and \
            (self.flag2 or self.skip2.checkState()) and \
            (self.flag3 or self.skip3.checkState()) and \
            (self.flag4 or self.skip4.checkState()) and \
            (self.flag5 or self.skip5.checkState()) and \
            (self.flag6 or self.skip6.checkState()) and \
            (self.flag7 or self.skip7.checkState()) and \
            (self.flag9 or self.skip9.checkState()) and \
            (self.flag10 or self.skip10.checkState()):
            self.close()
            playblasterUI.startDlg()
            return True
        else :
            return False
    
    def skipAll(self):
        self.close()
        playblasterUI.startDlg()
        return True
        
class ANIMIntercept(kxTool.KXTool):
    
    def __init__(self):
        '''
        13 动画规范拦截:
            1.相机锁定;[OK]
            2.相机缩放归1;[OK]
            3.清理除norender以外的层;
            4.清理空组;
            5.拦截cam的命名和文件命名不一样;(重要的)[OK]
            6.拦截帧数和数据库不一样;(重要的)[OK]
            7.清理多余的摄像机;[OK]
            8.自动在outerline里吧角色归到char组,场景归到set组,道具归到prop组;
        '''
        super(ANIMIntercept, self).__init__()
        self.getSceneName()
        self.analyzeSceneName()
        self.topGroups = ["persp", "top", "front", "side", "char", "set", "prop"]
    
    
    def checkResolution(self):
        try:
            resolution = pm.PyNode("defaultResolution")
            width = resolution.width.get()
            height = resolution.height.get()
            print self.projectName
            if width == self.resolutionDic[self.projectName][0] and height == self.resolutionDic[self.projectName][1] :
                return True
            else :
                return False
        except:
            pass
    
    def checkExt(self):
        if self.ext == ".ma" or self.ext == ".mayaAscii":
            return False
        elif self.ext == ".mb" or self.ext == ".mayaBinary":
            return True
        else :
            return False
    
    def checkSceneName(self):
        try:
            frameRange = pm.mel.eval('idmtProject -timeLine "%s.mb"' %self.sceneName)
            if frameRange :
                return True
            else :
                return False
        except:
            pass
    
    def getAnimCamera(self):
        if self.sceneName:
            cameraName = "cam_%s_%s_(%s|%s)" %(self.episodeNumber, self.sessionNumber, self.sceneNumber, self.sceneNumber.upper())
            try:
                self.camera = pm.ls(regex = cameraName)[0]
                self.topGroups.append(self.camera.getParent(-1))
                return True
            except:
                return False
    
    def getFrameRange(self):
        self.min = pm.playbackOptions(q = 1, min = 1)
        self.max = pm.playbackOptions(q = 1, max = 1)
        self.start = pm.playbackOptions(q = 1, animationStartTime = 1)
        self.end = pm.playbackOptions(q = 1, animationEndTime = 1)
        if self.start != self.min:
            pm.playbackOptions(e = 1, animationStartTime = self.min)
        if self.end != self.max:
            pm.playbackOptions(e = 1, animationEndTime = self.max)
        
    def getNeedlessCamera(self):
        cameraLst = [cam.getParent() for cam in pm.ls(type = 'camera')]
        if self.projectName == 'ROCK':
            self.needlessCamera = [cam for cam in cameraLst if cam not in self.defaultCameraNameLst and cam != self.camera and "_baked" not in cam.name() and 'CamL' not in cam.name() and 'CamR' not in cam.name()]
        else :
            self.needlessCamera = [cam for cam in cameraLst if cam not in self.defaultCameraNameLst and cam != self.camera and "_baked" not in cam.name()]
        if self.needlessCamera :
            return False
        else :
            return True
    
    def camScale1(self):
        if self.camera.getAllParents():
            for p in self.camera.getAllParents():
                pscale = p.s.get()
                if pscale != pm.dt.Vector([1.0, 1.0, 1.0]):
                    return False
                else :
                    pass
        scale = self.camera.s.get()
        if scale != pm.dt.Vector([1.0, 1.0, 1.0]):
            return False
        else:
            return True
    
    def camLock(self):
        if self.projectName == 'ROCK':
            cbAttr = [pm.PyNode('{0}.{1}'.format(self.camera.name(), attr)) for attr in ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']]
        else :
            cbAttr = self.camera.listAttr(k=1) + self.camera.getShape().listAttr(k=1)
        for attr in cbAttr:
            if not attr.isLocked():
                if "aiUserOptions" in attr.name() or "aiFiltermap" in attr.name() or "aiTranslator" in attr.name():
                    pass
                else :
                    return False
            else :
                pass
        return True
            
    def framesIntercept(self):
        try:
            frameRange = pm.mel.eval('idmtProject -timeLine "%s.mb"' %self.sceneName)
            self.getFrameRange()
            if self.min != frameRange[0]:
                return False
            if self.max != frameRange[1]:
                return False
            return True
        except :
            pass
    
    def displayLayerIntercept(self, exRef = 0):
        displayLayers = pm.ls(type = "displayLayer")
        if exRef :
            self.needlessDisLayers = [dl for dl in displayLayers if dl.name() != "norender" and not dl.isReferenced() and "defaultLayer" not in dl.name()]
        else :
            self.needlessDisLayers = [dl for dl in displayLayers if dl.name() != "norender" and "defaultLayer" not in dl.name()]
        if self.needlessDisLayers :
            return False
        return True  
    
    def clearUpOutliner(self):
        top = pm.ls(assemblies = 1)
        self.needlessTop = [t for t in top if t.name() not in self.topGroups]
        if self.needlessTop:
            return False
        return True
    
def show():
    if uiTool.windowExisted("animInterceptWindow"):
        pass
    else :
        a = ANIMInterceptTool()
        a.show()
        
if __name__ == "__main__":
    show()