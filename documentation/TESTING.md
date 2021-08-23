# TESTING
## TESTING PLAN (Pre-development)



### RESEARCH

[README/Research](/README.md/#research)

#### Required elements

- Read up on and learn the structure and syntax of Material Design. 
- Investigate what components will be suitable and meet the needs of this project.
- Research how the components work and how to write code to implement them.
- It is crucial to understand how the components function and what I can expect from them.
- Use [Web Maker App](https://webmaker.app/app/) to experiment, learn, and implement instances of the components to see which are better suited for the Garden Almanac.
- Research and study up on MongoDB, to see how to best design a Schema that will fulfil the needs of the Garden Almanac. 

### DEVELOPMENT

[README/Development](/README.md/#development)

#### HTML

-   Incorporate form components using HTML5 and materializecss with SCSS/ CSS. - Form components to incorporate
    -  Accordion
    -  Forms
    -  Inputs with labels, character counters, and browser validation patterns
    -  Nav-bar/ Off-canvas
    -  Modals 
    -  Contact form
    -  Social Icons - Incorporate Bootstrap Breakpoints as media queries in CSS for responsive display. - Use Chrome DevTools to ensure positioning of elements for each breakpoint.

#### JavaScript/ jQuery

- Initialize Materializecss components using jQuery. For this project, I will where possible maintain a preference for using jQuery. 

#### MongoDB
- Design the schema to serve the needs of the Garden Almanac application. 
- Create the database, and collections, along with sample data. 

#### Python/ Flask
- 
- Create and initialize the Flask application in Gitpod using Python. 
- Connect MongoDB database to the Flask application.

### DEPLOYMENT

[README/Deployment](/README.md/#deployment)

#### Test for production

-   **Test local and test live**
    
    - Due to the nature of Python and Jinja, much checking is completed in the process of development while writing the route paths and functions that run the app. 
    - Create the application in Gitpod, using the python server to view the work in the browser. This has two advantages:
	    -  The Python server, and pep8 syntax checking both ensure the code is compliant and structured properly, otherwise the server shuts down. 
	    - Set `debug=True`, ensuring that Jinja errors are shown in the browser, with a lot of detail, so I can fix mistakes as I go. 
    - Deploy the project live to Heroku early, so I can check the live site along the way, ensuring the behaviour I  experience locally is consistent with the live site. 
    -   Compare and test deployed version of the website.
        -   Ensure it is the same and there are no bugs.
        -   Inputs, forms, features need to display and function as expected.
        
-   **Responsiveness**
    
    -   Chrome DevTools:
        -   Test by screen sizes
        -   Test by viewing media queries which will specifically include Material Design breakpoints.
        -   Test on different devices, different operating systems, different browsers, screen sizes.
    -   Share the application to get third party feedback
    
-   **Function**
    
    -   Test on different devices, operating systems, and browsers.
    -   Test all external links, inputs, forms, navigation links, and features.
    
-   **404 Page not found**
    
    - Create 404 Page not found page.
    - Create 405 Method Not Allowed page
    - Create 500 Server Error page
    
-   **User Experience**
    
    -   **Feedback**: Share the application to get feedback and to test the UI to see how users intuit the process of using the application.
    -   **User Stories**: Check the application fulfils the needs expressed in the user stories.

### DEVELOPMENT SETUP

#### Code Editor

-   [Gitpod](https://www.gitpod.io/) I chose to use Gitpod, so I can get support from Code Institute when I need it. It makes it easy to share the workspace and get help troubleshooting problems. 
-   Python3 Development Server. I use the Python3 command `python3 app.py` to run my application in the development server and view the work in the browser. 

My preferred browser for development is Chrome DevTools. I have a USB-C to dual HDMI hub for my MacBook Pro, with 2 x Dell U2419H monitors, wireless keyboard, and mouse.

### TESTING DEVICES

#### MacBook Pro 15 inch

```shell
- Operating System
	- macOS Big Sur 11.2.3
		- Safari Version 14.0.3 (16610.4.3.1.7)
		- Chrome Version 90.0.4430.72 (Official Build) (x86_64)			
		- Firefox 88 (64-bit)
	- Windows 10 Pro (Boot Camp installation)
		- Microsoft Edge Version 
		- Firefox 
		- Chrome Version 
- External Monitors
	-  2 x Dell U2419H Monitor 23.8-inch Full HD 1920 x 1080 at 60 Hz
```

#### HP ProDesk 600 Desktop PC

```shell
- Operating System
	- Windows 10 Pro 
		- Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
		- Firefox 78.10.0esr (64-Bit)
		- Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
- Monitor
	- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz
```

#### Apple iPad Air Gen 1 9.7 inches 4:3 ratio

```shell
- Operating System
	- iOS 12.5.2 (16H30) released March 26
- Screen resolution
	- 1536 x 2048 pixels, 4:3 ratio (~264 ppi density)
```

#### Apple iPhone 11 Pro

```shell
- Operating System
	- iOS 14.4.2
- Screen resolution
	- 2436‑by-1125‑pixel resolution at 458 ppi
	- 5.8‑inch (diagonal) all‑screen OLED Multi‑Touch display
	- Width: 2.81 inches (71.4 mm)
	- Height: 5.67 inches (144.0 mm)
```
----------

## TESTING CHECKLIST (Development-Deployment)
[README/Testing](/README.md/#testing)

Testing is structured into sections, 
1. **All Users:** 
This section tests for pages and features available only to users who are: 1. Not registered, or 2. Logged out. 

2. **Session Users:**
This section tests pages and features available only to users who are logged in.

3. **Admin Users:** 
This section tests pages and features only available to admin users

## TESTING CHECKLIST (Development-Deployment)
[README/Testing](/README.md/#testing)

### ALL USERS
#### Main Navbar
![](/documentation/images/navbar-all-users.png)  
**Pages:** Home, Log in, Register, Contact.
- [x] I click on the home link. The home page is displayed.
- [x] I click on the log in link. The login page with the login form is displayed.
- [x] On the login page, I click on the "Register account" link, and I am redirected to the register page.
- [x] I click on the register link. The register page with the register form is displayed. 	 - [x] On the register page, I click on the "Log in" link, and I am redirected to the "Log in" page.
- [x] I click on the contact link, and I’m redirected to the contact page with the contact form.
- [x] I click on the "Your Garden Almanac" logo in the Navbar, and I am redirected to the home page 

#### Off-canvas Navbar
![](/documentation/images/off-canvas-all-users.png)  
- [x] On my iPhone, I click on the menu hamburger in the top left, the off-canvas menu appears. Four links are showing, Home, Log in, Register, and Contact. 
- [x] I click on the home link. The home page is displayed.
- [x] I click on the log in link. The login page with the login form is displayed.
- [x] On the login page, I click on the "Register account" link, and I am redirected to the register page.
- [x] I click on the register link. The register page with the register form is displayed. 
- [x] On the register page, I click on the "Log in" link, and I am redirected to the "Log in" page.
- [x] I click on the contact link, and I’m redirected to the contact page with the contact form.
- [x] I click on the "Your Garden Almanac" logo in the Navbar, and I am redirected to the home 

#### Footer Links
- [x] I click on the FAQ link. The bottom sheet modal opens, displaying information. 
	- [x] I click on the modal close button, the modal closes. 
- [x] I click on the GitHub icon link. It opens my GitHub profile in a new browser tab. 
- [x] I click on the LinkedIn icon link. It opens my LinkedIn profile in a new browser tab.
- [x] I click on the Contact icon link. It redirects me to the contact page and form. 

#### Home Page "Our World" images
- [x] I click on an image in the "Our World" block, it expands and there is a short text message under the image. 
- [x] I click a second time, it reduces and I am returned to the home page.

#### Contact Page
**Validation**
1. I used the HTML input pattern attribute in the form inputs to provide the first layer of browser validation.
2. I used Flask-WTForms to create the form, and added validation rules in the form class. 
3. In the app route function, I used Flask-WTF `validate_on_submit()` to check the inputs, and added a flash error alert and success alert to display after validation.

	- [x] I click on the send button without filling in any fields. A green line appears under the first input, and a browser validation tooltip message appears asking me to fill in the field. The line then turns red.
	- [x] I fill in the first name field, and the red line under the input turns green.
	- [x] I click send, and a line appears under the second input, with a message asking me to fill in the field.
	- [x] I fill in the last name field, and the red line under the input turns green. 
	- [x] I click send, a red line appears under the email input, and a message asks me to fill in the field. 
	- [x] I enter a false email, the line under the email input turns green.
	- [x] I click send, a red line appears under the message input, and a message asks me to fill in the field. 
	- [x] I enter some text into the message field, and the line under the input turns green. 
	- [x] I click send.
		- [x] A flash message error alert appears in red informing me "Failed Validation" (I only added 3 letters)
		- [x] A message in red appears under the first name input, informing me the field must be between 5 and 20 characters long.
		- [x] A message in red appears under the email input asking me to enter a valid email.
	- [x] I complete the field correctly, click send, and a green success message appears informing me the message has been sent. 
	- [x] I check in the MongoDB messages collection, and the data from the message has been inserted.
		- [x] I log in to the admin account to confirm the message was received. On the messages page, the message is displayed in the admin message inbox. 

#### Register Page
![](/documentation/images/all-users-register.png)  
- [x] On the register page, I click register without filling in any fields. Under each input is a required label. 
- [x] A green line appears under the field with a message asking me to fill in the field. The green line turns red. 
- [x] I enter my first name, a character counter appears, telling me I used 6/15 letters. The red line turns green. 
- [x] I check all the field in the same way, and they all have the same behaviour. I have entered the same username that I already registered.
- [x] I click register, a red flash error alert appears informing me the username already exists. I am still on the register page. 
- [x] I enter the details again, with a different username, I click register, and a green flash success message appears informing me registration successful. I am logged in, and directed to the profile page. The title is Peter's profile. The page is showing me my registration details. 
- [x] I check MongoDB, and the new user information has been inserted. 

#### Login Page
![](/documentation/images/all-users-login.png)  
- [x] On the login page, I click log-in without entering a username or password.
- [x] A green line appears under the field with a message asking me to fill in the field. The green line turns red when I click out of the field without adding a username.
- [x] I enter a username and password that are not registered. A red flash alert appears with a message "Incorrect Username and/or Password". I cannot log in without registering.

### SESSION USERS
#### Main Navbar
![](/documentation/images/navbar-session-user.png)  
Dropdown for "New".  
![](/documentation/images/navbar-session-user-b.png)  
**Pages:** ***"All Users"*** pages + Almanac, Plants, New>Event, New>Plant, New>Category, Log-out.
- [x] I click on the home link. The home page is displayed.
- [x] I click on the Almanac link. The event's page is displayed. 
- [x] I click on the Plant's link. The Plant's page is displayed. 
- [x] I click on New Event link. The add event page is displayed.
- [x] I click on New Plant link. The add plant page is displayed.
- [x] I click on New Category link. The add category page is displayed.
- [x] I click on "User First-name's" Profile link. The profile page is displayed.
- [x] I click on Log out link. I am logged out and the login page is displayed.
- [x] I click on Contact link. The contact page and form is displayed. 

#### Off-canvas Navbar
![](/documentation/images/off-canvas-session-user.png)  
- [x] I click on the home link. The home page is displayed.
- [x] I click on the Almanac link. The event's page is displayed. 
- [x] I click on the Plant's link. The Plant's page is displayed. 
- [x] I click on New Event link. The add event page is displayed.
- [x] I click on New Plant link. The add plant page is displayed.
- [x] I click on New Category link. The add category page is displayed.
- [x] I click on "User First-name's" Profile link. The profile page is displayed.
- [x] I click on Log out link. I am logged out and the login page is displayed.
- [x] I click on Contact link. The contact page and form is displayed. 
#### Login Page
- [x] I enter my username and password, and click log in. I am logged in and redirected to the Profile page. My name is displayed, "Daniel's Profile. A flash alert message says "Welcome, Daniel".
- [x] In the Navbar, my name is displayed "Daniel's Profile". The Logo "Your Garden Almanac" has changed to "My Garden Almanac".
![](/documentation/images/login-user-profile.png)    

#### Profile Page
- [x] All input fields displaying my information are disabled. I click on them, but I cannot change teh information. Below the disabled inputs is an edit profile button.
- [x] I click the edit profile button, it turns green and redirects me to the Update Daniel's Profile page. 

#### Edit Profile Page
- [x] The joined date, and the username inputs are disabled, and I cannot change the information in them. The first name, last name and email fields are editable, and required. The password field is empty, but a message under it says required. 
- [x] I change my email, click update information, a red line appears under the password field with a tooltip asking me to fill in the field.
- [x] I enter the wrong password, click update information, and a flash red alert message appears asking me to confirm the correct password. 
- [x] I enter the correct password, a green flash success alert appears informing me the information has been updated successfully. I am redirected to the profile page, and the information displayed in the disabled inputs is reflecting my changes.
- [x] I check MongoDB, and the updated information has been inserted to the users document in the users collection.

#### Almanac Page
The Almanac page has an Material Design Collapsible that displays garden events and related plant information. 
- [x] I click on the Almanac link in the Navbar, the "My Events" page opens. A closed Material Design collapsible is showing a list of events. The collabsible header of each event displays the event date, month, and name. 
![](/documentation/images/collapsible-events.png)    
- [x] I click on an item, it opens, showing me the event and plant information. The information is highlighted, and reflects the information I entered for the event and plant. 
- [x] The event and plant each have an edit button. 
- [x] The event name, event category,  repeat value, event notes, and created by are shown for the event. 
- [x] The plant displays the plant type, plant name, sowing date, planting date, harvesting dates, when are what to fertilise with, notes, and created by with my username. 
- [x] Where I entered no information, there is placeholder text informing me no information was added, or asking me to add information. 
![](/documentation/images/collapsible-event.png)    

#### Add Event Page
- [x] ***(no plants or categories created)*** In the Navbar, I click on New > Event.  I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add plants and categories before entering an event. 
- [x] ***(no categories created)*** In the Navbar, I click on New > Event.  I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add categories before entering an event. 
- [x] ***(no plants created)*** In the Navbar, I click on New > Event.  I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add plants before entering an event. 
- [x] ***(plants and categories created)*** In the Navbar, I click on New > Event.  I'm redirected to the Add Event page with a form and inputs for adding an event. Four fields are required, and two are optional.
![](/documentation/images/add-event-form.png)  
- [x] I click on add event without filling in the inputs. A tooltip message appears asking me to fill in the first field. 
- [x] I select a category, click add event, and the tooltip appears asking me to select an item in the plants list.
- [x] I select a plant, click add event, and the tooltip appears asking me to fill in the event name field.
- [x] I fill in the event name field, click add event, and the tooltip appears asking me to fill in the event date field. 
- [x] I select a date, click add event, I am redirected to the "My Events" page, and a green flash alert informs me the event was successfully added. The Event is displayed in the Collapsible. 
- [x] The two inputs did not fill in show messages in the collapsible. event "event repeats Enter how often", and "Event Notes: No Notes Recorded".
![](/documentation/images/add-event-success.png)  
- [x] I confirm the event data was inserted into the garden_events collection by checking in MongoDB Atlas. The event has been added.
 
#### Edit Event Page
- [x] I click on the edit event button in the collapsible and for the event, and I am redirected to the edit event page with a form and inputs displaying the information for the event.
- [x] I fill in the empty fields "Event Repeats", and "Event Notes", and click save. I'm redirected back to the "My Events" Page, and a green flash alert informs me the event was successfully updated. 
- [x] The updated event is now showing the new information in the collapsible. The information has been inserted into the database.

#### Delete Event
- [x] On the edit event page for the event, I click delete, a modal appears with a red flash alert informing me that deleting event data is irriversable. It asks me if I am sure I want to delete the "Plant Sname cucumbers".
![](/documentation/images/modal-delete-event.png)  
- [x] I click cancel and am redirected back to the Almanac "My Events" page.
- [x] I confirm and click delete, am redirected back to the Almanac "My Events" page, where a green flash alert informs me the event was successfully deleted. The event is no longer in the list in the collapsible. 

#### Plants Page**
- [x] 

#### Add Plant Page**
- [x] 

#### Edit Plant Page**
- [x] 

#### Delete Plant**
- [x] 

#### Add Category Page**
- [x] 

#### Edit Category Page**
- [x] 

#### Delete Category**
- [x] 

### ADMIN USERS
**Pages:** All pages + messages page.
#### Login Page
- [x] I enter my admin username and password, and click login. I am logged in and directed to the Admin Profile Page. 
#### Navbar
![](/documentation/images/navbar-admin.png)  
Admin user has one Navbar link exclusive for admin users. "Messages". 
- [x] I click on the Navbar messages link. The message's page opens, showing a collapsible with some messages.
#### Off-canvas Navbar
![](/documentation/images/off-canvas-admin-users.png)  
Admin user has one Navbar link exclusive for admin users. "Messages". 
- [x] I click on the Navbar messages link. The message's page opens, showing a collapsible with some messages.
#### Messages Page
- [x] I click on the Navbar messages link. The message's page opens, showing a collapsible with some messages.
#### View Messages

#### Delete Messages
	- [x] 







### NOTES - To Check reminders
1. 
2. Check 404 errors. 
3. Check user stories. 
4. Check differences between admin and normal user account.
5. New user vs user with data shows blue alert on the event, plants, and categories page. 




## Responsive Breakpoints and media queries

## Testing Devices

## USER STORIES REVIEW (Development-Deployment)

# NOTE TO SELF
Add individual elements list, and checked checkboxes with notes, bugs, unfinished etc
Document testing of user stories with images/ screenshots 


Issue 1. Collapsible displaying white background when the header of an item is clicked. Not showing locally. Fix default materializecss CSS style by adding `background-color: none` in style.css.
Issue 2. Add border-top to collapsible body so when the item opens, there is a border under the collapsible header. 
  
  

### Information Section