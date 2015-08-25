Metaphor comprehension
=======================

Prerequisites:
------------

- PsychoPy2 v1.81.00 or newer. PsychoPy can be installed as an application. The "Stand Alone" versions include everything you need to create and run the “metaphor comprehension” experiment.
[PsychoPy2 download link](http://sourceforge.net/projects/psychpy/files/).

Installation
------------

Get the source code:

    git clone git@github.com:languageguide/metaphor-comprehension.git

Get the stimuli zip file named “stimuli.zip”. The stimuli file will be publicly available when the scientific paper on this experiment will be released.

    cd metaphor-comprehension
    unzip stimuli.zip

Run
---

#### PsychoPy2
From the PsychoPy2 program open the file “main.psyexp” located into metaphor-comprehension directory.

#### Web app
In  order to run the web app you need to:
1. create a new `Google Apps Script` from your `Google Drive` account.
2. copy the script `utils/google-form.js` into the `Google Apps Script` file.
3. edit the main function specifing the `spreadsheet id`.
4. run the `Google Apps Script` and see the log `View -> Logs`.

Experiment Analysis
-------------------

The experimental results will be stored inside the "metaphor-comprehension/data/" directory.

To view the results of the experiments go to the [Metaphor comprehension analysis section](./analysis/README.md)

