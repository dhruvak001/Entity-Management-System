# Entity Management system (Python)

This Python script demonstrates a simple entity management system using classes and data structures like linked lists. The system primarily focuses on managing student records within different entities.

**Input format:**
The input format is a CSV file which contains the Name, Roll Number, Department, Course, Hostel and Club information about the students.

**Output Format:**
The output must contain the file student_solution(rollnumber).py

**Features:**</br>
**StudentRecord Class:** Defines a basic structure for student records, including attributes for student name and roll number.</br>
**Node Class:** Defines a node structure for linked lists.</br>
**Entity Class:** Represents a generic entity with a name and an iterator.</br>
**StudentPortfolio Class: **Inherits from Entity and manages student records using a linked list.</br>
**LinkedList Class:** Inherits from Entity and provides basic linked list operations to manage students.</br>
**EntityIterator Class: **(Incomplete) A class to iterate through entities (Not fully implemented).</br>
**read_input_file() Function:** Reads student records from an input file and populates the entity management system.</br>

**How to Use:**</br>
Ensure you have Python installed on your system.</br>
Download the script (entity_management.py) to your local machine.</br>
Prepare an input file with student records in the following format: StudentName,RollNumber,Entity1,Entity2,....so on</br>
Run the script and provide the path to the input file as an argument.</br>
