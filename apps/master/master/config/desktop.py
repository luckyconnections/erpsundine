# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Master",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Master")
		},
		{
			"module_name": "Master",
			"color": "#589494",
			"icon": "octicon octicon-graph",
			"type": "module",
			"link": "http://sundinepro.com:3500/desk#List/Master%20Purchase%20Order/List/",
			"label": _("Master PO")
		},
		{
			"module_name": "Master",
			"color": "#589494",
			"icon": "octicon octicon-graph",
			"type": "module",
			"link": "http://sundinepro.com:3500/sales_order/",
			"label": _("Sales Map")
		},
		{
			"module_name": "Master",
			"color": "#589494",
			"icon": "octicon octicon-graph",
			"type": "module",
			"link": "http://sundinepro.com:3500/driver_location/",
			"label": _("Driver Location")
		},
		{
			"module_name": "Master",
			"color": "#589494",
			"icon": "octicon octicon-graph",
			"type": "module",
			"link": "http://sundinepro.com:3500/desk#qty-adjust/",
			"label": _("Adjust QTY")
		}	
	
	]
