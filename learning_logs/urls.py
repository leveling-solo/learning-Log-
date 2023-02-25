from django.urls import  path
from learning_logs import views

urlpatterns = [
    path('', views.index , name ='index.html'),
    path('topics/',views.topics , name='topic.html'),
    path ('topics/<int:topic_id>/',views.topic ,name='topics.html'),
    path('new_topics/',views.new_topics,name = 'new_topics.html'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry.html'),
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry.html'),
    
]
