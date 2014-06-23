from django.shortcuts import HttpResponse, render_to_response,  get_object_or_404
from django.template import RequestContext, loader, Context
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, mail_admins
from django.contrib.auth.decorators import login_required

# import the models here
from django.contrib.auth.models import User
from webapp.models import Contributor, Reviewer, Subject ,Comment


# import the forms here
from webapp.forms import ContributorForm , ReviewerForm, UserForm, ContributorUploadForm, CommentForm


def index(request):
    """
    Argument:

    `REQUEST`: Request from client.

    This function takes the request of client and direct it to home page.
    """
    context = RequestContext(request)
    latest_uploads = Subject.objects.filter(review__gte = 3).order_by('-uploaded_on')[:3]
    print latest_uploads.query
    # print request.user.username
    context_dict = {'latest_uploads': latest_uploads,
    } 
    return render_to_response("webapp/index.html", context_dict, context)


def about(request):
    """
    Argument:
    
    `REQUEST`: This is the brief description about the site.
    """
    context = RequestContext(request)
    return render_to_response('about.html', context)


def userlogin(request):
    """
    Argument:

    `REQUEST` : Request from the user to login
    """
   
    context = RequestContext(request)
    if request.user.is_authenticated():
	return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    u=User.objects.get(username=user.username)
                    if Contributor.objects.filter(user=u):
                        login(request,user)
                        return HttpResponseRedirect('/contributor/profile/')
                       
                    elif Reviewer.objects.filter(user=u):
           		login(request,user)
			return HttpResponseRedirect('/reviewer/profile/')
		    elif user.username == 'admin':
			login(request,user)
			return HttpResponseRedirect('/admin')
	        else:
                    # An inactive account was used - no logging in!
                    messages.info(request, "Your account is disabled.")
		    return render_to_response('webapp/login.html', context)
            else:
                # Bad login details were provided. So we can't log the user in.
                messages.error(request, "Bad login!")
                return render_to_response('webapp/login.html', context)
        else:
            return render_to_response('webapp/login.html', context)


def contributor_profile(request):
    """
    Arguments:

    `REQUEST` : Request from user
   
    `CONTRI_USERNAME` : Username of the contributor logged in
	
    This function takes the request of user and direct it to profile page.
    """
    context = RequestContext(request)
    contributor= Contributor.objects.get(user=request.user)
    uploads = Subject.objects.values_list('class_number__class_number',flat=True).filter(contributor__user=request.user).distinct()  
    context_dict = {'uploads': uploads,'contributor':contributor}	     
    return render_to_response('contributor.html', context_dict, context)


def contributor_profile_subject(request,class_num):
    """
    Arguments:

    `REQUEST`: Request from user
    
    `CONTRI_USERNAME`: Username of the contributor logged in
    
    `CLASS_NUM` : Class in which the logged in contributor has contributed
    
    This function takes the request of user and direct it to profile page which consists of his contributions in a specific class.
    """
    context = RequestContext(request)
    contributor= Contributor.objects.get(user=request.user)
    uploads = Subject.objects.values_list('name',flat=True).filter(class_number__class_number=class_num).filter(contributor__user=request.user).distinct()
    context_dict = {'uploads': uploads, 'class_num':class_num, 'contributor':contributor}
    return render_to_response('contributor_subject.html', context_dict, context)


def contributor_profile_topic(request,class_num,sub):
    """
    Arguments:

    `REQUEST`: Request from user
    
    `CONTRI_USERNAME`: Username of the contributor logged in
    
    `CLASS_NUM`: Class in which the logged in contributor has contributed
    
    `SUB`: Subject in which the logged in contributor has contributed
    
    This function takes the request of user and direct it to profile page which consists of his contributions in a 
    specific subject of a  specific class.
    """
    context = RequestContext(request)
    contributor= Contributor.objects.get(user=request.user)
    uploads = Subject.objects.filter(class_number__class_number=class_num).filter(name=sub).filter(contributor__user=request.user)
    context_dict = {'uploads': uploads, 'class_num':class_num, 'sub':sub,'contributor':contributor}
    return render_to_response('contributor_topic.html', context_dict, context)


