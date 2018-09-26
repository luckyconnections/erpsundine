from __future__ import unicode_literals
import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

from datetime import datetime
from frappe.utils import getdate, validate_email_add, today, add_years,add_days,format_datetime
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice
from frappe.model.naming import make_autoname
from frappe import throw, _, scrub
import frappe.permissions
from frappe.model.document import Document
import json
import collections
# import urllib
# import urllib2

@frappe.whitelist()
def makePurchaseOrder(masterpo,method):
	#data=json.loads(json.dumps())	
	#data=json.dumps(result_list)
	#frappe.msgprint(str(data))
	return 
	# count=0
	# for row in masterpo.items:
	# 	data=frappe.get_doc({
	# 			"__islocal": 1,
	# 			"naming_series": "PO-",
	# 			"doctype": "Purchase Order",
	# 			"conversion_rate": 1,
	# 			"transaction_date": masterpo.transaction_date,
	# 			"supplier":row.supplier,
	# 			"docstatus": 1,
	# 			"buying_price_list": "Standard Buying",
	# 			"ignore_pricing_rule": 0,
	# 			"status": "Draft",
	# 			"schedule_date": row.schedule_date,
	# 			"name": "New Purchase Order 1",
	# 			"idx": 0,
	# 			"items": [{
	# 				"__islocal": 1,
	# 				"qty": row.qty,
	# 				"rate": row.rate,
	# 				"stock_uom": row.stock_uom,
	# 				"docstatus": 0,
	# 				"parent": "New Purchase Order 1",
	# 				"item_code": row.item_code,
	# 				"schedule_date": row.schedule_date,
	# 				"doctype": "Purchase Order Item",
	# 				"name": "New Purchase Order Item 1",
	# 				"parenttype": "Purchase Order",
	# 				"parentfield": "items",
	# 				"description": row.description,
	# 				"item_name": row.item_name,
	# 				"uom": row.uom,
	# 				"conversion_factor":row.conversion_factor
	# 			}],
	# 			"price_list_currency": "INR",
	# 			"plc_conversion_rate": 1,
	# 			"taxes_and_charges": masterpo.taxes_and_charges,
	# 			"__unsaved": 1
	# 		})
	# 	doc=data.insert(ignore_permissions=True)
	# 	if doc:
	# 		count=count+1
	# frappe.msgprint(str(count)+" "+"Purchase Order Added")

@frappe.whitelist()
def makeBackOrder(so,method):
	frappe.msgprint("Call")
	for row in so.items:
		if row.projected_qty<0:
			available=row.qty
		else:
			available=row.qty-row.projected_qty

		data=frappe.db.sql("""select parent from `tabBack Order Item` where sales_order_number=%s""",so.name)
		if data:
			frappe.msgprint("inside")
			getdoc=frappe.get_doc("Back Order",data[0][0])
			if row.projected_qty<row.qty:
				data=frappe.get_doc({
						"docstatus": 0,
						"doctype": "Back Order",
						"name": data[0][0],
						"modified":getdoc.modified,
						"naming_series": "SO-",
							"transaction_date": so.transaction_date,
							"items": [{
							"docstatus": 0,
							"doctype": "Back Order Item",
							"name": "New Back Order Item 1",
							"__islocal": 1,
							"__unsaved": 1,
							"owner": "Administrator",
							"parent": data[0][0],
							"parentfield": "items",
							"parenttype": "Back Order",
							"customer": "Administrator",
							"item_code": row.item_code,
							"order_qty": row.qty,
							"available_qty": row.projected_qty,
							"back_qty": available,
							"sales_order_number":so.name
						}]
					})
			doc=data.save()
			
		else:
			if row.projected_qty<row.qty:
				data=frappe.get_doc({
						"docstatus": 0,
						"doctype": "Back Order",
						"name": "New Back Order 1",
						"__islocal": 1,
						"__unsaved": 1,
						"naming_series": "SO-",
							"transaction_date": so.transaction_date,
							"items": [{
							"docstatus": 0,
							"doctype": "Back Order Item",
							"name": "New Back Order Item 1",
							"__islocal": 1,
							"__unsaved": 1,
							"owner": "Administrator",
							"parent": "New Back Order 1",
							"parentfield": "items",
							"parenttype": "Back Order",
							"customer": "Administrator",
							"item_code": row.item_code,
							"order_qty": row.qty,
							"available_qty": row.projected_qty,
							"back_qty": available,
							"sales_order_number":so.name
						}]
					})
			doc=data.insert()

		
	
	
	

