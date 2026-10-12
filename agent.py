goal = "Determine whether the stranger is female"

observation = input("Enter your observation: ")

def reason_about_observation(observation):
    observation = observation.lower()
    if observation == "yes, am female":
        reasoning = "yes, am feamle means that starnger assuring as female"
        classification = "FEMALE"
    elif observation == "i am guy":
        reasoning = "guy means more indicates to male than female"
        classification = "MALE"
    elif observation == "i'm a woman":
        reasoning = "i'm a woman means that stranger asssuring as female"
        classification = "FEMALE"
    elif observation == "i'm a man":
        reasoning = "i'm a man means person is male"
        classification = "MALE"
    elif "not" in observation and "woman" in observation:
        reasoning = "not & woman refers as refuse to be a woman"
        classification = "UNKNOWN"
    elif "am" in observation and "woman" in observation:
        reasoning = "am & woman refers to female"
        classification = "FEMALE"
    else:
        reasoning = "unknown observation is encountered"
        classification = "UNKNOWN"
    return reasoning, classification

def make_decision(classification):
    if classification == "FEMALE":
        decision = "match found"
    elif classification == "MALE":
        decision = "skip"
    elif classification == "UNKNOWN":
        decision = "need more information"
    else:
        decision = "skip"
    return decision


def take_action(decision):
    if decision == "skip":
        action = "skip stranger"
    elif decision == "match found":
        action = "notify user"
    elif decision == "need more information":
        action = "ask for clarification"
    return action



def run_agent(observation):
    reasoning, classification = reason_about_observation(observation)
    decision = make_decision(classification)
    action = take_action(decision)
    return {
        "reasoning" : reasoning,
        "classification" : classification,
        "decision" : decision,
        "action" : action
    }
result = run_agent(observation)
print(result)
