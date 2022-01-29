data = read.csv("cleaned_data.csv")

debt_to_income <- data$debt_to_income_ratio

accepted <-- data$accepted

debt_to_income_accepted <-- data.frame(debt_to_income, accepted)

acceptance_by_debt_to_income <- debt_to_income_accepted[debt_to_income_accepted$accepted == 1]

table(acceptance_by_debt_to_income)

barplot(table(acceptance_by_debt_to_income),
        main="Debt to Income",
        xlab="Age",
        ylab="Count",
)
