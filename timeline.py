#!/usr/bin/env python
# -*- coding: utf-8 -*-
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



import os
import sys
import gettext

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


import wx
from timelinelib.paths import LOCALE_DIR
from timelinelib.about import APPLICATION_NAME
from timelinelib.arguments import ApplicationArguments
from timelinelib.wxgui.dialogs.mainframe import MainFrame
from timelinelib.wxgui.dialogs.textdisplay import TextDisplayDialog
from timelinelib.unhandledex import create_error_message


#gettext.install(APPLICATION_NAME.lower(), LOCALE_DIR, unicode=True)

from gettext import gettext as _


from sugar.activity.activity import Activity


class TimeLine(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)

        iniciar_actividad()


def iniciar_actividad():
    application_arguments = ApplicationArguments()
    #application_arguments.parse_from(sys.argv[1:])
    application_arguments.parse_from()
    before_main_loop_hook=None
    app = wx.PySimpleApp()
    main_frame = MainFrame(application_arguments)
    main_frame.Show()
    sys.excepthook = unhandled_exception_hook
    if before_main_loop_hook:
        before_main_loop_hook()
    app.MainLoop()


def unhandled_exception_hook(type, value, tb):
    title = "Unexpected Error"
    text = create_error_message(type, value, tb)
    dialog = TextDisplayDialog(title, text)
    dialog.ShowModal()
    dialog.Destroy()


