from django.shortcuts import render
from . import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Episodes(request):
    return render(request,"Episodes.html")

@xframe_options_exempt
def SubmitEpisode(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        showid=request.POST['showid']
        episodenumber=request.POST['episodenumber']
        description=request.POST['description']
        poster=request.FILES['poster']
        trailer=request.FILES['trailer']
        video=request.FILES['video']
        q="insert into episodes (categoryid,showid,episodenumber,description,poster,trailer,video) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,showid,episodenumber,description,poster.name,trailer.name,video.name)
        print(q)
        cmd.execute(q)
        db.commit()
        E = open("D:/VideoStream/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
            E.write(chunk)
        E.close()
        F = open("D:/VideoStream/assets/" + trailer.name, "wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F = open("D:/VideoStream/assets/" + video.name, "wb")
        for chunk in video.chunks():
            F.write(chunk)
        db.close()
        return render(request, "Episodes.html", {'status': True})
    except Exception as a:
        print("error:", a)
        return render(request, "Episodes.html", {'status': False})

@xframe_options_exempt
def DispalyAllEpisodes(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid),(select S.showname from shows S where S.showid=E.showid) from episodes E"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllEpisodes.html",{'rows':rows})
    except Exception as e:
        return render(request,"DisplayAllEpisodes.html",{'rows':[]})

@xframe_options_exempt
def EpisodeById(request):
        try:
            eid = request.GET['eid']
            db, cmd = pool.ConnectionPooling()
            q = "select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid),(select S.showname from shows S where S.showid=E.showid) from episodes E where E.episodeid={}".format(eid)
            cmd.execute(q)
            row = cmd.fetchone()
            db.close()
            return render(request, "EpisodeById.html", {'row': row})
        except Exception as e:
            return render(request, "EpisodeById.html", {'row': []})

@xframe_options_exempt
def EditDeletetEpisode(request):
    try:
        btn = request.GET['btn']
        if(btn=="Edit"):
            db, cmd = pool.ConnectionPooling()
            showid=request.GET['showid']
            categoryid = request.GET['categoryid']
            episodeid = request.GET['episodeid']
            description = request.GET['description']
            episodenumber = request.GET['episodenumber']
            q ="update episodes set categoryid='{}',showid='{}',description='{}',episodenumber='{}'where episodeid='{}'".format(categoryid,showid,description,episodenumber,episodeid)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            db, cmd = pool.ConnectionPooling()
            episodeid = request.GET['episodeid']
            q = "delete from episodes where episodeid='{}'".format(episodeid)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request, "EpisodeById.html", {'status': True})
    except Exception as a:
        print("error:", a)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditEpisodePoster(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid = request.POST['episodeid']
        filename1=request.POST['filename1']
        poster=request.FILES['poster']
        q="update episodes set poster='{0}'where episodeid='{1}'".format(poster.name,episodeid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename1)
        db.close()
        return render(request,"EpisodeById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditEpisodeTrailer(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid=request.POST['episodeid']
        filename2=request.POST['filename2']
        trailer=request.FILE['trailer']
        q="update episodes set trailer='{0} where episodeid='{1}'".format(trailer.name,episodeid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+trailer.name,"wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename2)
        db.close()
        return render(request,"EpisodeById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "EpisodeById.html", {'status':False})

@xframe_options_exempt
def EditEpisodeVideo(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid=request.POST['episodeid']
        filename3=request.POST['filename3']
        video=request.FILE['video']
        q="update episodes set vidoe='{0}' where episodeid='{1}'".format(video.name,episodeid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+video.name,"wb")
        for chunk in video.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename3)
        db.close()
        return render(request,"EpisodeById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"EpisodeById.html",{'status':False})