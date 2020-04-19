from DownloadPage import *

url = "https://www.iimanhua.com/comic/2362/"
save_path = "F:/dongman"

downloadPage = DownloadPage()
content = downloadPage.get_page_chapter(url, save_path)
