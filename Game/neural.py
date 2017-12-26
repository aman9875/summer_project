import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import pickle

next_move=pd.read_csv('next_move.csv')

X=next_move[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16','x17','x18','x19','x20','x21','x22','x23','x24','x25','x26','x27','x28','x29','x30','x31','x32','x33','x34','x35','x36','x37','x38','x39','x40','x41','x42','x43','x44','x45','x46','x47','x48','x49','x50','x51','x52','x53','x54','x55','x56','x57','x58','x59','x60','x61','x62','x63','x64','x65','x66','x67','x68','x69','x70','x71','x72','x73','x74','x75','x76','x77','x78','x79','x80','x81','x82','x83','x84','x85','x86','x87','x88','x89','x90','x91','x92','x93','x94','x95','x96','x97','x98','x99','x100']]
y1=next_move['y1']
y2=next_move['y2']
y3=next_move['y3']
y4=next_move['y4']
y5=next_move['y5']
y6=next_move['y6']
y7=next_move['y7']
y8=next_move['y8']
y9=next_move['y9']
y10=next_move['y10']
y11=next_move['y11']
y12=next_move['y12']
y13=next_move['y13']
y14=next_move['y14']
y15=next_move['y15']
y16=next_move['y16']
y17=next_move['y17']
y18=next_move['y18']
y19=next_move['y19']
y20=next_move['y20']
y21=next_move['y21']
y22=next_move['y22']
y23=next_move['y23']
y24=next_move['y24']
y25=next_move['y25']
y26=next_move['y26']
y27=next_move['y27']
y28=next_move['y28']
y29=next_move['y29']
y30=next_move['y30']
y31=next_move['y31']
y32=next_move['y32']
y33=next_move['y33']
y34=next_move['y34']
y35=next_move['y35']
y36=next_move['y36']
y37=next_move['y37']
y38=next_move['y38']
y39=next_move['y39']
y40=next_move['y40']
y41=next_move['y41']
y42=next_move['y42']
y43=next_move['y43']
y44=next_move['y44']
y45=next_move['y45']
y46=next_move['y46']
y47=next_move['y47']
y48=next_move['y48']
y49=next_move['y49']
y50=next_move['y50']
y51=next_move['y51']
y52=next_move['y52']
y53=next_move['y53']
y54=next_move['y54']
y55=next_move['y55']
y56=next_move['y56']
y57=next_move['y57']
y58=next_move['y58']
y59=next_move['y59']
y60=next_move['y60']
y61=next_move['y61']
y62=next_move['y62']
y63=next_move['y63']
y64=next_move['y64']
y65=next_move['y65']
y66=next_move['y66']
y67=next_move['y67']
y68=next_move['y68']
y69=next_move['y69']
y70=next_move['y70']
y71=next_move['y71']
y72=next_move['y72']
y73=next_move['y73']
y74=next_move['y74']
y75=next_move['y75']
y76=next_move['y76']
y77=next_move['y77']
y78=next_move['y78']
y79=next_move['y79']
y80=next_move['y80']
y81=next_move['y81']
y82=next_move['y82']
y83=next_move['y83']
y84=next_move['y84']
y85=next_move['y85']
y86=next_move['y86']
y87=next_move['y87']
y88=next_move['y88']
y89=next_move['y89']
y90=next_move['y90']
y91=next_move['y91']
y92=next_move['y92']
y93=next_move['y93']
y94=next_move['y94']
y95=next_move['y95']
y96=next_move['y96']
y97=next_move['y97']
y98=next_move['y98']
y99=next_move['y99']
y100=next_move['y100']

mlpreg1= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y1)
mlpreg2= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y2)
mlpreg3= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y3)
mlpreg4= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y4)
mlpreg5= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y5)
mlpreg6= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y6)
mlpreg7= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y7)
mlpreg8= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y8)
mlpreg9= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y9)
mlpreg10= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y10)
mlpreg11= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y11)
mlpreg12= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y12)
mlpreg13= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y13)
mlpreg14= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y14)
mlpreg15= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y15)
mlpreg16= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y16)
mlpreg17= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y17)
mlpreg18= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y18)
mlpreg19= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y19)
mlpreg20= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y20)
mlpreg21= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y21)
mlpreg22= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y22)
mlpreg23= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y23)
mlpreg24= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y24)
mlpreg25= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y25)
mlpreg26= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y26)
mlpreg27= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y27)
mlpreg28= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y28)
mlpreg29= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y29)
mlpreg30= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y30)
mlpreg31= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y31)
mlpreg32= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y32)
mlpreg33= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y33)
mlpreg34= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y34)
mlpreg35= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y35)
mlpreg36= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y36)
mlpreg37= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y37)
mlpreg38= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y38)
mlpreg39= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y39)
mlpreg40= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y40)
mlpreg41= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y41)
mlpreg42= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y42)
mlpreg43= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y43)
mlpreg44= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y44)
mlpreg45= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y45)
mlpreg46= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y46)
mlpreg47= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y47)
mlpreg48= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y48)
mlpreg49= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y49)
mlpreg50= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y50)
mlpreg51= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y51)
mlpreg52= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y52)
mlpreg53= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y53)
mlpreg54= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y54)
mlpreg55= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y55)
mlpreg56= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y56)
mlpreg57= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y57)
mlpreg58= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y58)
mlpreg59= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y59)
mlpreg60= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y60)
mlpreg61= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y61)
mlpreg62= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y62)
mlpreg63= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y63)
mlpreg64= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y64)
mlpreg65= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y65)
mlpreg66= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y66)
mlpreg67= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y67)
mlpreg68= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y68)
mlpreg69= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y69)
mlpreg70= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y70)
mlpreg71= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y71)
mlpreg72= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y72)
mlpreg73= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y73)
mlpreg74= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y74)
mlpreg75= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y75)
mlpreg76= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y76)
mlpreg77= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y77)
mlpreg78= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y78)
mlpreg79= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y79)
mlpreg80= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y80)
mlpreg81= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y81)
mlpreg82= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y82)
mlpreg83= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y83)
mlpreg84= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y84)
mlpreg85= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y85)
mlpreg86= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y86)
mlpreg87= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y87)
mlpreg88= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y88)
mlpreg89= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y89)
mlpreg90= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y90)
mlpreg91= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y91)
mlpreg92= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y92)
mlpreg93= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y93)
mlpreg94= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y94)
mlpreg95= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y95)
mlpreg96= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y96)
mlpreg97= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y97)
mlpreg98= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y98)
mlpreg99= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y99)
mlpreg100= MLPRegressor(hidden_layer_sizes = [100,100], activation = 'tanh',alpha=1000,solver = 'lbfgs').fit(X,y100)

