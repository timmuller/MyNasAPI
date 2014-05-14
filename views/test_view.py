import subprocess
import tornado.web
from tornado.options import options

class TestView(tornado.web.RequestHandler):
    def get(self):
        mydata = {}
        for disk in ['sda', 'sdb', 'sdc', 'sdd', 'sde', 'sdf', 'sdg', 'sdh']:
            mydata[disk] = self.is_active(disk)
        self.render('test.html', **{'disk_results': mydata})
#        self.write("none testing<br/>")

#        for disk in ['sda', 'sdb', 'sdc', 'sdb']:
#            self.write("%s is active : %s<br/>" % (disk, self.is_active('sda')))
#        self.write("none testing<br/>")

    def is_active(self, disk):
        subprocess_object = subprocess.Popen('/sbin/hdparm -C /dev/%s | grep active' % disk, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, sterr = subprocess_object.communicate()
        if subprocess_object.returncode == 0:
            return True
        return False; 
