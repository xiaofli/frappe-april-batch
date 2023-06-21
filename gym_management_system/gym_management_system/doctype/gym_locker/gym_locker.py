# Copyright (c) 2023, Xiaofei Li and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymLocker(WebsiteGenerator):
	pass


@frappe.whitelist(allow_guest=True)
def book_locker(locker_id, user_id):
	# TODO: check if this locker has been booked
	print("user_id:", user_id)
	print("locker_id", locker_id)
	locker = frappe.get_doc("Gym Locker", locker_id)
	locker.user = user_id
	locker.available = "No"
	locker.save(
		ignore_permissions=True
	)
	return "You booked a locker successfully!"