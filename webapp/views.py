from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, mail_admins
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# import the models here
from django.contrib.auth.models import User
from webapp.models import Contributor, Reviewer, Subject ,Comment


# import the forms here
from webapp.forms import ContributorForm , ReviewerForm, UserForm, ContributorUploadForm, CommentForm

def index(request):
    """
    Argument:
    -`REQUEST`:request from user

    This function takes the request of user and direct it to home page.
    """
    return render_to_response("webapp/index.html")

def userlogin(request):
    """Login form, Enables the user to login after successful sign-up.
    
    Arguments:
    	REQUEST
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user1 = authenticate(username=username, password=password)

        if user1 is not None:
            # Is the account active? It could have been disabled.
            if user1.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
		u=User.objects.get(username=user1.username)
		if Contributor.objects.filter(user=u):		
			login(request,user1)
			return HttpResponseRedirect('/contributor/profile')
            	else:
			login(request,user1)
			return HttpResponseRedirect('/reviewer/profile')
	    else:
                # An inactive account was used - no logging in!
                messages.info(request, "Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Bad login!")
            return render_to_response('webapp/login.html', context)
    else:
        return render_to_response('webapp/login.html', context)



@login_required
def contributor_profile(request):
	context = RequestContext(request)
        uploads = Subject.objects.filter(contributor__user__username=request.user)
	context_dict = {'uploads': uploads}
    	return render_to_response('contributor.html', context_dict, context)


@login_required
def reviewer_profile(request):
	context = RequestContext(request)
	rev = Reviewer.objects.get(user = request.user)
	user = rev.user
	uploads = Subject.objects.filter(name = rev.specialised_subject).filter(review__lt = 3)
        context_dict = {'uploads' : uploads , 'user':user}
	return render_to_response("reviewer.html",context_dict,context)

def reviewer_comment(request,sub_id,rev_id):
	context = RequestContext(request)
	print "sub_id = " + sub_id
	print "rev_id = " + rev_id
	comment = Comment.objects.filter(subject_id = sub_id)
	reviewer = Reviewer.objects.get(user_id = rev_id)
	if request.method == 'POST':
		print  "we have a new comment"
		comment_form = CommentForm(data = request.POST)
		if comment_form.is_valid():
			comments = comment_form.save(commit=False)
			subject = Subject.objects.get(pk = sub_id)
			comments.subject = subject
			comments.user = reviewer
			comments.save()
			url = reverse('webapp.views.reviewer_comment', kwargs={'sub_id': sub_id, 'rev_id' : rev_id})
			return HttpResponseRedirect(url) 
			# return HttpResponseRedirect(reverse('/reviewer/profile/comments/%s/%s/' % sub_id % rev_id))
		else:
			if comment_form.errors:
				print comment_form.errors
	else:	
		comment_form = CommentForm()
        context_dict = {'comment_form': comment_form, 'comment' : comment}
	return render_to_response("comments.html",context_dict,context)



def contributor_signup(request):
        
	"""Request for new contributor to signup"""
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
	"""Request for new contributor to signup"""
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
			#messages.success(request,"form successfully submitted. Waiting for activation  from admin.")
			return HttpResponseRedirect(reverse('webapp.views.contributor_upload'))
	        else:
			if reviewer_form.errors or user_form.errors:
				print user_form.errors, reviewer_form.errors
	else:
		reviewer_form = ReviewerForm()
		user_form = UserForm()	
           
        context_dict = {'user_form':user_form, 'reviewer_form': reviewer_form, 'registered': registered}
        return render_to_response('webapp/reviewer_signup.html', context_dict, context)


def user_logout(request):
	context=RequestContext(request)
	logout(request)
	return HttpResponseRedirect('/')

		
def commentpost(request):
	return render_to_response('templates/comments/post.html')


def contributor_upload(request):
	"""Request for new upload by the contributor"""
	context = RequestContext(request)
	uploaded= False
	if request.method == 'POST':
	        print "we have a request for upload by the contributor"    
	        contributor_upload_form = ContributorUploadForm(request.POST,request.FILES)
		if contributor_upload_form.is_valid():	
			print "Forms are valid"
			subject=contributor_upload_form.save(commit=False)
			# contri=Contributor.objects.get(user_id=id)
      			contri = Contributor.objects.get(user=request.user)
			subject.contributor=contri
			subject.name=contri.specialised_subject
			if 'pdf' in request.FILES:
                		subject.pdf=request.FILES['pdf']
			if 'video' in request.FILES:
                		subject.video = request.FILES['video']
			if 'animation' in request.FILES:
                		subject.animation = request.FILES['animation']
			                     
                        subject.save()
			uploaded = True
			return HttpResponseRedirect(reverse('webapp.views.contributor_profile'))
	        else:
			if contributor_upload_form.errors:
				print contributor_upload_form.errors
	else:
		contributor_upload_form = ContributorUploadForm()	
           
        context_dict = {'contributor_upload_form': contributor_upload_form, 'uploaded':uploaded}
        return render_to_response("webapp/upload.html", context_dict, context)

