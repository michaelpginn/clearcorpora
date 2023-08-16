from django import forms

from .models import Corpusobject

class PostForm(forms.ModelForm):

    class Meta:
        model = Corpusobject
        fields = ('name', 'catid', 'verbsaddress', 'language', 'project', 'knownloc', 'physical', 'downloadable', 'project')


# class SearchForm(forms.Form):
# 	q_name = forms.CharField(label='Corpus Name', max_length=30)
# 	q_variants_sku_cont = forms.CharField(label='Catalog Number', max_length=30)
# 	