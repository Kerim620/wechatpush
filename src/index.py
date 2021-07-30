# -*- coding: utf-8 -*-
import re
import sys
import logging
import json
import os
import requests

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def main_handler(event, content):
    config = get_config()
    if config is None:
        return {'code':500, 'msg':'环境变量未配置成功'}
    elif 'key' in event['queryString'].keys() and 'msg' in event['queryString'].keys():  
        msg = event['queryString']['msg']
        key = event['queryString']['key']
        if key == config['push_key']:
            if 'touid' in event['queryString'].keys():
                response = push_wx(msg, config, event['queryString']['touid'])
            else:
                response = push_wx(msg, config)          
            if response:
                logger.info('推送成功')
                return {'code':200, 'msg':'推送成功'}
            else:
                logger.info('推送失败')
                return {'code':501, 'msg':'推送失败'}
        else:
            return {'code':502, 'msg':'参数错误'}
    else:
        return {'code':100, 'msg':'配置成功'}


# 推送消息
def push_wx(msg, config, touid='@all'):
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={config['wx_cid']}&corpsecret={config['wx_secret']}"
    response = requests.get(get_token_url).content
    if json.loads(response).get('errmsg') != 'ok':
        return False
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser":touid,
            "agentid":config['wx_aid'],
            "msgtype":"text",
            "text":{
                "content": raw(msg)
            },
            "duplicate_check_interval":600
        }
        response = requests.post(send_msg_url,data=json.dumps(data)).content
        logger.info('推送消息：' + str(data))
        return json.loads(response).get('errmsg') == 'ok'
    else:
        return False


# 从环境变量中读取配置
def get_config():
    config  = {
        'wx_aid': '',
        'wx_cid': '',
        'wx_secret': '',
        'push_key': '',
    }   
    config['wx_aid'] = os.getenv('WX_AID', None)
    config['wx_cid'] = os.getenv('WX_CID', None)
    config['wx_secret'] = os.getenv('WX_SECRET', None)
    config['push_key'] = os.getenv('PUSH_KEY', None)
    
    for v in config.values():
        if v is None:
            return None
    return config  


# 传参中的文本内容中的\n实际为\\n，要转化回去
# 暂时没想到好的方法，这里把常用的转化回去
def raw(text):
    text = re.sub(r'\\n',r'\n', text)
    text = re.sub(r'\\r',r'\r', text)
    text = re.sub(r'\\t',r'\t', text)
    return text
