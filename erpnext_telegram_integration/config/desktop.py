# coding=utf-8

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "SMS Notifications",
			"category": "Administration",
			"label": _("SMS Notifications"),
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module",
			"description": "SMS Notifications For ERPNext."
		}
	]
