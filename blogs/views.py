from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from profiles.models import UserProfile

# Create your views here.


def all_blogs(request):
    """
    A view to show all blogs along with search queries
    """
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    context = {
        'blogs': blogs,
        'comments': comments,
        'on_blog_page': True,
    }

    return render(request, 'blogs/blogs.html', context)



@login_required
def add_blog(request):
    """ Add a blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = BlogForm()
       
    template = 'blogs/add_blog.html'
    context = {
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def add_comment(request, blog_id):
    """ Add a comment to a blog """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_profile = user_profile
            form.blog = blog
            form.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to add comment. Please ensure the form is valid.')
    else:
        form = CommentForm()
   
    template = 'blogs/add_comment.html'
    user_profile = get_object_or_404(UserProfile, user=request.user)
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'form': form,
        'on_blog_page': True,
        'blog': blog,
        'user_profile': user_profile,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
   
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to update blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blogs/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit a comment """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to update comment. Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment)
        messages.info(request, f'You are editing a comment')

    template = 'blogs/edit_comment.html'
    context = {
        'form': form,
        'comment': comment,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Delete a blog """
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blogs'))


@login_required
def delete_comment(request, blog_id):

    """ Delete a comment """
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('blogs'))