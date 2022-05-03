from django.shortcuts import render
from . import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Show(request):
    return render(request,"Shows.html")
@xframe_options_exempt
def SubmitShow(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        showname=request.POST['showname']
        type=request.POST['type']
        description=request.POST['description']
        year=request.POST['year']
        rating=request.POST['rating']
        artist=request.POST['artist']
        status=request.POST['status']
        showstatus=request.POST['showstatus']
        episodes=request.POST['episodes']
        poster=request.FILES['poster']
        trailerurl=request.FILES['trailerurl']
        videourl=request.FILES['videourl']
        q="insert into shows (categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster,trailerurl,videourl) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster.name,trailerurl.name,videourl.name)
        print(q)
        cmd.execute(q)
        db.commit()
        E = open("D:/VideoStream/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
            E.write(chunk)
        E.close()
        F = open("D:/VideoStream/assets/" + trailerurl.name, "wb")
        for chunk in trailerurl.chunks():
            F.write(chunk)
        F = open("D:/VideoStream/assets/" + videourl.name, "wb")
        for chunk in videourl.chunks():
            F.write(chunk)
        db.close()
        return render(request, "Shows.html", {'status': True})
    except Exception as a:
        print("error:", a)
        return render(request, "Shows.html", {'status': False})

@xframe_options_exempt
def DispalyAllShow(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) from shows S"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllShows.html",{'rows':rows})
    except Exception as e:
        return render(request,"DisplayAllShows.html",{'rows':[]})

@xframe_options_exempt
def ShowById(request):
    try:
        sid = request.GET['sid']
        db, cmd = pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)from shows S where S.showid={}".format(sid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request, "ShowById.html", {'row': row})
    except Exception as e:
        return render(request, "ShowById.html", {'row': []})

@xframe_options_exempt
def EditDeletetShow(request):
    try:
        btn = request.GET['btn']
        if(btn=="edit"):
            db, cmd = pool.ConnectionPooling()
            showid=request.GET['showid']
            categoryid = request.GET['categoryid']
            showname = request.GET['showname']
            type = request.GET['type']
            description = request.GET['description']
            year = request.GET['year']
            rating = request.GET['rating']
            artist = request.GET['artist']
            status = request.GET['status']
            showstatus = request.GET['showstatus']
            episodes = request.GET['episodes']
            q ="update shows set categoryid='{}',showname='{}',type='{}',description='{}',year='{}',rating='{}',artist='{}',status='{}',showstatus='{}',episodes='{}'where showid='{}'".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,showid)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="delete"):
            db, cmd = pool.ConnectionPooling()
            showid = request.GET['showid']
            q = "delete from shows where showid='{}'".format(showid)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request, "ShowById.html", {'status': True})
    except Exception as a:
        print("error:", a)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditPoster(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid = request.POST['showid']
        filename1=request.POST['filename1']
        poster=request.FILES['poster']
        q="update shows set poster='{0}'where showid='{1}'".format(poster.name,showid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename1)
        db.close()
        return render(request,"ShowById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditTrailer(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid = request.POST['showid']
        filename2=request.POST['filename2']
        trailerurl=request.FILES['trailerurl']
        q="update shows set trailerurl='{0}'where showid='{1}'".format(trailerurl.name,showid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+trailerurl.name,"wb")
        for chunk in trailerurl.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename2)
        db.close()
        return render(request,"ShowById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditVideo(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid = request.POST['showid']
        filename3=request.POST['filename3']
        videourl=request.FILES['videourl']
        q="update shows set videourl='{0}' where showid='{1}'".format(videourl.name,showid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+videourl.name,"wb")
        for chunk in videourl.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename3)
        db.close()
        return render(request,"ShowById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def DispalyAllShowJSON(request):
    try:
        cid=request.GET['cid']
        db,cmd=pool.ConnectionPooling()
        q="select * from shows where categoryid={}".format(cid)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("Errror",e)
        return JsonResponse([],safe=False)