from django import forms
from .models import Tugas
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class TugasAddForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Tugas
        fields = ['judul', 'mata_kuliah', 'deskripsi', 'jenis', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            # 'deadline': forms.DateInput(format='%Y/%m/%d', attrs={'class':'datepicker'}),
        }


class TugasUpdateForm(forms.ModelForm):
    class Meta:
        model = Tugas
        fields = ['judul', 'mata_kuliah', 'deskripsi', 'jenis', 'status', 'deadline']
        widgets = {
            # 'deadline': forms.DateInput(),
            # 'deadline': forms.DateInput(format='%Y/%m/%d', attrs={'class':'datepicker'}),
            'deadline': forms.DateInput(),
        }

