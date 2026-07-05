import urllib.request
import re

# এখন টিভির লাইভ ভিডিও লিংক
youtube_url = "https://www.youtube.com/live/PRvnQNOaTFg"

try:
    # ইউটিউব পেজের সোর্স কোড রিকোয়েস্ট করা
    req = urllib.request.Request(youtube_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # সোর্স কোড থেকে আসল .m3u8 লাইভ লিংক খুঁজে বের করা
    matches = re.findall(r'(https://manifest.googlevideo.com/api/manifest/hls_variant/.*?\.m3u8)', html)
    
    if matches:
        # ব্যাকস্ল্যাশ রিমুভ করে আসল লিংকটি নেওয়া
        m3u8_url = matches[0].replace('\\/', '/')
        
        # m3u ফাইল তৈরি করা
        with open("ekhon_tv.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write('#EXTINF:-1 tvg-id="EkhonTV" tvg-name="Ekhon TV" tvg-logo="https://raw.githubusercontent.com/arshatb/EkhonTV-m3u8/main/logo.png" group-title="News",Ekhon TV\n')
            f.write(f"{m3u8_url}\n")
        print("Success: M3U8 link updated successfully!")
    else:
        print("Error: Could not find m3u8 link in page source.")
except Exception as e:
    print(f"An error occurred: {e}")
