# CASE STUDY

Anytime a doctor accepts things like lunches, gifts, etc. that cost greater than $10 dollars this has to be reported. Below is the site the contains all the data:

[https://openpaymentsdata.cms.gov/dataset/General-Payment-Data-Detailed-Dataset-2015-Reporti/8xjh-6p62](https://openpaymentsdata.cms.gov/dataset/General-Payment-Data-Detailed-Dataset-2015-Reporti/8xjh-6p62)

Create a web application that imports this data. Make sure that it checks regularly to get the most recent updates. Build a search tool with a typeahead that returns all relevant data. When search results are returned build an export to Excel feature. Make sure that this outputs to an XLS file.

## Requirements

**Python 3.7** [https://www.python.org/downloads/release/python-373/](https://www.python.org/downloads/release/python-373/)

**Django 2.2**

**Pipenv** for a virtual environment [https://docs.pipenv.org/en/latest/](https://docs.pipenv.org/en/latest/)

## Installation

    git clone
    cd groer
    pipenv install
    pipenv shell
    python3 reorg/manage.py migrate
    python3 reorg/manage.py migrate_data
    python3 reorg/manage.py runserver

## How To

Navigate to the homepage [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Start typing a name, suggestions will appear, then submit

The results are loaded onto the page

Click the `Export to Excel` to download an `.xls` file.

## Setting Up A Cron Schedule

Crontab is not apart of django and would be setup on my local environment (OSX). Type `crontab -e` into the terminal and paste the below, `save` and `exit`.

    */10 * * * * python3 /Users/rory/Documents/repositories/github/groer/reorg/manage.py migrate_data

The above should run the `migrate_data` custom management command every 10 minutes.
