from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserSignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        # print(form.cleaned_data) doesnot works as the forms needs to be valid first
        template_name = 'accounts/signup.html'
        if form.is_valid():
            print(form.cleaned_data)  # works as the form is valid
            user = form.save(commit=False)
            raw_password = user.cleaned_data.get('password1')
            print(raw_password)
            user.set_password(raw_password)
            print(user.password)
            user.save()
            template_name = 'accounts/signup_success.html'
            name = form.cleaned_data['username']
            return render(request, template_name, {'name':name})
        return render(request, template_name, {'form':form})

'''


Alternative createview for signupform -- for learning purpose -- 

class UserSignUpCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # print(form_class.cleaned_data) this doesnot work
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        obj = form.cleaned_data
        print(obj['username'])
        form.save()
        return super(UserSignUpCreateView, self).form_valid(form)


'''