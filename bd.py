class Task():
    def __init__(self, id:int, description:str, srok:int=1, status: bool=False):
        self.description = description
        self.srok = srok
        self.status = status
        self.id = id
    def __str__(self):
        stroka = f"{self.description}  {str(self.srok)} {'выполнено' if self.status else 'не выполнено' }" 
        return stroka     
    def done_task(self):
        self.status = True


class Tasks():
    def __init__(self):
        self.tasks = []
        self.id_task = 0

    def add_task (self, new_task, srok=1):
        task = Task(id = self.id_task, description=new_task,status=False, srok=srok)
        self.tasks.append(task)
        self.id_task+=1

    
    def spisok_not_done_task(self)->list[Task]:
        for task in self.tasks:
            if task.status == False:
                print(task)  
        return [task for task in self.tasks if not task.status]        
    def mark_done (self, ids):
        for task in self.tasks:
            if task.id == ids:
                task.done_task()


    
           


