from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from survey.models import *
# from survey.forms import ResearchForm, KnowledgeTrackerForm
from .utils import has_group


class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
        fields = (
            'msg_number',
            'audience',
            'sector',
            'adapted_by',
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
class MessageAdmin(ExportActionModelAdmin, VersionAdmin):
    resource_class = MessageResource
    # form = KnowledgeTrackerForm
    list_display = (
        'msg_number',
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
        'audience',
        'sector',
        'adapted_by',
        'desired_output',
        'message_type',
    )
    suit_list_filter_horizontal = (
        'audience',
        'sector',
        'adapted_by',
        'desired_output',
        'message_type',
    )
    search_fields = (
        'msg_number',
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
                'audience',
                'sector',
                'adapted_by',
                'desired_output',
                'message_type',
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

    # def has_import_permission(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return True
    #     return False
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


admin.site.register(Audience)
admin.site.register(Sector)
admin.site.register(Source)
admin.site.register(Output)
admin.site.register(Type)
