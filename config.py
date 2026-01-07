# B站登录后获取的SESSDATA，CURRENT_QUALITY等
# 定期更换COOKIE的值即可
COOKIE = "将此处的字符串替换为你的 COOKIE"

URL = [
    # 普通视频
    'https://www.bilibili.com/video/BV1xU4y1H7ob?vd_source=bc941dea3db5226cbee09e86bdaadf80&spm_id_from=333.788.videopod.episodes',
    'https://www.bilibili.com/video/BV1xU4y1H7ob/?p=2',
    'https://www.bilibili.com/video/BV1xU4y1H7ob/?p=3'

    # 充电专属视频
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&p=2',
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&p=3',

    # 番剧/电影（需要中国大陆 IP）
    # 'https://www.bilibili.com/bangumi/play/ss39429',      # 电影
    # 'https://www.bilibili.com/bangumi/play/ep271002',     # 番剧单集（暂不支持）
]



import os
# 程序根目录（请勿修改）
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 文件临时输出目录
TEMP_PATH = os.path.join(BASE_PATH, "temp")
# 视频输出目录
OUTPUT_PATH = os.path.join(BASE_PATH, "output")