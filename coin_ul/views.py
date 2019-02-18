from .models import Choice, Money
from django.views.generic.edit import FormView
from django.utils import timezone
from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


class SortFilter(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Имя и Фамилия...'}))
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'E-mail...'}))
    num = forms.IntegerField(initial=1, min_value=0, max_value=10000, label="Количество")
    description = forms.CharField(max_length=100,
                                  widget=forms.Textarea(attrs={'placeholder': 'Описание...', 'rows': 2}))


class Index(FormView):
    template_name = 'coin_ul/index.html'
    form_class = SortFilter
    success_url = '/'

    def form_valid(self, form):
        form = self.form_class(self.request.GET)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['contacts'] = Money.objects.get_queryset().order_by('id').filter(status='ЕСТЬ' or 'НЕТ')
        pk = self.request.GET.get('id')
        if pk:
            id = get_object_or_404(Money, pk=pk)
            context['id'] = id
        return context

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        num = int(self.request.POST.get('num'))
        text = self.request.POST.get('description')
        if not self.request.GET.get('id'):
            lot = Money.objects.get_queryset().order_by('id').filter(status='ЕСТЬ')[1]
            name = str(name) + ' ___default__'
        else:
            id = self.request.GET.get('id')
            lot = get_object_or_404(Money, pk=id)
        if num < 0:
            num = 1

        c = Choice(lot=lot, user=str(name), email=str(email),
                   choice_sum=num*lot.price, num=num, time=timezone.datetime.now(), description=text)
        c.save()
        return HttpResponseRedirect("/#contact")

# Create your views here.
