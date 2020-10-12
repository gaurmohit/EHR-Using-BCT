from django.urls import path
from .views import some_users, download_data, add_process, get_status, download_finished
from .crud import urls as crud_urls
block_urls = [
    path('user-list/', some_users),
    path('download-finished/', download_finished),
    path('add-process/', add_process),
    path('status/', get_status)
]

block_urls.extend(crud_urls)
