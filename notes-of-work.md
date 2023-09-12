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
