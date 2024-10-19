from data.dataset import data
from data.rules import rules



def calculate_ae(rules):
      attribute_scores = {
            attr: 0 for attr in ['age', 'income', 'education', 'employment']
      }
      classes = set(rule['result'] for rule in rules)

      for cls in classes:
            relevant_rules = [rule for rule in rules if rule['result'] == cls]
            for attribute in attribute_scores.keys(): 
                  dont_care_count = sum(1 for rule in relevant_rules if attribute not in rule['condition'])
                  attribute_scores[attribute] += 1 - (dont_care_count / len(relevant_rules))
      return attribute_scores

def calculate_aa_and_mvd(rules, ae_scores):
      attribute_scores = {attr: {'aa': 0, 'values': set()} for attr in ae_scores.keys()}
      classes = set(rule['result'] for rule in rules)

      for cls in classes:
            relevant_rules = [rule for rule in rules if rule['result'] == cls]
            for attribute, score in attribute_scores.keys():
                  values = {rule['condition'][attribute] for rule in relevant_rules if attribute in rule['condition']}
                  attribute_scores[attribute]['values'].update(values)

                  attribute_scores[attribute]['aa'] += ae_scores[attribute] / len(relevant_rules)
      
      for attr, scores in attribute_scores.items():
            scores['mvd'] = len(scores['values'])

      return attribute_scores

def select_fit_attribute(ae_scores, aa_scores):
      best_attribute = None
      best_value = float('-inf')

      for attribute in aa_scores.keys():
            value = ae_scores[attribute] + aa_scores[attribute]['aa'] - aa_scores[attribute]['mvd']
            if value > best_value:
                  best_value = value
                  best_attribute = attribute
      
      return best_attribute

def classify_credit():
    results = []
    ae_scores = calculate_ae(rules)
    aa_scores = calculate_aa_and_mvd(rules, ae_scores)
    fit_attribute = select_fit_attribute(ae_scores, aa_scores)

    for person in data:
            credit_status = "Credit Denied"
            for rule in rules:
                  if rule["condition"](person):
                        credit_status = rule["result"]
                        break
            results.append({**person, "credit_status": credit_status})
    return results
