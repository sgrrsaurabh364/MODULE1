# total revenue

import datetime


class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3  # diplay purpose only
    WHITE = 4  # data is missing for this field

# This is a already written for your reference
def latest_financial_index(data: dict):
   
    for index, financial in enumerate(data.get("financials")):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0


def total_revenue(data: dict, financial_index):
    if "financials" not in data or financial_index >= len(data["financials"]):
     return 0  # Handle cases where financials list is missing or index is out of bounds

 pnl_data = data["financials"][financial_index].get("pnl", {})
 line_items = pnl_data.get("lineItems", {})
 net_revenue = line_items.get("netRevenue", 0)

 return net_revenue


def total_borrowing(data: dict, financial_index):
    if "financials" not in data or financial_index >= len(data["financials"]):
      return 0  # Handle cases where financials list is missing or index is out of bounds

  bs_data = data["financials"][financial_index].get("bs", {})
  current_liabilities = bs_data.get("currentLiabilities", {})
  long_term_liabilities = bs_data.get("longTermLiabilities", {})

  total_borrowings = (
      current_liabilities.get("shortTermBorrowings", 0)
      + long_term_liabilities.get("longTermDebt", 0)
  )

  total_revenue = total_revenue(data, financial_index)

  if total_revenue == 0:
      return 0  # Avoid division by zero

  return total_borrowings / total_revenue



def iscr_flag(data: dict, financial_index):
   if iscr(data, financial_index) >= 2:
       return FLAGS.GREEN
     else:
       return FLAGS.RED


def total_revenue_5cr_flag(data: dict, financial_index):
    if total_revenue(data, financial_index) >= 50000000:
        return FLAGS.GREEN
     else:
     return FLAGS.RED


def iscr(data: dict, financial_index):
     if "financials" not in data or financial_index >= len(data["financials"]):
      return 0  # Handle cases where financials list is missing or index is out of bounds

  financial_data = data["financials"][financial_index]

  ebit = financial_data.get("ebit", 0)
  depreciation = financial_data.get("depreciation", 0)
  interest_expense = financial_data.get("interestExpense", 0)

  # Use EBITDA if available, otherwise fall back to EBIT
  if "ebitda" in financial_data:
      ebitda = financial_data["ebitda"]
  else:
      ebitda = ebit + depreciation

  numerator = ebitda + 1
  denominator = interest_expense + 1

  if denominator == 0:
      return 0  # Avoid division by zero

  return numerator / denominator


def borrowing_to_revenue_flag(data: dict, financial_index):
     borrowing_ratio = total_borrowing(data, financial_index)

  if borrowing_ratio <= 0.25:
      return FLAGS.GREEN
  else:
      return FLAGS.AMBER
