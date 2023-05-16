import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from payerLink.models import PayerLink
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import requests
def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=PayerLink.objects.filter().all()
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
    re=PayerLink.objects.get(id=id)
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
    re=PayerLink.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payerLink=PayerLink()
    try:
        payerLink.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        payerLink.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        payerLink.username=jsonData['username']
    except Exception:
        print("username is null")
    payerLink.create_time=now	
    payerLink.save()
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = PayerLink.objects.get(id=jsonData['id'])
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
        res1=PayerLink.objects.filter(name=search)
    else:
        res1=PayerLink.objects.filter()
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
def pay(request):
    jsonData = json.loads(request.body.decode())
    name=jsonData['name']
    reserve2=jsonData['reserve2']
    payNum=jsonData['payNum']
    re=PayerLink.objects.get(username=reserve2)
    headers = {'content-type': 'application/json'}
    ress=requests.post(re.link+"/fund/pay",data=request.body,headers=headers)
    res1=json.loads(ress.text)
    print(res1)
    return HttpResponse(content=json.dumps(res1, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def exitMoney(request):
    jsonData = json.loads(request.body.decode())
    name=jsonData['name']
    reserve2=jsonData['reserve2']
    payNum=jsonData['payNum']
    re=PayerLink.objects.get(username=reserve2)
    headers = {'content-type': 'application/json'}
    ress=requests.post(re.link+"/fund/exitMoney",data=request.body,headers=headers)
    res1=json.loads(ress.text)
    return HttpResponse(content=json.dumps(res1, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')