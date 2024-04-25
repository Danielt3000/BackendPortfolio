
from django.urls import path, include
from .items import urls as urls2
from .posts import urls as urls3
from .reviews import urls as urls4



urlpatterns = [
    path('apps/item', include(urls2.urlpatterns) ),
    path('apps/posts', include(urls3.urlpatterns) ),
    path('apps/reviews',  include(urls4.urlpatterns)),

   
    
]
