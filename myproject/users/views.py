from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .forms import UserRegisterForm, Newform


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class newForm(View):

    def __init__(self):

        super(newForm,self).__init__()

    def get(self,request):

        form = Newform()
        payload = {"form":form}

        return render(request,"users/newForm.html",payload)

    def post(self,request):

        order_type=request.POST.get('order_type')
        messages.success(request, f'Order created for {order_type}!')
        return redirect('blog-home')


