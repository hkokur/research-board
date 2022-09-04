from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy
# Models
from boards.models import Board
# Views
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)


class BoardList(ListView):
    context_object_name = "board_list"
    template_name = "boards/board_list.html"

    def get_queryset(self):
        # get boards through logged user
        try:
            boards = self.request.user.boards.all()
        except AttributeError:
            # create empty query set 
            boards = Board.objects.none()
        return boards


class BoardCreate(CreateView):
    model = Board
    fields = ["title","description"]
    template_name = "form.html"
    success_url = reverse_lazy("board-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BoardDetail(DetailView):
    model = Board
    context_object_name = "board"
    template_name = "boards/board_detail.html"
    # we use uuid as a slug because slug is not uniqe
    slug_field = 'uuid'
    slug_url_kwarg = "board_uuid"

    def get_context_data(self, **kwargs):
        board_list = get_list_or_404(Board, owner=self.request.user)
        kwargs['board_list'] = board_list
        return super().get_context_data(**kwargs)
    

class BoardDelete(DeleteView):
    model = Board
    template_name = "boards/board_delete.html"
    context_object_name = "board"
    slug_field = "uuid"
    slug_url_kwarg = "board_uuid"
    success_url = reverse_lazy("board-list")

    def post(self, request, *args, **kwargs):
        cards = self.get_object().urlcards.all()
        for card in cards:
            card.delete()
        return super().post(request, *args, **kwargs)


class BoardUpdate(UpdateView):
    model = Board
    fields = ["title", "description"]
    template_name = "form.html"
    slug_field = "uuid"
    slug_url_kwarg = "board_uuid"
    success_url = reverse_lazy("board-list")