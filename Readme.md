# CR EEXI calculator 使用手冊
網頁好讀版:
https://hackmd.io/@Ee55O50FQX6WTITGIrBYaQ/SkmAvg5xK

本計算程式使用MEPC.333(76)之EEXI計算指南為基礎\
:::info
☢️本計算程式之計算值++僅供參考++，非正式之EEXI計算值
:::
## **使用者介面**
![](https://i.imgur.com/zEs9qLS.png)

主要分成三欄:**input**、**original output**和**recommended output**，以下針對各欄各個參數說明。
## **Input**
![](https://i.imgur.com/aS5mZIh.png)\
:::info
:tokyo_tower:在input 欄中，只有**船型**、**DWT**和**MCR ME**為必要輸入，其他皆為選填，可由DWT、MCR_ME和其他預設值計算取得近似值
:::
### 船型:ship:
![](https://i.imgur.com/yj6WcxS.png)\
最上方之選單可以輸入船型，目前支援之船型有:
* Bulk carrier
* Container ship
* Tanker
* General cargo ship
* Refrigerated cargo carrier

### 載重噸(DWT)和主機連續最大出力(MCR_ME)
![](https://i.imgur.com/41qaDDj.png)
### LWT
![](https://i.imgur.com/AeuKiwu.png)\
若為CSR的船舶可輸入LWT，進行EEXI值折減
### VS EEDI & PS EEDI
![](https://i.imgur.com/EeePNPL.png)\
若有EEDI海試資料可輸入海試之船速及其對應之主機馬力
:::info
:boom:VS 和 PS需要兩者同時輸入，不行只輸入其中一個
:::
### PAE
![](https://i.imgur.com/jXefaNO.png)\
可輸入輔機功率，否則將以MCR_ME計算近似值

### SFC
![](https://i.imgur.com/CKqI00f.png)\
可輸入主機和輔機之燃油消耗量和作功之比值(燃油消耗率)
若為空白，則帶入預設值:
* SFC_ME=190(g/kWh)
* SFC_AE=215(g/kWh)
### PTO
![](https://i.imgur.com/1MU3jBN.png)\
可輸入軸發電機之功率，若無以零計算
> 參考EEDI計算指南MEPC.308(73) Annex 2.2.5.2
### CF
![](https://i.imgur.com/f8D19jI.png)\
CF為燃油消耗和二氧化碳排放之比值
若空白，預設值為3.114(t$CO_2$/tfuel)
> 參考EEDI計算指南MEPC.308(73) Annex 2.2.1
### EPL
![](https://i.imgur.com/PTR4gW1.png)\
:::info
:warning:若船舶已有裝置EPL，依其類型++擇一++填寫其最大之限制功率
:::
## **Original Output** 
![](https://i.imgur.com/M3fbaRS.png)\
依照輸入值計算
* 輔機功率 PAE
* 主機功率 PME
* 近似船速 Vapp
* 其餘參數 margin, Vavg, MCR avg為計算Vapp所需之參數
:::info
:ghost:若輸入值中有VS EEDI和PS EEDI，則Vapp直接由VS, PS和MCR計算取得
:::
> 參考MEPC.333(76) Annex 2.2.3

### EEXI

![](https://i.imgur.com/BTOEWMj.png)\
計算Attained EEXI 和Required EEXI，**Attained EEXI ≤ Required EEXI** 才算符合。若不符合，在下一欄**Recommended**提出MCR, V的建議值。

## **Recommended Output**

### MCR lim
![](https://i.imgur.com/n92STEu.png)\
計算若此船舶欲達到Required EEXI值，其主機限制功率MCR Lim應為多少
其中MCR lim = PME lim/0.83

###  Vapp lim
![](https://i.imgur.com/6mz1JEM.png)\
計算此時的限制船速Vapp lim，並計算與原始計算值之差距
其中:
%MCR = MCR_lim/MCR
Vapp Reduction = Vapp lim - Vapp
最後，取得新的Attained EEXI值，其應剛好與Required值相等。

## **Figure**
按下calculation鍵後，自動產生圖。圖中藍線為Required EEXI線 、橘色叉為original Attained EEXI，若original Attained值大於Required值，則顯示綠色點為new Attained 值。\
![](https://i.imgur.com/UIOn3ju.png)
![](https://i.imgur.com/tuwe1r5.png)


