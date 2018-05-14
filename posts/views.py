from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from utils.general import ret_obj_or_raise_404
from utils.string_utils import decode_id
from .forms import PostForm
from django.contrib import messages

# Create your views here.

# A class that a placeholder for a post... to be used for base64 encoded pks


def post_home(request):
    return HttpResponse("<h1>Hello world</h1>")


def post_create(request):
    # todo check if the person is authenticated
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect("/posts/"+instance.url())
        # Post.objects.create(title=title, content=content)

    context_data = {
        "form": form,
    }
    return render(request, "post_form.html", context_data)


def post_detail(request, id):  # retrieve post data

    # expecting the ids to be base64 encoded... decoding it here
    # the below line of code was written because initially the html template linked it as posts/posts/b64id...
    # django didnt refresh the changes... its fixed now
    # id = id[6:]
    obj_id = decode_id(id)
    obj = ret_obj_or_raise_404(Post.objects.filter(deleted=0), obj_id, request)

    context_data = {
        "instance": obj
    }
    if isinstance(obj, Post):
        return render(request, "post_detail.html", context_data)
    return obj


def post_list(request):  # lists all posts
    # if request.user.is_authenticated:
    #     context_data = {
    #         "title": "logged in list"
    #     }
    # else:

    queryset = Post.objects.filter(deleted=0)

    # list_of_post_holders = []
    # for row in queryset:
    #     list_of_post_holders.append(PostDataHolder(encode_id(row.id), row.title,row.content))
    context_data = {
            "title": "list",
            "queryset": queryset
    }
    return render(request, "all_posts.html", context_data)


def post_delete(request, id):  # deletes a post
    a = decode_id(id)
    obj = ret_obj_or_raise_404(Post.objects.filter(deleted=0), a, request)

    if isinstance(obj, Post):
        obj.delete()
        obj.save()
        messages.success(request, "Sucessfully deleted")
        return HttpResponseRedirect('/posts/')

    return obj


def post_update(request, id):  # updates a post
    # todo check if user is valid

    queryset = Post.objects.filter(deleted=0)
    instance = ret_obj_or_raise_404(queryset, decode_id(id), request)

    if not isinstance(instance, Post):
        return render(request, "404.html")

    form = PostForm(request.POST or None, instance=instance)

    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        # use extra_tags kwarg= 'css classes' ... you can also out html through this using html_safe
        return HttpResponseRedirect("/posts/%s/" % instance.url())

        # Post.objects.create(title=title, content=content)

    context_data = {
        "form": form,
    }
    return render(request, "post_form.html", context_data)




