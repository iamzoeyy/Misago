from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from misago.threads.views.labelsadmin import (LabelsList, NewLabel,
                                              EditLabel, DeleteLabel)


class MisagoAdminExtension(object):
    def register_urlpatterns(self, urlpatterns):
        # Threads Labels
        urlpatterns.namespace(r'^labels/', 'labels', 'categories')
        urlpatterns.patterns('categories:labels',
            url(r'^$', LabelsList.as_view(), name='index'),
            url(r'^new/$', NewLabel.as_view(), name='new'),
            url(r'^edit/(?P<label_id>\d+)/$', EditLabel.as_view(), name='edit'),
            url(r'^delete/(?P<label_id>\d+)/$', DeleteLabel.as_view(), name='delete'),
        )

    def register_navigation_nodes(self, site):
        site.add_node(name=_("Thread labels"),
                      icon='fa fa-tags',
                      parent='misago:admin:categories',
                      after='misago:admin:categories:nodes:index',
                      namespace='misago:admin:categories:labels',
                      link='misago:admin:categories:labels:index')
