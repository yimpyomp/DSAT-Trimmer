import json
mcq_reference = ['A', 'B', 'C', 'D', 'E']
module_headers = ["RW_Module1_Q", "RW_Module2_Q", "Math_Module1", "Math_Module2"]

'''
Target data is stored here:
data['responses'][0][0]['responses'] as a list of dicts
'''


def load_report(filepath: str) -> list:
    with open(filepath) as response_json:
        raw_report = json.load(response_json)
        response_json.close()
    # Isolating the useful part of the report
    return raw_report['responses'][0][0]['responses']


def convert_mcq(mcq_index):
    mcq_index = int(mcq_index)
    return mcq_reference[mcq_index]


def filter_responses(responses: list) -> list:
    incorrect_responses = []
    for entry in responses:
        next_entry = {}
        # Finding questions that were answered incorrectly
        try:
            if (entry["score"] < entry["max_score"]) or (entry["score"] == entry["max_score"] == 0):
                next_entry["Question"] = entry["item_reference"]
                next_entry["Absolute question"] = get_absolute_question(entry["item_reference"])
                # Convert response to proper letter if mcq, add whole answer otherwise
                if entry["question_type"] == "mcq":
                    next_entry["Student Answer"] = convert_mcq(entry["response"]["value"][0])
                else:
                    next_entry["Student Answer"] = entry["response"]["value"][0]
                # Add note for questions worth 0 points
                if entry["max_score"] == 0:
                    next_entry["Student Answer"] = next_entry["Student Answer"] + " Worth 0 Points"
                incorrect_responses.append(next_entry)
        except TypeError:
            pass
    return incorrect_responses


# Debug only
def test_me(sample_path):
    sample_report = load_report(sample_path)
    sample_responses = filter_responses(sample_report)
    for entry in sample_responses:
        print(entry)
    return sample_responses


def generate_filter(filepath):
    raw_report = load_report(filepath)
    filtered_responses = filter_responses(raw_report)
    return filtered_responses


def save_filter(filtered_responses, output_name):
    if '.txt' not in output_name:
        output_name += '.txt'
    filtered_filter = []
    for element in filtered_responses:
        next_element = element["Absolute question"] + ': ' + element["Student Answer"] + '\n'
        filtered_filter.append(next_element)
    with open(output_name, 'w') as f:
        f.writelines(filtered_filter)
    f.close()
    return None


def get_absolute_question(question_reference):
    # Initialize adjustment value, no adjustment needed for RW Module 1
    adjustment_value = 0
    # Check which module question belongs to, adjust accordingly
    if "RW_Module2" in question_reference:
        adjustment_value = 27
    elif "Math_Module1" in question_reference:
        adjustment_value = 81
    elif "Math_Module2" in question_reference:
        adjustment_value = 103
    unadjusted_index = isolate_question(question_reference)
    adjusted_index = adjustment_value + int(unadjusted_index)
    return "Question " + str(adjusted_index)


def isolate_question(reference_string):
    # Run through reference backwards until a non digit character is found
    container = []
    for character in reference_string[::-1]:
        if character.isdigit():
            container.append(character)
        else:
            break
    # Flip, join, return
    return ''.join(list(reversed(container)))


