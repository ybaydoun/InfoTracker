from django.apps import AppConfig
from django.conf import settings
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SurveyConfig(AppConfig):
    name = 'survey'


class SuitConfig(DjangoSuitConfig):
    menu_show_home = False

    menu = (
        ParentItem('Summary', url='/', icon='fa fa-list'),
        # ParentItem('Dashboard', url='/Dashboard', icon='fa fa-list'),
        ParentItem('Message Bank', children=[
            ChildItem('Messages', model='survey.message'),
            ChildItem('Audiences', model='survey.audience'),
            ChildItem('Sectors', model='survey.sector'),
            ChildItem('Sources', model='survey.source'),
            ChildItem('Outputs', model='survey.output'),
            ChildItem('Types', model='survey.type'),
        ], icon='fa fa-list'),
        ParentItem('Users', children=[
            ChildItem('Users', model='auth.user'),
            ChildItem('Groups', 'auth.group'),
        ], icon='fa fa-users'),
    )
