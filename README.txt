Simple GUI project that separates tax from a total sale.

Done for a restaurant that did not have a Point of sale (POS) system and had a credit card machine that wasn't able to turn off and on the tax (the tax is always added on the amount entered in the machine). Therefore, if customers decided to split the check with both cash and card(s), after deducting the cash from the total(tax included), the remaining balance would need to have the tax "deducted" so that the customer isn't charged tax twice.

Quick example of this problem:
Two customers but they don't want to split evenly. $125 check but one customer wants to pay $50 while the other customer wants to pay the rest.
In order for the waiter to charge $50 and not more, he/she needs to calculate the tax out of that 50. So after using the app, the waiter find out that pre-tax amount is 46.89, on which the credit card machine adds $3.11 as tax. Same is then done with the $75 from the other customer.


One more example:
Total with tax = $200.00
Cash given = $ 80
"Put the remaining balance on the card please"
If the waiter puts $120 into the machine, machine adds tax to $120 and the customer is overcharged. (80 + 120 + tax = More than 120)
Thus, waiter must find out the baked-in tax with the app: Tax is $7.46 so the waiter types in $112.54 into the machine, after which the credit card machine adds tax.
