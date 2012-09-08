#!/usr/bin/env python
#
# Copyright (C) 2009, 2010, 2011  Rickard Lindberg, Roger Lindberg
#
# This file is part of Timeline.
#
# Timeline is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Timeline is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Timeline.  If not, see <http://www.gnu.org/licenses/>.

import gettext
import locale
import os
import platform
import sys
import ConfigParser

sys.path.insert(0, "libs")
sys.path.insert(0, "timelinelib")

# Make sure that we can import timelinelib
sys.path.insert(0, os.path.dirname(__file__))
# Make sure that we can import pysvg
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs", "dependencies", "pysvg-0.2.1"))
# Make sure that we can import icalendar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs", "dependencies", "icalendar-2.1"))
# Make sure that we can import markdown
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs", "dependencies", "markdown-2.0.3"))

from timelinelib.config.arguments import ApplicationArguments
from timelinelib.wxgui.setup import start_wx_application

from sugar.activity.activity import Activity


class TimeLine(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)

        iniciar_actividad()

def iniciar_actividad():

    file_activity_info = ConfigParser.ConfigParser()
    activity_info_path = os.path.abspath('./activity/activity.info')
    file_activity_info.read(activity_info_path)
    bundle_id = file_activity_info.get('Activity', 'bundle_id')
    path = os.path.abspath('locale')

    gettext.install(bundle_id, path, unicode=True)

    application_arguments = ApplicationArguments()
    application_arguments.parse_from()

    start_wx_application(application_arguments)

