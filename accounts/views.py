from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from accounts.forms import UserSignUpViewForm
from accounts.forms import ProfileForm


class UserSignUpView(View):
    def get(self, request, *args, **kwargs):
        form1 = UserSignUpViewForm()
        form2 = ProfileForm()
        return render(request, 'accounts/signup.html', {'form1': form1, 'form2': form2})

    def post(self, request, *args, **kwargs):
        form1 = UserSignUpViewForm(request.POST)
        form2 = ProfileForm(request.POST)
        # print(form.cleaned_data) doesnot works as the forms needs to be valid first
        template_name = 'accounts/signup.html'
        if form1.is_valid() & form2.is_valid():
            print(form1.cleaned_data)  # works as the form is valid
            print(form2.cleaned_data)  # works as the form is valid
            user = form1.save(commit=False)
            profile = form2.save(commit=False)
            # profile.user_name = self.request.user
            # profile.user_name = form1
            print(form1)
            print(form1.cleaned_data['username'])
            raw_password = form1.cleaned_data.get('password1')
            print(raw_password)
            user.set_password(raw_password)
            print(user.password)
            user.save()
            profile.save()
            template_name = 'accounts/signup_success.html'
            name = form1.cleaned_data['username']
            return render(request, template_name, {'name':name})
        return render(request, template_name, {'form1': form1, 'form2': form2})

'''

How to pass form.cleaned_data using generic view ???

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