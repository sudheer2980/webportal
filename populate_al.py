import os
import sys
import store
import contributor_list
import reviewer_list
import subject_list
import class_list
import comment

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
			validation_docs=u['VALIDATION_DOC'])

    for u in reviewer_list.users:
        # Normal users
        print "Adding user: %s" % u['USERNAME']
        u['USERNAME'] = add_user(u['USERNAME'],
                                 u['FIRSTNAME'],
                                 u['LASTNAME'],
                                 u['EMAIL'],
                                 u['PASSWORD'],)
        
        
        add_reviewer(user=u['USERNAME'],
                        contact=u['CONTACT'],
                        picture=u['PHOTO'],
			
        
        
    user_list = User.objects.all()
    if user_list:
        print "Following user(s) created successfully."
        for i in user_list:
            print i.username





def populate_class():
    """Populate class"""
    for Class in class_list.Classes:
	add_Class( class_number=Class['class_number'] , remark=Class['remark'])
	


def populate_subject():
    """populate subjects and contributors corresponding to them""" 

    for sub in sub_list.subs:	
        print "Adding Topic: %s has contributors: %s" % (sub['NAME'], sub['CONTRIBUTOR'])
        usr_instance = User.objects.get(username=ac['COORDINATOR'])
        contributor_instance = Contributor.objects.get(user=usr_instance)
        add_sub(
            topic=sub['TOPIC'],
            name=sub['NAME'],
            contributor=coordinator_instance,
            city=ac['CITY'],
            state=ac['STATE'],
            active=True)


def populate_project():
    """Populate projects."""
n
    print "Populating projects.."
    for project in project_list.projects:
        if project['AC_ID'] == "0":
            print "Project: %s doest not have a valid AC_ID." % project['NAME']
        else:
            print "RC_ID: %s" % project['AC_ID']
            print "Project name: %s" % project['NAME'][:1].upper() + project['NAME'][1:].lower()
        
            inst_name = AakashCentre.objects.get(ac_id=project['AC_ID'])
            member = TeamMember(name=project['MEMBER'], email=project['MEMBER_EMAIL'])
            member.save()

            demo = Project(
                name=project['NAME'][:1].upper() + project['NAME'][1:].lower(),
                ac=inst_name,
                summary=project['DESCRIPTION'],
                src_url=project['SRC_CODE'],
                doc_url="",
                approve=True)

            demo.save()
            demo.member.add(member)
        
    """"
    # working
    inst_name = AakashCentre.objects.get(ac_id=1002)

    sachin = TeamMember(name="sachin", email="isachin@github.com")
    sachin.save()

    ac = AakashCentre.objects.get(ac_id=1001)
    demo = Project(name="demo", ac=inst_name, summary="demo desc.",
                   src_url="http://google.com", doc_url="http://google.com")
    demo.save()
    demo.member.add(sachin)
    """




def add_user(username, first_name, last_name, email, password):
    u = User.objects.create_user(username=username, first_name=first_name,
                                 last_name=last_name,
                                 email=email, password=password)
    u.is_active=False
    u.save()
    return u


def add_contributor(user, contact, picture, validation_doc):
    up = Coordinator(user=user, contact=contact, picture=picture, vaidation_doc=validation_doc)
    up.save()
def add_reviewer(user, contact, picture,):
    up = Coordinator(user=user, contact=contact, picture=picture,)
    up.save()


def add_class(class_number, remark):
    class_no = Class(class_number=class_number, remark=remark)
    class_no.save()


def add_faq(question, answer):
    faq = Faq(question=question, answer=answer)
    faq.save()


def add_project(name, ac, summary, team_member, src_url, doc_url=None,
                approve=False):
    project = Project(name=name, ac=ac, summary=summary,
                      src_url=src_url, doc_url=doc_url, approve=approve)
    project.save()
    project.member.add(team_member)


def add_member(name, email):
    member = TeamMember(name=name, email=email)
    member.save()

    
# start execution here!
if __name__ == '__main__':
    print "Starting Aakashlabs population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aakashlabs.settings')
    from ac.models import AakashCentre, Coordinator
    from ac.models import Faq
    from ac.models import Mentor, TeamMember, Project
    from django.contrib.auth.models import User

    if os.path.exists('ac.db'):
        os.system("rm ac.db")

    populate_users()
    populate_ac()
    populate_faq()
#    populate_project()
