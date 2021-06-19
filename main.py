length = input("How many days will you be staying? ")

#if length > 30 or length < 1: 
#  print("You can only stay for between 1 to 30 nights.")
#else:
#print("Got it. Please see prices below.")

print("================================================")

print("Single Room for one adult:	500")
print("Double Room for two adults: 900")
print("Family cottage for two adults and two children under 16: 1500")

print("================================================")

single = input("How many single rooms? ")
double= input("How many double rooms? ") 
cottage= input("How many family cottages? ")

print("================================================")
singles = single * 500 
doubles = double * 900
cottages = cottage * 1500

print("================================================")

cost1 = singles + doubles + cottages
#vat = cost1 * (15 / 100) # VAT at a rate of 15%
#inclvat = cost + vat # Adds VAT to cost

print("================================================")

print ("YOUR BOOKING AT")

#print("Booking name: " + name + surname)
#print("Number of single rooms booked" + singles)

print("See you soon.")