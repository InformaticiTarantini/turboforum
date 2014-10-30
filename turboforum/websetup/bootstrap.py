# -*- coding: utf-8 -*-
"""Setup the turboforum application"""
from __future__ import print_function

import logging
from tg import config
from turboforum import model

def bootstrap(command, conf, vars):
    """Place any commands to setup turboforum here"""

    # <websetup.bootstrap.before.auth
    g = model.Group()
    g.group_name = 'admins'
    g.display_name = 'Administrators'

    g1 = model.Group()
    g1.group_name = 'moderators'
    g1.display_name = 'Moderators'

    g2 = model.Group()
    g2.group_name = 'users'
    g2.display_name = 'Users'

    u = model.User()
    u.user_name = 'admin'
    u.display_name = 'Admin'
    u.email_address = 'admin@turboforum.com'
    u.groups = [g]
    u.password = 'adminpass'

    model.DBSession.flush()
    model.DBSession.clear()

    # <websetup.bootstrap.after.auth>
