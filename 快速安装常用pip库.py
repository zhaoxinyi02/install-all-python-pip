import os # 导入os库
libs = {"requests","PySpider","Scrapy","Crawley","Portia","cola","newspaper","XlsxWriter","win32com","pymysql","pymongo","smtplib","selenium","pdfminer","PyPDF2","openpyxl",'python-docx','matplotlib','numpy','pyecharts','pandas','Scipy','Plotly','wordcloud','jieba','Django','Pyramid','Tornado','Flask','IPython','PTVS','pydub','TimeSide','dnspython','pygame','PyQt5','PIL','OpenCV','Py2exe','WeRoBot'} # 将需要安装的库名称放到列表中
for lib in libs:
        os.system("pip3 install "+lib)
