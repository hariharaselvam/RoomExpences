

members = []
numbers = 0
expense = {}
v_total = 0

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
for i in range(number):
    print "Name : "+members[i]['name']
    print "Total: "+str(members[i]['total'])+" Rs/-"

print "Total Amount paid : "+str(v_total)+" Rs/-"