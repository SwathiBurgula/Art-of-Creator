from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Preference

# Create your views here.


@login_required
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.author= request.user
                post.save()
                

                return render(request, 'pics/posts/create.html')  

        

        else:
                return render(request,'pics/posts/create.html')


def home(request):
        allposts= Post.objects.all()

        context={'allposts': allposts }

        return render(request, 'pics/posts/create.html', context)


def detail_post_view(request, id=None):
        eachpost= get_object_or_404(Post, id=id)

        

        context={'eachpost': eachpost}

        return render (request, 'posts/detail.html', context)


@login_required
def postpreference(request, postid, userpreference):
        
        if request.method == "POST":
                eachpost= get_object_or_404(Post, id=postid)

                obj=''

                valueobj=''

                try:
                        obj= Preference.objects.get(user= request.user, post= eachpost)

                        valueobj= obj.value #value of userpreference


                        valueobj= int(valueobj)

                        userpreference= int(userpreference)
                
                        if valueobj != userpreference:
                                obj.delete()


                                upref= Preference()
                                upref.user= request.user

                                upref.post= eachpost

                                upref.value= userpreference


                                if userpreference == 1 and valueobj != 1:
                                        eachpost.likes += 1
                                        eachpost.dislikes -=1
                                elif userpreference == 2 and valueobj != 2:
                                        eachpost.dislikes += 1
                                        eachpost.likes -= 1
                                

                                upref.save()

                                eachpost.save()
                        
                        
                                context= {'eachpost': eachpost,
                                  'postid': postid}

                                return render (request, 'posts/detail.html', context)


                except:
                    pass