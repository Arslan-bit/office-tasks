from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def Signup(request):
      if request.method == 'POST':
          name = request.POST.get('fname')
          lname = request.POST.get('lname')
          email = request.POST.get('email')
          Cpassword = request.POST.get('apassword')
          pass1 = request.POST.get('password')
          user = request.POST.get('user').lower()

          if pass1 == Cpassword:
            user = User.objects.create_user(username=user,email=email,password=Cpassword)
            user.first_name = name
            user.last_name =  lname
            user.save()
            messages.success(request,'Your Account Successfully created ')
          else:
            messages.error(request,'Password not same ')
      else:
          pass    
      return render(request,'signup.html')


def Login(request):
      

  if request.method == 'POST':

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')

    else:
      messages.error(request,'username or password not correct')
      return redirect('login')
    
  else:
        pass

  return render(request,'login.html')



def change_password(request):
    if request.method == 'POST':
      username = request.POST['user']
      opassword = request.POST['opas']
      cpassword = request.POST['npas']
      acpassword = request.POST['anpas']

      if cpassword == acpassword:
        user = authenticate(request, username=username, password=opassword)
        if user is not None:
          u = User.objects.get(username=username)
          u.set_password(cpassword)
          u.save()
          return redirect('login')
        else:
            return messages.error(request,'password not same')
        
      else:
        return messages.error(request,'User Name and Password not same') 

    return render(request,'change.html')

  
        

       
def logout_view(request):
    logout(request)
    return redirect('home')
    # Redirect to a success page.
   


def forget_view(request):
      
  context={'data':'data'}
  return render(request,'forget.html',context)


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages #import messages
from django.conf import settings
import uuid 

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'http://127.0.0.1:8000',
					'site_name': 'Website Name',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': str(uuid.uuid4()),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("password_reset_done")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})
	