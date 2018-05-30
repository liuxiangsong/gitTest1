利用 selenium 库抓取动态网页

前言在抓取常规的静态网页时，我们直接请求对应的 url 就可以获取到完整的 HTML 页面，但是对于动态页面，网页显示的内容往往是通过 ajax 去生成的，所以如果是用 urllib.request 直接获取页面的 HTML 时，就获取不到我们所想用的内容，这时我们可以利用 selenium 库就可以轻松地获得我们所需要的内容了。

在测试过程中碰到的问题。
1、用 pip install selenium 安装 selenium 库时失败。可以利用下面的命令来安装
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org selenium
2、在使用时 webdriver.Chrome()时出现的问题，在网上看到的文章用的是火狐浏览器，他们直接使用 webdriver.Firefox()就可以了，而我是用谷歌浏览器，我以为用谷歌浏览器和用火狐浏览器一样的，但是在运行时出错了，后来再网上找了一下，是要在 selenium 官网下载谷歌的 Driver,然后在使用 webdriver.chorme()函数时,需要传 executable_path 参数，该参数的值就是在 selenium 官网下载的 Chrome Driver 文件所在的路径。
selenium 官网（https://selenium-python.readthedocs.io/）
3、下载 ChromeDriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="F:/chromedriver")
driver.get("https://www.deppon.com/deptlist/")
html = driver.page_source
print(html)

Chrom/firefox 浏览器插件：Katalon Recorder 可以用来记录浏览网页的所有操作，并且可以到出成 python 代码
