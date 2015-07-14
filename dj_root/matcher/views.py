from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from matcher.models import Playgroup, Player, FootballMetric
import utils

# Create your views here.


class PlayerList(ListView):
    model = Player


class PlayerCreate(CreateView):
    model = Player
    success_url = reverse_lazy('player_list')
    fields = ['playgroup', 'first_name', 'last_name']


class PlayerUpdate(UpdateView):
    model = Player
    success_url = reverse_lazy('player_list')
    fields = ['playgroup', 'first_name', 'last_name']


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def match(request, playgroup_id):
    playgroup = get_object_or_404(Playgroup, id=playgroup_id)
    player_list = get_list_or_404(Player.objects.filter(playgroup=playgroup).order_by('first_name'))

    present_players = player_list
    matched_teams = None
    if request.method == 'POST':
        is_present = {}
        for player in player_list:
            try:
                footballmetric = player.footballmetric

                if not footballmetric:
                    footballmetric = FootballMetric(player=player)

                footballmetric.defence = int(request.POST['defence' + str(player.id)])
                footballmetric.midfield = int(request.POST['midfield' + str(player.id)])
                footballmetric.attack = int(request.POST['attack' + str(player.id)])
                footballmetric.save()

                is_present[player] = request.POST.get('is_present' + str(player.id), u'off')
            except (KeyError, TypeError, ValidationError):
                pass

        present_players = [player for player in is_present if is_present[player] == u'on']
        matched_teams = utils.get_best_matched_teams(present_players)

    context = {
        'playgroup': playgroup,
        'player_list': player_list,
        'matched_teams': matched_teams,
        'present_players': present_players
    }

    return render(request, 'matcher/match.html', context)

