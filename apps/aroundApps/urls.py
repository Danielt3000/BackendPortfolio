
from django.urls import path, include
from .placesAround import urls as urls2
from .postsAround import urls as urls3
from .cat import urls as urls4



urlpatterns = [
    path('places/', include(urls2.urlpatterns) ),
    path('posts/', include(urls3.urlpatterns) ),
    path('categories/',  include(urls4.urlpatterns)),

   
    
]
