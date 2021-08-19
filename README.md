# Django Workshop Exercise 8

In this exercise we will apply a user restriction logic to the application so that only admin users have access to the Person creation page.
<br/><br/>
## 1. Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```
<br/><br/>
## 2. Hide the "Users" entry from side bar for non-admin users.
The sidebar is definied in the template file "base.html".  Open this file, and use a Django "if" block  to wrap around the third link in the sidebar where it leads to "/main/createPerson". You can assume that the current login user (called "login_user") is always passed into this "base.html" template when it is rendered.

<details>
  <summary>Click for solution</summary>
  
```sh
 <div class="sidenav">
        <a href="/main">Home</a>
        <a href="/main/createList">Create</a>
        <!-- ToDo: only show the link if the current login user is an admin  -->
        {% if login_user.isAdmin %}
                <a href="/main/createPerson">Users</a>
        {% endif %}
</div>
```
</details>

<br/><br/>
## 3. Restrict any non-admin users from accessing the "Users" Person creation page
Although we have hide the page entry from the side bar, any non-admin users can get around this by manually going into the path "/main/createPerson" To fix this, implement a check logic at the beginning of the view function "createPerson" in "views.py".  If a non-admin user is trying to access this page, redirect the user to a new page which says "Access Denided!" 


