from data.dataset import data
from data.rules import rules

def calculate_ae(rules):
    attribute_scores = {attr: 0 for attr in ['age', 'income', 'education', 'employment']}
    
    for rule in rules:
        for attribute in attribute_scores.keys():
            if attribute not in rule.attributes_involved:
                attribute_scores[attribute] += 1  # ‘don't care’ situation
    
    return attribute_scores


def calculate_aa_and_mvd(rules, ae_scores):
    attribute_scores = {attr: {'aa': 0, 'values': set()} for attr in ae_scores.keys()}
    
    for rule in rules:
        for attribute in attribute_scores.keys():
            if attribute in rule.attributes_involved:
                attribute_scores[attribute]['values'].add(attribute)
                attribute_scores[attribute]['aa'] += ae_scores[attribute]
    
    for attr, scores in attribute_scores.items():
        scores['mvd'] = len(scores['values'])
    
    return attribute_scores

def select_fit_attribute(ae_scores, aa_scores):
    """
    Selects the most suitable attribute for classification based on attribute evaluation scores.

    Parameters:
    ae_scores (dict): A dictionary containing attribute evaluation scores (AE) for each attribute.
    aa_scores (dict): A dictionary containing attribute accuracy scores (AA) and distinct values (MVD) for each attribute.

    Returns:
    str: The name of the most suitable attribute for classification.
    """
    best_attribute = None
    best_value = float('-inf')

    for attribute, scores in aa_scores.items():
        value = ae_scores[attribute] + scores['aa'] - scores['mvd']
        if value > best_value:
            best_value = value
            best_attribute = attribute

    return best_attribute



def classify_credit():
    """
    Classifies credit status for each person in the dataset based on the given rules.

    The function calculates attribute evaluation scores (AE) and attribute accuracy scores (AA) and distinct values (MVD)
    for each attribute. It then selects the most suitable attribute for classification based on these scores.
    Finally, it applies the rules to each person in the dataset to determine their credit status.

    Parameters:
    None

    Returns:
    list: A list of dictionaries, where each dictionary represents a person with their attributes and the assigned credit status.
    """
    results = []
    ae_scores = calculate_ae(rules)
    aa_scores = calculate_aa_and_mvd(rules, ae_scores)
    fit_attribute = select_fit_attribute(ae_scores, aa_scores)

    for person in data:
        credit_status = "Credit Denied"
        relevant_rules = [rule for rule 
                          in rules 
                          if fit_attribute 
                          in rule.attributes_involved]

        for rule in relevant_rules:
            if rule.condition(person):
                credit_status = rule.result
                break

        if credit_status == "Credit Denied":
            for rule in rules:
                if rule.condition(person):
                    credit_status = rule.result
                    break

        results.append({**person, "credit_status": credit_status})

    return results



