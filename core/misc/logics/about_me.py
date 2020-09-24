# @File: about_me.py
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


def get_about_me_data():
    """
    /misc/about-me
    """
    res = {
        "name": 'HUO Ke',
        "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
        "userid": '00000001',
        "email": 'hkhuoke@hotmail.com',
        "signature": '星星之火, 可以燎原',
        "title": '兴趣使然',
        "group": '新手村',
        "tags": [
            {
                "key": '0',
                "label": '桌游',
            },
            {
                "key": '1',
                "label": '篮球',
            },
            {
                "key": '2',
                "label": '乌鸦之霜',
            }
        ],
        "notice": [
            {
                "id": 'xxx1',
                "title": titles[0],
                "logo": avatars[0],
                "description": '那是一种内在的东西，他们到达不了，也无法触及的',
                "updatedAt": str(datetime.datetime.now().date()),
                "member": '科学搬砖组',
                "href": '',
                "memberLink": '',
            },
            {
                "id": 'xxx2',
                "title": titles[1],
                "logo": avatars[1],
                "description": '希望是一个好东西，也许是最好的，好东西是不会消亡的',
                "updatedAt": "2017-07-24",
                "member": '全组都是吴彦祖',
                "href": '',
                "memberLink": '',
            },
            {
                "id": 'xxx3',
                "title": titles[2],
                "logo": avatars[2],
                "description": '城镇中有那么多的酒馆，她却偏偏走进了我的酒馆',
                "updatedAt": str(datetime.datetime.now().date()),
                "member": '中二少女团',
                "href": '',
                "memberLink": '',
            },
            {
                "id": 'xxx4',
                "title": titles[3],
                "logo": avatars[3],
                "description": '那时候我只会想自己想要什么，从不想自己拥有什么',
                "updatedAt": str(datetime.datetime.now().date()),
                "member": '程序员日常',
                "href": '',
                "memberLink": '',
            },
            {
                "id": 'xxx5',
                "title": titles[4],
                "logo": avatars[4],
                "description": '凛冬将至',
                "updatedAt": str(datetime.datetime.now().date()),
                "member": '高逼格设计天团',
                "href": '',
                "memberLink": '',
            },
            {
                "id": 'xxx6',
                "title": titles[5],
                "logo": avatars[5],
                "description": '生命就像一盒巧克力，结果往往出人意料',
                "updatedAt": str(datetime.datetime.now().date()),
                "member": '骗你来学计算机',
                "href": '',
                "memberLink": '',
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
