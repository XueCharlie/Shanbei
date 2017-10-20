import urllib.request
import os
import re
import time
from prettytable import PrettyTable

# def book_content(url): #提取单词书主页下各个目录连接比如https://www.shanbay.com/wordbook/162217/
#     url=str(input('请输入主页网址比如:'))
#     return url

def specific_url(url):#提取网页目录连接
    # urls=input('输入目录网址：')
    # p=r'<a href="https://www.shanbay.com/wordlist/[^"]*"'
    # result = re.findall(p,urls)
    # for each in result:
    #     print (each)
    #     return each

    # html = url_open(url).decode('utf-8')
    # print (html)
    # table = []
    # a = r'<a href="[^"]*">'
    # url_list=re.findall(a,html)
    # for each in url_list:
    #     print (each)
    #     # return each
    pass

def input_def_change():
    pass 

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_page(url):
    pass


    # req = urllib.request.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER')
    # response = urllib.request.urlopen(url)
    # html = response.read().decode('utf-8')
    #
    # a = html.find('')+23
    # b = html.find(']',a)
    #
    # print(html[a:b])
    #
    # return html[a:b]

def find_table1(url):
    html = url_open(url).decode('utf-8')
    # f = open('word.txt','a')

    a =re.compile(r'<strong>(.*?)</strong>.*?<td class="span10"> (.*?)</td>',re.DOTALL)
    table= a.findall(html)
    x = PrettyTable(["英文", "中文"])
    x.padding_width = 1
    x.align = "l"
    
    for each in table:
        x.add_row(each)
    time.sleep(0.5)
    print (x)
        # f.writelines(x)

    # while a != -1:
    #     b = html.find ('</strong>',a,a+100)
    #     if b!= -1:
    #         table.append(html[a+8:b])
    #     else:
    #         b = a+8
    #
    #     a= html.find ('<strong>',b )
    # for each in table:



# def find_table2(url):
#     html = url_open(url).decode('utf-8')
#     table=[]
#     a = html.find ('<strong>')
#     while a != -1
#         b = html.find ('</strong>',a,a+100)
#         if b!= -1:
#             table.append(html[a+8:b])

# def get_pages(url):
#     html=url_open(url).decode('utf-8')
#     p=r'<a href="javascript:;" data-page=".*?</a>'
#     pages = re.findall(p,html)
#     print (html)
#     print (pages)
#     for each in pages:
#         print (each)


def save_result(folder,result):
    pass

def download_table(folder='shanbei',pages=10):
    stopword=":q"
    file_content=""

    # f = open('word.txt','a')
    # url=book_content(url)\
    print("请输入内容【单独输入‘:q‘保存退出】输入目录网址如https://www.shanbay.com/wordlist/162217/414649/：")
    for line in iter(input,stopword):
        file_content=file_content+line+"\n"
    '''file_content = input('输入目录网址如https://www.shanbay.com/wordlist/162217/414649/：') #https://www.shanbay.com/wordlist/162217/414649/ '''

    d=r'(.*?ttps://.*)'
    urls=re.findall(d,file_content)
    print (urls)

    for each in urls:
        newurls=''.join(each)
        page_num = 10
        # urls = specific_url(url)

        # # os.mkdir(folder)
        # # os.chdir(folder)
        for i in range(pages):
             page_num=i
             page_url = newurls+'?page='+ str(page_num)
             print(page_url)
             x=find_table1(page_url)

    # f.close()

         # save_result(folder,result1)

if __name__== '__main__':
    download_table()
