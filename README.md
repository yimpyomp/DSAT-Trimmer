# This is a work in progress, compatability has been tested on Linux as well as a personal, unmanaged machine running Windows 10.

## DSAT Trimmer: Trim a full DSAT DT/IT PDF to only the pages containing missed responses.
## Known Issues
* Extra pages of template PDF is being included regardless of whether it contains a question answered incorrectly
* Equations are not rendered in final missed questions page 
### Obtaining Necessary Brightspace DSAT Files
* The program requires two components to operate, the responses.json file _and_ a blank DSAT template
* To download the responses file:
    * Navigate to the student you are attempting to generate the trimmed test for
    * Using the Content Browser, choose any option. This will lead you to a new page containing all of the assignments supported on Brightspace
    * Select the appropriate test from the column on the left side of the screen
        * The box for the selected item will open, showing a second option for the same test just below the original box, there will be an gray icon that looks like a puzzle piece to the left of the title. Click this box
    * Near the top of the area where the test information is displayed, there will be four icons, a pencil, bar graph, eye, and three vertical dots.
        * If you are unsure of what the student's most recent test is, you can check by clicking the bar graph icon, choosing the Outcomes tab, and checking the summary. The most recent test will be displayed directly under the student's name.
    * Click the icon with the three vertical dots. On the resulting menu, select the option "Download Responses"
        * This will download the zipped responses.json file.
* The template DSAT file can be downloaded by following the same steps as outlined above, instead choosing the option to "Print Assignment"

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
* There is no current method in place to modify the output file to display the student's original answer. I will work on adding this feature as I am able to.
* I understand that the inconsistent requirement of when to add file extension is confusing, I am working on changing this as well. 

### Feedback
* Please direct any and all feedback on the functionality to Enzi at my work email, or in person, so I can work on implementing it. I am aware that the current output of the missed answers is not in the most readable format, and I am open to any suggestions on how to optimize it for readability. I'll work on implementing a GUI at some point if this tool ends up being used very much.

### Bug Reporting
* When a bug is inevitably, and probably frequently found, please report it using any of the following methods:
    * Email Enzi's work email address
    * Open an issue on this repository
    * Lmk next time you see me at work


