from django.shortcuts import render
from . import pool

def AdminLogin(request):
    return render(request,"AdminLogin.html",{'msg':''})

def CheckLogin(request):
    try:
        db,cmd=pool.ConnectionPooling()
        emailid=request.POST['emailid']
        password=request.POST['password']
        q="select * from adminlogin where emailid='{}' and password='{}'".format(emailid,password)
        cmd.execute(q)
        row=cmd.fetchone()
        if(row):
            return render(request,"Dashboard.html",{'row':row})
        else:
            return render(request,"AdminLogin.html",{'msg':'Pls Input Valid Emailid/Password'})
    except Exception as e:
        print("error",e)
        return render(request,"AdminLogin.html",{'msg':'Server Error...'})