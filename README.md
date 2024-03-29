# This is a work in progress, currently I have not tested functionality on anything other than Linux.

## DSAT Trimmer: Trim a full DSAT DT/IT PDF to only the pages containing missed responses.

### Basic usage:
1. Ensure *Python 3.10.9 or greater* is installed on your machine.
    * The Windows installer can be found [here](https://www.python.org/downloads/release/python-3109/)
    * When installing, ensure that you select the option to add Python to PATH on the initial splash screen.
2. Clone the repository to your machine using your preferred method
    * For Windows machines downloading and extracting the zip file will be the simplest method.
    * I recommend creating a directory to house both the current report you are using, full DSAT, _and_ the DSAT-Trimmer-main folder.
3. Install dependencies
    * _Windows Users skip to next_ A requirements.txt file *is* included. To install requirements, run the following in your terminal:
        * pip -r install requirements.txt
    * For Windows:
        * Open PowerShell. You can find it by using: Windows Key > PowerShell
        * Navigate to directory containing the scripts. This is done using the command 'cd'. Tab can be used to autocomplete directories, directories are separated by '\'.
        * Example usage for scripts saved to desktop directory DSAT_trimmer:
            * cd .\Desktop\DSAT_trimmer\DSAT-Trimmer-main
            * pip install -r requirements.txt
    * This will install the dependencies required for proper operation of the program. At the time of writing, the only dependencies not part of the Python standard library is pypdf
4. Run the program. Required arguments, in order of appearance are:
    1. -r/--responses: responses.json file containing student responses
    2. -t/--template: Filepath of *blank* DT/IT to be trimmed. This argument *requires you to include the full filepath, including the .pdf file extension*
    3. -o/--output: Name to save trimmed test to. *Do not include the .pdf file extension here. The program handles that*
    * _Example Windows Usage:_
        *  .\DSAT-Trimmer-main\dsat_trimmer.py -r responses.json -t _name of your blank DSAT_ -o _name of output pdf_
    *  This will produce two files, the first is a PDF containing only the pages containing incorrect answers. The second is a text file containing the student's original answers.

### Notes and Planned Updates
* As stated, I have not tested this implementation in any way whatsoever on anything other than Linux, I will get to this when I can.
* There is no current method in place to modify the output file to display the student's original answer. I will work on adding this feature as I am able to.
* I understand that the inconsistent requirement of when to add file extension is confusing, I am working on changing this as well. 

### Feedback
* Please direct any and all feedback on the functionality to Enzi at my work email, or in person, so I can work on implementing it. I am aware that the current output of the missed answers is not in the most readable format, and I am open to any suggestions on how to optimize it for readability. I'll work on implementing a GUI at some point if this tool ends up being used very much.
