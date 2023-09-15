#  Keep an eye on resources

Refer to virtual environments with this useful guide:

https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/

Also, it would be helpful to study the vagrant files and their structure.  This project uses the LondonAppDev Vagrant File to start off.

https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682
It also uses the MIT License.  Eventually, I may need to have legal advice on these licenses for protect me and what ways those protections work.
https://choosealicense.com/licenses/mit/
LondonAppDev / Python.dockerignore

https://www.vagrantup.com

https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-boxes

Note: It is simpler on Mac to use Homebrew to load vagrant and its dependencies.

brew install hashicorp/tap/hashicorp-vagrant

Of course, one can always download binaries for the Intel/AMD64 Mac or ARM64 Mac depending architecture.  

One can discover Vagrant boxes at the following URL.
https://app.vagrantup.com/boxes/search?page=2&provider=&q=ubuntu&sort=downloads&utf8=✓

https://developer.hashicorp.com/vagrant/vagrant-cloud

Watch out for reloading the vagrant boxes.   The configuration for port-forward might make things messy.  Try the guide from stack overflow:
https://stackoverflow.com/questions/34817312/how-do-i-remove-a-forwarded-port-in-vagrant


We establish a start project.   

## Recorded actions to get this far.

vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/
activate          activate.fish     easy_install-3.6  pip3              python
activate.csh      easy_install      pip               pip3.6            python3
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/
activate          activate.fish     easy_install-3.6  pip3              python
activate.csh      easy_install      pip               pip3.6            python3
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ pip  --versopm

Usage:   
  pip <command> [options]

no such option: --versopm
(env) vagrant@ubuntu-bionic:/vagrant$ pip  --version
pip 9.0.1 from /home/vagrant/env/lib/python3.6/site-packages (python 3.6)
(env) vagrant@ubuntu-bionic:/vagrant$ deactivate
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ deactivate
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ pip install -r requirements.txt
Collecting django==2.2 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/54/85/0bef63668fb170888c1a2970ec897d4528d6072f32dee27653381a332642/Django-2.2-py3-none-any.whl (7.4MB)
    100% |████████████████████████████████| 7.5MB 238kB/s
