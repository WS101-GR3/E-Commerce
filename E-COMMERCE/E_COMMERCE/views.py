from django.shortcuts import render


# LANDING PAGE NEED PREBUILD AND USER BUILD 
from PRODUCT.models import PackageBundle


def home(request):
    PreBuilds = PackageBundle.objects.filter(bundle_category='PreBuild') #Only picks the PreBuilds
    UserBuilds = PackageBundle.objects.filter(bundle_category='UserBuild') #Only picks the UserBuilds
    return render(request, 'home.html',{
        'PreBuilds':PreBuilds,
        'UserBuilds': UserBuilds[0:3] #SLICE THE BUILD TO ONLY PASS 3 INSTANCES
    })