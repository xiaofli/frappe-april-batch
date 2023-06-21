# Copyright (c) 2023, Xiaofei Li and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymMembership(WebsiteGenerator):
	pass



@frappe.whitelist(allow_guest=True)
def get_all_info():
	print("=" * 20 )
	doc = frappe.get_doc("Gym Membership", "PLAN-Bronze-2-0003")
	one_doc_type = frappe.get_doc("DocType", "DocType")
	print(doc.plan_name)
	print(one_doc_type.name)
	print("=" * 20 )
	return doc, one_doc_type