Collecting djangorestframework==3.9.2 (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/cc/6d/5f225f18d7978d8753c1861368efc62470947003c7f9f9a5cc425fc0689b/djangorestframework-3.9.2-py2.py3-none-any.whl (911kB)
    100% |████████████████████████████████| 921kB 1.7MB/s
Collecting pytz (from django==2.2->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl (502kB)
    100% |████████████████████████████████| 512kB 2.5MB/s
Collecting sqlparse (from django==2.2->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/98/5a/66d7c9305baa9f11857f247d4ba761402cea75db6058ff850ed7128957b7/sqlparse-0.4.4-py3-none-any.whl (41kB)
    100% |████████████████████████████████| 51kB 9.4MB/s
Installing collected packages: pytz, sqlparse, django, djangorestframework
Successfully installed django-2.2 djangorestframework-3.9.2 pytz-2023.3.post1 sqlparse-0.4.4
(env) vagrant@ubuntu-bionic:/vagrant$


## We now establish an app within our project
So what does this app look like?
A Django project can consist of one or more sub-applications within the project.   The idea is to separate functionality within the project.  



(env) vagrant@ubuntu-bionic:/vagrant$ django-admin.py startproject profiles_project .
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api


### What does this do?
We see these two things.  One the profiles_project gets created.  A manage.py comes about.  With the manage.py we now produce do a startup of profiles_api.  
Notice that the django-admin.py comes from the environment in the vagrant home user's bin directory.   

So, someone has though out these templates.  What do they do for us?   
We get a project that the Django engine can run and that contains a settings.py that we use to enable individual web-applications within our project.   This appears to adopt some qualities of WebObjects.  The main class in a WebObjects project is the WOApplication subclass.  It appears that we have something similar here that the project manages the whole collection, and it sets up individual applications.

### So how do we enable this first app that we named profiles-api.  

We open the profiles_project and find the settings.py file.   This file supports the configuration of each app in the project.  
In the settings.py file, we have a defined object called INSTALLED_APPS.  This list of strings identify the object URL of each app included in our project.
We used the requirements.txt specified external dependency applications.   We have

### We test the app via a development server

We have single command to start the development server in the vagrant virtual box.

python manage.py runserver 0.0.0.0:8000


# Set up of database
A weird thing our London based instructor brought up.   So, Django is a middleware or possibly an ORM.   Is this so?   

One thing that I liked about WebObjects is that Enterprise Objects and WebObjects were always two separate Application Program Interface Frameworks.  Sure, they may as well have been joined at the hip.  However, no developer had to use both together.  

One could use Enterprise Objects in any Objective-C project from the inception of Enterprise Objects until about OSX.4.   Come Tiger, Apple moved WebObjects over to Java to gain multi-platform capability in deploying WebObject projects with a premier Object-Relational Machine and stand alone for what ever Web-app the developer made.   They released Core Data as a successor to the Objective-C version of Enterprise Objects to run with native Apple apps.  When the iPhone arrived, Core Data was the native ORM.  Of course, iPhone still depended on WebObjects in so much that every app was a web app.  Then divisions came amongst the Apple leadership.

Java Enterprise Objects could be used with any Java based code.   Naturally, all of the examples entailed WebObjects.   Well, there were Java Direct applications.  Typically, these were Spring or some other UI made products to ensure that the product worked cross platform.  

Now, let us get back to Django.  We have Django Models.   What is that?  

## Example - Create the User Database Model
Each Django app includes a models.py.   This was created for us when we ran the manage.py startapp profiles_api.  This instruction at the command line produced profiles_api web-app source.  This includes init_py, admin.py, apps.py, tests.py, views.py.   

So, what is going on?  How do we work with this?
Well the instructor tells us to add some imports.  


It is clear that we create a class in models.py.   Why we don't have each class in the model in its own modular file, doesn't seem to be answered.

We do have an subclass declaration of AbstractBaseUser, PermissionsMixin.   These two classes / protocols provide some inherited definitions.   Check out these references:
https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
https://testdriven.io/blog/django-custom-user-model/
https://stackoverflow.com/questions/21514354/abstractuser-vs-abstractbaseuser-in-django
https://medium.com/@engr.tanveersultan53/abstractuser-vs-abstractbaseuser-in-django-7f231a276988


We also need something for connecting to the Django authentication system.   One thing that is smart about using developed frameworks is that a community of developers examine needs and produce commonly needed features as something to be shared.   At least, there goes the thinking.   Making an infrastructure that facilitates this action is another story.  But, the authentication system for DJango seems to be built with shared cloud resources in mind.  Check out these references:
https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
https://medium.com/@harshvb7/customizing-the-django-authentication-for-email-4ff2a7a3c65f

## So - how does Python or Django mange the User model?
One of the things we want out of a prototyping languages is to have the hard work of interfacing with the underlying system's user and authentication managed for us.  We want to use these features to provide a referee to actions the user is allowed to take.  We don't want our app to have to re-invent the User and Authentication management systems.   Those are already a full time occupation.
https://peps.python.org/pep-0008/
https://docs.djangoproject.com/en/1.11/ref/models/fields/
https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user
https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email


The whole point of creating profiles_api and its models.py with UserProfileManager and UserProfile class is to allow us to augment the Django user and authentication management system.  
The lecture (https://www.udemy.com/course/django-python/learn/lecture/6945622#content) provides us a means to connect these models to the overall project.   This is good as we typically make our project about something other than user and authentication management.  Reference (https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-AUTH_USER_MODEL)

Note, Python evolved in environments where Enterprise systems existed and managed desktop machines and servers, alike.  


This is where the instructor talks about integrating the models that we just made into the project at large.  

We set the user settings in the profiles_project.settings.py file of the project.  
