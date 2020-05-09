from DownloadPage import *
import  threading

url = "https://www.iimanhua.com/comic/2362/"
save_path = "F:/dongman"

url1 = 'https://www.iimanhua.com/comic/186/index.html'
url2 = 'https://www.iimanhua.com/comic/4/index.html'
url3 = 'https://www.iimanhua.com/comic/3/index.html'
url4 = 'https://www.iimanhua.com/comic/2203/index.html'

def thread1():
    downloadPage = DownloadPage('thread1')
    content = downloadPage.get_page_chapter(url1, save_path)

def thread2():
    downloadPage = DownloadPage('thread2')
    content = downloadPage.get_page_chapter(url2, save_path)

def thread3():
    downloadPage = DownloadPage('thread3')
    content = downloadPage.get_page_chapter(url3, save_path)

def thread4():
    downloadPage = DownloadPage('thread4')
    content = downloadPage.get_page_chapter(url4, save_path)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t3 = threading.Thread(target=thread3)
    t4 = threading.Thread(target=thread4)
    t1.start()
    t2.start()
    t3.start()
    t4.start()