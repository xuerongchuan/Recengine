# Recengine

### 数据表格式
#### 上传数据表（DataTable）
字段名|字段含义
-|-
id|自增，唯一标识
workId|项目id
name|数据名称
detail|数据描述
type|数据类型 0：项目表，1：行为表，2：用户表
path|数据存储路径


**path**：默认本地路径+id

#### 用户表（userTable）
字段名|字段含义
-|--
id|用户id，自增，数值型，唯一标识


#### 项目表（workTable）
字段名|字段含义
-|-
id|自增，唯一标识
userId|用户id
parameter|参数字典列表
result|推荐结果，默认为空


**parameter**：[{'algoId'：<算法1>,'<参数名>'：<参数值>···},{'algoId'：<算法2>,'<参数名>'：<参数值>···}]

#### 算法表（algoTable）
字段名|字段含义
-|-
id|算法id，自增，唯一标识
parameter|默认参数字典
type|算法类型，{0，1，2} 分别代表离线，近线，在线


**parameter**：{'<参数名>'：<默认参数值列表>}

### 传递参数
参数名|含义
-|-
workId|项目id
userDataPath|用户数据存储路径
itemDataPath|项目数据存储路径
actionDataPath|行为数据存储路径
algo



<!--stackedit_data:
eyJoaXN0b3J5IjpbMjM5OTMwMzM1LC0xMTIwMTI4NzUwLDEwND
I2OTExNDYsMTY5NDQ0ODMxOSwtNjQ1ODg3MTU0LDIwNDg5MTk4
NjBdfQ==
-->