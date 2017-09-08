
		# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from forms import MobileForm
from models import CustomerModel
from twilio.rest import Client
import random

# Create your views here.
def mobile_view(request):
    dict={}
    if request.method == "GET":
        mobile_form = MobileForm()
        dict['mobile-form'] = mobile_form
        return render(request,"mobile.html",dict)
    elif request.method == "POST":
        print("Getting values from request....")
        mobile_form = MobileForm(request.POST)
        if mobile_form.is_valid():
            clean_mob_no = mobile_form.cleaned_data['mob_no']
            filtered_mob_no = CustomerModel.objects.filter(mob_no =clean_mob_no)#Check mob_no from database..
            if filtered_mob_no:
                temp_mob_no = str(filtered_mob_no)
                otp = random.randint(1111,5555)
                otp_object = CustomerModel(otp_no = otp)
                otp_object.save()    #saving otp to data-base....
                account_sid = "AC7b92a83cd1b0aabb112528799226056b"
                auth_token  = "6c7499e091a84ae97ba3b756d8efaa35"
                client      = Client(account_sid, auth_token)
                message     = client.messages.create(
                    to = "+91"+temp_mob_no,
                    from_= "+14153013736",
                    body = otp
                )

                print message.sid
                return render(request,"success.html")
            else:
                return render(request,"success.html")
        else:
            return render(request, "success.html")