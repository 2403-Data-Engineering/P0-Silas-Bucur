# P0-Silas-Bucur
<!-- project notes


Milestones:Start on python presentation layer Tuesday 3/31 - complete around Friday 4/3

You don't need an actual database connection to complete nearly all of the presentation layer, just stub out some dummy data at the service layer. Service methods return dummy data to presentation layer. Later you have the service layer grab from data layer, when data layer is ready.

Start on data layer around Monday 4/4 - complete around Tuesday 4/7
-Set up the database connection and build a simple CRUD implementation just to test the functionality.
-Model the business objects and implement SQL schema for them
-implement CRUD as needed for workflows on the domain objects
-connect the layers and finish implementing user stories - complete around Thursday 4/9
-Now have the service layer return data from invoking data layer methods instead of the dummy data.
-Start end-to-end testing to see if your workflows behave the way you expected
wrap up and bugfix.

domain objects: professor, student, class

-presentation layer (api): ProfessorController, StudentController, ClassController OR keep it ONE Class
service layer: professorClass, studentClass, classClass
data layer: professorDao, studentDao, classDao

Data Access Object. It is a design pattern used to abstract and encapsulate all access to a data source, such as a relational database, NoSQL store, or even a remote API. 


render is continuous checker
	render prompt user ,accept, prompt, accept
	have MENU list enter first name, enter last name
	newstudent = Student(firstname, lastname)
	navigate(NewStudent)

def navigate(menu: Menu):
	currentmenu = menu

running = True
currentmenu = mainmenu
while(running)
	currentmenu.render()

pojo simplest encapsulation
6:13
Prof:
PK, first name last name, department, email
Stud:
PKIDautoincrement, first name last name, email, major, year
Class:
PK, class name (junction in students and professor)
minimum amount of data needed for professor, student, and class

delete can also mean hide from the database but not remove completely

presentation layer
menu.py

//from abc import abstractmethod

from presentationlayer.terminal import Terminal

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from presentationlayerterminal.terminal import Terminal

class Menu: //abstract class, just for defining inheritance
	def __init__(self, terminal):
		self.parentterminal = terminal

	@abstrictmethod //overriding?
	def render() - > None:
		pass
class MainMenu(Menu):
	def render() -> None:
		print("1 create new student, 2 create new professor, 3 create new class, 4 enroll student in class, run report, quit")

	userinput: str = input().lower()
	match userinput:
		case 1 
		self.terminal.navigate(NewStudentMenu(self.terminal))
		case 5
	..	case q:
			self.terminal.quit()
		//case _: //default// dont need because it tries again?
			
class NewStudent(Menu):
	def render(self):
		print("new student menu:)
		print("firnam:")
		firstname: str = input()
		print(") //
		lasname, major, email, year
		//validation steps between prompts?

		new_stundent : Student = Student(first_name, lastname.etc)
		self.terminatl.student_servi.save(new_student)
		self.terminal.navigate(MainMenu(termn??)?
terminal.py

from presentationlayer.menu import Menu
class Terminal:

	def __init__(self, student_service: StudentService):
	from presentationlayer.menu import MainMenu
		self.currentmenu = MainMenu(self)
		self.running = True
		self.stufent_service = student_service

	def navigate(self, menu: Menu):
		self.current_menu = menu

	def quit(self):
		self.running = False
		print ("quitting")
	

outside main.py



if __name__ == "__main__":
	terminal = Terminal(StudentService(this is were autowire must happen Sqlconnen(driver..)) //dependancy
//needs to pass prof and class in terminal
	wile (terminal.running)
		terminal.current_menu.render()
	print("Bye")

different foler models
student.py

from dataclass import dataclass

@dataclass
class student:
	id: int
	firnam: str
	las_n: str
	maj, rmail, yr

silas = Student(id=None, firstna="")kwargs
silas2 = Student(None, "silas")args

servicelayer folder
student_srvc.py

class StudentSevr:
def save(self, student: Student) -> Student:
	print("todo implement the sudent service save method)
	
def get_by_ud(id:int)->Student:



The OOP way is where every entity was a class. adds more difficult, circular imports, too many references with only 4 classees

make the Terminal a singleton, and not a class object. Onlyy needs to be 1 terminal presetnign to the user.

switch called match in python? 
selecting new student quees up next menu and exits the function


ask the user for the pk (or some way) to identify the student to get/add

get reports with sql queries, make into file? print it out?
python libraries (use yattag to create html)
yattag yet another tag
pipi install yattag
from yattag import Doc

doc, tag, text = Doc().tagText()

instead of printing it, save it in a file -->



<!-- Python (FastAPI)
@app.get("/users")
def get_users():
    return service.get_users()
	
Spring
@GetMapping("/users")
public List<User> getUsers() {
    return service.getUsers();
} -->