from django.urls import path
from tasks import views as tasks_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tasks_views.index, name='home'),
    path('', tasks_views.index.as_view(), name='home'),
    path('api/tasks/', tasks_views.task_list),
    path('api/tasks/<int:pk>/', tasks_views.task_detail),
    path('api/tasks/published/', tasks_views.task_list_published),
    path('api/tasks/completed/', tasks_views.task_list_completed)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)