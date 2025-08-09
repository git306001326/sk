
def get_html(url,param={},header={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}):
    import requests #引入类库
    re=requests.get(url=url,params=param,headers=header)
    return re.content.decode('utf-8')
# 导入BeautifulSoup库，用于解析HTML文档
from bs4 import BeautifulSoup as bs
# 定义一个变量url，存储一个网址
url='http://edu.gd.gov.cn/jyzxnew/gdjyxw/content/post_4290255.html'
# 获取url对应的html页面
html=get_html(url)
# 使用BeautifulSoup解析html页面，features参数指定解析器为html.parser
bs1=bs(html,features='html.parser')
d=bs1.find(name='div',attrs={'class':"main"}) #  查找名为'div'的标签，且class属性为'main'的元素
bt=d.find(name='h3').get_text() #  找到d中名为'h3'的标签，并获取其文本内容，赋值给bt
f1=open('d:/files/{0}.txt'.format(bt),'w+',encoding='utf-8')
f1.write(bt) #写入标题
f1.write('\n')
ps=d.find_all(name='p')
for p in ps:
    s=p.get_text()
    f1.write(s)
    f1.write('\n')
    #print(s)
f1.close()

