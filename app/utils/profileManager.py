import json
import os



def create_profile(uname,def_dest,temp_dest):
    profile_fp=open("./profile.json",'w+')
    profile_dict={}
    profile_dict['username']=uname
    profile_dict['default_dest']=def_dest
    profile_dict['temp_dest']=temp_dest
    json.dump(profile_dict,profile_fp,indent=4)


def get_profile():
    profile={}
    try:
        profile_fp=open("./profile.json",'r+')
        profile=json.load(profile_fp)
        return profile
    except:
        print('profile.json not valid')
        return None


def check_profile_integrity():
    profile_fp=open("./profile.json",'r+')
    try:
        profile=json.load(profile_fp)
        if(os.path.exists(profile['default_dest'])and os.path.exists(profile['temp_dest'])):
            return True
        else: return False
    except:
        print('profile.json not valid')
        return None

def modify_default_destination():
    try:
        profile_fp=open("./profile.json",'r+')
        profile=json.load(profile_fp)
        profile['default_dest']=input('enter new default destination')
        json.dump(profile,profile_fp,indent=4)
    except:
        print("profile.json not valid")

