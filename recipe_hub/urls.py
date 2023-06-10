from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls', namespace='recipes')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('recipes/', include('recipes.urls', namespace='recipes')),
     path('accounts/password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

   
]

# Add the following line to serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
