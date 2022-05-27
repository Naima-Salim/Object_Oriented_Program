#Assignment
# Add these methods to class student - full_name, year_of_birth, initials. 
# Create two instances and verify the work as expected       
class Student:
     def __init__(self,full_name,letters):
         self.full_name=full_name
         self.letters=letters

     def hello_full_name(self):
         return (f"Hello {self.full_name}")
     
     def year_of_birth(self, age):
         birth_date=2022-age
         return(f"Hello {self.full_name} you were born in {birth_date}") 

     def initials(self):
         return(f" Hello your initials are {self.letters}") 

