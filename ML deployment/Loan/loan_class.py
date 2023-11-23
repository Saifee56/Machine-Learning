from pydantic import BaseModel

class Loan(BaseModel):
    CurrentLoanAmount	: float
    Term : int
    CreditScore : float
    AnnualIncome :float
    HomeOwnership : float
    Purpose :int
    MonthlyDebt : float
    YearsofCreditHistory : float
    NumberofOpenAccounts :float
    NumberofCreditProblems: float
    CurrentCreditBalance: float
    MaximumOpenCredit	: float
    Bankruptcies : int
    TaxLiens: int

    
