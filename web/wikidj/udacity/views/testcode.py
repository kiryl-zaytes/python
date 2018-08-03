__author__ = 'Administrator'
#class SignIn(FormView):
#    template_name = 'udacity/login_page.html'
#    form_class = AuthenticationForm
#    success_url = 'success.html'

    #def get(self, request):
    #    form = AuthenticationForm()
    #    return render(request, SignIn.template, {'form':form})
    #
    #def post(self, request):
    #    form = AuthenticationForm(data=request.POST)
    #    if form.is_valid():
    #        username = form.cleaned_data.get('username')
    #        password = form.cleaned_data.get('password')
    #        uauth = authenticate(username=username, password=password)
    #        if uauth.is_active:
    #            login(request, user=uauth)
    #            return HttpResponseRedirect('success.html')
    #        else:
    #            return HttpResponse('user is not active')
    #    else:
    #        form = AuthenticationForm()
    #        return render(request, SignIn.template, {'form': form})

#class Registration(FormView):
#    template_name = 'udacity/registration.html'
#    form_class = UserCreationForm
#    success_url = 'success.html'

    #def get(self, request):
    #    form = UserCreationForm()
    #    return render(request, Registration.template, {'form': form})
    #
    #def post(self, request):
    #    try:
    #        form = UserCreationForm(request.POST)
    #        if form.is_valid():
    #            form.save()
    #            return HttpResponseRedirect('success.html')
    #    except (AttributeError, ValueError):
    #        form = UserCreationForm()
    #        return render(request, Registration.template, {'form': form})
