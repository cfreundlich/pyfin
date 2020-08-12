import datetime
import logging
import copy
import matplotlib.pyplot as plt
from src.one_time_expense import OneTimeExpense
from src.bank_account import BankAccount
from src.college_tuition import CollegeTuition
from src.living_expense import LivingExpenses
from src.mortgage import Mortgage
from src.pre_k import PreK
from src.property_tax import PropertyTax
from src.rsu import RestrictedStock
from src.salary import Salary
from src.sim import Sim


LOGGER = logging.getLogger()
import src.today
TODAY = src.today.today()


# ASSUMPTIONS
DEAD = datetime.date(day=1, month=1, year=2088)
RETIREMENT_DATE = datetime.date(day=11, month=7, year=2050)

CURRENT_COMPANY_SHARE_PRICE = 5e2
SALARY_IN_CURRENT_JOB = 1.5e5
LAST_DAY_AT_CURRENT_COMPANY = TODAY + datetime.timedelta(days=365 * 3)
JOB_SEARCH_TIME = datetime.timedelta(days=30*3)
SALARY_IN_NEXT_JOB = 1.5e5
UNVESTED_RSU_FILENAME = 'sample_etrade_unvested.xlsx'

STOCK_MARKET_YEARLY_RATE_OF_RETURN = 3e-2
BIG_TAX_HIT_AMOUNT = 5e4
BIG_TAX_HIT_DUE = datetime.date(year=2021, month=4, day=15)

INCOME_TAX_RATE = 0.4

PURCHASE_PRICE = 1.0e6
DOWNPAYMENT_HELP = 0.
INTEREST_RATE_30_YR = 3.2e-2
MOVE_IN_EXPENSE = 5e4
CLOSING_DATE = datetime.date(year=2020, month=10, day=1)

LIVING_EXPENSE_YEARLY = 7.5e4

PRE_K_YEARLY = 1.8e4
CHILD_1_END_PREK = datetime.date(year=2023, month=9, day=1)
CHILD_2_START_PREK = datetime.date(year=2020, month=12, day=1)
CHILD_2_END_PREK = datetime.date(year=2025, month=9, day=1)

SPOUSE_LAST_DAY_CURRENT_JOB = datetime.date(year=2020, month=11, day=14)
SPOUSE_CURRENT_JOB_YEARLY_SALARY = 9e4
SPOUSE_JOB_SEARCH_TIME = datetime.timedelta(days=30*9)
SPOUSE_NEW_JOB_YEARLY = 3e4

CHILD_1_COLLEGE_START = datetime.date(year=2036, month=9, day=1)
CHILD_2_COLLEGE_START = datetime.date(year=2038, month=9, day=1)
COLLEGE_TUITION_YEARLY = 5e4

SELL_CURRENT_HOME_FOR = 8e5
OWED_ON_CURRENT_HOME = 5e5
_ACCOUNT_1 = 1.5e5
_ACCOUNT_2 = 1.2e4
_CASH = 2.83e4
_HOUSE_FLIP = 0.9*(SELL_CURRENT_HOME_FOR - OWED_ON_CURRENT_HOME)
INIT_VAL = round(_HOUSE_FLIP + _ACCOUNT_1 + _ACCOUNT_2 + _CASH)
LOGGER.info(f'Starting with ${round(INIT_VAL/1e3)}k')

# CALCULATIONS
EVENTS = dict(
    current_job_base=Salary(yearly_amount=SALARY_IN_CURRENT_JOB,
                      start=TODAY,
                      end=LAST_DAY_AT_CURRENT_COMPANY),
    next_job_base=Salary(yearly_amount=SALARY_IN_NEXT_JOB,
                         start=LAST_DAY_AT_CURRENT_COMPANY + JOB_SEARCH_TIME,
                         end=RETIREMENT_DATE),
    spouse_current_job_base=Salary(yearly_amount=SPOUSE_CURRENT_JOB_YEARLY_SALARY,
                              start=TODAY,
                              end=SPOUSE_LAST_DAY_CURRENT_JOB),
    spouse_new_job_base=Salary(yearly_amount=SPOUSE_NEW_JOB_YEARLY,
                              start=SPOUSE_LAST_DAY_CURRENT_JOB + \
                                  SPOUSE_JOB_SEARCH_TIME,
                              end=RETIREMENT_DATE),
    tax_hit=OneTimeExpense(when=BIG_TAX_HIT_DUE,
                           amount=BIG_TAX_HIT_AMOUNT),
    new_home_mortgage=Mortgage(purchase_price=PURCHASE_PRICE,
                                closing_date=CLOSING_DATE,
                                downpayment_help=DOWNPAYMENT_HELP,
                                interest_rate=INTEREST_RATE_30_YR),
    RSU=RestrictedStock(init_price=CURRENT_COMPANY_SHARE_PRICE,
                        last_day=LAST_DAY_AT_CURRENT_COMPANY,
                        filename=UNVESTED_RSU_FILENAME),
    child_1_pre_k=PreK(yearly_amount=PRE_K_YEARLY,
                       end=CHILD_1_END_PREK),
    child_2_pre_k=PreK(yearly_amount=PRE_K_YEARLY,
                       start=CHILD_2_START_PREK,
                       end=CHILD_2_END_PREK),
    property_taxes=PropertyTax(purchase_price=PURCHASE_PRICE,
                               closing_date=CLOSING_DATE),
    move_in_expense=OneTimeExpense(when=CLOSING_DATE,
                                   amount=MOVE_IN_EXPENSE),
    living_expenses=LivingExpenses(yearly_amount=LIVING_EXPENSE_YEARLY),
    child_1_college=CollegeTuition(start=CHILD_1_COLLEGE_START,
                                  yearly_tuition=COLLEGE_TUITION_YEARLY),
    child_2_college=CollegeTuition(start=CHILD_2_COLLEGE_START,
                                   yearly_tuition=COLLEGE_TUITION_YEARLY)
)


