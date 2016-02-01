from django.contrib import admin

from .models import Flaw, Experiment, ProtocolAttachment, TreatmentType, \
    Treatment


class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25
    fields = ('name', 'description')


class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'flaw', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'description', 'flaw', 'sort_order')
    list_per_page = 25
    fields = ('name', 'code', 'description', 'flaw', 'sort_order')


class ProtocolAttachmentAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'protocol')
    list_display_links = ('protocol',)
    search_fields = ('protocol',)
    list_per_page = 25
    fields = ('experiment', 'protocol')


class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'name', 'code', 'treatment_type',
        'placement', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('experiment', 'name', 'code', 'treatment_type',
        'placement', 'description')
    list_per_page = 25
    fields = ('experiment', 'name', 'code', 'treatment_type', 'placement',
        'description', 'sort_order')


class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')
    list_display_links = ('treatment_type',)
    search_fields = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')
    list_per_page = 25
    fields = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')


admin.site.register(Flaw, FlawAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(ProtocolAttachment, ProtocolAttachmentAdmin)
admin.site.register(TreatmentType, TreatmentTypeAdmin)
admin.site.register(Treatment, TreatmentAdmin)