pickle.dump(mlpreg1,open('1.sav','wb'))
pickle.dump(mlpreg2,open('2.sav','wb'))
pickle.dump(mlpreg3,open('3.sav','wb'))
pickle.dump(mlpreg4,open('4.sav','wb'))
pickle.dump(mlpreg5,open('5.sav','wb'))
pickle.dump(mlpreg6,open('6.sav','wb'))
pickle.dump(mlpreg7,open('7.sav','wb'))
pickle.dump(mlpreg8,open('8.sav','wb'))
pickle.dump(mlpreg9,open('9.sav','wb'))
pickle.dump(mlpreg10,open('10.sav','wb'))
pickle.dump(mlpreg11,open('11.sav','wb'))
pickle.dump(mlpreg12,open('12.sav','wb'))
pickle.dump(mlpreg13,open('13.sav','wb'))
pickle.dump(mlpreg14,open('14.sav','wb'))
pickle.dump(mlpreg15,open('15.sav','wb'))
pickle.dump(mlpreg16,open('16.sav','wb'))
pickle.dump(mlpreg17,open('17.sav','wb'))
pickle.dump(mlpreg18,open('18.sav','wb'))
pickle.dump(mlpreg19,open('19.sav','wb'))
pickle.dump(mlpreg20,open('20.sav','wb'))
pickle.dump(mlpreg21,open('21.sav','wb'))
pickle.dump(mlpreg22,open('22.sav','wb'))
pickle.dump(mlpreg23,open('23.sav','wb'))
pickle.dump(mlpreg24,open('24.sav','wb'))
pickle.dump(mlpreg25,open('25.sav','wb'))
pickle.dump(mlpreg26,open('26.sav','wb'))
pickle.dump(mlpreg27,open('27.sav','wb'))
pickle.dump(mlpreg28,open('28.sav','wb'))
pickle.dump(mlpreg29,open('29.sav','wb'))
pickle.dump(mlpreg30,open('30.sav','wb'))
pickle.dump(mlpreg31,open('31.sav','wb'))
pickle.dump(mlpreg32,open('32.sav','wb'))
pickle.dump(mlpreg33,open('33.sav','wb'))
pickle.dump(mlpreg34,open('34.sav','wb'))
pickle.dump(mlpreg35,open('35.sav','wb'))
pickle.dump(mlpreg36,open('36.sav','wb'))
pickle.dump(mlpreg37,open('37.sav','wb'))
pickle.dump(mlpreg38,open('38.sav','wb'))
pickle.dump(mlpreg39,open('39.sav','wb'))
pickle.dump(mlpreg40,open('40.sav','wb'))
pickle.dump(mlpreg41,open('41.sav','wb'))
pickle.dump(mlpreg42,open('42.sav','wb'))
pickle.dump(mlpreg43,open('43.sav','wb'))
pickle.dump(mlpreg44,open('44.sav','wb'))
pickle.dump(mlpreg45,open('45.sav','wb'))
pickle.dump(mlpreg46,open('46.sav','wb'))
pickle.dump(mlpreg47,open('47.sav','wb'))
pickle.dump(mlpreg48,open('48.sav','wb'))
pickle.dump(mlpreg49,open('49.sav','wb'))
pickle.dump(mlpreg50,open('50.sav','wb'))
pickle.dump(mlpreg51,open('51.sav','wb'))
pickle.dump(mlpreg52,open('52.sav','wb'))
pickle.dump(mlpreg53,open('53.sav','wb'))
pickle.dump(mlpreg54,open('54.sav','wb'))
pickle.dump(mlpreg55,open('55.sav','wb'))
pickle.dump(mlpreg56,open('56.sav','wb'))
pickle.dump(mlpreg57,open('57.sav','wb'))
pickle.dump(mlpreg58,open('58.sav','wb'))
pickle.dump(mlpreg59,open('59.sav','wb'))
pickle.dump(mlpreg60,open('60.sav','wb'))
pickle.dump(mlpreg61,open('61.sav','wb'))
pickle.dump(mlpreg62,open('62.sav','wb'))
pickle.dump(mlpreg63,open('63.sav','wb'))
pickle.dump(mlpreg64,open('64.sav','wb'))
pickle.dump(mlpreg65,open('65.sav','wb'))
pickle.dump(mlpreg66,open('66.sav','wb'))
pickle.dump(mlpreg67,open('67.sav','wb'))
pickle.dump(mlpreg68,open('68.sav','wb'))
pickle.dump(mlpreg69,open('69.sav','wb'))
pickle.dump(mlpreg70,open('70.sav','wb'))
pickle.dump(mlpreg71,open('71.sav','wb'))
pickle.dump(mlpreg72,open('72.sav','wb'))
pickle.dump(mlpreg73,open('73.sav','wb'))
pickle.dump(mlpreg74,open('74.sav','wb'))
pickle.dump(mlpreg75,open('75.sav','wb'))
pickle.dump(mlpreg76,open('76.sav','wb'))
pickle.dump(mlpreg77,open('77.sav','wb'))
pickle.dump(mlpreg78,open('78.sav','wb'))
pickle.dump(mlpreg79,open('79.sav','wb'))
pickle.dump(mlpreg80,open('80.sav','wb'))
pickle.dump(mlpreg81,open('81.sav','wb'))
pickle.dump(mlpreg82,open('82.sav','wb'))
pickle.dump(mlpreg83,open('83.sav','wb'))
pickle.dump(mlpreg84,open('84.sav','wb'))
pickle.dump(mlpreg85,open('85.sav','wb'))
pickle.dump(mlpreg86,open('86.sav','wb'))
pickle.dump(mlpreg87,open('87.sav','wb'))
pickle.dump(mlpreg88,open('88.sav','wb'))
pickle.dump(mlpreg89,open('89.sav','wb'))
pickle.dump(mlpreg90,open('90.sav','wb'))
pickle.dump(mlpreg91,open('91.sav','wb'))
pickle.dump(mlpreg92,open('92.sav','wb'))
pickle.dump(mlpreg93,open('93.sav','wb'))
pickle.dump(mlpreg94,open('94.sav','wb'))
pickle.dump(mlpreg95,open('95.sav','wb'))
pickle.dump(mlpreg96,open('96.sav','wb'))
pickle.dump(mlpreg97,open('97.sav','wb'))
pickle.dump(mlpreg98,open('98.sav','wb'))
pickle.dump(mlpreg99,open('99.sav','wb'))
pickle.dump(mlpreg100,open('100.sav','wb'))
'''
print mlpreg.score(X_train,Y_train)
print i
print mlpreg.score(X_test,Y_test)
print mlpreg.predict([[-1,0,-1,-1,0,0,-1,-1,0,0,0,0,0,0,0,-1,0,0,0,-1,0,0,-1,0,0,0,0,0,-1,0,0,0,0,0,-1,0,-1,0,0,-1,-1,-1,0,0,0,-1,0,0,0,0,0,0,0,-1,-1,-1,0,0,0,-1,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,0,0,-1,1,0,0,0,0,0,0,-1,0,0,0,0,0,-1,-1,-1,-1,-1,0,0]])
print mlpreg.predict([[0,0,0,0,0,0,-1,-1,-1,-1,0,0,-1,-1,0,0,0,-1,-1,0,0,0,0,0,0,0,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,0,0,0,0,0,0,0,0,-1,-1,0,0,0,0,0,-1,-1,0,0,-1,0,0,-1,0,-1,-1,-1,-1,0,-1,0,0,0,0,0,-1,-1,0,-1,0,0,0,0,0,-1,0,0,-1,0,0,0,0,-1,0,0,-1,0,-1,0]])
print mlpreg.predict([[0,0,1,1,1,1,0,0,0,0,0,-1,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1,-1,0,0,0,0,0,0,0,-1,0,-1,0,0,-1,0,-1,-1,0,0,0,0,0,0,0,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,0,-1,-1,0,-1,0,0,0,0,0,0,-1,0,0]])
print mlpreg.predict([[0,0,1,1,1,1,0,0,0,0,0,-1,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1,-1,0,0,0,0,0,0,0,-1,0,-1,0,0,-1,0,-1,-1,0,0,0,0,0,0,0,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,0,-1,-1,0,-1,0,0,0,0,0,0,-1,0,0]])
print mlpreg.predict([[-1,1,1,1,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,-1,0,0,0,0,0,-1,-1,-1,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,0,0,0,-1,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,-1,-1,0,-1,0,0,0,-1,0,0,-1,0,-1,0,0]])

hidden=[10,50,100]
for size in hidden:
	mlpreg = MLPRegressor(hidden_layer_sizes = [size,size], activation = 'tanh',alpha=10,solver = 'lbfgs').fit(X_train, Y_train)                      
	print mlpreg.score(X_train,Y_train)
	print size
	print mlpreg.score(X_test,Y_test)
	print mlpreg.predict([[0,0,0,-1,-1,0,0,-1,0,-1,0,0,-1,0,0,-1,0,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,0,-1,0,0,-1,-1,0,-1,0,0,-1,0,0,0,0,0,0,0,0,0,-1,0,-1,-1,-1,0,0,-1,0,0,0,0,-1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1,0,0]])


cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap=cmap)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()
'''