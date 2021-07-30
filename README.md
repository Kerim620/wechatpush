# wechatpush

本项目为向微信推送消息的解决方案。

项目部署于腾讯云函数，通过调用api实现向微信直接推送消息的功能。

## 使用教程

### 创建企业应用

#### 一、注册企业

进入[企业微信官网](https://work.weixin.qq.com/)，注册一个企业。

#### 二、创建应用

点「管理企业」进入管理界面，选择「应用管理」 → 「自建」 → 「创建应用」。

![image-20210730092531953](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730092531953.png)

#### 三、 获取配置

点击进入应用，查看AgentId和Secret，其中Secret需要在手机端的企业微信查看。

![image-20210730092913129](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730092913129.png)

在「我的企业」中查看企业ID。

![image-20210730093512316](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730093512316.png)

### 部署云函数

#### 一、创建云函数

点[此处](https://console.cloud.tencent.com/scf/list-create?rid=4&ns=default&createType=empty&keyword=api)创建腾讯云函数，函数类型为事件函数，运行环境选Python3，函数代码选用本地上传[zip包文件](https://github.com/zzzjoy-620/wechatpush/releases/download/v1.0/index.zip)，也可选在线编辑，复制项目的index.py代码。触发器暂不创建。

![image-20210730103135112](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730103135112.png)

#### 二、配置环境变量

在函数管理编辑函数配置，设置如下的环境变量。

| key       | value                             |
| --------- | --------------------------------- |
| PUSH_KEY  | 自己设置的key，可随意，后面会用到 |
| WX_AID    | 企业微信应用的AgentId             |
| WX_CID    | 企业ID                            |
| WX_SECRET | 企业微信应用的Secret              |

![image-20210730105021360](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730105021360.png)

#### 三、创建触发器

触发管理中创建触发器，选择API网关触发，关闭集成响应（重要）。

![image-20210730105736995](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730105736995.png)

创建完成之后，记录访问路径，整个部署环节结束了。

![image-20210730110056499](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730110056499.png)

## 测试推送

目前只支持推送文本消息，支持get和post两种请求方案，建议使用post。

| 请求参数 | 说明                                                         | 是否必须 |
| -------- | ------------------------------------------------------------ | -------- |
| key      | 环境变量中的PUSH_KEY                                         | 是       |
| msg      | 推送的文本消息                                               | 是       |
| touid    | 推送到对应的成员的 ID，在企业微信后台，`通讯录`，成员资料 `账号` 字段多个ID用\|隔开，例如“zhangsan\|lisi”。默认为@all。 | 否       |

![image-20210730110624786](https://gitee.com/zzzjoy/My_Pictures/raw/master/image-20210730110624786.png)

## 项目参考

**[ wecomchan](https://github.com/easychen/wecomchan)**