plt.figure()
sim_share_prices = [max(0, CURRENT_COMPANY_SHARE_PRICE + i*5e1)
                    for i in range(-2, 3)]
for share_price in sim_share_prices:
    events = copy.deepcopy(EVENTS)
    simulation = Sim(bank_account=BankAccount(val=INIT_VAL, age=TODAY))
    events['RSU'] = RestrictedStock(init_price=share_price,
                                    last_day=LAST_DAY_AT_CURRENT_COMPANY,
                                    filename=UNVESTED_RSU_FILENAME)
    simulation.consume(events)
    simulation.run()
    simulation.plot(label=share_price)
plt.title('Company share price')
plt.ylabel('Net Worth ($)')
plt.legend()

plt.figure()
for salary_next_job in [SALARY_IN_CURRENT_JOB + 3e4*i for i in range(-2, 3)]:
    events = copy.deepcopy(EVENTS)
    simulation = Sim(bank_account=BankAccount(val=INIT_VAL, age=TODAY))
    events['next_job_base'] = Salary(yearly_amount=salary_next_job,
                                     start=LAST_DAY_AT_CURRENT_COMPANY + JOB_SEARCH_TIME,
                                     end=RETIREMENT_DATE)
    simulation.consume(events)
    simulation.run()
    simulation.plot(label=salary_next_job/1e3)
plt.title('Next Job Salary ($k)')
plt.ylabel('Net Worth ($)')
plt.legend()

plt.figure()
for more_years_in_role in range(1, 5):
    events = copy.deepcopy(EVENTS)
    simulation = Sim(bank_account=BankAccount(val=INIT_VAL, age=TODAY))
    last_day = TODAY + datetime.timedelta(days=365.25 * more_years_in_role)
    events.update(dict(
        current_job_base=Salary(yearly_amount=SALARY_IN_CURRENT_JOB,
                          start=TODAY,
                          end=last_day),
        next_job_base=Salary(yearly_amount=SALARY_IN_NEXT_JOB,
                             start=last_day + JOB_SEARCH_TIME,
                             end=RETIREMENT_DATE),
        RSU=RestrictedStock(init_price=CURRENT_COMPANY_SHARE_PRICE,
                            last_day=last_day,
                            filename=UNVESTED_RSU_FILENAME)
    ))
    simulation.consume(events)
    simulation.run()
    simulation.plot(label=more_years_in_role)
plt.title('More years at current job')
plt.ylabel('Net Worth ($)')
plt.legend()


plt.figure()
prices = [PURCHASE_PRICE + i*5e4 for i in range(-2, 3)]
for purchase_price in prices:
    events = copy.deepcopy(EVENTS)
    simulation = Sim(bank_account=BankAccount(val=INIT_VAL, age=TODAY))
    events.update(dict(
        new_home_mortgage=Mortgage(purchase_price=purchase_price,
                                    closing_date=CLOSING_DATE,
                                    downpayment_help=DOWNPAYMENT_HELP,
                                    interest_rate=INTEREST_RATE_30_YR),
        property_taxes=PropertyTax(purchase_price=purchase_price,
                                   closing_date=CLOSING_DATE)
    ))
    simulation.consume(events)
    simulation.run()
    simulation.plot(label=round(purchase_price/1e6, 3))
plt.title('Purchase Price ($M)')
plt.ylabel('Net Worth ($)')
plt.legend()
