import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from custom.models import Custom
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=Custom.objects.filter().all()
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
        college['cusEmail'] =p.cusEmail
        college['cusId'] =p.cusId
        college['cusName'] =p.cusName
        college['cusNames'] =p.cusNames
        college['cusPwd'] =p.cusPwd
        college['cusSex'] =p.cusSex
        college['cusTelNumber'] =p.cusTelNumber
        college['seccode'] =p.seccode
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
    re=Custom.objects.get(id=id)
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
    newre['cusEmail'] =re.cusEmail
    newre['cusId'] =re.cusId
    newre['cusName'] =re.cusName
    newre['cusNames'] =re.cusNames
    newre['cusPwd'] =re.cusPwd
    newre['cusSex'] =re.cusSex
    newre['cusTelNumber'] =re.cusTelNumber
    newre['seccode'] =re.seccode
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
    re=Custom.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    custom=Custom()
    try:
        custom.cusAccount=jsonData['cusAccount']
    except Exception:
        print("cusAccount is null")
    try:
        custom.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        custom.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        custom.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        custom.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        custom.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        custom.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        custom.cusEmail=jsonData['cusEmail']
    except Exception:
        print("cusEmail is null")
    try:
        custom.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        custom.cusName=jsonData['cusName']
    except Exception:
        print("cusName is null")
    try:
        custom.cusNames=jsonData['cusNames']
    except Exception:
        print("cusNames is null")
    try:
        custom.cusPwd=jsonData['cusPwd']
    except Exception:
        print("cusPwd is null")
    try:
        custom.cusSex=jsonData['cusSex']
    except Exception:
        print("cusSex is null")
    try:
        custom.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        custom.seccode=jsonData['seccode']
    except Exception:
        print("seccode is null")
    custom.create_time=now	
    custom.save()
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = Custom.objects.get(id=jsonData['id'])
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
        re.cusEmail=jsonData['cusEmail']
    except Exception:
        print("cusEmail is null")
    try:
        re.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        re.cusName=jsonData['cusName']
    except Exception:
        print("cusName is null")
    try:
        re.cusNames=jsonData['cusNames']
    except Exception:
        print("cusNames is null")
    try:
        re.cusPwd=jsonData['cusPwd']
    except Exception:
        print("cusPwd is null")
    try:
        re.cusSex=jsonData['cusSex']
    except Exception:
        print("cusSex is null")
    try:
        re.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        re.seccode=jsonData['seccode']
    except Exception:
        print("seccode is null")
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
        res1=Custom.objects.filter(name=search)
    else:
        res1=Custom.objects.filter()
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
        college['cusEmail'] =p.cusEmail
        college['cusId'] =p.cusId
        college['cusName'] =p.cusName
        college['cusNames'] =p.cusNames
        college['cusPwd'] =p.cusPwd
        college['cusSex'] =p.cusSex
        college['cusTelNumber'] =p.cusTelNumber
        college['seccode'] =p.seccode
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def login(request):  # request是必须带的实例。类似class下方法必须带self一样    
    jsonData = json.loads(request.body.decode())
    res1=Custom.objects.filter(cusAccount=jsonData['cusAccount']).all()
    content={}
    if  len(res1)>0:
        res2=Custom.objects.filter(cusAccount=jsonData['cusAccount'],cusPwd=jsonData['cusPwd'])
        res3={
            "username":res1[0].cusAccount,
             "name":res1[0].cusName,
             "payPwd":  res1[0].reserve1
     

        }
        if len(res2)>0:
            content = {
                    'success': True,
                    'message': '登录成功',
                    'data':res3
                }
        else:
            content = {
                    'success': False,
                    'message': '密码错误'
                }
    else:
        content = {
                    'success': False,
                    'message': '用户不存在'
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')