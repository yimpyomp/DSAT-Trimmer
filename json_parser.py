import json
mcq_reference = ['A', 'B', 'C', 'D', 'E']

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
        absolute_question_number = responses.index(entry) + 1
        next_entry = {}
        # Finding questions that were answered incorrectly
        if entry["score"] < entry["max_score"]:
            next_entry["Question"] = entry["item_reference"]
            next_entry["Absolute question"] = "Question " + str(absolute_question_number)
            # Convert response to proper letter if mcq, add whole answer otherwise
            if entry["question_type"] == "mcq":
                next_entry["Student Answer"] = convert_mcq(entry["response"]["value"][0])
            else:
                next_entry["Student Answer"] = entry["response"]["value"][0]
            incorrect_responses.append(next_entry)
    return incorrect_responses


def test_me():
    sample_report = load_report('sample_data/responses.json')
    sample_responses = filter_responses(sample_report)
    for entry in sample_responses:
        print(entry)
    return sample_responses


if __name__ == '__main__':
    my_test = test_me()
