# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "Master"
app_title = "master"
app_publisher = "master"
app_description = "master"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/luckyconnection/css/luckyconnection.css"
# app_include_js = "/assets/luckyconnection/js/luckyconnection.js"

# include js, css files in header of web template
# web_include_css = "/assets/luckyconnection/css/luckyconnection.css"
# web_include_js = "/assets/luckyconnection/js/luckyconnection.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "luckyconnection.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "luckyconnection.install.before_install"
# after_install = "luckyconnection.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "luckyconnection.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Master Purchase Order": {
		"on_submit": "master.api.makePurchaseOrder"
	}
# 	#"Sales Order":{
# #		"on_submit":"master.api.makeBackOrder"
# #	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"luckyconnection.tasks.all"
# 	],
# 	"daily": [
# 		"luckyconnection.tasks.daily"
# 	],
# 	"hourly": [
# 		"luckyconnection.tasks.hourly"
# 	],
# 	"weekly": [
# 		"luckyconnection.tasks.weekly"
# 	]
# 	"monthly": [
# 		"luckyconnection.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "luckyconnection.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "luckyconnection.event.get_events"
# }

