from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .api_views import predict_chord
from . import api_views
from .views import chord

urlpatterns = [
    path('', views.home, name='home'),
    path('subscription/', views.subscription, name='subscription'),
    path('project/', views.project, name='project'),
    path('community/', views.community, name='community'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('chord/', chord, name='chord'),
    path('predict_chord/', api_views.predict_chord_api, name='predict_chord'),
    path('our_story/', views.our_story, name='our_story'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('faq/', views.faq, name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)