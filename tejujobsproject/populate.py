import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tejujobsproject.settings')
import django
django.setup()
import random
from faker import Faker
from testapp.models import hydjobs,chennaijobs,punejobs,blorejobs
fake=Faker()
def numgen():
    s=random.randint(6,9)
    s=''+str(s)
    for i in range(9):
        s=s+str(random.randint(0,9))
    return int(s)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','sr.software engineer'))
        feligibility=fake.random_element(elements=['B.Tech','M.Tech','MCA','Phd'])
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=numgen()
        punejobs_records=punejobs.objects.get_or_create(date=fdate,title=ftitle,eligibility=feligibility,company=fcompany,address=faddress,email=femail,phonenumber=fphonenumber)
populate(25)
