from django.contrib import admin
from django.urls import path
from myapp.views import home_view, signup_view, login_view, validaciones_view, validacionsig_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup.html/', signup_view, name='signup'),
    path('login.html/', login_view, name='login'),
    path('validaciones_login.js/', validaciones_view, name='validacionlog'),
    path('validaciones_singup.js/', validacionsig_view, name='validacionsign'),
    path('registro_completo.html/', TemplateView.as_view(template_name='registro_completo.html'), name='registro_completo'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
