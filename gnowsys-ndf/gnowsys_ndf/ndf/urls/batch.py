from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.batch',
                       url(r'^$', 'batch', name='batch'),
                       url(r'^/create$', 'create_and_edit', name='create'),
                       url(r'^/edit/(?P<_id>[\w-]+)$', 'create_and_edit', name='edit'),
                       url(r'^/save$', 'save_and_update', name='save'),
                       )
