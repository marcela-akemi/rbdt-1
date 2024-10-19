from data.dataset import data
from data.rules import rules

def classify_credit():
    results = []
    for person in data:
            credit_status = "Credit Denied"
            for rule in rules:
                  if rule["condition"](person):
                        credit_status = rule["result"]
                        break
            results.append({**person, "credit_status": credit_status})
    return results

def calculate_ae(rules):
      attribute_scores = {
            attr: 0 for attr in ['age', 'income', 'education', 'employment']
      }
      classes = set(rule['result'] for rule in rules)

      for cls in classes:
            relevant_rules = [rule for rule in rules if rule['result'] == cls]