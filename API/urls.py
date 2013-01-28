from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'product/(?P<id>\d+)', 'API.views.getProduct'),
    url(r'grocerylist/(?P<id>\d+)', 'API.views.getGroceryList'),
    url(r'product/bought/(?P<products>(?:\w+/)+)', 'API.views.boughtProducts')

    )