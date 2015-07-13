import itertools
import random
import numpy

from .models import Playgroup, Player, FootballMetric

def match_metric(team1, team2):
    metric1 = numpy.array([
        sum([player.footballmetric.speed for player in team1]),
        sum([player.footballmetric.skill for player in team1]),
        sum([player.footballmetric.stamina for player in team1]),
        sum([player.footballmetric.aggression for player in team1]),
    ])
    metric2 = numpy.array([
        sum([player.footballmetric.speed for player in team2]),
        sum([player.footballmetric.skill for player in team2]),
        sum([player.footballmetric.stamina for player in team2]),
        sum([player.footballmetric.aggression for player in team2]),
    ])
    diff = metric1 - metric2
    return diff.dot(diff)


def get_matched_teams(players):
    matched_teams = []

    sorted_players_speed = sorted(players, key=lambda p: (
        -p.footballmetric.speed, p.footballmetric.skill, -p.footballmetric.stamina, p.footballmetric.aggression
    ))
    team1 = sorted_players_speed[0::2]
    team2 = sorted_players_speed[1::2]
    matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})

    sorted_players_skill = sorted(players, key=lambda p: (
        -p.footballmetric.skill, p.footballmetric.stamina, -p.footballmetric.aggression, p.footballmetric.speed
    ))
    team1 = sorted_players_skill[0::2]
    team2 = sorted_players_skill[1::2]
    matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})

    sorted_players_stamina = sorted(players, key=lambda p: (
        -p.footballmetric.stamina, p.footballmetric.aggression, -p.footballmetric.speed, p.footballmetric.skill
    ))
    team1 = sorted_players_stamina[0::2]
    team2 = sorted_players_stamina[1::2]
    matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})

    sorted_players_aggression = sorted(players, key=lambda p: (
        -p.footballmetric.aggression, p.footballmetric.speed, -p.footballmetric.skill, p.footballmetric.stamina
    ))
    team1 = sorted_players_aggression[0::2]
    team2 = sorted_players_aggression[1::2]
    matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})

    random.seed()
    for i in range(10):
        team1 = []
        team2 = []
        for player in players:
            if random.random() >= 0.5:
                team1.append(player)
            else:
                team2.append(player)
        matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})

    return matched_teams


def get_best_matched_teams(players):
    matched_teams = []
    combinations = itertools.combinations(players, len(players)/2)
    for team1 in combinations:
        team2 = [p for p in players if p not in team1]
        matched_teams.append({'diff': match_metric(team1, team2), 'team1': team1, 'team2': team2})
    sorted_matched_teams = sorted(matched_teams, key=lambda mt: mt['diff'])
    return sorted_matched_teams[0:10]


