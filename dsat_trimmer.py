#!/usr/bin/env python
import argparse
from json_parser import *
from test_trimmer import *


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Trim DSAT PDF for reviewing missed questions only")
    parse.add_argument('-r', '--responses', type=str, help='Path to responses.json file')
    parse.add_argument('-t', '--template', type=str, help='Path to full DSAT pdf')
    parse.add_argument('-o', '--output', type=str,
                       help='Name to save trimmed test file to. Do not include ".pdf"')
    args = parse.parse_args()

    # Do the thing
    # Generate list of incorrect responses
    filtered_responses = generate_filter(args.responses)
    # Load template file
    user_template = load_test(args.template)
    # Create list of pages to filter from final
    target_pages = find_target_pages(user_template, filtered_responses)
    # Generate final PDF
    trim_test(target_pages, user_template, args.output)
