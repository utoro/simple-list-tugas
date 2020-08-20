from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django_datatables_view.base_datatable_view import BaseDatatableView
from bootstrap_modal_forms.mixins import PassRequestMixin
# from django.utils.html import escape

from .models import Tugas
from .forms import TugasAddForm, TugasUpdateForm


class TugasListJson(BaseDatatableView):
    # The model we're going to show
    model = Tugas

    # define the columns that will be returned
    columns = ['mata_kuliah', 'judul', 'deadline', 'status', 'id']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['mata_kuliah', 'judul', 'deadline', 'status', '']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 100

    def get_initial_queryset(self):
        return Tugas.objects.filter(pemilik=self.request.user.id)

    # def render_column(self, row, column):
        # We want to render user as a custom column
        # if column == 'Judul':
            # escape HTML for security reasons
            # return 'nganu %s'.format(row.judul)
        # else:
            # return super(TugasListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(judul__icontains=search) | Q(mata_kuliah__icontains=search))

        # more advanced example using extra parameters
        filter_tugas = self.request.GET.get('q', None)

        if filter_tugas:
            tugas_parts = filter_tugas.split(' ')
            qs_params = None
            for part in tugas_parts:
                q = Q(Q(judul__icontains=part) | Q(mata_kuliah__icontains=part))
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs


class TugasListView(ListView):
    model = Tugas
    template_name = 'tugas/tugas.html'
    context_object_name = 'list_tugas'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            tugas = Tugas.objects.filter(pemilik=self.request.user.id)
            return tugas.filter(Q(judul__icontains=query) | Q(mata_kuliah__icontains=query)).distinct()
        else:
            return Tugas.objects.filter(pemilik=self.request.user.id)


class TugasDetailView(DetailView):
    model = Tugas
    template_name = 'tugas/detail_tugas.html'
    context_object_name = 'detail_tugas'

    def get_queryset(self):
        return Tugas.objects.filter(pemilik=self.request.user.id)


class TugasCreate(PassRequestMixin, SuccessMessageMixin, CreateView):
    form_class = TugasAddForm
    model = Tugas
    template_name = 'tugas/tambah_tugas.html'
    success_message = 'Success: Tugas berhasil ditambah.'
    success_url = reverse_lazy('tugas')

    def form_valid(self, form):
        form.instance.pemilik = self.request.user
        return super(TugasCreate, self).form_valid(form)


class TugasUpdate(UpdateView):
    form_class = TugasUpdateForm
    model = Tugas
    # fields = ['judul', 'mata_kuliah', 'deskripsi', 'jenis', 'status', 'deadline']
    template_name = 'tugas/ubah_tugas.html'
    success_url = reverse_lazy('tugas')

    def get_queryset(self):
        return Tugas.objects.filter(pemilik=self.request.user.id)



class TugasDelete(DeleteView):
    model = Tugas
    template_name = 'tugas/hapus_tugas.html'
    success_url = reverse_lazy('tugas')

    def get_queryset(self):
        return Tugas.objects.filter(pemilik=self.request.user.id)

def delete_tugas(request, pk):
    tugas = Tugas.objects.filter(pemilik=request.user.id)
    tugas = get_object_or_404(tugas, id=pk)
    tugas.delete()
    return HttpResponseRedirect(reverse_lazy("tugas"))
