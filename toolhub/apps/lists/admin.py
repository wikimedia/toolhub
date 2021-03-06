# Copyright (c) 2021 Wikimedia Foundation and contributors.
# All Rights Reserved.
#
# This file is part of Toolhub.
#
# Toolhub is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Toolhub is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Toolhub.  If not, see <http://www.gnu.org/licenses/>.
import django.contrib.admin

from reversion_compare.admin import CompareVersionAdmin

from rules.contrib.admin import ObjectPermissionsModelAdmin

from safedelete.admin import SafeDeleteAdmin
from safedelete.admin import highlight_deleted

from . import models


class ToolsInline(django.contrib.admin.TabularInline):
    """Tools in a list."""

    model = models.ToolList.tools.through
    extra = 1


@django.contrib.admin.register(models.ToolList)
class ToolListAdmin(
    CompareVersionAdmin,
    ObjectPermissionsModelAdmin,
    SafeDeleteAdmin,
):
    """Register with admin."""

    inlines = (ToolsInline,)
    exclude = ("tools",)
    list_display = (
        highlight_deleted,
        "favorites",
        "published",
        "created_by",
    )
    list_filter = (
        "created_by",
        "favorites",
        "published",
    ) + SafeDeleteAdmin.list_filter
    ordering = ("title",)
