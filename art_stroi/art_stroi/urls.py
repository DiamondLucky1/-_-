from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import permission_denied

from art_stroi import settings
from stock import views

handler403 = 'stock.views.permission_denied'

urlpatterns = [
    path('403/', views.permission_denied, name='permission_denied'),
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('main/', views.main, name='main'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('search/', views.product_search, name='product_search'),
    path('form/', views.purchase, name='form'),
    # path('report1/', views.make_report1, name='report1'), #На основе ф-нкции
    path('report1/', views.MakeReport1.as_view(), name='report1'),
    # path('report2/', views.MakeReport2.as_view(), name='report2'),
    path('report2/', views.make_report2, name='report2' ) #На основе ф-нкции
    # path('form/', views.Formpost.as_view(), name='form'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