def contributor_profile_comment(request,class_num,sub,topics,id):
    """
    Arguments:
	
    `REQUEST`: Request from user
    
    `CONTRI_USERNAME`:  Username of the contributor logged in
    
    `CLASS_NUM`: Class in which the logged in contributor has contributed
    
    `SUB`: Subject in which the logged in contributor has contributed
    
    `TOPIC`: Subject topic in which the logged in contributor has contributed
    
     This function takes the request of user and direct it to profile page which consists of his comments of reviewer on a 
     specific subject of a  specific class. 
    """	
    context = RequestContext(request)
    contributor= Contributor.objects.get(user=request.user)
    comment = Comment.objects.filter(subject_id=id)
    context_dict = {'comment': comment, 'class_num':class_num, 'sub':sub,'topics':topics,'id':id,'contributor':contributor}
    return render_to_response('contributor_comment.html', context_dict, context)


def contributor_profile_topic_detail(request,class_num,sub,topics,id):
    """
    Arguments:

    `REQUEST`: Request from user.

    `CLASS_NUM` : Class in which the logged in contributor has contributed.

    `SUB` : Subject in which the logged in contributor has contributed.

    `TOPICS` : Subject topic in which the logged in contributor has contributed.

    `ID` : Id of the subject in which the logged in contributor has contributed.

    This function takes the request of user and direct it to profile page which consists of his comments of reviewer on a specified topic of a subject of a specific class.
    """
    context = RequestContext(request)
    contributor= Contributor.objects.get(user=request.user)
    subject = Subject.objects.get(id=id)
    context_dict = {'subject': subject, 'class_num':class_num, 'sub':sub,'contributor':contributor,'topics':topics,'id':id}
    return render_to_response('contributor_topic_detail.html', context_dict, context)


def reviewer_profile_topic_detail(request,class_num,sub,topics,id):
    """
    Arguments:

    `REQUEST`: Request from user.

    `CLASS_NUM` : Class in which the logged in contributor has contributed.

    `SUB` : Subject in which the logged in contributor has contributed.

    `TOPICS` : Subject topic in which the logged in contributor has contributed.

    `ID` : Id of the subject in which the logged in contributor has contributed.

    This function takes the request of user and direct it to profile page which consists of his comments of reviewer on a specified topic of a subject of a specific class.
    """
    context = RequestContext(request)
    reviewer= Reviewer.objects.get(user=request.user)
    subject = Subject.objects.get(pk=id)
    context_dict = {'subject': subject, 'class_num':class_num, 'sub':sub,'reviewer':reviewer,'topics':topics,'id':id}
    return render_to_response('reviewer_topic_detail.html', context_dict, context)


@login_required
def reviewer_profile(request):
    """
    Arguments:

    `REQUEST`: Request from user

    This function takes the request of user and directs it to the profile page.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    uploads = Subject.objects.values_list('class_number__class_number',flat=True).filter(review__lt = 3).distinct()
    context_dict = {'uploads' : uploads , 'reviewer':reviewer}
    return render_to_response("reviewer.html",context_dict,context)


def reviewer_profile_subject(request,class_num):
    """
    Arguments:

    `REQUEST`: Request from user
    
    `REV_USERNAME` : Username of the contributor logged in
    
    `CLASS_NUM` : Class in which the contributor has contributed.
    
    This function takes the request of user and direct it to the profile page which consists of the contributor's contributions in a specific class.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    uploads = Subject.objects.values_list('name',flat=True).filter(class_number__class_number=class_num).filter(review__lt = 3).distinct()
	
    context_dict = {'uploads': uploads, 'class_num':class_num,'reviewer':reviewer}
    return render_to_response('reviewer_subject.html', context_dict, context)


