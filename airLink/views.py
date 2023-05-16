import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from airLink.models import AirLink
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
airapis=["http://101.43.132.23:8001"]
def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=AirLink.objects.filter().all()
    resList=[]
    for p in res:
        college = {}
        college['id'] =p.id
        college['link'] =p.link
        college['name'] =p.name
        college['username'] =p.username
        resList.append(college)   
    content = {
                'success': True,
                'message': '查询成功',
                'data':resList
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def info(request):  # request是必须带的实例。类似class下方法必须带self一样  
    query_dict = request.GET
    id = query_dict.get('id')  
    re=AirLink.objects.get(id=id)
    newre={}
    newre['id'] =re.id
    newre['link'] =re.link
    newre['name'] =re.name
    newre['username'] =re.username
    content = {
                'success': True,
                'message': '查询成功',
                'data':newre
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def delete(request):  # request是必须带的实例。类似class下方法必须带self一样  
    query_dict = request.GET
    id = query_dict.get('id')  
    re=AirLink.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    airLink=AirLink()
    try:
        airLink.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        airLink.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        airLink.username=jsonData['username']
    except Exception:
        print("username is null")
    airLink.create_time=now	
    airLink.save()
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = AirLink.objects.get(id=jsonData['id'])
    try:
        re.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        re.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        re.username=jsonData['username']
    except Exception:
        print("username is null")
    re.save()
    content = {
                    'success': True,
                    'message': '修改成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def page(request):  # request是必须带的实例。类似class下方法必须带self一样   
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize']
    search = data['search']
    res1=[]
    if search:
        res1=AirLink.objects.filter(name=search)
    else:
        res1=AirLink.objects.filter()
        #Pagination
    total = res1.count()
    p = Paginator(res1, pagesize) # Show 10 contacts per page.
    page=[]
    try:
        page = p.page(pageNum)
    except PageNotAnInteger:
        page = p.page(pageNum)
    except EmptyPage:
        page = p.page(pageNum)
    resList=[]
    for p in page:
        college = {} 
        college['id'] =p.id
        college['link'] =p.link
        college['name'] =p.name
        college['username'] =p.username
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
#查询所有的航班
def airList(request):
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize'] 
    result =requestAirApi("/flight/page1",request.body)  #将请求的数据转换为json格式    
    return HttpResponse(content=json.dumps(result, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def requestAirApi(url,data):
    res=AirLink.objects.filter().all()    
    list=[]
    for airapi in res:
        # url = airapi+url  #api链接
        # print(url)
        headers = {'content-type': 'application/json'}
        wb_data = requests.post(airapi.link+url,data=data,headers=headers)  #引入requests库来请求数据
        result = wb_data.json()   #将请求的数据转换为json格式
        list=list+result['data']
    return list

