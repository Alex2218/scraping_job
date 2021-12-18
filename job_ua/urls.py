from django.contrib import admin
from django.urls import path, include
from scraping.views import VacancyDelete, VacancyUpdate, home_view, list_view, \
    VacancyDetail, VacancyCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list_view, name='list'),
    path('accounts_app/', include(('accounts_app.urls', 'accounts'))),
    path('detail/<int:pk>/', VacancyDetail.as_view(), name='detail'),
    path('create/', VacancyCreate.as_view(), name='create'),
    path('update/<int:pk>/', VacancyUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', VacancyDelete.as_view(), name='delete'),
    path('', home_view, name='home'),

]
