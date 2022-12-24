from flask import Flask,render_template,request,jsonify
import pymysql,random
from flask_cors import CORS
import json
import requests
import re

from elasticsearch import Elasticsearch
es = Elasticsearch()

app = Flask(__name__)
CORS(app,supports_credentials=True)

#使json显示为中文
app.config['JSON_AS_ASCII'] = False

conn = pymysql.connect(host='rm-uf6q2j49y3xo8ny5hno.mysql.rds.aliyuncs.com',
                    port=3306,
                    user='music_root',
                    passwd='DIANgongdao123root',
                    db='netease',  
                    charset='utf8',
                cursorclass = pymysql.cursors.DictCursor)


#1.	按标签获取歌单函数
def getPlayListPlus(label, page, num = 35):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    cursor.execute('SELECT name,listid,listimage FROM taglist WHERE label LIKE %s LIMIT ' + str(num*(page-1)) +','+str(num) ,'%'+label+'%')
    result1 = cursor.fetchall()
    cursor.execute('SELECT COUNT(*) FROM taglist WHERE label LIKE %s ','%'+label+'%')
    result2 = [{'pages':int(cursor.fetchall()[0]['COUNT(*)'])//num}]
    result2+=result1
    return result2

#2.	按歌单id获取歌单信息
def queryList(listId):
    cursor = conn.cursor()
    cursor.execute('SELECT name,author,label,amount, views,description,ids FROM taglist WHERE listid LIKE %s',listId)
    result = cursor.fetchone()
    ids = result['ids'].split(',')
    #result['ids'] = [int(i) for i in ids]
    result2 = querySongs(ids)
    result['SongsData'] = result2
    #cursor.close()
    return result

#3.	按歌曲id获取歌曲信息
def querySong(songId):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    cursor.execute('SELECT songid,title,singer,album FROM songlist WHERE songid LIKE %s',songId)
    result = cursor.fetchone()
    #cursor.close()
    return result

#3.1	按歌曲ids获取歌曲信息
def querySongs(SongIds):
    conn.ping(reconnect=True)
    result = []
    for id in SongIds:
        temp = querySong(id)
        if (temp!=None):
            result.append(temp)
    return result

#3.2	按歌曲id获取歌曲信息
def querydetailSong(songId):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    cursor.execute('SELECT songid,title,singer,album,image,lyric FROM songlist WHERE songid LIKE %s',songId)
    result = cursor.fetchone()
    #cursor.close()
    return result

#4.	按歌曲名搜索

songMappings = {
        "mappings": {
            "properties": {
                "songid": {
                    "type": "long",
                },
                "title": {
                    "type": "text",
                }
            }
        }
    }

queryBySongName_cnt = 0

def queryBySongName_pre():
    queryBySongName_cnt = 1
    cursor = conn.cursor()
    cursor.execute('SELECT songid,title FROM songlist')
    result = cursor.fetchall()
    cursor.close()
    # print(result)
    result_len = len(result)

    if(es.indices.exists("querybysongname")):
        # print("querybysongname exists")
        es.indices.delete("querybysongname")

    res = es.indices.create(index='querybysongname', body=songMappings)

    for i in range(result_len):
        es.index(index="querybysongname", id=i,
                body={"songid" : result[i]["songid"],"title" : result[i]["title"]})
    ress = es.get(index="querybysongname", id=1, ignore=404)
    print(ress)

# json格式化显示函数
def json_print(string):
    print(json.dumps(string, sort_keys=True, indent=4, separators=(',', ':')))
    return

def queryBySongName(title):
    if(queryBySongName_cnt==0):
        queryBySongName_pre()
    query_title = {
        "query": {
        "match": {
          "title": title
        }
      }
    }
    raw_result = es.search(index="querybysongname", body=query_title)
    result = []
    for i in raw_result["hits"]["hits"]:
        result.append(i["_source"])
    return result


# queryBySongName("真的")

#5.	按歌单名搜索

listMappings = {
        "mappings": {
            "properties": {
                "listid": {
                    "type": "long",
                },
                "name": {
                    "type": "text",
                }
            }
        }
    }

queryByListName_cnt = 0
def queryByListName_pre():
    queryByListName_cnt = 1
    cursor = conn.cursor()
    cursor.execute('SELECT listid,name FROM taglist')
    result = cursor.fetchall()
    cursor.close()
    result_len = len(result)
    if(es.indices.exists(("querybylistname"))):
        es.indices.delete("querybylistname") #删除索引
    res = es.indices.create(index='querybylistname', body=listMappings)
    for i in range(result_len):
        es.index(index="querybylistname", id=i,
                body={"listid" : result[i]["listid"],"name" : result[i]["name"]})
    ress = es.get(index="querybylistname", id=1, ignore=404)
    print(ress)

def queryByListName(name):
    if(queryByListName_cnt==0):
        queryByListName_pre()
    query_name = {
        "query": {
            "match": {
                "name": name
                }
        }
    }
    raw_result = es.search(index="querybylistname", body=query_name)
    print(raw_result)
    result = []
    for i in raw_result["hits"]["hits"]:
        result.append(i["_source"])
    return result

@app.route("/gedans",methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        label = request.args.get('label')
        page = int(request.args.get('page'))
        #print('label is ' + label)
        data = getPlayListPlus(label,page)
        return jsonify(data)


@app.route("/list1/<int:id>",methods=['GET','POST'])
def hellolist1(id):
    #id = int(request.args.get('id'))
    data = queryList(id)
    print(data)
    return jsonify(data)


@app.route("/songs/<ids>")
def hellosongs(ids):
    ids = ids.split(',')
    ids = [int(i) for i in ids]
    print(ids)
    data = querySongs(ids)
    print(data)
    return jsonify(data)



@app.route("/song/<int:id>")
def hellosong(id):
    data = querySong(id)
    return jsonify(data)


@app.route("/querysong/<int:id>")
def hellodesong(id):
    data = querydetailSong(id)
    return jsonify(data)



@app.route("/zhuye",methods=['GET','POST'])
def getTopLists():
    cursor = conn.cursor()
    cursor.execute('select name,listid,listimage from taglist order by views desc limit 100')
    result1 = cursor.fetchall()
    result1=random.sample(result1,10)
    #print(result1)
    #print(len(result1))
    return jsonify(result1)

# wpy
@app.route("/geci/<string:music_id>",methods=['GET','POST'])
def lyric(music_id):
# music_id = input("请输入歌曲的id：")
#我们这里以周杰伦的“布拉格广场”为例，id=210049

  headers={"User-Agent" : "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 ",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "Connection" : "keep-alive",
    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}
  url = 'http://music.163.com/api/song/lyric?'+ 'id=' + music_id + '&lv=1&kv=1&tv=-1'

  r = requests.get(url,headers=headers,allow_redirects=False)
  #allow_redirects设置为重定向的参数

  #用js将获取的歌词源码进行解析
  json_obj = r.text#.text返回的是unicode 型的数据，需要解析
  j = json.loads(json_obj)#进行json解析
  words = j['lrc']['lyric'] #将解析后的歌词存在words变量中

  print(words)

  return jsonify(words)

@app.route("/search",methods=['GET','POST'])
def hello_list_search():
     if request.method == 'GET':
        search = request.args.get('search')
        #print('label is ' + label)
        data = queryByListName(str(search))
        print(data)
        return jsonify(data)
    
# wpy end

if __name__ == '__main__':
    app.run()