from enums.enumClasses import *
# rules = [
#     {"condition": lambda x: x['age'] < 18, "result": "Credit Denied: Minor"},
#     {"condition": lambda x: x['income'] > 100000, "result": "Credit Approved: High Income"},
#     {"condition": lambda x: x['income'] <= 50000 and x['education'] == 'High School', "result": "Credit Denied: Low Income with High School Education"},
#     {"condition": lambda x: x['income'] > 50000 and x['employment'] == 'Unemployed', "result": "Credit Denied: Unemployed High Income"},
#     {"condition": lambda x: x['age'] >= 18 and x['income'] <= 30000 and x['employment'] == 'Unemployed', "result": "Credit Denied: Adult Low Income Unemployed"},
#     {"condition": lambda x: x['education'] in ['Master', 'PhD'] and x['employment'] == 'Employed', "result": "Credit Approved: Educated and Employed"},
# ]

# rules = [
#     {"condition": lambda x: x['age'] < 18, "result": "Credit Denied: Minor"},
#     {"condition": lambda x: x['income'] > 100000, "result": "Credit Approved: High Income"},
#     {"condition": lambda x: x['income'] <= 50000 and x['education'] == 'High School', "result": "Credit Denied: Low Income with High School Education"},
#     {"condition": lambda x: x['income'] > 50000 and (x['employment'] == 'Unemployed'), "result": "Credit Denied: Unemployed High Income"},
#     {"condition": lambda x: x['age'] >= 18 and x['income'] <= 30000 and (x['employment'] == 'Unemployed' or x['employment'] == 'dont_care'), "result": "Credit Denied: Adult Low Income Unemployed"},
#     {"condition": lambda x: (x['education'] in ['Master', 'PhD']) and (x['employment'] == 'Employed' or x['employment'] == 'dont_care'), "result": "Credit Approved: Educated and Employed"},
# ]


class Rule:
    def __init__(self, condition, result, attributes_involved):
        self.condition = condition
        self.result = result
        self.attributes_involved = attributes_involved

# rules = [
#     {"condition": lambda x: x['age'] < 18, "result": "Credit Denied: Minor"},
#     {"condition": lambda x: x['income'] > 100000, "result": "Credit Approved: High Income"},
#     {"condition": lambda x: x['income'] <= 50000 and x['education'] == Education.high_school.value, "result": "Credit Denied: Low Income with High School Education"},
#     {"condition": lambda x: x['income'] > 50000 and x['employment'] ==  Employment.unemployment.value, "result": "Credit Denied: Unemployed High Income"},
#     {"condition": lambda x: x['age'] >= 18 and x['income'] <= 30000 and (x['employment'] == Employment.unemployment.value or x['employment'] == Employment.dont_care.value), "result": "Credit Denied: Adult Low Income Unemployed"},
#     {"condition": lambda x: (x['education'] in [Education.master.value, Education.phd.value]) and (x['employment'] == Employment.employed.value or x['employment'] == 'dont_care'), "result": "Credit Approved: Educated and Employed"},
#     {"condition": lambda x: x['employment'] != Employment.unemployment.value, "result": "Credit Approved: All Other Conditions"},
# ]
rules = [
    Rule( lambda x: 
            x['age'] < 18 and x['employment'] == Employment.dont_care.value
        ,   "Credit Denied: Minor"
        ,   ['age']
        ),
    Rule( lambda x: 
            x['income'] > 100000
        ,   "Credit Approved: High Income"
        ,   ['income']
        ),
    Rule( lambda x: 
            x['income'] <= 50000 and x['education'] == Education.high_school.value
        ,   "Credit Denied: Low Income with High School Education"
        ,   ['income', 'education']
        ),
    Rule( lambda x: 
            x['income'] > 50000 and x['employment'] ==  Employment.unemployment.value
        ,   "Credit Denied: Unemployed High Income"
        ,   ['employment']
        ),
    Rule( lambda x: 
            x['age'] >= 18 and x['income'] <= 30000 and (x['employment'] == Employment.unemployment.value or x['employment'] == Employment.dont_care.value)
        ,   "Credit Denied: Adult Low Income Unemployed"
        ,   ['age', 'income'] 
        ),
    Rule( lambda x: (
            x['education'] in [Education.master.value, Education.phd.value]) 
            and (x['employment'] == Employment.employed.value or x['employment'] == 'dont_care')
        ,   "Credit Approved: Educated and Employed"
        ,   ['education', 'employment']
        ),
    Rule( lambda x: 
            x['employment'] != Employment.unemployment.value,
            "Credit Approved: All Other Conditions"
        ,   ['employment']
    )
]


def evaluate_rules(person):
    return next((rule["result"] for rule in rules if rule["condition"](person)), "Credit Denied: No Conditions met")
