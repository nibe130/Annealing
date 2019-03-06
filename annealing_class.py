import random

class annealing:
 def expOpgenerator(self, input_array):
        correct_op = []
        for i in range(0, 100):
            correct_op.append(((input_array[i] - 1) & (~input_array[i])))
        return correct_op


 def annealing(self, input_array, expected_output):

    threshold=0.1
    max_error = 100.00
    output_temp = []
    while max_error >= threshold:
        op1, op2, inte = self.RandomSol()
        output_temp = self.resultGenerator(input_array, inte, op1, op2)
        max_error = self.approx_error(expected_output, output_temp, input_array)
    return output_temp


 def RandomSol(self):
    operator1 = random.choice(['&', '|'])
    operator2 = random.choice(['~', ''])
    value = random.randint(0, 10)
    return operator1, operator2, value


 def resultGenerator(self, input_array, value, operator1, operator2):
    output = []
    for i in range(0, 100):
        express = str(input_array[i]) + "-" + str(value) + " " + operator1 + " " + operator2 + str(input_array[i])
        output.append(eval(express))
    return output


 def approx_error(self, expected_output, tempOutput, input_array):
    count = 0
    exp_num = ""
    exp_num2 = ""
    for i in range(0, 100):
        exp_num = str(bin(expected_output[i]))[2:] + exp_num
        exp_num2 = str(bin(tempOutput[i]))[2:] + exp_num2

    for row in range(0, (len(exp_num) & len(exp_num2))):
        if exp_num[row] != exp_num2[row]:
            count += 1

    return (count / len(input_array))


