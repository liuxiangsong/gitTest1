# import urllib.request
# from bs4 import BeautifulSoup
# response = urllib.request.urlopen('https://www.cnblogs.com/')
# html = response.read()
# soup = BeautifulSoup(html, 'lxml')
# items = soup.select(".post_item_body a[class='titlelnk']")
# for item in items:
#     print(item.string)

f = open("d:/1.txt", 'w')
f.write("hello world")
