// Copyright (c) 2023, Xiaofei Li and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	refresh: function(frm) {
		frm.add_custom_button(__('Show Plan Name'), function(){
			frappe.msgprint(frm.doc.plan_name);
		},);
	}
});
