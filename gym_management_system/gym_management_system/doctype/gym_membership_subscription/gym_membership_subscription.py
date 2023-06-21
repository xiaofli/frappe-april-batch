# Copyright (c) 2023, Xiaofei Li and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class GymMembershipSubscription(Document):
	pass





@frappe.whitelist(allow_guest=True)
def new_membership_subscription(user_id, plan):
	membership_plan = plan
	doc = frappe.new_doc("Gym Membership Subscription")
	doc.user = user_id
	doc.membership = membership_plan
	print("\n" * 5)
	print(user_id, membership_plan)
	print("\n" * 5)
	doc.insert(ignore_permissions=True)
	return "Nice Job!"
