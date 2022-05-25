class Person:

    count = 0

    """
    This class defines a generic person.
    
    Attributes: first (name), last (name), weight (in lbs), height (in inches), age, gender
    """

    def __init__(self, first, last, weight, height, age=0, gender=''):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count = Person.count + 1

    @classmethod
    def print_count(cls, ):
        return cls.count


class Adult(Person):

    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / self.height_in_inches ** 2

        print('BMI number is: ' + str(bmi_tmp))

        if bmi_tmp < 18:
            self.bmi = 'Underweight'
        elif 18 < bmi_tmp < 25:
            self.bmi = 'Normal'
        elif 25 < bmi_tmp < 30:
            self.bmi = 'Overweight'
        elif bmi_tmp > 30:
            self.bmi = 'Obese'
        return self.bmi


class Teacher(Adult):

    def __init__(self, teacher_type):
        self.teacher_type = teacher_type
        bmi_risk_factor = 0
        if teacher_type == 'kindergarten':
            bmi_risk_factor = 1
        elif teacher_type == 'secondary':
            bmi_risk_factor = 2
        elif teacher_type == 'higher ed':
            bmi_risk_factor = 3
        self.bmi_risk_factor = bmi_risk_factor
