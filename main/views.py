from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, UpdateView

from .forms import SignUpForm, StatementForm
from .models import Profile, Statement

# данная функция обрабатывает главную страницу страницу 
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                phone_number=form.cleaned_data.get('phone_number'),
                full_name=form.cleaned_data.get('full_name'),
                city=form.cleaned_data.get('city'),
            )
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/index.html',
                  {
                    'form': form,
                    'statements': Statement.objects.all()
                }
            )

def logout_view(request):
    logout(request)
    return redirect('/')

def create_statement(request):
    if request.method == 'POST':
        form = StatementForm(request.POST, user=request.user)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.save(user=request.user)
            return redirect('/')
    else:
        form = StatementForm(user=request.user)
    return render(request, 'main/create_statement.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')

class TaskDeleteView(DeleteView):
    model = Statement
    success_url = '/'
    template_name = 'main/delete.html'

class TaskUpdateView(UpdateView):
    model = Statement
    template_name = 'main/create_statement.html'
    form_class = StatementForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs