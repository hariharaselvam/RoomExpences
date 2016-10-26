

members = []
numbers = 0
expense = {}
v_total = 0
e_total = 0
g_total = 0

print "_______________________________________________"
print "             WAKE UP Room                      "
print "_______________________________________________"
print "Enter the number of count :"
number=raw_input("Enter the people count : ")
number = int(number)
for i in range(number):
    name = raw_input("Enter the person name : ")
    paid_str = raw_input("Enter the list of amount paid :")
    paid_lst = paid_str.split(",")
    paid_int = [int(x) for x in paid_lst]
    total = sum(paid_int)
    v_total += total
    members.append({"name":name,"paid":paid_str,"total":total})


print "Total Amount paid : "+str(v_total)+" Rs/-"
#g_total += v_total
while True:
    name = raw_input("Enter the expens")
    if name=="":
        break
    else:
        amount = raw_input("Enter the amount")
        expense[name]=int(amount)
        e_total += amount

g_total = e_total + v_total
average = g_total / number
p_total = 0

for i in range(number):
    total = average - members[i]['total']
    members[i]["to_pay"] = total
    p_total += total

print " Final result "
for key in expense:
    print key +".........."+"  "+expense[amount]+"  Rs/-"
print "Expense Total    : "+str(e_total)+"     Rs/-"
print "Vegitables Total : "+str(v_total)+"     Rs/-"
print "Grand Total      : "+str(g_total)+"     Rs/-"
print "Average to "+str(number)+" : "+str(average)+"    Rs/-"
print " Distribution "
for i in range(number):
    print members[i]['name']+"  "+str(average)+" - "+str(members[i]['total'])+"  =  "+str(members[i]['to_pay'])

