from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def UserInterface(request):
    try:
        ses=''
        user=''
        try:
            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print("USER",user)
        except:
            pass
        db, cmd = pool.ConnectionPooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        q="select * from shows where status='Trending'"
        cmd.execute(q)
        trows = cmd.fetchall()

        q = "select * from shows where categoryid in (select categoryid from category where categoryname='TV Shows')"
        cmd.execute(q)
        tvrows = cmd.fetchall()

        q = "select * from shows where categoryid in (select categoryid from category where categoryname='English Movies')"
        cmd.execute(q)
        erows = cmd.fetchall()
        db.close()
        return render(request, "UserInterface.html", {'rows': rows,'trows':trows,'tvrows':tvrows,'erows':erows,'ses':ses,'user':user})
    except Exception as e:
        return render(request, "UserInterface.html", {'rows': []})

def Preview(request):
    try:
        ses=''
        user=''
        try:
            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print("USER",user)
        except:
            pass
        row=request.GET['row']
        row=eval(row)
        db, cmd = pool.ConnectionPooling()
        #main menu
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        #movies
        q="select * from shows where categoryid=6"
        cmd.execute(q)
        movies=cmd.fetchall()
        db.close()
        return render(request,"Preview.html",{'row':row,'rows': rows,'movies':movies,'ses':ses,'user':user})
    except Exception as e:
        print("error",e)
        return render(request,"Preview.html",{'row':[]})

def TvPreview(request):
    try:
        row=request.GET['row']
        row=eval(row)
        #main menu
        db, cmd = pool.ConnectionPooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        #episodes
        q="select * from episodes where categoryid=8 and showid={}".format(row[1])
        cmd.execute(q)
        episodes=cmd.fetchall()

        #Tv shows
        q="select * from shows where categoryid in(select categoryid from category where categoryname='TV Shows')"
        cmd.execute(q)
        tvshows=cmd.fetchall()
        db.close()

        return render(request,"TvPreview.html",{'row':row,'rows':rows,'tvshows':tvshows,'episodes':episodes})
    except Exception as e:
        print("error",e)
        return render(request,"TvPreview.html",{'row':[]})


def UserDetailsSubmit(request):
    try:
        mobileno=request.GET['mobileno']
        username=request.GET['username']
        age=request.GET['age']
        gender=request.GET['gender']
        status=request.GET['status']
        q="insert into clientdetails (mobilenumber,username,age,gender,status) values('{0}','{1}','{2}','{3}','{4}')".format(mobileno,username,age,gender,status)
        db, cmd = pool.ConnectionPooling()
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse("Registration Completed Successfully",safe=False)
    except Exception as e:
        return JsonResponse("Fail to Submit Record",safe=False)


def CheckMobileNumber(request):
    try:
        mobileno=request.GET['mobileno']
        db,cmd=pool.ConnectionPooling()
        q="select * from clientdetails where mobilenumber='{}'".format(mobileno)
        cmd.execute(q)
        row=cmd.fetchone()
        return JsonResponse(row,safe=False)
        db.close()
    except Exception as e:
        return JsonResponse(null,safe=False)


def UserSession(request):
    try:
        mobileno=request.GET['mobileno']
        username=request.GET['username']
        request.session["USER"]=[mobileno,username]

        return JsonResponse(True,safe=False)
    except Exception as e:
        return JsonResponse(False,safe=False)



def UserLogout(request):
    try:
        del request.session['USER']
        return UserInterface(request)
    except Exception as e:
        print(e)


def Searching(request):
    try:
        st = request.GET['st']
        db, cmd = pool.ConnectionPooling()

        q = "select *  from shows where showname like '%{}%'".format(st)
        print(q)
        cmd.execute(q)
        rows = cmd.fetchall()
        return JsonResponse(rows, safe=False)

        db.close()

    except Exception as e:
        print("error.....",e)
        return JsonResponse(null, safe=False)


def Movies(request):
    try:
        ses = ''
        user = ''
        try:
            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print("USER", user)
        except:
            pass

        db,cmd=pool.ConnectionPooling()
        q="select * from shows where status='Trending'"
        cmd.execute(q)
        hm = cmd.fetchall()
        db.close()
        return render(request,"Movies.html",{'hm':hm,'ses':ses,'user':user})
    except Exception as e:
        return render(request,"Movies.html",{'hm':[]})


def EnglishMovies(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select * from shows where categoryid in (select categoryid from category where categoryname='English Movies')"
        cmd.execute(q)
        em = cmd.fetchall()
        db.close()
        return render(request,"EnglishMovies.html",{'em':em})
    except Exception as e:
        return render(request,"EnglishMovies.html",{'em':[]})

def Subscription(request):
    return render(request,"Subscription.html")