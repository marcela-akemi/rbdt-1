rules = [
    {"condition": lambda x: x['age'] < 18, "result": "Credit Denied: Minor"},
    {"condition": lambda x: x['income'] > 100000, "result": "Credit Approved: High Income"},
    {"condition": lambda x: x['income'] <= 50000 and x['education'] == 'High School', "result": "Credit Denied: Low Income with High School Education"},
    {"condition": lambda x: x['income'] > 50000 and x['employment'] == 'Unemployed', "result": "Credit Denied: Unemployed High Income"},
    {"condition": lambda x: x['age'] >= 18 and x['income'] <= 30000 and x['employment'] == 'Unemployed', "result": "Credit Denied: Adult Low Income Unemployed"},
    {"condition": lambda x: x['education'] in ['Master', 'PhD'] and x['employment'] == 'Employed', "result": "Credit Approved: Educated and Employed"},
]


def evaluate_rules(person):
    for rule in rules:
        if rule["condition"](person):
            return rule["result"]
    return "Credit Denied: No Conditions met"