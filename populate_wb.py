import os
import sys
#import store
import contributors_list
import reviewers_list
import subject_list
import class_list
import comment_list
import language_list

def populate_users():

    """Populate Contributors."""

    # Admin
    os.system("python manage.py syncdb --noinput")
    os.system("python manage.py createsuperuser --username=admin --email=admin@example.com")


    for u in contributors_list.users:

        # Normal users
        print "Adding user: %s" % u['USERNAME']
        u['USERNAME'] = add_user(u['USERNAME'],
                                 u['FIRSTNAME'],
                                 u['LASTNAME'],
                                 u['EMAIL'],
                                 u['PASSWORD'],)
        
        
        add_contributor(user=u['USERNAME'],
                        contact=u['CONTACT'],
                        picture=u['PHOTO'],
validation_docs=u['validation_docs'])



    for u in reviewers_list.users:
        # Normal users
        print "Adding user: %s" % u['USERNAME']
        u['USERNAME'] = add_user(u['USERNAME'],
                                 u['FIRSTNAME'],
                                 u['LASTNAME'],
                                 u['EMAIL'],
                                 u['PASSWORD'],)
        
        
        add_reviewer(user=u['USERNAME'],
                        contact=u['CONTACT'],
                        picture=u['PHOTO'],)

        
        
    user_list = User.objects.all()
    if user_list:
        print "Following user(s) created successfully."
        for i in user_list:
            print i.username






def populate_class():

    for Class in class_list.classes:
	add_Class( class_number=Class['class_number'] , remark=Class['remark'])


def populate_language():
    for Language in language_list.languages:
	add_language(language=Language['language'])

def populate_subject():

    for Subject in subject_list.subjects:	
        print "Adding Topic: %s has contributors: %s" % (Subject['topic'], Subject['contributor'])
        usr_instance = User.objects.get(username=Subject['contributor'])
        contributor_instance = Contributor.objects.get(user=usr_instance)
	class_num_instance = Class.objects.get(class_number=Subject['class'])
	lang_instance = Language.objects.get(language=Subject['language'])

        add_sub(
            topic=Subject['topic'],
            name=Subject['name'],
            contributor=contributor_instance,
	    class_number=class_num_instance,
	    language=lang_instance,
            summary=Subject['summary'],
	    )

    

def populate_comments():

    for Comment in comment_list.comment:
	print "Adding Comment: %s has Reviewer: %s" % (Comment['comment'], Comment['user'])
	usr_instance = User.objects.get(username=Comment['user'])
	reviewer_instance = Reviewer.objects.get(user=usr_instance)
	sub_instance = Subject.objects.filter(name=Comment['subject'])

	for subjec in sub_instance:
		add_comment(
		subject=subjec,
		user=reviewer_instance,
		comment=Comment['comment'],
		submit_date=Comment['submit_date'])	

def populate_faq():
    """Populate FAQs.
"""
    print "Populating FAQ"
    q1 = add_faq(
        
        question="I have forgotten the pattern set by me, how can I login to Aakash tablet?",
        
        answer="""
1. Foremost make sure that you USB debugging is enabled.
2. Connect your tablet to the computer.

For Window User.
3. Go to the Start option. Open command prompt. Type cmd and press enter.
4. A window will pop up with a C: prompt.
Ex :- C:\Users\user>
5. Type the following commands
C:\Users\user>adb shell
sh-3.2# rm/data/system/gesture.key
rm/data/system/gesture.key
sh-3.2#

Once this is done, one has to restart/reboot their tablet. Now
the tablet is ready to use.
For Ubuntu User.
6. Go to the terminal.
7. Then go to the folder where adb is installed.
8. Repeat the commands from step number 5.

In addition to the above steps, a link has been provided for
your reference(http://www.youtube.com/watch?v=QYdkgO1KHmk)"""
    
    )
    print "FAQ successfully populated"





def add_user(username, first_name, last_name, email, password):
    u = User.objects.create_user(username=username, first_name=first_name,
                                 last_name=last_name,
                                 email=email, password=password)
    u.is_active=True
    u.save()
    return u


def add_contributor(user, contact, picture, validation_docs):
    up = Contributor(user=user, contact=contact, picture=picture, validation_docs=validation_docs)
    up.save()

def add_reviewer(user, contact, picture,):
    up = Reviewer(user=user, contact=contact, picture=picture)
    up.save()


def add_Class(class_number, remark):
    class_no = Class(class_number=class_number, remark=remark)
    class_no.save()

def add_language(language):
    lang = Language(language=language)
    lang.save() 

def add_sub(topic, name, contributor, class_number, summary, language):
    sub = Subject(topic=topic, name=name, contributor=contributor, class_number=class_number, summary=summary, language=language)
    sub.save()

def add_faq(question, answer):
    faq = Faq(question=question, answer=answer)
    faq.save()

def add_comment(subject, user, comment, submit_date):
    com = Comment(subject=subject, user=user, comment=comment, submit_date=submit_date)
    com.save()



    
# start execution here!
if __name__ == '__main__':
    print "Starting Webportal population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webportal.settings')
    from webapp.models import Contributor, Reviewer
    from webapp.models import Faq, Language
    from webapp.models import Class, Subject, Comment
    from django.contrib.auth.models import User

    if os.path.exists('webportal.db'):
        os.system("rm webportal.db")

    populate_users()
    populate_class()
    populate_language()
    populate_subject()
    populate_comments()
    populate_faq()
    
