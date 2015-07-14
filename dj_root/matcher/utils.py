import itertools
import random
import numpy

from .models import Playgroup, Player, FootballMetric

def match_metric(team1, team2):
    metric1 = numpy.array([
        sum([player.footballmetric.defence for player in team1]),
        sum([player.footballmetric.midfield for player in team1]),
        sum([player.footballmetric.attack for player in team1]),
    ])
    metric2 = numpy.array([
        sum([player.footballmetric.defence for player in team2]),
        sum([player.footballmetric.midfield for player in team2]),
        sum([player.footballmetric.attack for player in team2]),
    ])
    diff = metric1 - metric2
    return diff.dot(diff)


def get_best_matched_teams(players):
    matched_teams = []
    combinations = itertools.combinations(players, len(players)/2)
    for team1 in combinations:
        team2 = [p for p in players if p not in team1]
        matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})
    sorted_matched_teams = sorted(matched_teams, key=lambda mt: mt['diff'])
    return sorted_matched_teams[0:10]


