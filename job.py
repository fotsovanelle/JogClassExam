class Job:
    def __init__(self, job_id,description) -> None:
        self.__job_id = job_id
        self.__description =description

    def get_Job_id(self):
        return self.__job_id
    def get_description(self):
        return self.__description
    def set_Job_id(self,job_id):
        self.__job_id = job_id 
    def set_Job_description(self,description):
        self.description = description        

    def __str__(self) -> str:
        return(f"Job_id: {self.get_Job_id()}  \nDesription:{self.get_description()} " )

           
