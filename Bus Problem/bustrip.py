'''The school teacher would like a computer program that will:

Ask for the number of students taking part in the trip.
Ask for the number of teachers taking part in the trip.
Calculate the total number of participants (by adding the number of students and the number of teachers).
Find out and output the number of large coaches that will be required.
Find out and output the number of small coaches that will be required.
Calculate and output the total cost of hiring these coaches for a day.'''

students=int(input("Enter the number of students--> "))
teachers=int(input("Enter the number of teachers--> "))
participants=students+teachers
print("total number of participants-->",participants)
busL=participants//46
print("number of larger buses-->", busL)
rem=participants % 46
busS=rem//16
rem= rem%16
if rem>0:
    busS+=1
print("Number of small buses--> ", busS)
total=(busL*360) + (busS*140)
print("total cost -->", total )