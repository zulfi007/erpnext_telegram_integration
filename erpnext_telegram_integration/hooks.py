# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_telegram_integration"
app_title = "ERPNext SMS Notifications"
app_publisher = "Youssef Restom"
app_description = "SMS Notifications For Frappe - ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "youssef@totrox.com"
app_license = "MIT"

# Fixtures
# --------
fixtures = [
	{
		"dt": "Custom Field",
		"filters": [["dt", "in", ["SMS Settings", "SMS Notification"]]],
	}
]

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_update": [
			"erpnext_telegram_integration.sms_notifications.doctype.sms_notification.sms_notification.run_sms_notifications"
		],
		"on_cancel": [
			"erpnext_telegram_integration.sms_notifications.doctype.sms_notification.sms_notification.run_sms_notifications"
		],
		"on_trash": [
			"erpnext_telegram_integration.sms_notifications.doctype.sms_notification.sms_notification.run_sms_notifications"
		],
		"on_submit": [
			"erpnext_telegram_integration.sms_notifications.doctype.sms_notification.sms_notification.run_sms_notifications"
		],
	}
}
