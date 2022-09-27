from fuzzywuzzy import fuzz

from AutomationFramework_DDT.utils import get_input_data, validation, test_driven


def test_case(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)
    validation(similarity)
    return similarity


if __name__ == '__main__':
    data = get_input_data(
        "/03 - AutomationFramework_DDT/TestData/input_data.json")
    print(data)
    output = test_driven(data, test_case)  # nu apelam functia, ci doar ii returnam numele pentru a putea fi folosita mai departe
    print(output)
