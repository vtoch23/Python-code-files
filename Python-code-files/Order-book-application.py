class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, program, programmer, workload, status = "NOT FINISHED"):
        self.program = program
        self.programmer = programmer
        self.workload = workload
        self.status = status
        self.id = Task.new_id()
    
    def mark_finished(self):
        self.status = "FINISHED"
 
    def __str__(self):
        return f"{self.id}: {self.program} ({self.workload} hours), programmer {self.programmer} {self.status}"           
 
 
class Tasks:
    def __init__(self):
        self.tasks = []   
        
    def add_task(self, descrition, programmer, workload, status):
        self.tasks.append(Task(descrition, programmer, workload, status))
        print("added!")
 
    def mark_finished(self, id):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError
 
    def unfinished_orders(self):
        return [t for t in self.tasks if t.status == "NOT FINISHED"]
 
    def finished_orders(self):
        return [t for t in self.tasks if t.status == "FINISHED"]         
 
    def programmers(self):
        return list(set([t.programmer for t in self.tasks]))
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished = [t for t in self.finished_orders() if t.programmer == programmer and t.status == "FINISHED"]
        unfinished =[t for t in self.unfinished_orders() if t.programmer == programmer and t.status == "NOT FINISHED"]
        finished_hours = sum(int(t.workload) for t in self.finished_orders() if t.programmer == programmer)
        not_finished_hours = sum(int(t.workload) for t in self.unfinished_orders() if t.programmer == programmer)
 
        print(f"tasks: finished {len(finished)} not finished {len(unfinished)}, hours: done {finished_hours} scheduled {not_finished_hours}")
    
    def all_tasks(self):
        return self.tasks
 
class Application:
    def __init__(self):
        self.taskList = Tasks()
 
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def check_programmer(self, programmer):
        if len(programmer) > 0:
            for i in range(len(programmer)):
                if programmer[i] in self.numbers():
                    return False
                    
        elif len(programmer) == 0: 
            return False
        else:
            return True    
 
    def check_workload(self, workload):
        for i in range(len(workload)):
            try:
                if not int(workload[i]) in self.numbers():
                    return False    
            except:
                return False
        return True
 
    def numbers(self):
        return [0,1,2,3,4,5,6,7,8,9] 
 
    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "1":
                description = input("description:")
                programmerAndWorkload = input("programmer and workload estimate: ")
                space = programmerAndWorkload.find(" ")
                programmer = programmerAndWorkload[0:space]
                workload = programmerAndWorkload[space+1:]
                if self.check_programmer(programmer) == False or self.check_workload(workload) == False:
                    print("erroneous input")
    
                else:
                    self.taskList.add_task(description, programmer, workload, status = "NOT FINISHED")
                    
            elif command == "2":
                if len(self.taskList.finished_orders()) > 0:
                    for task in self.taskList.finished_orders():
                        print(task)
                else:
                    print("no finished tasks")
 
            elif command == "3":
                if len(self.taskList.unfinished_orders()) > 0:
                    for task in self.taskList.unfinished_orders():
                        print(task)
                else:
                    print("no unfinished tasks")
 
            elif command == "4":
                try:
                    searched_id = int(input("id:"))
                    if int(searched_id) > 9 or not int(searched_id) in self.numbers():
                        print("erroneous input")
                    else:
                        self.taskList.mark_finished(searched_id) 
                        print("marked as finished")
                except:
                    print("erroneous input")
 
            elif command == "5":
                for programmer in self.taskList.programmers():
                    print(programmer)
 
            elif command == "6":
                programmer = input("programmer: ")
                if not programmer in self.taskList.programmers():
                    print("erroneous input")
                else:
                    print(self.taskList.status_of_programmer(programmer))      
 
            elif command == "0":
                break
task = Application()
task.execute()