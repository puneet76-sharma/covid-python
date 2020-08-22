# pip install covid

# covid-python

Python package to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info

Requirements
python >= 3.6

How to install
pip install covid

Dependencies
pydantic
requests

from covid import Covid

# by default data source is "john_hopkins"
covid = Covid()

# or
covid = Covid(source="john_hopkins")

# to get data from worldometers.info
covid = Covid(source="worldometers")

# get all data
covid.get_data()
