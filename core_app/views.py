from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class HomePage(View):
    template_name: str = 'home.html'

    def get(self, request):
        users = User.objects.all().order_by('-pk')
        page = request.GET.get('page', 1)
        paginator = Paginator(users, 10)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            obj, created = User.objects.update_or_create(email=email)
            obj.f_name = f_name
            obj.l_name = l_name
            if created:
                random_string = get_random_string(10)
                obj.username = random_string
                obj.password = random_string
            obj.is_active = True
            obj.save()
            return redirect('core_app:home')
        except Exception as e:
            return redirect('core_app:home')