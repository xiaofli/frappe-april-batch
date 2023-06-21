// Copyright (c) 2023, Xiaofei Li and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker', {
	refresh: function(frm) {
		frm.add_custom_button(__('Free This Locker'), function(){
			console.log(frm.doc);
			frm.set_value("available", "Yes");
			frm.set_value("user", null);
			frm.save();
		},);
	}
});
