import random as rand

def generate_invoice_number():
    return f"{rand.randint(10000000, 99999999):08}"

def generate_invoices(num_invoices):
    return [generate_invoice_number() for _ in range(num_invoices)]

def count_matches(winning_number, invoice_numbers, num_digits):
    winning_suffix = winning_number[-num_digits:]
    return sum(1 for invoice in invoice_numbers if invoice[-num_digits:] == winning_suffix)

winning_invoice = generate_invoice_number()
print(f"Winning Invoice Number: {winning_invoice}")
invoices = generate_invoices(10000)

match_statistics = {}
for digit in range(3, 9):
    match_statistics[digit] = count_matches(winning_invoice, invoices, digit)

for digit, matches in match_statistics.items():
    print(f"Last {digit} digits: {matches} matches")
  
