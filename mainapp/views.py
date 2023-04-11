from django.shortcuts import render , redirect
from .models import*
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth  import authenticate, logout
from django.contrib.auth  import login as auth_login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


# Create your views here.


def home(request):
    return render(request,'home_page.html')

def add_subject(request):
    if request.method == "POST":
        subject = request.POST['sname']
        discription = request.POST['discp']
        subject = Subject(  Subject_name  = subject  ,  Discription = discription )
        subject.save()
        messages.success(request,'Subject is succesfully added')
        return render(request,"add_Subject.html")
        
    
    return render(request,"add_Subject.html")

def add_topic(request):
    subject = Subject.objects.all()
    context = {'subject' : subject}
    if request.method == "POST":
        subject_data = request.POST['subject']
        topic = request.POST['topic']
        content = request.POST['content']
        subjects = Subject.objects.get(Subject_name = subject_data)
        topic = Topic(    subject  = subjects  , topic  =  topic ,   content =    content)
        topic.save()
        messages.success(request,'Topic is succesfully added')
        return render(request,"topic_add.html")
        
    
    return render(request,"topic_add.html" , context)


def show_subject(request):
    
    subject = Subject.objects.all()
    context = {'subject': subject }
    return render (request, 'show_subjects.html' , context)

def show_topic(request, id):
    topic = Topic.objects.filter(subject= id)
    context = {'topic':topic}
    return render (request, "topic_list.html" ,context)
def info(request):
    
    return render(request,'info.html')
               
               
def search(request):
    query = request.GET.get('q')
    results = None
    
    if query:
        results = Subject.objects.filter( Subject_name =query)
        print('ssss')
        print(results)
        context = {'results': results}
    return render(request, 'home_page.html', context )


def login(request):
       if request.method == "POST":
        # Get the post parameters
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  
        if user is not None:
           
            auth_login(request  , user)
            return redirect('/')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "login.html")
       return render(request, 'login.html')


def Userlogout(request):
    logout(request)
    return redirect('/login')


def  signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'signup.html')

        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'signup.html')
    
        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')

        # Create the user
        user = User.objects.create_user(username, email, password)
       
        user.save()
        # user.save()
        # current_site = get_current_site(request)
        # email_body = {
        #             'user': user,
        #             'domain': current_site.domain,
        #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #             'token': account_activation_token.make_token(user),
        #         }

        # link = reverse('activate', kwargs={
        #                        'uidb64': email_body['uid'], 'token': email_body['token']})

        # email_subject = 'Activate your account'

        # activate_url = 'http://'+current_site.domain+link

        # emailsend = EmailMessage(
        #             email_subject,
        #             'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
        #             'testingapp895@gmail.com',
        #             [email],
        #         )
        # emailsend.send(fail_silently=False)
        messages.success(request, "Your Account is created")
        return render(request, 'signup.html')
            
      
    return render(request, 'signup.html')

def revision(request):
 return render(request ,'revision.html')



def delete_subject(request , id):
    

    delete1 =  Subject.objects.get(pk=id)
    delete1.delete()
    messages.success(request, "Your content is successfully Deleted.")
    return redirect('/show_subject')