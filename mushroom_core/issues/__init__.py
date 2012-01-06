from django.contrib import admin
from issues.models import *

admin.site.register(Issue)
admin.site.register(Project)
admin.site.register(Assign)
admin.site.register(Team)
admin.site.register(CoWork)
