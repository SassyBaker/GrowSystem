from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Grow Control Panel'
admin.site.index_title = 'Grow System'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),

    path('auth/', include('djoser.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
