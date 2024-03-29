from pypdf import PdfReader, PdfWriter
from json_parser import *


def load_test(test_path):
    test_reader = PdfReader(test_path)
    return test_reader


def find_target_pages(test_reader, target_responses):
    target_pages = []
    last_page = 0
    upper_bound = test_reader._get_num_pages()
    for entry in target_responses:
        target = entry['Absolute question']
        print(f'Searching for {target}')
        for page in range(last_page, upper_bound):
            # Check if question is contained on the page
            current_text = test_reader.pages[page].extract_text()
            if target in current_text:
                target_pages.append(page)
                last_page = page
            else:
                continue
    return target_pages


def trim_test(target_pages, test_reader, save_name):
    save_path = save_name + '.pdf'
    trimmed_writer = PdfWriter()
    for page in target_pages:
        trimmed_writer.add_page(test_reader.pages[page])
    trimmed_test = open(save_path, 'wb')
    trimmed_writer.write(trimmed_test)
    trimmed_writer.close()
    trimmed_test.close()
    print('Done')
    return None

