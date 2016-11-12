"""wakeup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import SimpleRouter
from ui.api import *
import inspect
#router = SimpleRouter()
#router.register('users',UserViewSet)
#router.register('session',SystemInfoViewSet)

def module_import(name):
    """
    If you need to import a module on the fly, this helper function assists
    you.  So say you want to import something like spam.eggs.are.cool, this
    will sort out the full import.
    """
    mod = __import__(name, globals(), locals(), [], -1)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('ui.urls')),
    url(r'^api/', include('api.urls')),
    #url(r'^api/v1/', include(router.urls))
]

module = module_import("ui")
for name, obj in inspect.getmembers(module):
    if name == 'dynamicurlpatterns':
        if len(obj) > 0:
            urlpatterns += obj
#urlpatterns += SystemInfoViewSet

urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
