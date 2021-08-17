from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import base64
from pic2str import explode
from PIL import Image, ImageQt

import matplotlib.pyplot as plt
import numpy as np
import sys
from io import BytesIO
import example_ui as ui

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.image = QImage("./CR EEXI Calcuation_Bulk.png")
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
        self.setWindowTitle('CR EEXIcalculator')
        self.im = QPixmap("CR EEXI Calcuation_Bulk.png")
        self.label_m = QLabel()
        self.label_m.setPixmap(self.im)
        self.label_m.move(810,600)
        self.show()
        
        # self.label_24 = QtWidgets.QLabel(self.widget_3)
        # self.label_24.setGeometry(QtCore.QRect(20, 400, 301, 51))
        # self.label_24.setText("")
        # self.label_24.setPixmap(QtGui.QPixmap("CR EEXI Calcuation_Bulk.png"))
        # self.label_24.setScaledContents(True)
        # self.label_24.setObjectName("label_24")
        # DWT_value = int(self.DWT.text())
        # MCR_ME_value = int(self.MCR_ME.text
        
        byte_data = base64.b64decode(explode)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)
        qImage = ImageQt.ImageQt(image)
        image = QPixmap.fromImage(qImage)
        self.label_24.setPixmap(image)
        self.label_24.setScaledContents(True)
        
        choices = ['Bulk carrier', 'Container ship', 'Tanker','General cargo ship','Refrigerated cargo carrier']
        self.comboBox.addItems(choices)
        
    # def shiptype(self):
        # DWT_value = int(self.DWT.text())
        # if self.comboBox.currentIndex()==0:
            # A = 10.6585
            # C = 0.02706
            # D = 23.7510
            # F = 0.54087
            # a = 961.79
            # c = 0.477
            # if DWT_value>=200000:
                # referenceRate=0.15
            # elif DWT_value<200000 and DWT_value>=20000:
                # referenceRate=0.2
            # elif DWT_value<20000 and DWT_value>=10000:
                # referenceRate=0.2*DWT_value/10000-0.2
            # else:
                # referenceRate=0
        # elif self.comboBox.currentIndex()==1:
            # A = 3.2395
            # C = 0.18294
            # D = 0.5042
            # F = 1.03046
            # a = 174.22
            # c = 0.201
            # if DWT_value>200000:
                # referenceRate=0.5
            # elif DWT_value<200000 and DWT_value>=120000:
                # referenceRate=0.45                
            # elif DWT_value<120000 and DWT_value>=80000:
                # referenceRate=0.35
            # elif DWT_value<80000 and DWT_value>=40000:
                # referenceRate=0.3            
            # elif DWT_value<40000 and DWT_value>=15000:
                # referenceRate=0.2
            # elif DWT_value<15000 and DWT_value>10000:
                # referenceRate=0.2*(DWT_value-10000)/5000
            # else:
                # referenceRate=0
        # else:
            # A=1
            # C=1
            # D=1
            # F=1
            # a = 1
            # c = 1
            # # referenceRate=0
    # def fun(x, y, a, c, d):
        # if y < (a*x**(-c))*(1-d):
            # return 1
        # else:
            # return -1
        # return (1-x/2+x**3+y**5) * np.exp(-x**2-y**2)



    def calculate(self):
        # self.shiptype()
        
        # def fun(x, y, a, c, d):
            # for i in x:
                # for j in y:
                    # if j < (a*i**(-c))*(1-d):
                        # return 1
                    # else:
                        # return -1

        DWT_value = float(self.DWT.text())
        if self.comboBox.currentIndex()==0:
            A = 10.6585
            C = 0.02706
            D = 23.7510
            F = 0.54087
            a = 961.79
            c = 0.477
            if DWT_value>=200000:
                referenceRate=0.15
            elif DWT_value<200000 and DWT_value>=20000:
                referenceRate=0.2
            elif DWT_value<20000 and DWT_value>=10000:
                referenceRate=0.2*DWT_value/10000-0.2
            else:
                referenceRate=0
        elif self.comboBox.currentIndex()==1:
            A = 3.2395
            C = 0.18294
            D = 0.5042
            F = 1.03046
            a = 174.22
            c = 0.201
            if DWT_value>200000:
                referenceRate=0.5
            elif DWT_value<200000 and DWT_value>=120000:
                referenceRate=0.45                
            elif DWT_value<120000 and DWT_value>=80000:
                referenceRate=0.35
            elif DWT_value<80000 and DWT_value>=40000:
                referenceRate=0.3            
            elif DWT_value<40000 and DWT_value>=15000:
                referenceRate=0.2
            elif DWT_value<15000 and DWT_value>10000:
                referenceRate=0.2*(DWT_value-10000)/5000
            else:
                referenceRate=0
        elif self.comboBox.currentIndex()==2:
            A = 8.1358
            C = 0.05383
            D = 22.8415
            F = 0.55826
            a = 1218.8
            c = 0.488
            if DWT_value>200000:
                referenceRate=0.15
            elif DWT_value<200000 and DWT_value>=20000:
                referenceRate=0.2                
            elif DWT_value<20000 and DWT_value>=4000:
                referenceRate=0.2*(DWT_value-4000)/16000
            else:
                referenceRate=0
        elif self.comboBox.currentIndex()==3:
            A = 2.4538
            C = 0.18832
            D = 0.8816
            F = 0.92050
            a = 107.48
            c = 0.216
            if DWT_value>15000:
                referenceRate=0.3
            elif DWT_value<15000 and DWT_value>=3000:
                referenceRate=0.3*(DWT_value-3000)/12000
            else:
                referenceRate=0
        elif self.comboBox.currentIndex()==4:
            A = 1.06
            C = 0.31518
            D = 0.0272
            F = 1.38634
            a = 227.01
            c = 0.244
            if DWT_value>5000:
                referenceRate=0.15
            elif DWT_value<5000 and DWT_value>=3000:
                referenceRate=0.15*(DWT_value-3000)/2000
            else:
                referenceRate=0
        else:
            A=1
            C=1
            D=1
            F=1
            a = 1
            c = 1
            referenceRate=0
        ####    
        MCR_ME_value = float(self.MCR_ME.text())
        if self.LWT.text()!='':
            LWT_value = float(self.LWT.text())
        else:
            LWT_value=0
        if self.VS_EEDI.text()!='':
            VS_EEDI_value = float(self.VS_EEDI.text())
        else:
            VS_EEDI_value=0
        if self.PS_EEDI.text()!='':
            PS_EEDI_value = float(self.PS_EEDI.text())
        else:
            PS_EEDI_value=0   
        if self.PAE_in.text()!='':
            PAE = float(self.PAE_in.text())
        else:
            PAE=0   
        if self.SFC_ME_in.text()!='':
            SFC_ME = float(self.SFC_ME_in.text())
        else:
            SFC_ME=190
        if self.SFC_AE_in.text()!='':
            SFC_AE = float(self.SFC_AE_in.text())
        else:
            SFC_AE=215   
        if self.PTO_in.text()!='':
            PTO = float(self.PTO_in.text())
        else: 
            PTO=0   
        if self.CF_ME_in.text()!='':
            CF_ME = float(self.CF_ME_in.text())
        else:
            CF_ME=3.114
        if self.CF_AE_in.text()!='':
            CF_AE = float(self.CF_AE_in.text())
        else:
            CF_AE=3.114    
        ###########
        
        
        
        if self.comboBox.currentIndex()==1:
            if DWT_value<=95000:    
                MCR_avg = D*(DWT_value**(F))
            else:
                MCR_avg = D*(95000**(F))
        else:
            MCR_avg = D*(DWT_value**(F))
        
        PME = 0.75*(MCR_ME_value-PTO)
        if self.comboBox.currentIndex()==1:
            if DWT_value<=80000:
                Vavg = A*(DWT_value**(C))
            else:
                Vavg = A*(80000**(C))
        else:
            Vavg = A*(DWT_value**(C))
        margin = min(1,Vavg*0.05)
        if VS_EEDI_value == 0:
            Vapp = (Vavg-margin)*(MCR_ME_value/MCR_avg)**(1/3)
        else:
            Vapp = VS_EEDI_value*(PME/PS_EEDI_value)**(1/3)
        if PAE==0:
            if MCR_ME_value>=10000:
                PAE=0.025*MCR_ME_value+250
            else:
                PAE=0.05*MCR_ME_value
        else:
            PAE = PAE
        print(PAE)
        
        fiCSR=1+0.08*LWT_value/DWT_value
        fcCHIP=1
        if self.comboBox.currentIndex()==1:
            attainedEEXI_value=(CF_ME*SFC_ME*PME+CF_AE*SFC_AE*PAE)/(fcCHIP*fiCSR*0.7*DWT_value*Vapp)       
        else:
            attainedEEXI_value=(CF_ME*SFC_ME*PME+CF_AE*SFC_AE*PAE)/(fcCHIP*fiCSR*DWT_value*Vapp)       

        
        referenceline=a*DWT_value**(-c)
        
        reqEEXI_value = referenceline*(1-referenceRate)
        
        attainedEEXI_valuei=attainedEEXI_value
        PMEi = PME
        Vappi = Vapp
        i=0
        attainedEEXI_valuei2=0
        while attainedEEXI_valuei-reqEEXI_value>0.001:
            PMEi2 = ((0.9999*1/(attainedEEXI_valuei/reqEEXI_value))**(3/2))*PMEi
            Vappi2 = Vappi*(PMEi2/PMEi)**(1/3)
            if self.comboBox.currentIndex()==1:
                attainedEEXI_valuei2=(CF_ME*SFC_ME*PMEi2+CF_AE*SFC_AE*PAE)/(fcCHIP*fiCSR*0.7*DWT_value*Vappi2)       
            else:
                attainedEEXI_valuei2=(CF_ME*SFC_ME*PMEi2+CF_AE*SFC_AE*PAE)/(fcCHIP*fiCSR*DWT_value*Vappi2)       
            PMEi = PMEi2
            Vappi = Vappi2
            attainedEEXI_valuei = attainedEEXI_valuei2
            print(attainedEEXI_valuei-reqEEXI_value)
            print(i)
            i=i+1
            
            
         
        #a=int(self.DWT.text())+int(self.MCR_ME.text())
        self.PAEt.setText(str(round(PAE,2)))
        self.PMEt.setText(str(round(PME,2)))
        self.margint.setText(str(round(margin,2)))
        self.EEXI.setText(str(round(attainedEEXI_value,2)))
        self.EEXI_2.setText(str(round(attainedEEXI_valuei2,2)))
        self.Vavgt.setText(str(round(Vavg,2)))
        self.Vappt.setText(str(round(Vapp,2)))
        self.MCR_avgt.setText(str(round(MCR_avg,2)))
        self.reqEEXI.setText(str(round(reqEEXI_value,2)))
        
        self.PME_lim.setText(str(round(PMEi,2)))
        self.MCR_lim.setText(str(round(PMEi/0.83,2)))
        self.Vappt_lim.setText(str(round(Vappi,2)))
        self.reduction.setText(str(round((PMEi/0.83)/MCR_ME_value*100,2))+'%')
        self.Vapp_reduction.setText(str(round(Vappi-Vapp,2)))
        
        ###plot###
        if self.comboBox.currentIndex()==0:
            x = np.linspace(10000,2*DWT_value,100)
        elif self.comboBox.currentIndex()==1:
            x = np.linspace(10000,2*DWT_value,100)
        elif self.comboBox.currentIndex()==2:
            x = np.linspace(4000,2*DWT_value,100)
        elif self.comboBox.currentIndex()==3:
            x = np.linspace(3000,2*DWT_value,100)
        elif self.comboBox.currentIndex()==4:
            x = np.linspace(3000,2*DWT_value,100)
        else:
            x = np.linspace(100,1000,100)
        referenceline_plot = a*x**(-c)
        y = referenceline_plot*(1-referenceRate)
        
        # xc = np.linspace(1000, 2*DWT_value, 256)
        # yc = np.linspace( 1, 2*attainedEEXI_value, 256)
        # X, Y = np.meshgrid(xc, yc)
        # plt.contourf(X, Y, fun(X, Y,a,c,referenceRate))
        
        if self.comboBox.currentIndex()!=1:
            plt.plot(x,y,label='Required EEXI')
            plt.plot(DWT_value,attainedEEXI_value, marker ='x', markersize=7, label='original Attained EEXI')
            plt.plot(DWT_value,reqEEXI_value, marker ='o', markersize=5, label='new Attained EEXI')
        else:
            plt.plot(x*0.7,y,label='Required EEXI')
            plt.plot(DWT_value*0.7,attainedEEXI_value, marker ='x', markersize=7, label='original Attained EEXI')
            plt.plot(DWT_value*0.7,reqEEXI_value, marker ='o', markersize=5, label='new Attained EEXI')
        plt.legend(loc = 'upper right')
        plt.xlabel('Capacity (tonnes)', color = 'blue')
        plt.ylabel('EEXI (g-CO2/t-mile)', color = 'blue')
        plt.title('Capacity-EEXI', color = 'black')
        plt.show()
        

    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())