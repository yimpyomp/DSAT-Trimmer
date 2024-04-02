#!/usr/bin/env python
import argparse
from json_parser import *
from test_trimmer import *
build_version = 'eMFdTrimmer v1.0.1\n\n'


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Trim DSAT PDF for reviewing missed questions only")
    parse.add_argument('-r', '--responses', type=str, help='Path to responses.json file')
    parse.add_argument('-t', '--template', type=str, help='Path to full DSAT pdf')
    parse.add_argument('-o', '--output', type=str,
                       help='Name to save trimmed test file to. Do not include ".pdf"')

    args = parse.parse_args()
    print(f'\n\n{build_version}')

    # Do the thing
    # Generate list of incorrect responses
    filtered_responses = generate_filter(args.responses)
    # Save text file containing filter data
    filter_only_title = args.output + '_filter_only.txt'
    save_filter(filtered_responses, filter_only_title)
    # Create pdf
    make_error_page(filter_only_title)
    # Load template file
    user_template = load_test(args.template)
    # Create list of pages to filter from final
    target_pages = find_target_pages(user_template, filtered_responses)
    # Generate final PDF, add error page
    trim_test(target_pages, user_template, filter_only_title.replace('.txt', '.pdf'), args.output)

