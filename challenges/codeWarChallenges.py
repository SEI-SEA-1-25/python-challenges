def odd_or_even():
    l = [11657, 8779, 18, 1287, 24]
    total = sum(l)
    remainder = total % 2
    Even = (remainder == 0)
    Odd = (Even == False, "odd")

    if Even:
        return "even"
    elif Odd:
        return "odd"


print(odd_or_even())

# ? return "EVEN!! "
# ? return " ODD!! "

# ? print("        for a remainder of: ", remainder, "\n\n")
# ? print("        **********************\n        *                    *\n        *      ", odd_or_even(l,
# ?       total, remainder), "     *\n        *                    *\n        **********************")

# ? print(odd_or_even(l, total, remainder))
# ? print("            -------------\n              Sum = ", total,
# ?       "\n            -------------" "\n\n         Divided ", total, " by two\n")
