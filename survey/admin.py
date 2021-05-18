from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from survey.models import *
# from survey.forms import ResearchForm, KnowledgeTrackerForm
from .utils import has_group , get_default_formats

class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
        fields = (
            'id',
            # 'msg_number',
            'topic',
            'language',
            'channel',
            'audience',
            'sector',
            # 'adapted_by',
            'desired_output',
            'message_type',
            'english_message',
            'relevant_link',
        )
        export_order = fields


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin, VersionAdmin):
    resource_class = MessageResource

    # form = KnowledgeTrackerForm
    list_display = (
        'msg_number',
        'topic',
        'audience',
        'sector',
        # 'adapted_by',
        'desired_output',
        'message_type',
        # 'english_message',
        'relevant_link',
    )
    date_hierarchy = 'created'

    list_filter = (
        'topic',
        'audience',
        'sector',
        'adapted_by',
        'desired_output',
        'message_type',
    )
    suit_list_filter_horizontal = (
        'topic',
        'audience',
        'sector',
        'adapted_by',
        'desired_output',
        'message_type',
    )
    search_fields = (
        'msg_number',
        'topic',
        'audience',
        'sector',
        'adapted_by',
        'desired_output',
        'message_type',
        'english_message',
        'relevant_link',
    )
    readonly_fields = (
        'msg_number',
    )

    fieldsets = [
        ('Message details', {
            'fields': [
                'msg_number',
                'topic',
                'audience',
                'language',
                'sector',
                'adapted_by',
                'desired_output',
                'message_type',
                'channel',
                'relevant_link',
            ]
        }),
        ('English Messages', {
            'fields': [
                'english_message',
            ]
        }),
        ('Arabic Messages', {
            'fields': [
                'arabic_message',
            ]
        })
    ]

    def has_import_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return True
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     if has_group(request.user, 'EDITOR'):
    #         if obj and obj.created_by == request.user:
    #             return True
    #         return False
    #     return True

    # def get_readonly_fields(self, request, obj=None):
    #
    #     fields = [
    #         'issue_number',
    #         'reported_by',
    #         'issue_category',
    #         'issue_description',
    #         'target_population',
    #         'source',
    #         'answer',
    #         'validated_by_technical_committee',
    #         'validated_by_moph',
    #         'dissemination_method',
    #         'relevant_link',
    #     ]
    #
    #     if has_group(request.user, 'ADMIN'):
    #         fields = [
    #             'issue_number',
    #         ]
    #
    #     if has_group(request.user, 'EDITOR'):
    #         if obj:
    #             if obj.created_by == request.user:
    #                 fields = [
    #                     'issue_number',
    #                     'answer',
    #                     'validated_by_technical_committee',
    #                     'validated_by_moph',
    #                     'dissemination_method',
    #                     'relevant_link',
    #                 ]
    #             else:
    #                 fields = [
    #                     'issue_number',
    #                     'reported_by',
    #                     'issue_category',
    #                     'issue_description',
    #                     'target_population',
    #                     'source',
    #                     'answer',
    #                     'validated_by_technical_committee',
    #                     'validated_by_moph',
    #                     'dissemination_method',
    #                     'relevant_link',
    #                 ]
    #         else:
    #             fields = [
    #                 'issue_number',
    #                 'answer',
    #                 'validated_by_technical_committee',
    #                 'validated_by_moph',
    #                 'dissemination_method',
    #                 'relevant_link',
    #             ]
    #
    #     return fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.reported_by = request.user
        else:
            obj.modified_by = request.user

        super(MessageAdmin, self).save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     if has_group(request.user, 'EDITOR'):
    #         return KnowledgeTracker.objects.filter(created_by=request.user)
    #     return KnowledgeTracker.objects.all()


class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic
        fields = (
            'id',
            'name',
        )
        export_order = fields

class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource



class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
        fields = (
            'id',
            'name',
        )
        export_order = fields

class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource



class ChannelResource(resources.ModelResource):
    class Meta:
        model = Channel
        fields = (
            'id',
            'name',
        )
        export_order = fields

class ChannelAdmin(ImportExportModelAdmin):
    resource_class = ChannelResource


class AudienceResource(resources.ModelResource):
    class Meta:
        model = Audience
        fields = (
            'id',
            'name',
        )
        export_order = fields

class AudienceAdmin(ImportExportModelAdmin):
    resource_class = AudienceResource


class SectorResource(resources.ModelResource):
    class Meta:
        model = Sector
        fields = (
            'id',
            'name',
        )
        export_order = fields

class SectorAdmin(ImportExportModelAdmin):
    resource_class = SectorResource


class SourceResource(resources.ModelResource):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
        )
        export_order = fields

class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource


class OutputResource(resources.ModelResource):
    class Meta:
        model = Output
        fields = (
            'id',
            'name',
        )
        export_order = fields

class OutputAdmin(ImportExportModelAdmin):
    resource_class = OutputResource


class TypeResource(resources.ModelResource):
    class Meta:
        model = Type
        fields = (
            'id',
            'name',
        )
        export_order = fields

class TypeAdmin(ImportExportModelAdmin):
    resource_class = TypeResource

admin.site.register(Topic, TopicAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Channel, ChannelAdmin)

admin.site.register(Audience, AudienceAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Output, OutputAdmin)
admin.site.register(Type, TypeAdmin)
