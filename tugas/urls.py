from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.TugasDelete.as_view()), name='hapusTugas'),
    url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.delete_tugas), name='hapusTugas'),
    url(r'^(?P<pk>[0-9]+)/edit/$', login_required(views.TugasUpdate.as_view()), name='ubahTugas'),
    url(r'^add/$', login_required(views.TugasCreate.as_view()), name='tambahTugas'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.TugasDetailView.as_view()), name='detailTugas'),
    url(r'^ajx/$', login_required(views.TugasListJson.as_view()), name='tugas_list_json'),
    url(r'^$', TemplateView.as_view(template_name='tugas/tugas_ajax.html'), name='tugas'),
    # url(r'^$', login_required(views.TugasListView.as_view()), name='tugas'),
]
