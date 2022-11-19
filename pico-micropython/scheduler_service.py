class  SchedulerService:
    _tasks: dict
    _tasks_keys: list
    
    def __init__(self):
        self._tasks = {}
        self._tasks_keys = []
        

    def register_task(self, time, func, args):
        self._tasks[time] = {
            "func": func,
            "args": args
        }
        self._tasks_keys.append(time)
        self._tasks_keys = sorted(self._tasks_keys)
    def execute_task(self, key):
        if key in self._tasks:
            self._tasks[key]["func"](self._tasks[key]["args"])
            self._tasks.pop(key)
    def check_tasks(self, now):
        for task_key in self._tasks_keys:
            if task_key <= now:
                self.execute_task(task_key)
            else:
                return



