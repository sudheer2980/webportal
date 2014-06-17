import os
import sys
#import store
import contributors_list
import reviewers_list
import subject_list
import class_list
#import comment

def populate_users():

    """Populate Contributors."""

    # Admin
    os.system("python manage.py syncdb --noinput")
    # os.system("python manage.py schemamigration ac --initial")
    # os.system("python manage.py migrate ac")    
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
	


def populate_subject():

     

    for Subject in subject_list.subjects:	
        print "Adding Topic: %s has contributors: %s" % (Subject['topic'], Subject['contributor'])
        usr_instance = User.objects.get(username=Subject['contributor'])
        contributor_instance = Contributor.objects.get(user=usr_instance)
	class_num_instance = Class.objects.get(class_number=Subject['class'])
        add_sub(
            topic=Subject['topic'],
            name=Subject['name'],
            contributor=contributor_instance,
	    class_number=class_num_instance,
	    summary=Subject['summary'])

    

  	







def add_user(username, first_name, last_name, email, password):
    u = User.objects.create_user(username=username, first_name=first_name,
                                 last_name=last_name,
                                 email=email, password=password)
    u.is_active=False
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

def add_sub(topic, name, contributor, class_number, summary):
    sub = Subject(topic=topic, name=name, class_number=class_number, summary=summary)
    sub.save()

def add_faq(question, answer):
    faq = Faq(question=question, answer=answer)
    faq.save()





    
# start execution here!
if __name__ == '__main__':
    print "Starting Webportal population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webportal.settings')
    from webapp.models import Contributor, Reviewer
    from webapp.models import Faq
    from webapp.models import Class, Subject, Comment
    from django.contrib.auth.models import User

    if os.path.exists('webportal.db'):
        os.system("rm webportal.db")

    populate_users()
    populate_class()
    populate_subject()
#    populate_project()
