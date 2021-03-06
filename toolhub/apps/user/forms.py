# Copyright (c) 2020 Wikimedia Foundation and contributors.
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
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from .models import ToolhubUser


class ToolhubUserCreationForm(UserCreationForm):
    """Form for creating a new ToolhubUser."""

    class Meta:
        """Configure form."""

        model = ToolhubUser
        fields = ("username", "email")


class ToolhubUserChangeForm(UserChangeForm):
    """Form for updating an existing ToolhubUser."""

    class Meta:
        """Configure form."""

        model = ToolhubUser
        fields = "__all__"
