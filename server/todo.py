class Todo:

    #placeholder of sql connection
    def __init__(self,tasks =None):

        self.tasks= tasks if tasks else [] # need to got to sql/json?
        self.statuts ="Open" #default
        
    
    def add(self,task):
        self.tasks.append(task)
    
    def remove(self,task):
        self.tasks.remove(task)
    
    def finish(self,task):
        self.tasks.remove(task)
        task.status="Done"
    
    def get(self):
        return self.tasks
    
    def main():
        mytodo=Todo()
        while True:
            input_task=input("Enter your task or press q to quit")
            mytodo.add(input_task)
            if input_task=="q":
                break
            print(mytodo.get())
    
Todo.main()