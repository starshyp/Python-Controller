class Column:
    def __init__(_id, _amountOfFloors, _amountOfElevators):
        this.ID = _id
        this.status = 'offline'
        this.elevatorsList = []
        this.callButtonsList = []
        # return _amountOfElevators
        # this._amountOfFloors = _amountOfFloors
        #this._amountOfElevators = _amountOfElevators
    # if __name__ == '__Column__': Column()
    for i in _amountOfElevators:
        elevator = Elevator(i, _amountOfElevators)
        this.elevatorsList.push(elevator)

    for j in _amountOfFloors:
        floorButton = j
        if j != 1:
            button = CallButton(j, 'offline', floorButton, 'down');
            this.callButtonsList.push(button)
        else:
            j != _amountOfFloors
            button = CallButton(j, 'offline', floorButton, 'up');
            this.callButtonsList.push(button)


    def requestElevator(_requestedFloor, _direction):
        # //Select an elevator/available cage
        this.bestElevator(_requestedFloor, _direction);

        # //process request
        elevator2 = Elevator(this.ID)
        elevator2.floorRequestList.push(_requestedFloor)
        elevator2.floorRequestList.sort(sortFloors)
        console.log("Elevator Requested on Floor: " + elevator2.floorRequestList);

        # //Make the chosen elevator move to the user/routed
        elevator2.go()

        # //Operate the doors
        elevator2.open()


    def bestElevator(_requestedFloor, _direction):
        findElevator;
        floorCost = 999999;
        for i in this.elevatorsList.length:
            elevatorToll = Math.abs(this.elevatorsList[i].currentFloor - _requestedFloor);
            if (elevatorToll < floorCost):
                floorCost = elevatorToll
                findElevator = this.elevatorsList[i]

        return findElevator;
        console.log(findElevator);
        console.log("Elevator " + this.ID + " is on route.")


class Elevator:
    def __init__(_id, _amountOfFloors):
        this.ID = _id
        this.status = 'online'
        this.direction
        this.currentFloor = 1
        this.door = Door(_id)
        this.floorRequestButtonsList = []
        this.floorRequestList = []

    for i in _amountOfFloors:
        requestButtonObject = FloorRequestButton(i, _amountOfFloors)
        this.floorRequestButtonsList.push(requestButtonObject)

    def requestFloor(_requestedFloor):

        # //process request
        this.floorRequestList.push(_requestedFloor)
        console.log("Floor to go to once inside: " + this.floorRequestList)
        this.floorRequestList.sort(sortFloors)

        # //Make the elevator move to the user’s destination
        this.go()

        # //Operate the doors
        this.open()

    def go():
        while (this.floorRequestList.length != 0):
            requestedDestination = this.floorRequestList[0];
            this.status = 'in transit';

        if (this.currentFloor == requestedDestination):
            this.status = 'at destination'
            this.direction = 'idle';
            this.door.status = 'open';
            console.log("Door Status: " + this.door.status);

        elif (this.currentFloor < requestedDestination):
            this.direction = 'up';
            while (this.currentFloor < requestedDestination):
              console.log("Elevator " + this.ID + " is currently on floor: " + this.currentFloor)
              this.currentFloor += this.currentFloor

        elif (this.currentFloor > requestedDestination):
            this.direction = 'down'
            while (this.currentFloor > requestedDestination):
              console.log("Elevator " + this.ID + " is currently on floor: " + this.currentFloor);
              this.currentFloor -= this.currentFloor

        this.status = 'offline'
        this.floorRequestList.shift()
        console.log("Elevator " + this.ID + " has arrived on floor: " + this.currentFloor)
        console.log("Opening doors <>")

        this.status = 'idle'

    def open():
        while (this.currentFloor == this._requestedFloor):
            this.door.status = 'open';
            console.log("Opening doors <>")

class CallButton:
    def __init__(_id, _floor, _direction):
        this.ID = _id,
        this.status = 'off',
        this.floor = _floor,
        this.direction

class FloorRequestButton:
    def __init__(_id, _floor):
        this.ID = _id,
        this.status = 'closed',
        this.floor = _floor

class Door:
    def __init__(_id):
        this.ID = _id,
        this.status = 'closed'

def sortFloors(a,b):
    return a-b


# //SCENARIO 1 REVISED *NOT WORKING*
# // let column = new Column("A",1,1) //_id, _amountOfFloors, _amountOfElevators
# // column.elevatorsList[0].currentFloor = 3
# // let elevator = column.requestElevator(3,'up') //_requestedFloor, _direction
# // elevator.requestFloor(7) //_requestedFloor

# // SCENARIO 1
column1 = Column("A",1,1) //_id, _amountOfFloors,
column1.elevatorsList[0].currentFloor = 3
column1.requestElevator(3,'up') //_requestedFloor, _direction
# // console.log(column1);

elevator1 = Elevator("A",4) //_id, _amountOfFloors
elevator1.requestFloor(7) //_requestedFloor
# // console.log(elevator1);
