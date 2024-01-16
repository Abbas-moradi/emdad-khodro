from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        all_user = User.objects.all()

        return render(request, self.template_name, {'users': all_user})


