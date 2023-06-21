import frappe


def get_context(context):
    membership = ""
    professional_plan = ""
    workout_plan = ""

    memberships = frappe.db.get_list("Gym Membership Subscription",
                                     filters={
                                         'User': ['=', frappe.session.user]},
                                     fields=['name', 'membership']
                                     )
    if len(memberships) > 0:
        membership = memberships[0]['membership'].split('-')[-1]
    context.membership = membership

    professional_plans = frappe.db.get_list("Gym Professional Plan Subscription",
                                            filters={
                                                'User': ['=', frappe.session.user]},
                                            fields=[
                                                'name', 'professional_plan']
                                            )
    if len(professional_plans) > 0:
        professional_plan = professional_plans[0]['professional_plan']
    context.professional_plan = professional_plan

    workout_plans = frappe.db.get_list("Gym Workout Plan Subscription",
                                       filters={
                                           'User': ['=', frappe.session.user]},
                                       fields=['name', 'workout_plan']
                                       )
    if len(workout_plans) > 0:
        workout_plan = workout_plans[0]['workout_plan']
    context.workout_plan = workout_plan

    print("membership:", membership)
    print("professional_plan:", len(professional_plan))
    print("workout_plan:", workout_plan)

    return context
