# @File: welcome.py
# @Author: Kevin Huo
# @Date: 2020/9/23

import math
import random
import datetime

titles = [
  "Algorithms & Data Structures",
  "Programming Languages",
  "Machine Learning",
  "Misc"
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

descriptions = [
  "掌握算法及数据结构, 处变有道也。",
  "选择一门适合自己的编程语言, 如悟空择定海神针铁, 趁手之兵器也。",
  "机器学习及深度学习相关, 创造无限可能。",
  "无丝竹之乱耳, 无案牍之劳形。",
]

users = [
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

hrefs = [
  "/algorithms/index",
  "/prog-lang/index",
  "/ml/index",
  "/misc/index"
]


def get_welcome_data(args):
    """
    :param args: {"count": 4}
    """
    res = []
    count = args.get("count", 20) if args else 20
    print(args)
    print("count=%s" % count)
    for i in range(count):
        res.append(
            {"id": "welcome_list_%s" % i,
             "href": hrefs[i % 4],
             "owner": users[i % 10],
             "title": titles[i % 4],
             "avartar": avatars[i % 8],
             "cover": covers[i % 4] if (i/4)%2 == 0 else covers[i % 3],
             "status": ["active", "exception", "normal"][i % 3],
             "percent": math.ceil(round(random.uniform(0, 1), 2)) + 50,
             "logo": avatars[i % 8],
             "updatedAt": str(datetime.datetime.today().date()),
             "createdAt": str(datetime.datetime.today().date()),
             "subDescription": descriptions[i % 4],
             "description": "个人网站的研发需要不断学习和进步。",
             "activeUser": 100,
             "newUser": 50,
             "star": 10,
             "like": 20,
             "message": 30,
             "content": "段落示意：蚂蚁金服设计平台 ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 "
                        "ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。 ",
             "members": [
                 {"avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png",
                  "name": "小脱",
                  "id": "member1"},
                 {"avatar": "https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png",
                  "name": "小张",
                  "id": "member2"},
                 {"avatar": "https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png",
                  "name": "小火",
                  "id": "member3"}
             ]
             }
        )
    return res
