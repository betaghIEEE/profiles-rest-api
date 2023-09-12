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
