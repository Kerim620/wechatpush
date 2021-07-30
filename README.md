# Wx_Push

本项目为向微信推送消息的解决方案

项目部署于腾讯云函数，通过调用api实现向微信直接推送消息的功能。

## 使用教程

### 创建企业应用

#### 一、注册企业

进入[企业微信官网](https://work.weixin.qq.com/)，注册一个企业。

#### 二、创建应用

点「管理企业」进入管理界面，选择「应用管理」 → 「自建」 → 「创建应用」。可见范围设置为自己。

![image-20210730092531953](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730092531953.png)

#### 三、 获取配置

点击进入应用，查看AgentId和Secret，其中Secret需要在手机端的企业微信查看。

![image-20210730092913129](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730092913129.png)

在「我的企业」中查看企业ID

![image-20210730093512316](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730093512316.png)

### 部署云函数

点[此处](https://console.cloud.tencent.com/scf/list-create?rid=4&ns=default&createType=empty&keyword=api)创建腾讯云函数，触发器暂不创建

![image-20210730103135112](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730103135112.png)



