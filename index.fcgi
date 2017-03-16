#!/opt/python27/bin/python
import sys, os, user

# Add a custom Python path. (optional)
sys.path.insert(0, "/var/www/vhosts/cruzrojatijuana.org.mx/httpdocs")

# Switch to the directory of your project.
os.chdir("/var/www/vhosts/cruzrojatijuana.org.mx/httpdocs")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
