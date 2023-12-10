class Job:
    def __init__(self, idJob = -1, nameJob = "", industryName = "", salary = -1):
        self.__idJob = idJob
        self.__nameJob = nameJob
        self.__industryName = industryName
        self.__salary = salary
    def skill(self):
        return 0
    def score(self):
        return []
    def evaluate(self) -> str:
        k = self.skill()
        if k > 9.0:
            return "Rat phu hop"
        elif k > 7.0:
            return "Phu hop"
        elif k > 5.0:
            return "Tam duoc"
        elif k > 3.0:
            a = self.score()
            return "Can bo sung them kien thuc: {', '.join(a)}"
        else:
            return "Can hoc lai kien thuc base"
    def __str__(self) -> str:
        return f"ID Job: {self.__idJob}\tName Job: {self.__nameJob}\tIndustry Name: {self.__industryName}\tSalary: {self.__salary}\tEvaluation: {self.evaluate()}"
class AI(Job):
    def __init__(self, idJob = -1, nameJob = "", industryName = "", salary = -1, pythonSkill = -1, mlSkill = -1, deepSkill = -1, mathSkill = -1):
        Job.__init__(self, idJob, nameJob, industryName, salary)
        self.__pythonSkill = pythonSkill
        self.__mlSkill = mlSkill
        self.__deepSkill = deepSkill
        self.__mathSkill = mathSkill
    def skill(self):
        return (self.__pythonSkill + self.__mlSkill + self.__deepSkill + self.__mathSkill) * 0.25
    def score(self):
        a = []
        if (3 < self.__pythonSkill and self.__pythonSkill < 4.0):
            a.append(self.__pythonSkill)
        if (3 < self.__mlSkill and self.__mlSkill < 4.0):
            a.append(self.__mlSkill)
        if (3 < self.__deepSkill and self.__deepSkill < 4.0):
            a.append(self.__deepSkill)
        if (3 < self.__mathSkill and self.__mathSkill < 4.0):
            a.append(self.__mathSkill)
        return a
    # def __str__(self) -> str:
    #     return super().__str__() + f"\nSkill: {self.skill}"
class Backend(Job):
    def __init__(self, idJob = -1, nameJob = "", industryName = "", salary = -1, sqlSkill = -1, oopSkill = -1, apiSkill = -1, javaSkill = -1):
        Job.__init__(self, idJob, nameJob, industryName, salary)
        self.__sqlSkill = sqlSkill
        self.__oopSkill = oopSkill
        self.__apiSkill = apiSkill
        self.__javaSkill = javaSkill
    def skill(self):
        return (self.__sqlSkill + self.__oopSkill + self.__apiSkill + self.__javaSkill) * 0.25
    def score(self):
        a = []
        if (3 < self.__sqlSkill and self.__sqlSkill < 4.0):
            a.append(self.__sqlSkill)
        if (3 < self.__oopSkill and self.__oopSkill < 4.0):
            a.append(self.__oopSkill)
        if (3 < self.__apiSkill and self.__apiSkill < 4.0):
            a.append(self.__apiSkill)
        if (3 < self.__javaSkill and self.__javaSkill < 4.0):
            a.append(self.__javaSkill)
        return a
    # def __str__(self) -> str:
    #     return super().__str__() + f"\nSkill: {self.skill}"
class Frontend(Job):
    def __init__(self, idJob = -1, nameJob = "", industryName = "", salary = -1, htmlSkill = -1, cssSkill = -1, nodejsSkill = -1, ux = -1, ui = -1): 
        Job.__init__(self, idJob, nameJob, industryName, salary)
        self.__htmlSkill = htmlSkill
        self.__cssSkill = cssSkill
        self.__nodejsSkill = nodejsSkill
        self.__ux = ux
        self.__ui = ui
    def skill(self):
        return (self.__htmlSkill + self.__cssSkill + self.__nodejsSkill + self.__ux + self.__ui) * 0.2
    def score(self):
        a = []
        if (3 < self.__htmlSkill and self.__htmlSkill < 4.0):
            a.append(self.__htmlSkill)
        if (3 < self.__cssSkill and self.__cssSkill < 4.0):
            a.append(self.__cssSkill)
        if (3 < self.__nodejsSkill and self.__nodejsSkill < 4.0):
            a.append(self.__nodejsSkill)
        if (3 < self.__ux and self.__ux < 4.0):
            a.append(self.__ux)
        if (3 < self.__ui and self.__ui < 4.0):
            a.append(self.__ui)
        return a
    # def __str__(self) -> str:
    #     return super().__str__() + f"\nSkill: {self.skill}"
class FullStack(Backend, Frontend):
    def __init__(self, idJob = -1, nameJob = "", industryName = "", salary = -1, sqlSkill = -1, oopSkill = -1, apiSkill = -1, javaSkill = -1, htmlSkill = -1, cssSkill = -1, nodejsSkill = -1, ux = -1, ui = -1):
        Backend.__init__(self, idJob, nameJob, industryName, salary, sqlSkill, oopSkill, apiSkill, javaSkill)
        Frontend.__init__(self, idJob, nameJob, industryName, salary, htmlSkill, cssSkill, nodejsSkill, ux, ui)
    
ai_job = AI(1, "AI Development", "AI", 10000, 9.5, 8.5, 9.0, 8.0)
frontend_job = Frontend(2, "Frontend Developer", "Web Development", 8000,  8.0, 9.0, 8.5, 9.0)
backend_job = Backend(3, "Backend Developer", "Web Development", 8500, 8.5, 9.0, 8.0, 8.0)
fullstack_job = FullStack(4, "Fullstack Developer", "Web Development", 9500, 8.0, 8.5, 8.5, 8.0, 9.0, 9.0, 8.5, 8, 8.5)

print("AI Job:")
print(ai_job)
print("Frontend Job:")
print(frontend_job)
print("Backend Job:")
print(backend_job)
print("Fullstack Job:")
print(fullstack_job)