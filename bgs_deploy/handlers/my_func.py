# -*- coding: utf-8 -*-

from bgs_deploy.devops.config_init import config

def handler(event, context):
    msg = "Hello {}! This is a demo project called %s" % config.PROJECT_NAME.get_value()
    if event.get("name"):
        return msg.format(event.get("name"))
    else:
        return msg.format("World")
