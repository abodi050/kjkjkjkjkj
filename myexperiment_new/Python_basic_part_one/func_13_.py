




def facility():
    NumOfEmployWorked = int(
        input('{0:5} {1:60}:'.format(
            "", "Number of employees who have worked overtime")))
    TotalNumOfHourWorked = int(
        input("{0:5} {1:60}:".format(
            "", "Total number of worked overtime hours per employee")))
    return NumOfEmployWorked, TotalNumOfHourWorked


def constant():
    #ph=per hour
    #HR=Human Resource department
    #PA=Public Administration department
    #FD=Finance Department
    global HR_num, PA_num, FD_num
    HR_num = 30
    PA_num = 50
    FD_num = 10
    global HR_cost_ph, PA_cost_ph, FD_cost_ph
    HR_cost_ph = 150
    PA_cost_ph = 120
    FD_cost_ph = 170
    return (HR_num and PA_num and FD_num and HR_cost_ph and PA_cost_ph
            and FD_cost_ph)


constant()


def interface(data):
    print("\nPlease enter the information for %s department :" % (data))


print(
    "THIS PROGRAM CALCULATES THE OVERTIME PAYMENT OF A COMPANY WITH THREE DIFFERENT DEPARTMENTS."
)

interface(data="HR")
HR_NumOfEmployWorked, HR_TotalNumOfHourWorked = facility()
interface(data="PA")
PA_NumOfEmployWorked, PA_TotalNumOfHourWorked = facility()
interface(data="FD")
FD_NumOfEmployWorked, FD_TotalNumOfHourWorked = facility()

print(
    "Detailed Report of the Overtime Payment System for all three Department")
print("-" * 88)
print(
    "Dept.        #of Emp.     Rate/hour     #of working Emp.    Total overtime hours    Total Payment     Percentage "
)
print("*" * 88)
print("{0:6} {1:9} {2:15} {3:18} {4:16} {5:20} {6:20.4}%".format(
    "HR", HR_num, HR_cost_ph, HR_NumOfEmployWorked, HR_TotalNumOfHourWorked,
    HR_cost_ph * HR_NumOfEmployWorked * HR_TotalNumOfHourWorked,
    (HR_NumOfEmployWorked * 100 / HR_num)))
print("{0:6} {1:9} {2:15} {3:18} {4:16} {5:20} {6:20.4}%".format(
    "PA", PA_num, PA_cost_ph, PA_NumOfEmployWorked, PA_TotalNumOfHourWorked,
    PA_cost_ph * PA_NumOfEmployWorked * PA_TotalNumOfHourWorked,
    (PA_NumOfEmployWorked * 100 / PA_num)))
print("{0:6} {1:9} {2:15} {3:18} {4:16} {5:20} {6:20.4}%".format(
    "PA", FD_num, FD_cost_ph, FD_NumOfEmployWorked, FD_TotalNumOfHourWorked,
    FD_cost_ph * FD_NumOfEmployWorked * FD_TotalNumOfHourWorked,
    (FD_NumOfEmployWorked * 100 / FD_num)))
print("Total Overtime Payment of the company =%10.02f Riyal." % (
    (HR_cost_ph * HR_NumOfEmployWorked * HR_TotalNumOfHourWorked) +
    (PA_cost_ph * PA_NumOfEmployWorked * PA_TotalNumOfHourWorked) +
    (FD_cost_ph * FD_NumOfEmployWorked * FD_TotalNumOfHourWorked)))
