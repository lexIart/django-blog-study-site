from django.shortcuts import render, get_object_or_404, redirect
from .models import *


class ObjectDetailMixin:
    model = None  # None because we gonna override variables values.
    template = None
    # method GET - GET requests processing.
    def get(self, request, slug):  # 2 - musthave argue. 3 - waiting for slug to catch by this method.
        obj = get_object_or_404(self.model, slug__iexact=slug)  # catching does not existing urls with django-method.
        # now taking a new object (post) with slug from DB.
        # iexact - exact that argue that we got from third func param.
        # after getting into the function, 'slug' become local variable that we using.
        # now rendering request.
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'admin_object': obj,
                                                       'detail': True,})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})


    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid() == True:
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:  # updating an existing element (model) of a project by a user in this method.
    model = None
    form_model = None
    template = None

    def get(self, request, slug):  # getting object.
        obj = self.model.objects.get(slug__iexact=slug)  # identify object (tag in this situation) as a slug.
        bound_form = self.form_model(instance=obj)  # taking an object from DB, creating bound form.
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin():
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))