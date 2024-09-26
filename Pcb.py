from StateEnum import State
import os

class Pcb():
    def __init__(self, state: State, pid: int, program_counter: int, registers: list[bool], memory_limits: tuple, list_of_open_files: list ) -> None:
        self._state = state
        self._pid = pid
        self._program_counter = program_counter
        self._registers = registers
        self._memory_limits = memory_limits
        self._list_of_open_files = list_of_open_files


    # Setters
    def setState(self, state: State) -> None:
        self._state = state

    
    def setPid(self, pid: int) -> None:
        self._pid = pid

        
    def setProgramCounter(self, program_counter: int) -> None:
        self._program_counter = program_counter

        
    def setRegisters(self, registers: list[bool]) -> None:
        self._registers = registers

        
    def setMemoryLimits(self, memory_limits: tuple) -> None:
        self._memory_limits = memory_limits

    
    def setListOfOpenFiles(self, list_of_open_files: list) -> None:
        self._list_of_open_files = list_of_open_files

    
    # Getters
    def getState(self) -> State:
        return self._state
    
    
    def getPid(self) -> int:
        return self._pid
    
        
    def getProgramCounter(self) -> int:
        return self._program_counter
    
        
    def getRegisters(self) -> list[bool]:
        return self._registers
    
        
    def getMemoryLimits(self) -> tuple:
        return self._memory_limits
    
    
    def getListOfOpenFiles(self) -> list:
        return self._list_of_open_files
  

    def __repr__(self) -> str:
        string = ""
        for member in self.__dict__:
            string += str(member) + ": " + str(self.__dict__[member]) + os.linesep
        return string


if __name__ == "__main__":
    test_process = Pcb(State.READY, 1, 12, [True, False], (203, 556), [])
    print(test_process)

