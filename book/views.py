import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from book.models import Book
from bookuser.models import BookUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=Book.objects.filter().all()
    resList=[]
    for p in res:
        college = {}
        college['id'] =p.id
        college['booAAddress'] =p.booAAddress
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['booAtime'] =p.booAtime
        college['Column1'] =p.Column1
        college['booFare'] =p.booFare
        college['booNo'] =p.booNo
        college['booNumber'] =p.booNumber
        college['booOrderNum'] =p.booOrderNum
        college['booTime'] =p.booTime
        college['boobAddress'] =p.boobAddress
        college['boobTime'] =p.boobTime
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['flag'] =p.flag
        college['flagPay'] =p.flagPay
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
    re=Book.objects.get(id=id)
    newre={}
    newre['id'] =re.id
    newre['booAAddress'] =re.booAAddress
    newre['create_time'] =re.create_time
    newre['status'] =re.status
    newre['reserve1'] =re.reserve1
    newre['reserve2'] =re.reserve2
    newre['reserve3'] =re.reserve3
    newre['reserve4'] =re.reserve4
    newre['reserve5'] =re.reserve5
    newre['booAtime'] =re.booAtime
    newre['Column1'] =re.Column1
    newre['booFare'] =re.booFare
    newre['booNo'] =re.booNo
    newre['booNumber'] =re.booNumber
    newre['booOrderNum'] =re.booOrderNum
    newre['booTime'] =re.booTime
    newre['boobAddress'] =re.boobAddress
    newre['boobTime'] =re.boobTime
    newre['comCode'] =re.comCode
    newre['cusTelNumber'] =re.cusTelNumber
    newre['flag'] =re.flag
    newre['flagPay'] =re.flagPay
    res=BookUser.objects.filter(reserve1=id).all()
    resList=[]
    for re in res:
        college = {}
        college['cusTelNumber'] =re.cusTelNumber
        college['cusId'] =re.cusId
        college['booBerth'] =re.booBerth
        college['fliYfare'] =re.fliYfare
        college['comCode'] =re.comCode
        college['cusAccount'] =re.cusAccount
        resList.append(college) 
    newre['persions'] =resList

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
    re=Book.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    book=Book()
    try:
        book.booAAddress=jsonData['booAAddress']
    except Exception:
        print("booAAddress is null")
    try:
        book.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        book.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        book.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        book.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        book.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        book.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        book.booAtime=jsonData['booAtime']
    except Exception:
        print("booAtime is null")
    try:
        book.Column1=jsonData['Column1']
    except Exception:
        print("Column1 is null")
    try:
        book.booFare=jsonData['booFare']
    except Exception:
        print("booFare is null")
    try:
        book.booNo=jsonData['booNo']
    except Exception:
        print("booNo is null")
    try:
        book.booNumber=jsonData['booNumber']
    except Exception:
        print("booNumber is null")
    try:
        book.booOrderNum=jsonData['booOrderNum']
    except Exception:
        print("booOrderNum is null")
    try:
        book.booTime=jsonData['booTime']
    except Exception:
        print("booTime is null")
    try:
        book.boobAddress=jsonData['boobAddress']
    except Exception:
        print("boobAddress is null")
    try:
        book.boobTime=jsonData['boobTime']
    except Exception:
        print("boobTime is null")
    try:
        book.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        book.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        book.flag=jsonData['flag']
    except Exception:
        print("flag is null")
    try:
        book.flagPay=jsonData['flagPay']
    except Exception:
        print("flagPay is null")
    book.create_time=now	
    book.save()
    pserions=jsonData['persions']
    for per in pserions:
        bookuser=BookUser()        
        bookuser.cusAccount=per['cusAccount']
        bookuser.cusId=per['cusId']
        bookuser.booBerth=per['booBerth']
        bookuser.comCode=per['comCode']
        bookuser.fliYfare=per['fliYfare']
        bookuser.cusTelNumber=per['cusTelNumber']
        bookuser.reserve1=book.id
        bookuser.save()

    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = Book.objects.get(id=jsonData['id'])
    try:
        re.booAAddress=jsonData['booAAddress']
    except Exception:
        print("booAAddress is null")
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
        re.booAtime=jsonData['booAtime']
    except Exception:
        print("booAtime is null")
    try:
        re.Column1=jsonData['Column1']
    except Exception:
        print("Column1 is null")
    try:
        re.booFare=jsonData['booFare']
    except Exception:
        print("booFare is null")
    try:
        re.booNo=jsonData['booNo']
    except Exception:
        print("booNo is null")
    try:
        re.booNumber=jsonData['booNumber']
    except Exception:
        print("booNumber is null")
    try:
        re.booOrderNum=jsonData['booOrderNum']
    except Exception:
        print("booOrderNum is null")
    try:
        re.booTime=jsonData['booTime']
    except Exception:
        print("booTime is null")
    try:
        re.boobAddress=jsonData['boobAddress']
    except Exception:
        print("boobAddress is null")
    try:
        re.boobTime=jsonData['boobTime']
    except Exception:
        print("boobTime is null")
    try:
        re.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        re.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        re.flag=jsonData['flag']
    except Exception:
        print("flag is null")
    try:
        re.flagPay=jsonData['flagPay']
    except Exception:
        print("flagPay is null")
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
    air = data['air']
    res1=[]
    if search:
        res1=Book.objects.filter(reserve1=search)
    elif air:
         res1=Book.objects.filter(reserve4=air)
    else:
        res1=Book.objects.filter()
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
        college['booAAddress'] =p.booAAddress
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['booAtime'] =p.booAtime
        college['Column1'] =p.Column1
        college['booFare'] =p.booFare
        college['booNo'] =p.booNo
        college['booNumber'] =p.booNumber
        college['booOrderNum'] =p.booOrderNum
        college['booTime'] =p.booTime
        college['boobAddress'] =p.boobAddress
        college['boobTime'] =p.boobTime
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['flag'] =p.flag
        college['flagPay'] =p.flagPay
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')