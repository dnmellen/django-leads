from django.conf.urls import patterns, url


from .views import IndexView, ThanksView

urlpatterns = patterns(
    '',

    # Index lead page
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks_register')
)
