

from abc import abstractmethod
from unittest import case

from presentationlayer.presentationlayerterminal.terminal import Terminal

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from presentationlayerterminal.terminal import Terminal

class Menu: #abstract class, just for defining inheritance
    def __init__(self, terminal):
        self.parentterminal = terminal

    @abstractmethod #overriding?
    def render() -> None:
        pass
class MainMenu(Menu):
    def render() -> None:
        print("1 create new student, 2 create new professor, 3 create new class, 4 enroll student in class, run report, quit")

    userinput: str = input().lower()
    match userinput:
        case 1:
            self.terminal.navigate(NewStudentMenu(self.terminal))
        case 2:
            # Handle case 2
            print()
        case 3:
            pass
        case 4:
            pass
        case 5:
            # Handle case 5
            pass    
        case q:
            self.terminal.quit()
            #case _: //default// dont need because it tries again?