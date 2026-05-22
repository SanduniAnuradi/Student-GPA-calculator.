#student GPA calculator

s1 = float(input("Enter marks for subject1:"))
s2 = float(input("Enter marks for subject2:"))
s3 = float(input("Enter marks for subject 3:"))
s4 = float(input("Enter marks for subject 4:"))
Total = s1+s2+s3+s4
Average = Total/4
GPA = Average/25
print("Total Marks :", Total)
print("Average Marks :",Average)
print("GPA:",GPA)
