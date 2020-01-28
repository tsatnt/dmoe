import numpy
import threading
import random
# Create your models here.
from model_app.models import user_info,md_doc
###########################################################################
class login:
    def user(self,uname):
        temp = user_info.objects.get(user_name=uname)
        user_id = temp.ID
        auth_v_id = temp.v_id
        user = [[temp.ID,temp.user_name,temp.user_key],auth_v_id]
        return user
###########################################################################
class signon:
    def cnki(self,uname):
        usernum = user_info.objects.filter(user_name = uname)
        un = numpy.size(usernum)
        return un
    def sign(self,uname,ukey,vid):
        obj = user_info.objects.create(user_name = uname, user_key = ukey, v_id = vid)
        return self
##########################################################################33
class md_list:
    def user_model(self,vid):
        um = md_doc.objects.filter(val_id__lte=vid)
        # for i in range(len(um)):
        #     minfo[i] = [um[i].ID,um[i].val_id,um[i].md_name,um[i].md_type]
        return um
    def model_info(self,mdid):
        mi = md_doc.objects.get(ID=mdid)
        # minfo = [mi.ID,mi.val_id,mi.md_name,mi.md_type]
        return mi
    # def model_val(self,mdid):
    #     mv = md_doc.objects.get(ID=mdid)
    #     return mv.val_id

################################################################################