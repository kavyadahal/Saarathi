"""
Week 4 Practice Lab · Shared dataset builder — LOAN APPROVALS
A fresh, mixed-column dataset so you practise the full Week 4 workflow on
something you haven't seen. Import it from your lab scripts:
    from data_gen import make_loans
    df, approved = make_loans()
Needs:  pip install pandas numpy
"""

import numpy as np
import pandas as pd


def make_loans(n=800, seed=7):
    """A toy bank dataset. Returns (df, approved).

    df       : applicant features (numbers + text) —
               income, loan_amount, age, credit_history, purpose.
    approved : the 0/1 label (1 = the loan was approved).

    The real driver is the DEBT-TO-INCOME ratio (loan_amount / income): a small
    ratio is safe (approve), a big ratio is risky (reject). Credit history nudges
    it. Because approval depends on a RATIO of two columns, a model given income
    and loan_amount separately struggles — until a student engineers dti.
    """
    rng = np.random.default_rng(seed)
    income      = rng.uniform(20, 120, n)                 # annual income, thousands
    loan_amount = rng.uniform(5, 60, n)                   # requested loan, thousands
    age         = rng.integers(21, 65, n)                 # applicant age
    credit      = rng.choice(["good", "poor", "none"], n, p=[0.5, 0.3, 0.2])
    purpose     = rng.choice(["home", "car", "business", "education"], n)

    dti = loan_amount / income                            # the hidden driver
    # good credit tolerates a bit more debt; poor credit tolerates less
    effective = (dti
                 - np.where(credit == "good", 0.15, 0.0)
                 + np.where(credit == "poor", 0.15, 0.0)
                 + rng.normal(0, 0.08, n))                # a little noise
    approved = (effective < 0.55).astype(int)            # low debt-to-income -> approved

    df = pd.DataFrame({"income": income, "loan_amount": loan_amount, "age": age,
                       "credit_history": credit, "purpose": purpose})
    return df, approved


if __name__ == "__main__":
    df, approved = make_loans()
    print(df.head())
    print("approved share:", round(approved.mean(), 2))
