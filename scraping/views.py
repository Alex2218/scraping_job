from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from .models import Vacancy
from .forms import FindForm, VacancyForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView


def home_view(request):
    form = FindForm()
    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    context = {'city': city, 'language': language, 'form': form}
    if city or language:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if language:
            _filter['language__name'] = language

        qs = Vacancy.objects.filter(**_filter).select_related('city', 'language')
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)


class VacancyDetail(DetailView):
    queryset = Vacancy.objects.all()
    template_name = 'scraping/detail.html'


class VacancyCreate(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('home')


class VacancyUpdate(UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'scraping/create.html'
    success_url = reverse_lazy('home')


class VacancyDelete(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Запись успешно удалена.')
        return self.post(request, *args, **kwargs)
