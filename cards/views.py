from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
# Views
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
# Models
from .models import UrlCard, Url
from boards.models import Board


class UrlCardCreate(CreateView):
    model = UrlCard
    template_name = "form.html"
    fields = ["title"]

    def get_success_url(self):
        board = get_object_or_404(Board, uuid = self.kwargs.get("board_uuid"))
        return reverse('board-detail', kwargs={"board_slug": board.slug, "board_uuid" : board.uuid })

    def form_valid(self, form):
        response = super().form_valid(form)
        # we must save the m2m relationship after creation
        self.object.boards.add(get_object_or_404(Board, uuid = self.kwargs.get("board_uuid")))
        self.object.save()
        return response


class UrlCardUpdate(UpdateView):
    model = UrlCard
    fields = ["note"]
    template_name = "cards/urlcard_update.html"
    slug_field = "uuid"
    slug_url_kwarg = "urlcard_uuid"
    context_object_name = "urlcard"

    def get_success_url(self):
        return reverse("urlcard-update", kwargs= {
            "urlcard_slug" : self.kwargs.get("urlcard_slug"),
            "urlcard_uuid"  : self.kwargs.get("urlcard_uuid"),
        })


class UrlCardDelete(DeleteView):
    model = UrlCard
    slug_field = "uuid"
    slug_url_kwarg = "urlcard_uuid"

    def get_success_url(self):
        return reverse("board-detail", kwargs = {
            'board_slug' : self.object.boards.all()[0].slug,
            'board_uuid' : self.object.boards.all()[0].uuid,
        })

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UrlCreate(CreateView):
    model = Url
    fields = ["url"]
    template_name = "form.html"

    def get_success_url(self):
        urlcard = get_object_or_404(UrlCard, uuid = self.kwargs.get("urlcard_uuid"))
        return reverse("urlcard-update", kwargs={
            "urlcard_slug" : urlcard.slug ,
            "urlcard_uuid" : urlcard.uuid ,
        })

    def form_valid(self, form):
        urlcard = get_object_or_404(UrlCard, uuid = self.kwargs.get("urlcard_uuid"))
        form.instance.card = urlcard
        return  super().form_valid(form)


class UrlDelete(DeleteView):
    model = Url
    slug_field = "uuid"
    slug_url_kwarg = "url_uuid"

    def get_success_url(self):
        return reverse('urlcard-update', kwargs={
            "urlcard_slug" : self.object.card.slug,
            "urlcard_uuid" : self.object.card.uuid,
        })

    # redirect get request to post because i don't want to serve any approvement page 
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
