# Bilibili视频下载(pgitosib集成库版)

<div align="center">
    <img src="docs/bilibili-logo.png">
</div>

## :pushpin: 功能说明

- [x] B站视频下载
- [x] 支持使用账号 cookie 下载大会员视频
- [x] 异步并发下载
- [x] 批量下载
- [x] 支持分P视频
- [x] 支持充电专属视频下载
- [x] 下载进度条
- [x] 下载摘要统计
- [x] 自动清理临时文件
- [ ] 支持番剧、纪录片下载【待测试】
- [ ] 添加代理【待更新】
# 本仓库(forked)计划:
- [x] 集成库到libs文件夹内
- [ ] 将所有功能打包成exe

## :pencil2: COOKIE设置说明

打开`config.py`，**需要定期(30天)替换** cookie

替换方法：

1. 浏览器登录 B 站，打开要下载的视频页
2. `Ctrl + Shift + I` 或者鼠标右键选择检查，然后选择`网络`
3. `Ctrl + R` 刷新网页，选择第一个(通常是`BV`打头)，请求标头中找到 `cookie`
4. 打开`config.py`，将 `COOKIE` 字符串替换为你的 COOKIE
```py
# B站登录后获取的SESSDATA，CURRENT_QUALITY等
# 定期更换COOKIE的值即可
COOKIE = "将此处的字符串替换为你的 COOKIE"
```

![](docs/set-cookie.png)

## :pencil2: 下载链接添加说明

打开`config.py`，在 `URL` 列表中添加视频 URL

```py
# 下载视频的 URL
URL = [
    # # 普通视频
    # 'https://www.bilibili.com/video/BV1M4411c7P4/?vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',
    # 'https://www.bilibili.com/video/BV1hB4y147j8/?spm_id_from=333.337.search-card.all.click&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',

    # # 分P视频（第1个分P）
    # 'https://www.bilibili.com/video/BV1TnsZzHEcz/?vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63&spm_id_from=333.788.videopod.episodes',

    # # 分P视频（第2个分P）
    # 'https://www.bilibili.com/video/BV1TnsZzHEcz/?p=2&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',

    # 充电专属视频
    'https://www.bilibili.com/video/BV1W1wKeWEVe/?spm_id_from=333.1387.upload.video_card.click&vd_source=9c3224b88b8a3c4cc210fc6ff9b28f63',
]
```

## :rocket: 运行方法

双击运行 `run.bat`

```bash


============================================================
📹 【13小时完结】国民女神带着可爱女儿找上门求我负责？！可我明明却是个万能单身狗。
📺 清晰度：高清 1080P
============================================================

📥 开始下载视频和音频：【13小时完结】国民女神带着可爱女儿找上门求我负责？！可我明明却是个万能单身狗。_P1.mp4

  音频: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 726M/726M [04:49<00:00, 2.51MB/s]
  视频: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.43G/1.43G [33:48<00:00, 707kB/s]

✅ 视频和音频下载完成

🎬 合并视频和音频...
✅ 视频合成完成

🧹 已清理临时文件

============================================================
📊 下载摘要
============================================================
✅ 成功下载 1 个视频
⏱️  总计用时：34分钟17秒

已下载的视频：
  1. 【13小时完结】国民女神带着可爱女儿找上门求我负责？！可我明明却是个万能单身狗。 (高清 1080P)

💾 视频保存位置：/home/user/work/repos/bilibili-downloader/output
============================================================
```

## :tv: 运行效果

![](docs/screen.gif)

## :information_source: 第三方组件声明

本项目为了方便用户使用，**捆绑了FFmpeg的可执行文件 (`ffmpeg.exe`)**。
- FFmpeg 受 **GNU General Public License v3.0 (GPL-3.0)** 许可证保护。
- 本项目所使用的FFmpeg版本为 `ffmpeg version 8.0.1-essentials_build-www.gyan.dev` 。
- 本项目的Python代码与FFmpeg通过独立的进程调用方式进行交互，二者为聚合关系。
- 本项目的主程序代码采用 **MIT 许可证**，此许可证仅适用于本项目的Python源代码，**不适用于FFmpeg**。

### 关于FFmpeg的GPL合规
- 随本程序分发的FFmpeg二进制文件对应的完整源代码、构建说明及修改（如有）均可从以下官方渠道获取：
    - 官方网站：[https://ffmpeg.org/](https://ffmpeg.org/)
    - 官方源代码仓库：[https://git.ffmpeg.org/ffmpeg.git](https://git.ffmpeg.org/ffmpeg.git)
- GPL-3.0许可证全文已附于：[libs/ffmpeg/LICENSE](libs/ffmpeg/LICENSE)