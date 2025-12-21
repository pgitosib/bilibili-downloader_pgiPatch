import os

# 程序根目录（请勿修改）
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 文件临时输出目录
TEMP_PATH = os.path.join(BASE_PATH, "temp")
# 视频输出目录
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

# B站登录后获取的SESSDATA，CURRENT_QUALITY
# 定期更换COOKIE的值即可
COOKIE = 'buvid3=5EF59BBB-DADF-AC38-2862-7E588DAA63F567589infoc; b_nut=1763285667; _uuid=F428A1C1-417D-8849-BAAF-810510A74B126972040infoc; home_feed_column=4; buvid4=C41C1D3C-CA9D-5596-B4EF-1493932BBB8C68965-025111617-zyhkyNiMl7JwzP8ZDdUFdg%3D%3D; buvid_fp=563263ed7718f630443e30a1295bc3bb; DedeUserID=8366997; DedeUserID__ckMd5=b6567189d34e3723; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; rpdid=|(u)Y|~m|k|J0J\'u~YJk)l~Rm; browser_resolution=1016-1046; CURRENT_QUALITY=80; bp_t_offset_8366997=1146124276479295488; CURRENT_FNVAL=4048; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjY0ODI0OTEsImlhdCI6MTc2NjIyMzIzMSwicGx0IjotMX0.hw6IatXKwfDF4nEreJrbt0qCSwYMJvlhYSdVh0j_wXI; bili_ticket_expires=1766482431; SESSDATA=0fc66a0b%2C1781775686%2Cf5c0a%2Ac2CjC05PNQ0L9jWVoAJd3TvemJGpn47adAG5pbU7T9OLF0GO0tlONrQ5t1T8rMgF820cYSVnNOZk5YLXo5bU5XaTdZR3ZWMmNFZzNuU3N6RnMtQnBndVBkZWlUc3ZhblVlTC1naWs1N25yb2RnZGVMcUhyVkQ2QXdEcXVRal9ld1BDcDFzaVQwZVBBIIEC; bili_jct=9a517578e7e0e887d8e6f853fa0ef6de; sid=4ycvaa49; b_lsid=109FC8CF3_19B3F32DB0B'

URL = [
    # 普通视频
    'https://www.bilibili.com/video/BV1M4411c7P4/?vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',
    'https://www.bilibili.com/video/BV1hB4y147j8/?spm_id_from=333.337.search-card.all.click&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',

    # 分P视频（第1个分P）
    'https://www.bilibili.com/video/BV1TnsZzHEcz/?vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&spm_id_from=333.788.videopod.episodes',

    # 分P视频（第2个分P）
    'https://www.bilibili.com/video/BV1TnsZzHEcz/?p=2&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',

    # 充电专属视频
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&p=2',
    # 'https://www.bilibili.com/video/BV15FK6zTEuj/?spm_id_from=333.788.videopod.episodes&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&p=3',

    # 番剧/电影（需要中国大陆 IP）
    # 'https://www.bilibili.com/bangumi/play/ss39429',      # 电影
    # 'https://www.bilibili.com/bangumi/play/ep271002',     # 番剧单集（暂不支持）
]