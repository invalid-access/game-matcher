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
        'football_metric_defence',
        'football_metric_midfield',
        'football_metric_attack',
    )

    def football_metric_defence(self, player):
        return player.footballmetric.defence

    football_metric_defence.short_description = 'Speed'
    football_metric_defence.admin_order_field = 'footballmetric__defence'

    def football_metric_midfield(self, player):
        return player.footballmetric.midfield

    football_metric_midfield.short_description = 'Skill'
    football_metric_midfield.admin_order_field = 'footballmetric__midfield'

    def football_metric_attack(self, player):
        return player.footballmetric.attack

    football_metric_attack.short_description = 'Stamina'
    football_metric_attack.admin_order_field = 'footballmetric__attack'

    pass


class FootballMetricAdmin(admin.ModelAdmin):
    pass


admin.site.register(Playgroup, PlaygroupAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(FootballMetric, FootballMetricAdmin)
