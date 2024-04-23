from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .forms import MainForm
from .models import Main


class Search(ListView):
    model = Main

    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Main.objects.filter(name__icontains=query)

        return object_list


def about(request):
    return render(request, 'about.html')


def admin(request):
    return render(request, 'admin.html')


def Home(request):
    #news = Main.objects.order_by('-id')
    news = Main.objects.all()
    return render(request, 'home.html', {'title': 'Кабинет заказчика', 'news': news})


def create (request):
    error=''
    if request.method =='POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма введена неправильно'

    form = MainForm()
    context = {
         'form': form,
         'error': error
    }
    return render(request, 'create.html', context)

