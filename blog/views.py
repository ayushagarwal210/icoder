from django.shortcuts import render,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def bloghome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post, parent=None)
    replies = BlogComment.objects.filter(post = post).exclude(parent=None)
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    context = {'post' : post, 'comments' : comments, 'user' : request.user, 'replydict' : replydict}
    return render(request,'blog/blogpost.html',context)

def postcomment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(sno=postsno)
        parentsno = request.POST.get("parentsno")
        if parentsno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request,"Your comment posted successfully")
        else:
            parent = BlogComment.objects.get(sno = parentsno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request,"Your reply posted successfully")
        comment.save()
    return redirect(f"/blog/{post.slug}")
    