class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators) -> None:
        self.ID = _id
        self.status = 'offline'
        self.elevatorsList = []
        self.callButtonsList = []

        for i in range(0, _amountOfElevators):
            elevator = Elevator(i, _amountOfElevators)
            self.elevatorsList.append(elevator)

        for j in range(0, _amountOfFloors + 1):
            floorButton = j
            if j != 1:
                button = CallButton(j, j, 'down');
                self.callButtonsList.append(button)
            else:
                j != _amountOfFloors
                button = CallButton(j, j, 'up');
                self.callButtonsList.append(button)

    def bestElevator(self, _requestedFloor):
        getElevator = ""
        floorCost = 10000

        for i in range(len(self.elevatorsList)):
            if self.elevatorsList[i].status == 'idle':
                elevatorDistance = abs(self.elevatorsList[i].currentFloor - _requestedFloor)
            if elevatorDistance < floorCost:
                floorCost = elevatorDistance
                getElevator = self.elevatorsList[i]
                getElevator.status = 'active'

            return getElevator

    def requestElevator(self, _requestedFloor, _direction):
        getElevator = self.bestElevator(_requestedFloor)
        print("** ELEVATOR " + self.ID + " IS ON ROUTE **");

        getElevator.floorRequestList.append(_requestedFloor);
        # getElevator.floorRequestList.sort(sortFloors);
        getElevator.go(_requestedFloor);

        return getElevator

class Elevator:
    def __init__(self, _id, _amountOfFloors) -> None:
        self.ID = _id
        self.status = 'idle'
        self.direction = ""
        self.currentFloor = 1
        self.door = Door(_id)
        self.floorRequestButtonsList = []
        self.floorRequestList = []

        for i in range(_amountOfFloors):
            requestButtonObject = FloorRequestButton(i, _amountOfFloors)
            self.floorRequestButtonsList.append(requestButtonObject)

    def requestFloor(self, _requestedFloor):

        self.floorRequestList.append(_requestedFloor)
        print("Floor to go to once inside: ", self.floorRequestList)
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
        print("Elevator has arrived on floor: ", self.currentFloor)
        print("Opening doors <>")

        self.status = 'idle'

class CallButton:
    def __init__(self, _id, _floor, _direction) -> None:
        self.ID = _id,
        self.status = 'off',
        self.floor = _floor,
        self.direction = ""

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
column = Column('B',2,2)

column.elevatorsList[0].currentFloor = 3
elevator = column.requestElevator(1,'down')
elevator.requestFloor(6)

column.elevatorsList[0].currentFloor = 6
elevator1 = column.requestElevator(3,'down')
elevator1.requestFloor(5)

column2 = Column('A',4,1)

column2.elevatorsList[0].currentFloor = 10
elevator2 = column2.requestElevator(9,'up')
elevator2.requestFloor(2)

        # return _amountOfElevators
        # self._amountOfFloors = _amountOfFloors
        #self._amountOfElevators = _amountOfElevators
    # if __name__ == '__Column__': Column()
