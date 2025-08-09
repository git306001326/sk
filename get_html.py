#利用urllib库写一个通用获取网页内容的函数，并调用
def get_htm(url,data={},headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import urllib.request
    import urllib.parse #引入模块
    try:
        data1=bytes(urllib.parse.urlencode(data).encode('utf-8'))
        request1=urllib.request.Request(url=url,data=data1)
        response1=urllib.request.urlopen(request1)
        html=response1.read() #.decode('utf-8')
    except: #万一异常
        html=''
        print('出现异常')
    finally: #不管正常或异常，都要执行
        pass #空语句
    print('11111')
    return html
def get_html(url,param={},header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import requests #引入类库
    re=requests.get(url=url,params=param,headers=header)
    return re.content.decode('utf-8')
def get_requests(url,param={},header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import requests #引入类库
    re=requests.get(url=url,params=param,headers=header)
    return re
def post_html(url,param={},data={},header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import requests #引入类库
    re=requests.post(url=url,params=param,data=data,headers=header)
    return re.text
def get_htmlbin(url,param={},header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import requests #引入类库
    re=requests.get(url=url,params=param,headers=header)
    return re.content #返回原样的二进制码 #.decode('utf-8')不能转
def download(url,filename):
    #url='https://music.163.com/song/media/outer/url?id=5232547.mp3'
    print('正在下载,请稍后....')
    f1=open(filename,'wb')
    f1.write(get_htmlbin(url))
    f1.close()
    print('下载完成.')

