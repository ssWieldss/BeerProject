import json

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from beer.forms import ManSignUpForm, ManSignInForm
from beer.models import Beer


def index(request):
    return render(request, 'beer/main_page.html')


def main_menu(request):
    return render(request, 'beer/main_menu.html')


def first_beer(request):
    return render(request, 'beer/paint_page.html')


def second_beer(request):
    return render(request, 'beer/second_paint.html')


def outro(request):
    return render(request, 'beer/authors.html')


def main_page(request):
    return render(request, 'beer/main_page.html')


class SignUpView(generic.CreateView):
    form_class = ManSignUpForm
    template_name = 'beer/registration.html'
    success_url = reverse_lazy('main_page')


class SignInView(LoginView):
    form_class = ManSignInForm
    template_name = 'beer/login.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('main_menu')


def logout_user(request):
    logout(request)
    return redirect('main_page')


def beer_all_view(request):
    beer = Beer.objects.all()
    context = {'beer': beer}
    return render(request, 'beer/main_menu.html', context=context)


class BeerView(generic.DetailView):
    model = Beer
    template_name = "beer/beer_page.html"
    context_object_name = "beer"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        try:
            if request.user.man in self.object.likes.all():
                context["like_flag"] = True
            else:
                context["like_flag"] = False
        except AttributeError:
            raise Http404("IMPOSTER!!!! You have no profile!")

        try:
            context["next"] = Beer.objects.get(pk=(self.object.pk + 1))
        except Beer.DoesNotExist:
            pass

        try:
            context["previous"] = Beer.objects.get(pk=(self.object.pk - 1))
        except Beer.DoesNotExist:
            pass
        return self.render_to_response(context)


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        try:
            user = request.user.man
            data = json.loads(request.body.decode())

            paint = get_object_or_404(Beer, pk=int(data.get("beerId")))
            flag = data.get("flag")
            print(user)

            if flag:
                # add a new like for a company
                paint.likes.add(user)
                # paint.save()
                message = 'You liked this'
            else:
                # user has already liked this company
                # remove like/user
                paint.likes.remove(user)
                # paint.save()
                message = 'You disliked this'

            ctx = {'likes_count': paint.total_likes}
            # use mimetype instead of content_type if django < 5
            return HttpResponse(json.dumps(ctx), content_type='application/json')
        except:
            return HttpResponse({"error": "Can't to make a like"})


def get_likes_count(request, pk):
    if request.method == 'GET':
        paint = get_object_or_404(Beer, pk=int(pk))
        ctx = {'likes_count': paint.total_likes}
        # use mimetype instead of content_type if django < 5
        return HttpResponse(json.dumps(ctx), content_type='application/json')
