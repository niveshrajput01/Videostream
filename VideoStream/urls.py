"""VideoStream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryView
from . import AdminView
from . import ShowsView
from . import EpisodeView
from . import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
#user
    path('userinterface/',UserView.UserInterface),
    path('preview/',UserView.Preview),
    path('tvpreview/',UserView.TvPreview),
    path('userdetailssubmit/',UserView.UserDetailsSubmit),
    path('checkmobilenumber/',UserView.CheckMobileNumber),
    path('usersession/',UserView.UserSession),
    path('userlogout/',UserView.UserLogout),
    path('searching/',UserView.Searching),
    path('movies/',UserView.Movies),
    path('englishmovies/',UserView.EnglishMovies),
    path('subscription/',UserView.Subscription),

#admin
    path('adminlogin/',AdminView.AdminLogin),
    path('chklogin',AdminView.CheckLogin),
#category
    path('categoryinterface/',CategoryView.CategoryInterface),
    path('submitcategory',CategoryView.SumitCategory),
    path('displayallcategory',CategoryView.DispalyAll),
    path('categorybyid/', CategoryView.CategoryById),
    path('editdeletecategorydata/', CategoryView.EditDeleteCategoryData),
    path('editicon', CategoryView.EditIcon),
    path('displayallcategoryjson/',CategoryView.DispalyAllJSON),
#shows
    path('show/',ShowsView.Show),
    path('submitshow',ShowsView.SubmitShow),
    path('displayallshow',ShowsView.DispalyAllShow),
    path('showbyid/',ShowsView.ShowById),
    path('editdeleteshow/',ShowsView.EditDeletetShow),
    path('editposter',ShowsView.EditPoster),
    path('edittrailer',ShowsView.EditTrailer),
    path('editvideo',ShowsView.EditVideo),
    path('displayallshowjson/',ShowsView.DispalyAllShowJSON),
#eipsodes
    path('episodes/',EpisodeView.Episodes),
    path('submitepisode',EpisodeView.SubmitEpisode),
    path('displayallepisodes', EpisodeView.DispalyAllEpisodes),
    path('episodebyid/',EpisodeView.EpisodeById),
    path('editdeleteepisode/', EpisodeView.EditDeletetEpisode),
    path('editepisodeposter', EpisodeView.EditEpisodePoster),
    path('editepisodetrailer', EpisodeView.EditEpisodeTrailer),
    path('editepisodevideo', EpisodeView.EditEpisodeVideo),

]
