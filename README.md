A simulation tool for making big decisions (like buying a house).
The general idea is you create "event generators," like having a kid, that over the course of time generate positive and negative "impacts" on your financial state.

# Intended Use
Take a look at the sample and create your own script to help with some important decision you need to make.
For me, it was to decide if I could afford buying a big house using some RSUs that ended up being worth much more than I was expecting.

## On data and APIs
I manually copied in my personal data when I did this exercise.
Its probably possible to do that with the companies APIs, but that was not worth it for me.

I did download unvested stock information from etrade, and I included very rudimentary support for that.
You will need to download a specific file from etrade and put it [here](./data_inputs) and tell the source code where to find it in your simulation.

## Sample Simulation
You can try to simulate a fictional person's future net worth in [the sample](./house_upgrade_sample.py) as they contemplate selling their apartment and buying a big fancy house.
This file tries to plot several scenarios based on if the fictional person gets fired before all their RSUs vest, if the company's stock tanks, and a few other factors.
### Main assumptions for this simulation
1. The person will not recieve any additional bonuses ever
1. Living expenses are fairly high
1. Kids will attend public school
1. Wages will grow 3% annually
1. Any cash balance will be put into indicies that return about 3% yearly
1. The person's spouse also is a source of income
1. Ignores ISO grants (prints a warning)
1. Ignores employee stock purchase plans
1. Equity in the house is ignored

- All of these assumptions are generally to make the simulation easier to write without sacrificing too much quality or becoming overly optimistic.
- Each assumption could be lifted or made less severe with a bit more code.
- There are probably more assumptions in there that may also be important.

Use at your own risk.

# Running the code

## In a virtualenv
I prefer running it in a virtual environment:
```bash
cd /path/to/this/repo
virtualenv --python=/path/to/bin/python3.6 env
source ./env/bin/activate
pip install -r requirements.txt
python house_upgrade_sample.py
```
Any version of python 3 would probably work fine.

### Testing
With the virtualenv activated,
```bash
python -m unittest
```

## In a container
If you prefer not to pollute you system, you can bash into the Dockerfile and run it from there, but you will be have to write a few extra lines of code to see figures from matplotlib.
### Testing
With the virtualenv activated,
```bash
docker-compose run test
```
