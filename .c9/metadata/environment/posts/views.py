{"filter":false,"title":"views.py","tooltip":"/posts/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":45,"column":63},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, redirect","from django.utils import timezone","from .models import Post","from .forms import BlogPostForm","","","def get_posts(request):","    \"\"\"","    Create a view that will return a list","    of Posts that were published prior to 'now'","    and render them to the 'blogposts.html' template","    \"\"\"","    posts = Post.objects.filter(published_date__lte=timezone.now()","        ).order_by('-published_date')","    return render(request, \"blogposts.html\", {'posts': posts})","","","def post_detail(request, pk):","    \"\"\"","    Create a view that returns a single","    Post object based on the post ID (pk) and","    render it to the 'postdetail.html' template.","    Or return a 404 error if the post is","    not found","    \"\"\"","    post = get_object_or_404(Post, pk=pk)","    post.views += 1","    post.save()","    return render(request, \"postdetail.html\", {'post': post})","","","def create_or_edit_post(request, pk=None):","    \"\"\"","    Create a view that allows us to create","    or edit a post depending if the Post ID","    is null or not","    \"\"\"","    post = get_object_or_404(Post, pk=pk) if pk else None","    if request.method == \"POST\":","        form = BlogPostForm(request.POST, request.FILES, instance=post)","        if form.is_valid():","            post = form.save()","            return redirect(post_detail, post.pk)","    else:","        form = BlogPostForm(instance=post)","    return render(request, 'blogpostform.html', {'form': form})"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":49},"end":{"row":12,"column":49},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568397782035,"hash":"ad61df8521ce8d372928be78693484a510ac6c41"}