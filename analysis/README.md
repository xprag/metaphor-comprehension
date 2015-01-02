Metaphor comprehension analysis
=======================

Prerequisites:
------------

- SQLite version 3.7.13 or greater.
- Python version 2.7.5 or greater.
- PHP version 5.4 or greater.
- [Bower](http://bower.io/), a package manager for the web.

Installation
------------

Get the data output file named. In order to get the stimuli file, you can send an email to antonio.pierro_at_gmail.com or francesca.ervas_at_gmail.com.

Install package

	bower install

Run
---

Create data-base file running the bash script named `main.sh`

	./main.sh -w y

To determinate the trusted students, run the bash script named `main.sh` with the `s` option. For example:

	./main.sh -s 5

The `s option accepts a number which stands for the minimum number of distractors questions wrong.

To view the data you can lunch the built-in web server with the following command:

    php -S localhost:8001

Finally you can access the analysis data by opening a browser and navigating to the following URL: `http://localhost:8001`.
