

from abc import abstractmethod
from unittest import case

# from presentation.terminal import Terminal

# from __future__ import annotations
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from presentation.terminal import Terminal



class Terminal:

    def __init__(self):#, student_service: StudentService
        from menu import MainMenu
        self.currentmenu = MainMenu(self)
        self.running = True
        # self.student_service = student_service


    def navigate(self, menu: Menu):
        self.current_menu = menu

    def quit(self):
        self.running = False
        print ("quitting")
    

class Menu: #abstract class, just for defining inheritance
    def __init__(self, terminal):
        self.terminal = terminal

    @abstractmethod #children must override
    def render(self) -> None:
        pass


class StudentMenu(Menu):
    def render(self):
        print("\n=== Student Menu ===")
        print("1. Create Student")
        print("2. Back")

        choice = input()

        if choice == "2":
            self.terminal.navigate("MainMenu")

class ProfessorMenu(Menu):
    def render(self):
        print("\n=== Professor Menu ===")
        print("1. Create Professor")
        print("2. Back")

        choice = input()

        if choice == "2":
            self.terminal.navigate("MainMenu")

class ClassMenu(Menu):
    def render(self):
        print("\n=== Class Menu ===")
        print("1. Create Class")
        print("2. Back")

        choice = input()

        if choice == "2":
            self.terminal.navigate("MainMenu")
            from enum import Enum

MENU_MAP = {
    # "MainMenu": MainMenu,
    "StudentMenu": StudentMenu,
    "ProfessorMenu": ProfessorMenu,
    "ClassMenu": ClassMenu,
}

class MainMenu(Menu):
    def render(self) -> None:
        print("1 create new student, 2 create new professor, 3 create new class, 4 enroll student in class, run report, quit")

        userinput: str = input().lower()
        match userinput:
            case 1:
                self.terminal.navigate(StudentMenu(self.terminal))#instead just navigate("MainMenu")
                print("case 1")
            case 2:
                    self.terminal.navigate("ProfessorMenu")
            case 3:
                    self.terminal.navigate("ClassMenu")
            case 4:
                print("case 4")
            case 5:
                # Handle case 5
                print("case 5")
            # case q:
                # self.terminal.quit()
            # case _: #//default// dont need because it tries again?
            #     self.render()

if __name__ == "__main__":
    term = Terminal()
    while term.running:
        term.currentmenu.render()