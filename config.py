# B站登录后获取的SESSDATA，CURRENT_QUALITY等
# 定期更换COOKIE的值即可
COOKIE = "buvid4=1D617680-848D-23B9-B3FA-6237EFCD9F6649365-024061605-4XLEjysIwD6yapSy9UXvIQ%3D%3D; DedeUserID=1154242240; DedeUserID__ckMd5=af19b4f6e6cac183; enable_web_push=DISABLE; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; enable_feed_channel=ENABLE; blackside_state=0; fingerprint=fb24a777ad3bd31e6503429c13b83109; buvid_fp=fb24a777ad3bd31e6503429c13b83109; _uuid=EB62EFB7-263E-F363-2DCE-E2C7DEDD893932081infoc; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; theme_style=dark; hit-dyn-v2=1; buvid3=894F09A0-E466-B749-7178-F7818C54C74519791infoc; b_nut=1753156919; LIVE_BUVID=AUTO4917531569204425; rpdid=|(u)~m))kJY)0J'u~lJ~l~J~|; PVID=1; SESSDATA=340eee74%2C1776238177%2C16d3d%2Aa1CjAeSWoYkqf1iPPybkdTvQ4L-cCSAmVSeII14hLDlkBF1q3zn-rH4wcc1IWxX60tcmoSVmx2YU1XYTctSG02dC1aZVdFNDNDYnMzS3lVbDhxZXhGWm9zNlU0SVRLby1COFdJTVJWUVRZMVg0OGE1SDFuRVJsd1ZZMXJhNVFKdmtCUjVWeHNRVC1BIIEC; bili_jct=839f20240dfb1b3febdc0c886a377410; historyviewmode=list; go-old-space=-1; dy_spec_agreed=1; CURRENT_LANGUAGE=; browser_resolution=1358-697; home_feed_column=4; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjY3MzU1MzEsImlhdCI6MTc2NjQ3NjI3MSwicGx0IjotMX0.JtJ6yqgapy3YYUydUAZt1muFDnCwsA0-sVqGkydKtTM; bili_ticket_expires=1766735471; CURRENT_QUALITY=80; bp_t_offset_1154242240=1150010414428323840; CURRENT_FNVAL=4048; b_lsid=867D49C2_19B54945BEA; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; sid=71ocm22u"

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