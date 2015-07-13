from django.contrib import admin

from matcher.models import Playgroup, Player, FootballMetric

# Register your models here.


class PlaygroupAdmin(admin.ModelAdmin):
    pass


class FootballMetricStackedInline(admin.StackedInline):
    model = FootballMetric


class PlayerAdmin(admin.ModelAdmin):
    inlines = [FootballMetricStackedInline]
    list_display = (
        'first_name',
        'last_name',
        'football_metric_speed',
        'football_metric_skill',
        'football_metric_stamina',
        'football_metric_aggression',
    )

    def football_metric_speed(self, player):
        return player.footballmetric.speed

    football_metric_speed.short_description = 'Speed'
    football_metric_speed.admin_order_field = 'footballmetric__speed'

    def football_metric_skill(self, player):
        return player.footballmetric.skill

    football_metric_skill.short_description = 'Skill'
    football_metric_skill.admin_order_field = 'footballmetric__skill'

    def football_metric_stamina(self, player):
        return player.footballmetric.stamina

    football_metric_stamina.short_description = 'Stamina'
    football_metric_stamina.admin_order_field = 'footballmetric__stamina'

    def football_metric_aggression(self, player):
        return player.footballmetric.aggression

    football_metric_aggression.short_description = 'Aggression'
    football_metric_aggression.admin_order_field = 'footballmetric__aggression'

    pass


class FootballMetricAdmin(admin.ModelAdmin):
    pass


admin.site.register(Playgroup, PlaygroupAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(FootballMetric, FootballMetricAdmin)
