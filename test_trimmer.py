from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pathlib


module_titles = ["Section 1, Module 1: Reading and Writing", "Section 1, Module 2: Reading and Writing",
                 "Section 2, Module 1: Math", "Section 2, Module 2: Math"]


def load_test(test_path):
    test_reader = PdfReader(test_path)
    return test_reader


def find_target_pages(test_reader, target_responses):
    # Create
    target_pages = []
    upper_bound = test_reader._get_num_pages()
    for entry in target_responses:
        target = entry['Absolute question']
        print(f'Searching for {target}')
        for page in range(upper_bound):
            # Check if question is contained on the page
            current_text = test_reader.pages[page].extract_text()
            if target in current_text:
                target_pages.append(page)
                # Check if next question appears on the page, if not, add one more page to ensure entire question
                # is included
                next_question = increment_target(target)
                try:
                    if next_question not in current_text:
                        target_pages.append(page + 1)
                        break
                except IndexError:
                    pass
                break

    return filter_duplicate_pages(target_pages)


def trim_test(target_pages, test_reader, error_path, save_name):
    error_page = PdfReader(error_path)
    error_path = pathlib.Path(error_path)
    save_path = save_name + '.pdf'
    trimmed_writer = PdfWriter()
    # Add pages of error report
    for page in error_page.pages:
        trimmed_writer.add_page(page)
    # Delete error report
    pathlib.Path(error_path).unlink()
    for page in target_pages:
        trimmed_writer.add_page(test_reader.pages[page])
    trimmed_test = open(save_path, 'wb')
    trimmed_writer.write(trimmed_test)
    trimmed_writer.close()
    trimmed_test.close()
    print('Done')
    return None


def make_error_page(error_file_path):
    output_path = error_file_path.replace('.txt', '.pdf')
    # Create a canvas
    c = canvas.Canvas(output_path, pagesize=letter)

    # Open the input text file
    with open(error_file_path, 'r') as f:
        lines = f.readlines()

    # Set font and size
    c.setFont("Helvetica", 10)

    # Write each line to the PDF
    y = 750  # Starting y position (you can adjust this)
    x_position = 50
    for line in lines:
        c.drawString(x_position, y, line.strip())
        y -= 20  # Move to the next line
        # Moving over, resetting y position if bottom of page is reached
        if y == 10:
            x_position += 100
            y = 750

    # Save the PDF
    c.save()

    # Delete text file
    pathlib.Path(error_file_path).unlink()
    return None


def increment_target(target_question):
    # Get numbers from question
    question_number = []
    for character in target_question[::-1]:
        if character.isdigit():
            question_number.append(character)
        else:
            break
    # Flip number, increment, return
    next_question_number = int(''.join(question_number[::-1])) + 1
    return 'Question ' + str(next_question_number)


def filter_duplicate_pages(page_list):
    final_list = [page_list[0]]
    for i in range(1, len(page_list)):
        if page_list[i] not in final_list:
            final_list.append(page_list[i])
    return final_list