def reviewer_profile_topic(request,class_num,sub):
    """
    Arguments:

    `REQUEST`: Request from user
    
    `REV_USERNAME` : Username of the reviewer logged in
    
    `CLASS_NUM` : Class in which the contributor has contributed
    
    `SUB` : subject in which the contributor has contributed
    
    This function takes the request of user and directs it to the profile page which consists of the contributor's contributions in a specific subject of a specific class.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user=request.user)
    if request.POST:
	print request
	subject = get_object_or_404(Subject, id=request.POST['id'])
	subject.increment_review()
	subject.reviewer.add(reviewer)
	print "reviewer has reviewed"
	print subject.review
	print subject.id
    uploads = Subject.objects.filter(class_number__class_number=class_num).filter(name=sub).filter(review__lt = 3)
    context_dict = {'uploads': uploads, 'class_num':class_num, 'sub':sub,'reviewer':reviewer}
    return render_to_response('reviewer_topic.html', context_dict, context)


def reviewer_profile_comment(request,class_num,sub,topics,id):
    """
    Arguments:

    `REQUEST`: Request from user
    
    `REV_USERNAME` : Username of the reviewer logged in
    
    `CLASS_NUM` : Class in which the contributor has contributed
    
    `SUB` : subject in which the contributor has contributed
    
    `TOPIC` : Topic on which reviewer commented
    
    `ID` : Id of the reviewer
    
    This function takes the request of user and directs it to the profile page which consists of the contributor's contributions in a specific subject of a specific class.
    """
    context = RequestContext(request)
    comment = Comment.objects.filter(subject_id = id)
    reviewer = Reviewer.objects.get(user = request.user)
    if request.method == 'POST':
	print  "we have a new comment"
	comment_form = CommentForm(data = request.POST)
	if comment_form.is_valid():
	    comments = comment_form.save(commit=False)
	    subject = Subject.objects.get(pk = id)
	    comments.subject = subject
	    comments.user = reviewer
	    comments.save()
	    url = reverse('webapp.views.reviewer_profile_comment', kwargs={
	        'class_num' : class_num ,'sub':sub,'topics':topics,'id':id}
	    )
            return HttpResponseRedirect(url) 
	else:
	    if comment_form.errors:
		print comment_form.errors
    else:	
	comment_form = CommentForm()
        context_dict = {'comment_form': comment_form,
        'comment' : comment,'reviewer':reviewer}
	return render_to_response("reviewer_comment.html",context_dict,context)


def reviewer_past_approvals(request):
    """
    Argument:

    `REQUEST`: Request from contributor to sign up
    
    This function takes the request of user and directs it to the profile page which consists of the reviewer's past approvals.
    """
    context = RequestContext(request)
    reviewer = Reviewer.objects.get(user = request.user)
    subject = Subject.objects.all().order_by('-uploaded_on')
    context_dict = { 'subject':subject ,'reviewer':reviewer }
    return render_to_response("reviewer_past_approvals.html",context_dict,context)


def contributor_signup(request):
    """
    Argument:

    `REQUEST`: Request from contributor to sign up
    
    This function is used for a new contributor to sign up.
    """
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        print "we have a request to register"    
	user_form = UserForm(data=request.POST)
        contributor_form = ContributorForm(data=request.POST)
	if user_form.is_valid() and contributor_form.is_valid():
	    user = user_form.save()
            print "Forms are Valid"
            print user.username
            print user.first_name
            user.set_password(user.password)
	    user.is_active = False
            user.save()
            contributor = contributor_form.save(commit=False)
            contributor.user = user
            if 'picture' in request.FILES:
            	contributor.picture = request.FILES['picture']
	    if 'validation_docs' in request.FILES:
	        contributor.validation_docs=request.FILES['validation_docs']
            contributor.save()                       
            registered = True
            email_subject="New Contributor has registered"
	    email_message="""
New Contributor has registered.
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """
Waiting for your your approval"""
#send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com', ['pri.chundawat@gmail.com'],fail_silently=False)
            messages.success(request,"Form successfully submitted. Waiting for activation  from admin.")
	    return HttpResponseRedirect(reverse('webapp.views.contributor_signup'))
	else:
	    if contributor_form.errors or user_form.errors:
		print user_form.errors, contributor_form.errors
    else:
        contributor_form = ContributorForm()
	user_form = UserForm()
    context_dict = {'user_form':user_form, 'contributor_form': contributor_form, 'registered': registered}
    return render_to_response('webapp/contributor_signup.html', context_dict, context)


