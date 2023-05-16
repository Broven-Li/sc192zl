from django.contrib import admin
from django.urls import path

from book import views as book
from bookuser import views as BookUser
from custom import views as custom
from payerLink import views as payerLink
from airLink import views as airLink
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'', TemplateView.as_view(template_name="index.html")),
    path('api/admin/', admin.site.urls),
    path('api/air/air/list',airLink.airList,name='upload'),#文件上传
    path('api/custom/info',custom.info,name='info'),#详情
    path('api/custom/delete',custom.delete,name='delete'),#删除
    path('api/custom/list',custom.list,name='list'),#查询所有
    path('api/custom/save',custom.save,name='save'),#新增
    path('api/custom/update',custom.update,name='update'),#修改
    path('api/custom/page',custom.page,name='pag'),#分页条件查询
    path('api/custom/login',custom.login,name='login'),#登录
    path('api/book/info',book.info,name='info'),#详情
    path('api/book/delete',book.delete,name='delete'),#删除
    path('api/book/list',book.list,name='list'),#查询所有
    path('api/book/save',book.save,name='save'),#新增
    path('api/book/update',book.update,name='update'),#修改
    path('api/book/page',book.page,name='pag'),#分页条件查询
    path('api/bookUser/info',BookUser.info,name='info'),#详情
    path('api/bookUser/delete',BookUser.delete,name='delete'),#删除
    path('api/bookUser/list',BookUser.list,name='list'),#查询所有
    path('api/bookUser/save',BookUser.save,name='save'),#新增
    path('api/bookUser/update',BookUser.update,name='update'),#修改
    path('api/bookUser/page',BookUser.page,name='pag'),#分页条件查询
    path('api/airLink/info',airLink.info,name='info'),#详情
    path('api/airLink/delete',airLink.delete,name='delete'),#删除
    path('api/airLink/list',airLink.list,name='list'),#查询所有
    path('api/airLink/save',airLink.save,name='save'),#新增
    path('api/airLink/update',airLink.update,name='update'),#修改
    path('api/airLink/page',airLink.page,name='pag'),#分页条件查询
    path('api/airLink/airList',airLink.airList,name='airList'),#分页条件查询payerLink/exitMoney
    path('api/payerLink/exitMoney',payerLink.exitMoney,name='exitMoney'),#分页条件查询
    path('api/payerLink/pay',payerLink.pay,name='pay'),#分页条件查询
    path('api/payerLink/info',payerLink.info,name='info'),#详情
    path('api/payerLink/delete',payerLink.delete,name='delete'),#删除
    path('api/payerLink/list',payerLink.list,name='list'),#查询所有
    path('api/payerLink/save',payerLink.save,name='save'),#新增
    path('api/payerLink/update',payerLink.update,name='update'),#修改
    path('api/payerLink/page',payerLink.page,name='pag'),#分页条件查询

]
