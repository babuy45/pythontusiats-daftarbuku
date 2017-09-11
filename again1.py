# check if an employee has achieved his weekly target or not

class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    def hasAchivedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achived")

employeeOne = Employee()
employeeOne.name
#'Ben'
employeeOne.hasAchivedTarget()
#Target has been achieved
employeeTwo = Employee()
employeeTwo.name

numbers = [1, 2, 3]
type(numbers)

numbers.append(4)
