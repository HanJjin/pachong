import requests
import re

host = 'https://1.yasee6.com/'


def getVideoId():
    videoId = int(input("Input Video ID: "))
    videoUrl = host + str("video-") + str(videoId)
    return str(videoUrl)


def getXHR():
    videoUrl = getVideoId()
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }
    response = requests.get(videoUrl, headers=headers)
    if response.status_code == 200:
        reg = re.compile(r'm3u8_url = \'(.*?)\', poster_url')
        m3u8_link = reg.findall(response.text)[0]
        return m3u8_link
    else:
        return None


def m3u8(m3u8_link):
    if '[domain_dan]' in m3u8_link:
        m3u8_link = m3u8_link.replace("[domain_dan]", "hone.yyhdyl.com")
    elif '[domain_fourth]' in m3u8_link:
        m3u8_link = m3u8_link.replace("[domain_fourth]", "head2.yyhdyl.com")
    elif '[domain_shuang]' in m3u8_link:
        m3u8_link = m3u8_link.replace("[domain_shuang]", "htwo.yyhdyl.com")
    elif '[domain_three]' in m3u8_link:
        m3u8_link = m3u8_link.replace("[domain_three]", "head.yyhdyl.com")
    else:
        m3u8_link = None
    return m3u8_link


if __name__ == '__main__':
    while True:
        m3u8_link = getXHR()
        if not m3u8_link:
            print('Error!\n')
        else:
            m3u8_url = m3u8(m3u8_link)
            print(m3u8_url)