def reviewer_signup(request):
    """
    Argument:

    `REQUEST`: Request from reviewer to sign up
    
    This function is used for a new revieweer to sign up.
    
    """
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        print "we have a request to register"    
	user_form = UserForm(data=request.POST)
	reviewer_form = ReviewerForm(data=request.POST)
	if user_form.is_valid() and reviewer_form.is_valid():
	    user = user_form.save()
            print "Forms are Valid"
            print user.username
            print user.first_name
            user.set_password(user.password)
            user.is_active = False
            user.save()
            reviewer = reviewer_form.save(commit=False)
            reviewer.user = user
            if 'picture' in request.FILES:
  	        reviewer.picture = request.FILES['picture']
	    reviewer.save()                       
	    registered = True
            email_subject="New reviewer has registered"
	    email_message="""
New reviewer has registered.
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """
Waiting for your your approval"""
	    #send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com', ['pri.chundawat@gmail.com'],fail_silently=False)
	    messages.success(request,"form successfully submitted. Waiting for activation  from admin.")
	    return HttpResponseRedirect(reverse('webapp.views.reviewer_signup'))
	else:
            if reviewer_form.errors or user_form.errors:
		print user_form.errors, reviewer_form.errors
    else:
	reviewer_form = ReviewerForm()
        user_form = UserForm() 

    context_dict = {
	'user_form' : user_form,
        'reviewer_from' : reviewer_form,
	'registered' : registered,
    } 
    return render_to_response('webapp/reviewer_signup.html', context_dict, context) 


def user_logout(request):
    """
    Argument:

    `REQUEST`: Request from user to log out

    This function is used for logging out.
    
    """
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')
	

def commentpost(request):
    """
    Argument:

    `REQUEST`: This redirects the comments to comments.html page
    
    """
    return render_to_response('templates/comments.html')


def contributor_upload(request):
    """
    Argument:

    `REQUEST`: Request from contributor for a new upload   

     This function is used to upload a new file by contributor.
    """
    context = RequestContext(request)
    uploaded= False
    if request.POST:
        print "we have a request for upload by the contributor"
        contributor_upload_form = ContributorUploadForm(request.POST,
                                                        request.FILES)
        if contributor_upload_form.is_valid():
            print "Forms is valid"
            subject=contributor_upload_form.save(commit=False)
            # contri=Contributor.objects.get(user_id=id)
            if ( 'pdf' not in request.FILES and  'video' not in request.FILES and 'animantion' not in request.FILES):		 
	    	# Bad upload details were provided.
            	messages.error(request, "need to provide atleast one upload")
		contributor_upload_form = ContributorUploadForm()
		context_dict = {
	        'contributor_upload_form': contributor_upload_form,
	        'uploaded': uploaded
   		}
		return render_to_response("upload.html", context_dict, context)
	    else:	
	    	if 'pdf' in request.FILES:
                	subject.pdf=request.FILES['pdf']
         	if 'video' in request.FILES:
               		 subject.video = request.FILES['video']
           	if 'animation' in request.FILES:
               		 subject.animation = request.FILES['animation']
	    contributor = Contributor.objects.get(user=request.user)
            subject.contributor=contributor

            subject.save()
            uploaded = True
            contributor_name = request.user.username
            return HttpResponseRedirect('/contributor/profile/')
        else:
            if contributor_upload_form.errors:
                print contributor_upload_form.errors
    else:
        # empty form
        contributor_upload_form = ContributorUploadForm()

    context_dict = {
        'contributor_upload_form': contributor_upload_form,
        'uploaded': uploaded
    }

    return render_to_response("upload.html", context_dict, context)

	
@login_required
def contributor_profile_edit(request):
    """
    Argument:

    `REQUEST`: Contributor to edit his profile
    
    Edit user's/Coordinators profile.
    
    """
    context = RequestContext(request)
    print request.user
    user = get_object_or_404(User, username=request.user)
    old_username = user.username
    print user.first_name
    print user.last_name
    contributor = get_object_or_404(Contributor, user=request.user)
    if request.method == 'POST':
        print "We've a request to register"
        contributorform = ContributorForm(data=request.POST, instance=contributor)
        userform = UserForm(data=request.POST, instance=user)
        if contributorform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            if old_username != user.username:
                messages.error(request,'Username cant be changed')
                context_dict = {'contributorform': contributorform,
                    			'userform': userform}
                return render_to_response('contributor_profile_edit.html', context_dict, context)
            user.set_password(user.password)
            user.save()
            contributor = contributorform.save(commit=False)
            if 'picture' in request.FILES:
                contributor.picture = request.FILES['picture']
            contributor.user = User.objects.get(username=user.username)
            contributor.save()

            
            messages.success(request, "Profile updated successfully.")
            return render_to_response("edit_success.html",context)
        else:
            if contributorform.errors or userform.errors:
                print contributorform.errors, userform.errors
    else:
        contributorform = ContributorForm(instance=contributor)
        userform = UserForm(instance=user)
    context_dict = {'contributorform': contributorform,'userform': userform}
    return render_to_response('contributor_profile_edit.html', context_dict, context)


@login_required
def reviewer_profile_edit(request):
    """
    Argument:

    `REQUEST`: Reviewer to edit his profile
    
    Edit user's/Reviewer's profile.
    """
    context = RequestContext(request)
    print request.user
    user = get_object_or_404(User, username=request.user)
    old_username = user.username
    print user.first_name
    print user.last_name
    reviewer = get_object_or_404(Reviewer, user=request.user)
    if request.method == 'POST':
        print "We've a request to register"
        reviewerform = ReviewerForm(data=request.POST, instance=reviewer)
        userform = UserForm(data=request.POST, instance=user)
        if reviewerform.is_valid() and userform.is_valid():
            print "Forms are Valid"
            user = userform.save(commit=False)
            if old_username != user.username:
                messages.error(request,'Username cant be changed')
                context_dict = {'reviewerform': reviewerform,
                    			'userform': userform}
                return render_to_response('reviewer_profile_edit.html', context_dict, context)
            user.set_password(user.password)
            user.save()
            reviewer = reviewerform.save(commit=False)
            if 'picture' in request.FILES:
                reviewer.picture = request.FILES['picture']
            reviewer.user = User.objects.get(username=user.username)
            reviewer.save()         
            messages.success(request, "Profile updated successfully.")
            return render_to_response("edit_success.html",context)
        else:
            if reviewerform.errors or userform.errors:
                print reviewerform.errors, userform.errors
    else:
	print "ELSE"
        reviewerform = ReviewerForm(instance=reviewer)
        userform = UserForm(instance=user)

    context_dict = {'reviewerform': reviewerform,
                    'userform': userform}
    return render_to_response('reviewer_profile_edit.html', context_dict, context)


def content(request):
    """
    Argument:

    `REQUEST`: This requests the particular content. 
    """
    context=RequestContext(request)
    contributor= Contributor.objects.all()
    uploads = Subject.objects.all().filter(review__gte = 3).order_by('class_number')
    count = len(uploads)
    print count
    context_dict = {
	'uploads': uploads,
	'count':count,
        'contributor':contributor
    }
    return render_to_response('content.html',context_dict,context)


def search(request):
	context = RequestContext(request)
	try:
		user = User.objects.get(username=request.user.username)
	except:
		user = None
	query = request.GET['q']
	results_topic = Subject.objects.filter(topic__icontains=query).filter(review__gte = 3).order_by('class_number')
	results_name = Subject.objects.filter(name__icontains=query).filter(review__gte = 3).order_by('class_number')
	template = loader.get_template('search.html')
	context = Context({'query':query ,
	 'results_topic':results_topic,
	  'results_name':results_name,
	  'user':user})
	response = template.render(context)
	return HttpResponse(response)


def edit_success(request):
    """
    Argument:

    `REQUEST`: This function redirects the page to edit_success.html page.
    
    Editing user's/Reviewer's profile is successful.
    """
    return render_to_response('edit_success.html')

