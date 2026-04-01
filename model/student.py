
from dataclasses import dataclass

@dataclass
class student:
	id: int
	firnam: str
	las_n: str
	major: str
	email: str
	year: int

# silas = Student(id=None, first_name="")#kwargs
# silas2 = Student(None, "silas")#args


