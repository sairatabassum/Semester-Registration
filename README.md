# Semester-Registration
First Python GUI Application With Tkinter
![Capture](https://user-images.githubusercontent.com/52861859/114088039-67fd2a00-98d6-11eb-9304-3d3293fb33d8.PNG)


### Features:

   ***Entry***

- ID No
- Name
- Section
- Registration Course
- Write Course
- Enter ID No

 ***Button***

- Add
- Delete
- Update
- Clear
- Search
- Show Details
- Clear

**Language:** Python 

**Use:** Python file handling, Tkinter Package



To change the icon of tkinter, I used iconbitmap widget. First , I converted diu png image to diu icon by online icon converter. Then I store the icon image into the python file where the application code stores. For storing data,I am using file handling. Each student has a record file ,where the name,id,section,registration status,course with codes of student's data is stored. For adding course title, used text widget.we can write multiple line into the text box.For adding new student registration data , we have to fill all entries or we will get error message. Then by clicking add button, we can store data in file. The file name will be “ID no(The id that we enter).txt”.We can clear the current entries of application by clicking clear button.We can search by id no if the registration data is existing  or not. If data is existing then it will show “Record is found!!” in text box. If we want to see the details of any student registration data.we have to click “Show details” Button. The data of file will show into the id no,name,section,status,course’s entry.Then we can update or delete the registration data of student by clicking update and delete button. If the file is not exist ,it will show error message.

***For running this program, make sure the diu.ico(icon image) and the python file is in the same folder , Otherwise, it won’t run the program***
