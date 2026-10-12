goal = "Determine whether the stranger is female"

observation = "i am guy"




def reason_about_observation(observation):
    observation = observation.lower()
    if observation == "yes, am female":
        reasoning = "yes, am feamle means that starnger assuring as female"
    elif observation == "i am guy":
        reasoning = "guy means more indicates to male than female"
    elif observation == "i'm a woman":
        reasoning = "i'm a woman means that stranger asssuring as female"
    elif observation == "i'm a man":
        reasoning = "i'm a man means person is male"
    else:
        reasoning = "unknown observation is encountered"
    return reasoning

reasoning = reason_about_observation(observation)

def classify_observation(reasoning):
    if reasoning == "yes, am feamle means that starnger assuring as female":
        classification = "FEMALE"
    elif reasoning == "guy means more indicates to male than female":
        classification = "MALE"
    else:
        classification = "UNKNOWN"
    return classification
classification = classify_observation(reasoning)

def make_decision(classification):
    if classification == "FEMALE":
        decision = "match found"
    elif classification == "MALE":
        decision = "skip"
    else:
        decision = "skip"
    return decision
decision = make_decision(classification)

def take_action(decision):
    if decision == "skip":
        action = "skip stranger"
    elif decision == "match found":
        action = "notify user"
    return action
action = take_action(decision)

print(f"observation : {observation}")
print(f"reasoning is {reasoning}")
print(f"classification is {classification}")
print(f"decision is {decision}")
print(f"action is {action}")



def run_agent(observation):
    reasoning = reason_about_observation(observation)
    classification = classify_observation(reasoning)
    decision = make_decision(classification)
    action = take_action(decision)
    return {
        "reasoning" : reasoning,
        "classification" : classification,
        "decision" : decision,
        "action" : action
    }
result = run_agent("I'm a WOMAN")
print(result)
