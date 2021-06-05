buttonID = 1
elevatorID = 1
floorButtonID = 1

class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators) -> None:
        self.ID = _id
        self.status = 'offline'
        self.elevatorsList = []
        self.callButtonsList = []

        self.callButtons(_amountOfFloors)
        self.elevators(_amountOfFloors, _amountOfElevators)

        # for j in range(0, _amountOfFloors + 1):
        #     floorButton = j
        #     if j != 1:
        #         button = CallButton(j, j, 'down');
        #         self.callButtonsList.append(button)
        #     else:
        #         j != _amountOfFloors
        #         button = CallButton(j, j, 'up');
        #         self.callButtonsList.append(button)

    def callButtons(self, _amountOfFloors) -> None:
        floorButton = 1
        global buttonID
        for i in range(_amountOfFloors):
            if floorButton < _amountOfFloors:
                button = CallButton(buttonID, floorButton, 'up')
                self.callButtonsList.append(button)
                buttonID += 1

            if floorButton > 1:
                button = CallButton(buttonID, floorButton, 'down')
                self.callButtonsList.append(button)
                buttonID += 1

            floorButton += 1

    def elevators(self, _amountOfFloors, _amountOfElevators) -> None:
        global elevatorID
        for i in range(_amountOfElevators):
            elevator = Elevator(elevatorID, _amountOfElevators)
            self.elevatorsList.append(elevator)
            elevatorID += 1

    def bestElevator(self, _requestedFloor, _requestedDirection) -> None:
        bestElevatorInfo = {
            "getElevator": "",
            "score": 5,
            "floorCost": 10000
        }

        for elevator in self.elevatorsList:
            if _requestedFloor == elevator.currentFloor and elevator.status == 'stopped' and _requestedDirection == elevator.direction:
                bestElevatorInfo = self.elevatorScore(1, elevator, bestElevatorInfo, _requestedFloor)

            elif _requestedFloor > elevator.currentFloor and elevator.direction == 'up' and _requestedDirection == elevator.direction:
                bestElevatorInfo = self.elevatorScore(2, elevator, bestElevatorInfo, _requestedFloor)

            elif _requestedFloor < elevator.currentFloor and elevator.direction == 'down' and _requestedDirection == elevator.direction:
                bestElevatorInfo = self.elevatorScore(2, elevator, bestElevatorInfo, _requestedFloor)

            elif elevator.status == 'idle':
                bestElevatorInfo = self.elevatorScore(3, elevator, bestElevatorInfo, _requestedFloor)

            else:
                bestElevatorInfo = self.elevatorScore(4, elevator, bestElevatorInfo, _requestedFloor)

        return bestElevatorInfo["getElevator"]

    def elevatorScore(self, scoreCheck, newElevator, bestElevatorInfo, floor) -> None:
        if scoreCheck < bestElevatorInfo["score"]:
            bestElevatorInfo["score"] = scoreCheck
            bestElevatorInfo["getElevator"] = newElevator
            bestElevatorInfo["floorCost"] = abs(newElevator.currentFloor - floor)
        elif bestElevatorInfo["score"] == scoreCheck:
            gap = abs(newElevator.currentFloor - floor)
            if bestElevatorInfo["floorCost"] > gap:
                bestElevatorInfo["score"] = scoreCheck
                bestElevatorInfo["getElevator"] = newElevator
                bestElevatorInfo["floorCost"] = gap

        return bestElevatorInfo

        # for i in range(len(self.elevatorsList)):
        #     if self.elevatorsList[i].status == 'idle':
        #         elevatorDistance = abs(self.elevatorsList[i].currentFloor - _requestedFloor)
        #     if elevatorDistance < floorCost:
        #         floorCost = elevatorDistance
        #         getElevator = self.elevatorsList[i]
        #         getElevator.status = 'active'
        #
        #     return getElevator

    def requestElevator(self, _requestedFloor, _direction):
        chooseElevator = self.bestElevator(_requestedFloor, _direction)
        print("** ELEVATOR " + str(self.ID) + " IS ON ROUTE **");
        chooseElevator.floorRequestList.append(_requestedFloor);
        # getElevator.floorRequestList.sort(sortFloors);
        chooseElevator.go(_requestedFloor);
        return chooseElevator

class Elevator:
    def __init__(self, _id, _amountOfFloors) -> None:
        self.ID = _id
        self.status = 'idle'
        self.direction = ""
        self.currentFloor = 1
        self.door = Door(_id)
        self.floorRequestButtonsList = []
        self.floorRequestList = []

        self.floorRequestButtons(_amountOfFloors)

    def floorRequestButtons(self, _amountOfFloors):
        floorButton = 1
        global floorButtonID
        for i in range(_amountOfFloors):
            requestButtonObject = FloorRequestButton(floorButtonID, floorButton)
            self.floorRequestButtonsList.append(requestButtonObject)
            floorButton += 1
            floorButtonID += 1

    def requestFloor(self, _requestedFloor):
        self.floorRequestList.append(_requestedFloor)
        print("Floor to go to once inside: ", str(self.floorRequestList))
        # self.floorRequestList.sort(sortFloors)
        self.go(_requestedFloor)

    def go(self, _requestedFloor):
        if range(len(self.floorRequestList)):
            requestedDestination = self.floorRequestList[0]
            self.status = 'in transit'

            if (self.currentFloor == requestedDestination):
                self.status = 'at destination'
                self.direction = 'idle'
                self.door.status = 'open'

            elif (self.currentFloor < requestedDestination):
                self.direction = 'up'
                while (self.currentFloor < requestedDestination):
                  print("Elevator is currently on floor: ", self.currentFloor)
                  self.currentFloor += 1

            elif (self.currentFloor > requestedDestination):
                self.direction = 'down'
                while (self.currentFloor > requestedDestination):
                  print("Elevator is currently on floor: ", self.currentFloor)
                  self.currentFloor -= 1

        self.status = 'offline'
        self.floorRequestList.pop()
        print("Elevator has arrived on floor: ", str(self.currentFloor))
        print("Opening doors <>")

        self.status = 'idle'

class CallButton:
    def __init__(self, _id, _floor, _direction) -> None:
        self.ID = _id,
        self.status = 'off',
        self.floor = _floor,
        self.direction = _direction

class FloorRequestButton:
    def __init__(self, _id, _floor) -> None:
        self.ID = _id,
        self.status = 'closed',
        self.floor = _floor

class Door:
    def __init__(self, _id) -> None:
        self.ID = _id,
        self.status = 'closed'

# def sortFloors(self, a, b):
#     return a-b

#test scenario
# column = Column('B',2,2)
#
# column.elevatorsList[0].currentFloor = 3
# elevator = column.requestElevator(1,'down')
# elevator.requestFloor(6)
#
# column.elevatorsList[0].currentFloor = 6
# elevator1 = column.requestElevator(3,'down')
# elevator1.requestFloor(5)
#
# column2 = Column('A',4,1)
#
# column2.elevatorsList[0].currentFloor = 10
# elevator2 = column2.requestElevator(9,'up')
# elevator2.requestFloor(2)

        # return _amountOfElevators
        # self._amountOfFloors = _amountOfFloors
        #self._amountOfElevators = _amountOfElevators
    # if __name__ == '__Column__': Column()
