import json
import subprocess

with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

results = []

for ch in channels:
    try:
        cmd = [
            "yt-dlp",
            "-g",
            ch["url"]
        ]

        stream = subprocess.check_output(
            cmd,
            text=True
        ).strip()

        results.append(
            f'#EXTINF:-1,{ch["name"]}\n{stream}'
        )

        print(f'OK : {ch["name"]}')

    except Exception as e:
        print(e)

with open("output.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    f.write("\n".join(results))
