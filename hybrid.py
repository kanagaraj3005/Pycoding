class CEO:
    def info(self):
        print("CEO is head of all departments in the office")
class GM(CEO):
    def control(self):
        print("GM controls the office")
class Manager(CEO):
    def execution(self):
        print("Each Department manager executes the functions")
class Incharge(GM, Manager):
    def sub_execution(self):
        print("Each department incharge prepares plan with the instructions by manager")
class Supervisor(Incharge):
    def supervising(self):
        print("Supervisor receives plan from incharge")
class Operator(Incharge):
    def production(self):
        print("Operator produces product on basis of supervisor instructions")

act = Supervisor()
act.info()
act.control()
act.execution()
act.sub_execution()
act.supervising()
act = Operator()
act.info()
act.control()
act.execution()
act.sub_execution()
act.production()
