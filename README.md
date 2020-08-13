A simulation tool for making big decisions (like buying a house).
General idea is to create "event generators," like having a kid, that over the course of a time interval into the future generates positive and negative impacts on your financial state.

# Intended Use
You can take a look at the sample and create your own script based on some important decision you need to make.
For me it was to decide if I could afford buying a big house using some RSUs that ended up being worth much more than I was expecting.

## Sample Simulation
You can try to simulate a fictional person's future net worth in [the sample](./house_upgrade_sample.py) as they contemplate buying a big fancy house with made up data.
This file tries to plot several scenarios based on if the fictional person gets fired before all their RSUs vest, if the company's stock tanks, and a few other factors.
### Assumptions for this simulation
1. the person will not recieve any additional bonuses ever
1. living expenses are fairly high
1. kids will attend public school
1. wages will grow 3% annually
1. any cash balance will be put into indicies that return about 3% yearly
1. the person's spouse also is a source of income
1. ignores ISO grants (prints a warning)
1. ignores employee stock purchase plans
1. equity in the house is ignored

All of these assumptions are generally to make the simulation easier to write without sacrificing too much quality or becoming overly optimistic.
Each assumption could be lifted or made less severe with a bit more code.