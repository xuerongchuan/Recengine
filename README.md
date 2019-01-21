# Recengine

### 数据表格式
#### 上传数据表（DataRouteTable）
字段名|字段含义
-|-
id|自增，唯一标识
workId|项目id
name|数据名称
detail|数据描述


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




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjI2ODMzNzAsLTY0NTg4NzE1NCwyMD
Q4OTE5ODYwXX0=
-->