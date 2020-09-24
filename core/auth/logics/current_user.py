# @File: current_user.py
# @Author: Kevin Huo
# @Date: 2020/9/24

import datetime

titles = [
    'Alipay',
    'Angular',
    'Ant Design',
    'Ant Design Pro',
    'Bootstrap',
    'React',
    'Vue',
    'Webpack',
]

avatars = [
    'https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png',
    'https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png',
    'https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png',
    'https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png',
    'https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png',
    'https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png',
    'https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png',
    'https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png',
]

covers = [
    'https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png',
    'https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png',
    'https://gw.alipayobjects.com/zos/rmsportal/iXjVmWVHbCJAyqvDxdtx.png',
    'https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png',
]

desc = [
    '那是一种内在的东西， 他们到达不了，也无法触及的',
    '希望是一个好东西，也许是最好的，好东西是不会消亡的',
    '生命就像一盒巧克力，结果往往出人意料',
    '城镇中有那么多的酒馆，她却偏偏走进了我的酒馆',
    '那时候我只会想自己想要什么，从不想自己拥有什么',
]

user = [
    '付小小',
    '曲丽丽',
    '林东东',
    '周星星',
    '吴加好',
    '朱偏右',
    '鱼酱',
    '乐哥',
    '谭小仪',
    '仲尼',
]


def get_current_user():
    res = {
              "name": 'Guest',
              "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
              "userid": '00000001',
              "email": 'guest@kevinhuo.com',
              "signature": '星星之火, 可以燎原',
              "title": '兴趣使然',
              "group": '新手村',
              "tags": [
                  {
                      "key": '0',
                      "label": '篮球',
                  },
                  {
                      "key": '1',
                      "label": '桌游',
                  },
                  {
                      "key": '2',
                      "label": '野草',
                  },
                  {
                      "key": '3',
                      "label": '瓦尔登湖',
                  },
                  {
                      "key": '4',
                      "label": '炒面',
                  },
                  {
                      "key": '5',
                      "label": '乔丹',
                  },
              ],
              "notifyCount": 12,
              "unreadCount": 11,
              "country": 'China',
              "geographic": {
                  "province": {
                      "label": 'xx',
                      "key": '330000',
                  },
                  "city": {
                      "label": 'xx',
                      "key": '330100',
                  },
              },
              "address": 'xx',
              "phone": '0752-268888888',
          }

    return res
