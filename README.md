# Annealing
Program synthesis using Annealing
Program synthesis is generally performed using a complete set of specifications. Authors of this paper use oracle guided learning and constraint-based synthesis from components using SAT solvers.

It has 3 components: a validation oracle, I/O oracle and a set of specifications called a library. The library contains the input and output variables, it also specifies the input-output relationship.

Program synthesis is the task of automatically finding a program in the underlying programming language that satisfies the user intent expressed in the form of some specification. Unlike typical compilers that translate a fully specified high-level code to low-level machine representation using a syntax-directed translation, program synthesizers typically perform some form of search over the space of programs to generate a program that is consistent with a variety of constraints.

In order to achieve this a specification of what the program should do is to be made. However, in oracle guided synthesis it is assumed that an implementation of the program that needs to be synthesized is already there, which is called an oracle program. This implementation is the specification for oracle-guided synthesis.

Program synthesis is a notoriously challenging problem. Its inherent challenge lies in two main components of the problem: intractability of the program space and diversity of user intent.

Example:
P8(x) : Form a mask that identifies the trailing 0’s
o1=(x - 1)
o2=(¬ x)
res=(o1 & o2) PSEUDOCODE: 1. First, generate a random solution to form a mask that identifies trailing 0’s 2. Calculate its cost using cost function 3. Generate a random neighboring solution 4. Calculate the new solution's cost 5. Compare them: o If cnew < cold: move to the new solution o If cnew > cold: maybe move to the new solution 6. Repeat steps 3-5 above until an acceptable solution is found or you reach some maximum number of iterations.


The cost function that we are using is the execution time. The program first validates if the newly synthesized program is correct and works for our test cases. If it is correct and works on all our test cases we calculate the cost. Which in our case is the execution time to produce the correct output.

The acceptance probability function n takes in the old cost, new cost, and current temperature and returns a number between 0 and 1, which is a sort of recommendation to the new solution. For example: • 1.0: definitely switch (the new solution is better) • 0.0: definitely stay put (the new solution is infinitely worse) • 0.5: the odds are 50-50 Once the acceptance probability is calculated, it's compared to a randomly-generated number between 0 and 1. If the acceptance probability is larger than the random number, you're switching!

Error Function: 
We apply this use of annealing function till the time we get the least error function. It is also called the fitness factor. We implement both of the or program and keep repeating it till the time we don’t find a solution with least error function.
