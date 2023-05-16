import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from bookuser.models import BookUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=BookUser.objects.filter().all()
    resList=[]
    for p in res:
        college = {}
        college['id'] =p.id
        college['cusAccount'] =p.cusAccount
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['cusId'] =p.cusId
        college['booBerth'] =p.booBerth
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['fliYfare'] =p.fliYfare
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
    re=BookUser.objects.get(id=id)
    newre={}
    newre['id'] =re.id
    newre['cusAccount'] =re.cusAccount
    newre['create_time'] =re.create_time
    newre['status'] =re.status
    newre['reserve1'] =re.reserve1
    newre['reserve2'] =re.reserve2
    newre['reserve3'] =re.reserve3
    newre['reserve4'] =re.reserve4
    newre['reserve5'] =re.reserve5
    newre['cusId'] =re.cusId
    newre['booBerth'] =re.booBerth
    newre['comCode'] =re.comCode
    newre['cusTelNumber'] =re.cusTelNumber
    newre['fliYfare'] =re.fliYfare
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
    re=BookUser.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bookUser=BookUser()
    try:
        bookUser.cusAccount=jsonData['cusAccount']
    except Exception:
        print("cusAccount is null")
    try:
        bookUser.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        bookUser.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        bookUser.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        bookUser.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        bookUser.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        bookUser.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        bookUser.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        bookUser.booBerth=jsonData['booBerth']
    except Exception:
        print("booBerth is null")
    try:
        bookUser.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        bookUser.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        bookUser.fliYfare=jsonData['fliYfare']
    except Exception:
        print("fliYfare is null")
    bookUser.create_time=now	
    bookUser.save()
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = BookUser.objects.get(id=jsonData['id'])
    try:
        re.cusAccount=jsonData['cusAccount']
    except Exception:
        print("cusAccount is null")
    try:
        re.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        re.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        re.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        re.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        re.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        re.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        re.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        re.booBerth=jsonData['booBerth']
    except Exception:
        print("booBerth is null")
    try:
        re.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        re.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        re.fliYfare=jsonData['fliYfare']
    except Exception:
        print("fliYfare is null")
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
        res1=BookUser.objects.filter(name=search)
    else:
        res1=BookUser.objects.filter()
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
        college['cusAccount'] =p.cusAccount
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['cusId'] =p.cusId
        college['booBerth'] =p.booBerth
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['fliYfare'] =p.fliYfare
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')