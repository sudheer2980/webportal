from django import forms
from models import Contributor , Reviewer, Class, Subject ,Comment
from django.contrib.auth.models import User
from webapp.models import Contributor

class UserForm(forms.ModelForm):
    """
    Fields are:

    USERNAME: He is the user who sign in.

    FIRST_NAME: This field tells the First name of the user. 

    LAST_NAME: This field tells the Last name of the user. 

    EMAIL: Email field tells the mail id of the user who sign in.

    PASSWORD: This tells the user to set his own password.
    """
    username = forms.CharField(label='Username',
    	widget = forms.TextInput(attrs={'class': 'form-control',
	    'placeholder': 'Username  to login*.'}), 
		help_text="", required =True,
		    error_messages={'required':'Username is required.'})
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                'placeholder': 'First name*.'}),
           				 help_text="", required=True,
       						 error_messages={'required':'First name is required.'})
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control',
                'placeholder': 'Last name*.'}),
       		    help_text="", required=True,
        	        error_messages={'required':'Last name is required.'})

    email = forms.CharField(
       	widget= forms.TextInput(
            attrs={'class': 'form-control',
                'placeholder': 'Valid email*.'}),
                    help_text="", required=True,
        	        error_messages={'required':'Valid Email address is required.'})
    password = forms.CharField(
       	widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                'placeholder': 'Password*.'}),
       	            help_text="", required=True,
      		        error_messages={'required':'Password is missing.'})

    class Meta:
   	model =  User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class ContributorForm(forms.ModelForm):	
    """
    Fields are:

    CONTACT: This is the contact number of the user. It must be an integer.

    VALIDATION_DOCS: The Valid certificate of the user stating his educational qualifications. 

    PICTURE: The profile picture of the contributor. may be jpg or jpeg or png or bmp.
    """
    contact  = forms.CharField(
       	widget= forms.TextInput(
           attrs={'class': 'form-control', 
               'placeholder': 'Contribter contact number.'}),
                   help_text="", required=False,
       		       error_messages={'required':'Last name is required.'})

    validation_docs = forms.FileField(
       	label = 'Validation file.',
    	    widget = forms.FileInput(),
                #help_text = 'Upload validation file.',
        	    required=False)

    picture = forms.ImageField(label='Profile picture',
        widget = forms.FileInput(
            attrs={'placeholder': 'Contributor picture.'}),
                required=False)
    class Meta:
        model =  Contributor
        fields = ('picture', 'contact', 'validation_docs')

    def clean_validtion_docs_file(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['validation_docs']:
            validation_docs= self.cleaned_data['validation_docs']
            return validation_docs
	else:
            raise forms.ValidationError("Not a valid file!")

class ReviewerForm(forms.ModelForm):	
    """
    Fields are:

    PICTURE: The profile picture of the Reviewer. may be jpg or jpeg or png or bmp.

    CONTACT: This is the contact number of the user. It must be an integer.
    """
    error_css_class = 'error'
    required_css_class = 'required'
    picture = forms.ImageField(label='Profile picture',
        widget = forms.FileInput(
            attrs={'placeholder': 'Reviewer picture.'}),required=False)
    contact  = forms.CharField(
       	widget= forms.TextInput(
            attrs={'class': 'form-control','placeholder': 'Reviewer contact number.'}),
        	help_text="", required=False,
       		    error_messages={'required':'Last name is required.'})
    class Meta:
        model =  Reviewer
     	fields = ('picture', 'contact')

class ContributorUploadForm(forms.ModelForm):
    """
    Fields are:

    CLASS_NUMBER: This will be class number like first, second .. eight .. tenth.

    NAME: This field is the name of the subject,the contributor is specialized in.

    TOPIC: The subject of the topic the contibutor is going to contribute.

    PDF: The contributor has to upload the files.This field describes that the uploaded file must be a pdf file. 

    VIDEO: The contributor has to upload the files.This field describes that the uploaded file must be a video. May be mp4.

    ANIMATION: The contributor has to upload the files.This field describes that the uploaded file must be an animation file. This may be gif.

    SUMMARY: This is the summary given by the contributor about the specified topic of the specified subject including when to use and how to use.
    """
    class_number = forms.ModelChoiceField(
	label='Class',
	cache_choices=True,
	widget=None,
	queryset=Class.objects.all(),
	empty_label=None,
	help_text="",required=True,
        error_messages={'required':'Class is required'})	
    name = forms.CharField(
        widget= forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Subject name*.'}),
        help_text="", required=True,
       	error_messages={'required':'Subject name is required.'})			
    topic = forms.CharField(
        widget= forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Subject topic*.'}),
        help_text="", required=True,
        error_messages={'required':'Subject topic is required.'})
    pdf = forms.FileField(
        label = 'pdf file.',
        widget = forms.FileInput(),
        help_text = 'Upload pdf file.',required=False)
    video = forms.FileField(
        label = 'video file.', 
        help_text = 'Upload video file.',required=False)
    animation = forms.FileField(
        label = 'animations file.',
        widget = forms.FileInput(),
        help_text = 'Upload animations file.',required=False)
    summary = forms.CharField(label='Summary',
	widget= forms.Textarea(
        attrs={'class': 'form-control','placeholder': 'Summary for the uploaded documents.'}),
	help_text="", required=True,
	error_messages={'required':'Summary is required.'})       	
    class Meta:
        model = Subject
        fields = ['class_number', 'name','topic', 'pdf', 'video', 'animation', 'summary']
    
    def clean_pdf_doc_file(self):
        """Upload a valid ."""
        if self.cleaned_data['pdf']:
            pdf= self.cleaned_data['pdf']
            return pdf
        else:
	    raise forms.ValidationError("Not a valid file!")

    def clean_video_doc_file(self):
      	"""Limit doc_file upload size."""
        if self.cleaned_data['video']:
            video= self.cleaned_data['video']
            return video
        else:
	    raise forms.ValidationError("Not a valid file!")
    def clean_animations_doc_file(self):
        """Limit doc_file upload size."""
        if self.cleaned_data['animation']:
            animation= self.cleaned_data['animation']
            return animation
	else:
	    raise forms.ValidationError("Not a valid file!")

class CommentForm(forms.ModelForm):
    """
    Field  is: 
  
    COMMENT: This field describes the comment form which takes maximum length of 1000 characters. The comment is made by the reviewer.
    """
    comment = forms.CharField(
        widget= forms.Textarea(
        attrs={'class': 'form-control','rows': '3'}),
        help_text="", required=False,
	)

    class Meta:
        model = Comment
        fields = ['comment']	
	
