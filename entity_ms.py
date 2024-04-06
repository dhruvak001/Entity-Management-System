students = []
EntityArray = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, Name):
        self.studentName = Name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum

class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student

class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, Name):
        self.name = Name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter


class StudentPortfolio(Entity):
    def __init__(self):
        super().__init__()
        self.head = None

    def add_student_record(self, student):
        new_node = Node(student)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.set_next(new_node)

    def delete_student_record(self, student_name):
        if not self.head:
            return

        if self.head.get_element().get_studentName() == student_name:
            self.head = self.head.get_next()
            return

        current_node = self.head
        while current_node.get_next():
            if current_node.get_next().get_element().get_studentName() == student_name:
                current_node.set_next(current_node.get_next().get_next())
                return

    def find_student(self, student_name):           # not required for now
        current_node = self.head
        while current_node:
            if current_node.get_element().get_studentName() == student_name:
                return current_node.get_element()
            current_node = current_node.get_next()
        return None

    def count_students(self):                       # not required for now
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.get_next()



class LinkedList(Entity):
    def add_student(self, student):
        newNode = Node()
        newNode.set_element(student)
        newNode.set_next(None)
        if not self.get_iterator():
            self.set_iterator(newNode)
        else:
            current = self.get_iterator()
            while current.get_next():
                current = current.get_next()
            current.set_next(newNode)

    def delete_student(self, studentName):
        current = self.get_iterator()
        prev = None
        while current:
            student = current.get_element()
            if student.get_studentName() == studentName:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.set_iterator(current.get_next())
                del current
                return
            prev = current
            current = current.get_next()


'''class Entityarray:              # tried failed , not required
    entities = []

    @classmethod
    def add_entity(cls, entity):
        cls.entities.append(entity)

    @classmethod
    def get_entities(cls):
        return cls.entities
        

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.entities):
            entity = self.entities[self.current_index]
            self.current_index += 1
            return entity
        else:
            raise StopIteration'''



class EntityIterator:               # tried failed

    def __init__(self,EntityArray):
        self.EntityArray = EntityArray
        self.index = 0

    def __next__(self):
        if self.current_index < len(self.entities):
            entity = self.entities[self.current_index]
            self.current_index += 1
            return entity
        else:
            raise StopIteration

def read_input_file(file_path):
    with open(file_path, 'r') as inputFile:
        entities = set()
        for line in inputFile:
            line = line.rstrip('\n')
            checklist = line.split(',')
            student = StudentRecord()
            student.set_studentName(checklist[0])
            student.set_rollNumber(checklist[1])
            students.append(student)

            for i in range(0, len(checklist)-2):
                entityName = checklist[i+2]
                entityExists = False

                if not entityExists:
                    newentityName = ""

                    if entityName[0] == '[':
                        for j in range(0, len(entityName)-1):
                            newentityName += entityName[j+1]
                    elif entityName[len(entityName)-1] == ']':
                        for j in range(0, len(entityName) - 1):
                            newentityName += entityName[j]
                    elif entityName[0] == '[' and entityName[len(entityName)-1] == ']':
                        for j in range(1, len(entityName) - 2):
                            newentityName += entityName[j]
                    else:
                        newentityName = entityName
                    entities.add(newentityName)

        for entityName in entities:
            ll = LinkedList()
            ll.set_name(entityName)
            ll.set_iterator(None)
            EntityArray.append(ll)

    with open(file_path, 'r') as input:
        stptr = 0
        for line in input:
            line = line.rstrip('\n')
            line = line.rstrip('[]')
            checklist = line.split(',')


            for i in range(0, len(checklist)-2):
                entityName = checklist[i+2]
                newentityName = ""

                if entityName[0] == '[':
                    for j in range(0, len(entityName)-1):
                        newentityName += entityName[j+1]
                elif entityName[len(entityName)-1] == ']':
                    for j in range(0, len(entityName) - 1):
                        newentityName += entityName[j]
                elif entityName[0] == '[' and entityName[len(entityName)-1] == ']':
                    for j in range(1, len(entityName) - 2):
                        newentityName += entityName[j]
                else:
                    newentityName = entityName

                for entity in EntityArray:
                    if entity.get_name() == newentityName:
                        entity.add_student(students[stptr])

            stptr += 1

                    
'''if entityName[0] == '[' and entityName[(len(entityName))-1] == ']':
    line = line.rstrip('\n')
        if 
            newentityName += entityName[j] '''
