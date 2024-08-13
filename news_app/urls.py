from django.urls import path
from .views import news_list, news_detail, ContactPageView, errorPageView, HomePageView, \
    LocalNewsView, ForeignNewsView, TexnologyNewsView, SportNewsView, NewsDeleteView, \
    NewsUpdateView, NewsCreateView, admin_page_view, SearchResultsList

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news_slug>/', news_detail, name="news_detail_page"),
    path('news/<slug:slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug:slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('xatolik/', errorPageView, name='xatolik_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('texnology/', TexnologyNewsView.as_view(), name='texnology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),

]