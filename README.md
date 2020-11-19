# Semester-Registration
First Python GUI Application With Tkinter


Features:

   ***Entry***

1.	ID No
2.	Name
3.	Section
4.	Registration Course
5.	Write Course
6.	Enter ID No

  ***Button***

1.	Add
2.	Delete
3.	Update
4.	Clear
5.	Search
6.	Show Details
7.	Clear

Language:

*Python Tkinter GUI 

Use:

*Python file handling 



->To change the icon of tkinter, I used iconbitmap widgets. First , I converted DIU png image to icon by online icon converter. Then I store the icon image into the python file where the application code stores. For storing data,I am using file handling.Each student has a record file ,where the name,id,section,registration status,course of student's datas are stored. For adding course, used text widgets.we can write multiple line into the text box.We have to fill all entries or we will get error message.For adding new student registration data , we have to fill all entries. Then by clicking add button, we can store data in file. The file name will be “ID no.txt”.We can clear current entries of application by clicking clear button. Then we can add another new data by filling  all entries. We can search by id no if the registration data is existing  or not. If data is existing then it will show “Record is found!!” in text box.  if we want to see the details of any student registration data.we have to click “Show details” Button. The data of file will show into the id no,name,section,status,course’s entry.Then we can update or delete the registration data of student by clicking update and delete button. If the file does not exist ,it will show error message.

***For running this program, make sure the diu.ico(icon image) and the python file is in the same folder , Otherwise, it won’t run the program***