from django.conf.urls import patterns, url


from .views import IndexView

urlpatterns = patterns(
    '',

    # Index lead page
    url(r'^$', IndexView.as_view(), name='index')
)
