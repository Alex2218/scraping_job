from django.contrib import admin
from django.urls import path, include
from scraping.views import home_view, list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_view, name='list'),
    path('accounts_app/', include(('accounts_app.urls', 'accounts'))),
    path('', home_view, name='home'),

]
