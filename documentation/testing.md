
# TESTING
## TESTING PLAN (Pre-development)

[README](/README.md) Documentation for the project

[README/Testing](/README.md/#testing)


### RESEARCH

[README/Research](/README.md/#research)

#### Required elements

- Read up on and learn the structure and syntax of Material Design. 
- Investigate what components will be suitable and meet the needs of this project.
- Research how the components work and how to write code to implement them.
- It is crucial to understand how the components function and what I can expect from them.
- Use [Web Maker App](https://webmaker.app/app/) to experiment, learn, and implement instances of the components to see which are better suited for the Garden Almanac.
- Research and study up on MongoDB to see how to best design a Schema that will fulfill the needs of the Garden Almanac. 

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

- Initialize Materializecss components using jQuery. For this project, I will, where possible, maintain a preference for using jQuery. 

#### MongoDB
[README/MongoDB](/README.md/#mongodb)

- Design the schema to serve the needs of the Garden Almanac application. 
- Create the database, and collections, along with sample data. 

#### Python/ Flask
- 
- Create and initialize the Flask application in Gitpod using Python. 
- Connect the MongoDB database to the Flask application.

### DEPLOYMENT
[README/Deployment](/README.md/#deployment)

#### Test for production

-   ** Test local and Test live**
    
    - Due to the nature of Python and Jinja, checking is completed in the process of development while writing route paths and functions that run the app. 
    - Create the application in Gitpod, using the python server to view the work in the browser. It has two advantages:
	    -  The Python server and pep8 syntax checking ensure the code is compliant and structured correctly; otherwise, the server shuts down. 
	    - Set `debug=True`, ensuring that Jinja errors show in the browser, with a lot of detail, so I can fix mistakes as I go. 
    Deploy the project live to Heroku early to check the live site along the way, ensuring the behavior I  experience locally is consistent with the live site. 
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
    
    **Feedback**: Share the application to get feedback and test the UI to see how users intuit the application process.
    -   **User Stories**: Check the application fulfills the needs expressed in the user stories.

### DEVELOPMENT SETUP

#### Code Editor

[Gitpod](https://www.gitpod.io/): I chose to use Gitpod to get support from Code Institute when I need it. It makes it easy to share the workspace and get help troubleshooting problems. 
-   Python3 Development Server: I use the Python3 command `python3 app.py` to run my application in the development server and view the work in the browser. 

My preferred browser for development is Chrome DevTools. I have a USB-C to dual HDMI hub for my MacBook Pro, with 2 x Dell U2419H monitors, a wireless keyboard, and a mouse.

### TESTING DEVICES
[README/Testing Devices Info](/README.md/#testing-devices-information)
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

Testing structured into sections, 
1. **All Users:** 
This section tests for pages and features available only to users who are: 1. Not registered, or 2. Logged out. 

2. **Session Users:**
This section tests pages and features available only to logged-in users.

3. **Admin Users:** 
This section tests pages and features only available to admin users
---
### ALL USERS
#### Main Navbar
![](/documentation/images/navbar-all-users.png)  
**Pages:** Home, Log in, Register, Contact.
- [x] I click on the home link. The home page is displayed.
- [x] I click on the login link. The login page with the login form is displayed.
- [x] On the login page, I click on the "Register account" link, and it opens the registration page.
- [x] I click on the register link. The register page with the registration form is displayed. 	 - [x] On the register page, I click on the "Log in" link, and it opens the "Log in" page.
- [x] I click on the contact link, and it opens the contact page with the contact form.
- [x] I click on the "Your Garden Almanac" logo in the Navbar, and it links to the home page 

#### Off-canvas Navbar
![](/documentation/images/off-canvas-all-users.png)  
- [x] On my iPhone, I click on the menu hamburger in the top left, the off-canvas menu appears. Four links are showing, Home, Log in, Register, and Contact. 
- [x] I click on the home link. The home page is displayed.
- [x] I click on the login link. The login page with the login form is displayed.
- [x] On the login page, I click on the "Register account" link, and it opens the registration page.
- [x] I click on the register link. The registration page with the registration form is displayed. 
- [x] On the register page, I click on the "Log in" link, and it opens the "Log in" page.
- [x] I click on the contact link, and it opens the contact page with the contact form.
- [x] I click on the "Your Garden Almanac" logo in the Navbar, which links to the home page.

#### Footer Links
- [x] I click on the FAQ link. The bottom sheet modal opens, displaying information. 
	- [x] I click on the modal close button, the modal closes. 
- [x] I click on the GitHub icon link. It opens my GitHub profile in a new browser tab. 
- [x] I click on the LinkedIn icon link. It opens my LinkedIn profile in a new browser tab.
- [x] I click on the Contact icon link. It redirects me to the contact page and form. 

#### Home Page "Our World" images
- [x] I click on an image in the "Our World" block, it expands, and there is a short text message under the image. 
- [x] I click a second time, it reduces, and I'm back on the home page.

#### Contact Page
**Validation**
1. I used the HTML input pattern attribute in the form inputs to provide the first layer of browser validation.
2. I used Flask-WTForms to create the form and added validation rules in the form class. 
3. In the app route function, I used Flask-WTF `validate_on_submit()` to check the inputs and added a flash error alert and success alert to display after validation.

	- [x] I click on the send button without filling in any fields. A green line appears under the first input, and a browser validation tooltip message asks me to fill in the form field. The line then turns red.
	- [x] I fill in the first name field, and the red line under the input turns green.
	- [x] I click send, and a line appears under the second input, with a message asking me to fill in the field.
	- [x] I fill in the last name field, and the red line under the input turns green. 
	- [x] I click send, a red line appears under the email input, and a message asks me to fill in the field. 
	- [x] I enter a false email, the line under the email input turns green.
	- [x] I click send, a red line appears under the message input, and a message asks me to fill in the field. 
	- [x] I enter some text into the message field, and the line under the input turns green. 
	- [x] I click send.
		- [x] A flash message error alert appears in red informing me "Failed Validation" (I only added three letters)
		- [x] A message in red appears under the first name input, informing me the field must be between 5 and 20 characters long.
		- [x] A message in red appears under the email input asking me to enter a valid email.
	- [x] I complete the field correctly and click send. A green success message confirms the app sent the message. 
	- [x] I check in the MongoDB messages collection, and the app inserted the data from the message.
		- [x] I log in to the admin account to confirm I received the message. I see the message displayed on the message page in the admin message inbox. 

#### Register Page
![](/documentation/images/all-users-register.png)  
- [x] On the register page, I click register without filling in any fields. Under each input is a required label. 
- [x] A green line appears under the field with a message asking me to fill in the field. The green line turns red. 
- [x] I enter my first name, a character counter appears, telling me I used 6/15 letters. The red line turns green. 
- [x] I check all the form fields in the same way, and they all have the same behavior. I have entered the same username that I already registered.
- [x] I click register, a red flash error alert appears informing me the username already exists. I am still on the register page. 
- [x] I enter the details again, with a different username, I click register, and a green flash success message appears informing me registration is successful. I am logged in and directed to the profile page. The title is Peter's profile. The page is showing me my registration details. 
- [x] I check MongoDB, and the app inserted the new user information. 

#### Login Page
![](/documentation/images/all-users-login.png)  
- [x] On the login page, I click login without entering a username or password.
- [x] A green line appears under the field with a message asking me to fill in the field. The green line turns red when I click out of the field without adding a username.
- [x] I enter a username and password that are not registered. A red flash alert appears with the message "Incorrect Username and/or Password". I cannot log in without registering.

### SESSION USERS
#### Main Navbar
![](/documentation/images/navbar-session-user.png)  
Dropdown for "New".
![](/documentation/images/navbar-session-user-b.png)  
**Pages:** ***"All Users"*** pages + Almanac, Plants, New>Event, New>Plant, New>Category, Log-out.
- [x] I click on the home link. The home page is displayed.
- [x] I click on the Almanac link. The event's page is displayed. 
- [x] I click on the plant's link. The plant's page is displayed. 
- [x] I click on the New Event link. The add event page is displayed.
- [x] I click on the New Plant link. The add plant page is displayed.
- [x] I click on the New Category link. The add category page is displayed.
- [x] I click on the "User First-name's" Profile link. The profile page is displayed.
- [x] I click on the "Log out" link. The app logged me out, and the login page is displayed.
- [x] I click on the Contact link. The contact page and form are displayed. 

#### Off-canvas Navbar
![](/documentation/images/off-canvas-session-user.png)  
- [x] I click on the home link. The home page is displayed.
- [x] I click on the Almanac link. The event's page is displayed. 
- [x] I click on the plant's link. The plant's page is displayed. 
- [x] I click on the New Event link. The add event page is displayed.
- [x] I click on the New Plant link. The add plant page is displayed.
- [x] I click on the New Category link. The add category page is displayed.
- [x] I click on the "User First-name's" Profile link. The profile page is displayed.
- [x] I click on the "Log out" link. The app logged me out, and the login page is displayed.
- [x] I click on the Contact link. The contact page and form are displayed. 
#### Login Page
- [x] I enter my username and password and click log in. I am logged in and redirected to the Profile page. My name is displayed, "Daniel's Profile. A flash alert message says, "Welcome, Daniel".
- [x] The Navbar displays my name as "Daniel's Profile". The Logo, "Your Garden Almanac", has changed to "My Garden Almanac".
![](/documentation/images/login-user-profile.png)    

#### Profile Page
- [x] All input fields displaying my information are disabled. I click on them, but I cannot change the information. Below the disabled inputs is an edit profile button.
- [x] I click the edit profile button, it turns green and redirects me to the Update Daniel's Profile page. 

#### Edit Profile Page
- [x] The joined date and the username inputs are disabled, and I cannot change the information in them. The first name, last name, and email fields are editable and required. The password field is empty, but a message under it says required. 
- [x] I change my email, click update information. A red line appears under the password field with a tooltip asking me to fill in the form field.
- [x] I enter the wrong password, click update information, and a flash red alert message appears asking me to confirm the correct password. 
- [x] I enter the correct password, a green flash success alert appears informing me the app updated the information successfully. The app redirects me to the profile page, and the information displayed in the disabled inputs reflects my changes.
- [x] I check MongoDB, and the app inserted the updated information into the "users" document in the "users" collection.

#### Almanac Page
The Almanac page has a Material Design Collapsible that displays garden events and related plant information. 
- [x] I click on the Almanac link in the Navbar, the "My Events" page opens. A closed Material Design collapsible is showing a list of events. The collapsible-header of each event displays the event date, month, and name. 
![](/documentation/images/collapsible-events.png)    
- [x] I click on an item, it opens, showing me the event and plant information. The information is highlighted and reflects the information I entered for the event and plant. 
- [x] The event and plant each have an edit button. 
- [x] The collapsible displays event name, event category,  repeat value, event notes, and created by for the event. 
- [x] The plant displays the plant type, plant name, sowing date, planting date, harvesting dates, when and what to fertilize with, notes, and created by with my username. 
- [x] Where I entered no information, there is placeholder text informing me no information was added or asking me to add information. 
![](/documentation/images/collapsible-event.png)    

#### Add Event Page
- [x] ***(no plants or categories created)*** In the Navbar, I click on New > Event. I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add plants and categories before entering an event. 
- [x] ***(no categories created)*** In the Navbar, I click on New > Event. I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add categories before entering an event. 
- [x] ***(no plants created)*** In the Navbar, I click on New > Event. I'm redirected to the Add Event page with a form and inputs for adding an event, and there is a blue flash alert message informing me to add plants before entering an event. 
- [x] ***(plants and categories created)*** In the Navbar, I click on New > Event. I'm redirected to the Add Event page with a form and inputs for adding an event. Four fields are required, and two are optional.
![](/documentation/images/add-event-form.png)  
- [x] I click on add event without filling in the inputs. A tooltip message appears asking me to fill in the first field. 
- [x] I select a category, click "add event", and the tooltip appears asking me to choose an item in the plant's list.
- [x] I select a plant, click "add event", and the tooltip appears asking me to fill in the event name field.
- [x] I fill in the event name field, click "add event", and the tooltip appears asking me to fill in the event date field. 
- [x] I select a date, click "add event".  The app directs me to the "My Events" page, and a green flash alert informs me the app successfully added the event. The event is in the collapsible. 
- [x] The two inputs did not fill in show messages in the collapsible. Event "event repeats Enter how often", and "Event Notes: No Notes Recorded".
![](/documentation/images/add-event-success.png)  
- [x] I confirm the event data was inserted into the garden_events collection by checking in MongoDB Atlas. The app added the event.
 
#### Edit Event Page
- [x] I click on the edit event button in the collapsible and for the event, and the app redirects me to the edit event page with a form and inputs displaying the information for the event.
- [x] I fill in the empty fields "Event Repeats" and "Event Notes" and click save. The app redirects me back to the "My Events" Page, and a green flash alert informs me the app successfully updated the event. 
- [x] The updated event is now showing the new information in the collapsible. The app inserted the data into the database.

#### Delete Event
- [x] On the edit event page for the event, I click delete, a modal appears with a red flash alert informing me that deleting event data is irreversible. It asks me if I am sure I want to delete the "Plant Snack cucumbers" event.  
![](/documentation/images/modal-delete-event.png)  
- [x] I click cancel and am redirected back to the Almanac "My Events" page.
- [x] I confirm and click delete, and the app redirects me back to the Almanac "My Events" page, where a green flash alert informs me the app successfully deleted the event. The event is no longer on the list in the collapsible. 

#### Plants Page
The Plants page uses a Material Design Collection to displays a list of plants. Clicking on one of the plants opens a modal to view the plant information. 
![](/documentation/images/collection-plants.png)   
- [x] I click on the view for a plant, a modal opens displaying the plant information.
![](/documentation/images/modal-plants.png)  
-[x] I click cancel, the modal closes, and I am back at the plant's page. 

#### Add Plant Page
- [x] In the Navbar, I click on New > Plant. I'm redirected to the Add Plant page with a form and inputs for adding a Plant. Two fields are required, and seven are optional.
- [x] I click add plant without filling the fields, a tooltip appears asking me to fill the field. 
- [x] I fill in the plant type input, click "add plant", and the tooltip appears asking me to fill in the plant name field.
- [x] I fill in the plant name field, click add plant, and the app redirects me back to the plant's page, where a green flash alert informs me the app successfully added the plant 
- [x] The plant is showing in the list, I open the item in the modal, and the information I entered shows. The form fields I left blank have placeholder text to show me I can add that info into the plant.
![](/documentation/images/add-plant.png)  

#### Edit Plant Page
- [x] I click edit in the plant modal, I am redirected to the "Edit Plant" page, displaying a form with inputs filled with the information from the plant. 
- [x] I fill in the inputs I left blank when creating the plant, click save, and am redirected back to the plant's page. A green flash message informs me the app successfully updated the plant.
- [x] I open the modal, and the app displays the new information in the modal. The app inserted the data into the database.
- [x] I click edit again in the modal for the same plant, and the app redirects me to the "Edit Plant" page, displaying a form with inputs filled with the information from the plant. 
- [x] I change some information in the inputs, click save, and am redirected back to the plant's page. A green flash message informs me the app successfully updated the plant. 
- [x] I open the modal, and the app displays the new information in the modal. The app inserted the information has into the database.

#### Delete Plant
- [x] On the edit plant page for the plant, I click delete, a modal appears with a red flash alert informing me that deleting plant data is irreversible. It asks me if I am sure I want to delete the "Eden" plant.
	- [x] I click cancel and am redirected back to the plant's page.
	- [x] I confirm and click delete, and the app redirects me back to the plant's page, where a green flash alert informs me the app successfully deleted the plant. The plant is no longer on the list of the collection. 
- [x] I select a plant that has an associated event.
![](/documentation/images/delete-plant-1.png)  
- [x] I click edit plant, delete, the modal opens asking me if I am sure I want to delete the plant. 
- [x] I click delete to confirm, am redirected to the plant's page, and a green flash alert informs me the app deleted the plant. It is not on the list. 
[x] I open the Almanac page and click on the event still in the list. The event information is showing, but the plant information is no longer there. 
![](/documentation/images/delete-plant-2.png)  
See [Issues and Fixes](#issues-and-fixes) . Issue 1: I resolved this issue by changing the delete_plant function. Test as follows. 
- [x] I select a plant with a related event.
![](/documentation/images/delete-plant-3.png)  
- [x] I click the edit button for the plant, redirecting me to the edit plant page. I click delete, and the modal appears warning me data deletion is irreversible, that plants with related events cannot be deleted, and asks me if I am sure I want to delete the plant. 
- [x] I confirm and click delete and am redirected to the plant's page, where a red flash alert message informs me I cannot delete plants with related events. 
- [x] I delete the related event in the edit events page. The app returns me to the Almanac events page, where a green flash alert message confirms the app deleted the event successfully. The event is no longer in the collapsible. 
- [x] On the plant page, I click on the plant, the modal opens, and click edit plant. 
- [x] It redirects me to the edit plant page where I click on Delete. A modal opens, informing me data deletion is irreversible, plants with related events cannot be deleted, and asks me if I am sure I want to delete the plant. 
- [x] I confirm by clicking delete, and the app redirects me to the plant's page, a green flash alert informs me the app deleted the plant successfully, and the plant is no longer on the list. The app deleted it without compromising the data integrity of the related event. 
	
#### Categories
I chose to display the categories in a materializecss collection on the add category page. 
- [x] I select new > category in the Navbar and am directed to the add category page. A list below the add category input displays created garden event categories. Each item in the list has an edit icon.
#### Add Category Page
- [x] I click add category without filling in the input. A tooltip message appears asking me to fill in the field. 
- [x] I fill in the field and click "add category". The page refreshes, a green flash alert informs me the app successfully added the new category, and the app displays the new category in the numbered list below the input. 

#### Edit Category Page
- [x] I click the edit button in the listed category, the app redirects me to the edit category page, and the app displays the selected category in the input. 
- [x] I change the category name and click save, am redirected back to the add category page, and a green flash alert message informs me the app successfully updated the category. The new category name is in the list below the input. 

#### Delete Category
NOTE: See [Issues and Fixes](#issues-and-fixes) . Issue 2. 
- [x] On the add category page, I click edit for a category with a related event. The app redirects me to the edit category page, entering the category in the edit category input. 
- [x] I click delete, a modal appears with a red flash alert informing me that deleting plant data is irreversible. The app tells me categories with related events cannot be deleted and asks me if I'm sure I want to delete the category.
- [x] I click cancel and am redirected back to the add category page.
[x] I confirm and click delete and am redirected back to the add category page, where a red flash alert informs me that the app cannot delete categories with related events. 
- [x] I delete the related event. I click edit category on the add category page, and the app redirects me to the edit category page, where I click delete. 
- [x] A modal appears, with a red flash alert informing me deleting category data is irreversible, categories with related events cannot be deleted, and asks me if I am sure I want to delete the category. I confirm and click delete, and the app redirects me back to the add categories page. A green flash alert informs me the category was successfully deleted and is no longer on the list. 

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
![](/documentation/images/navbar-admin.png)   
#### View Messages
- [x] On the messages page, I click on one of the messages, the collapsible message opens and displays the message. 
- [x] I click on the email icon in the message header. It opens my default mail application on my computer and opens a new message with the sender's email inserted in the email. I write a short message and click send to send a reply to the sender. 
#### Delete Messages
- [x] I click the delete icon on the message, a modal appears with a red flash alert informing me deleting the message is irreversible and asks me if I am sure I want to delete the message. 
- [x] I click delete to confirm, the modal closes, I am on the messages page, a green flash alert informs me the app successfully deleted the message, and the message is no longer in the email inbox. 
#### 404 Errors
##### ALL USERS
- [x] I enter URL to a page that doesn't exist. A custom 404 page not found page appears, with a link to the home page. A red flash alert also informs me, "Error, the page was not found".
##### USERS NOT LOGGED IN
- [x] I enter a URL to a page only available to logged-in users, e.g., http://mp3-garden-journal.herokuapp.com/add_plant. The app redirects me to the "Log in" page, and a red flash alert informs me to log in to view the page.
### Issues and Fixes
See also [README/BUGS and ISSUES](/README.md/#bugs-and-issues)

**Issue 1: Delete plant with a related event.**
I had this issue but had not thought about it until testing. I had to think it out to discern what is expected behavior in this case. 
There is one select in the add event form that the app populates with the plant names. It is a required field. The user has to add the plant for an event first; otherwise, they can't add the garden event. However, once the user created the event, it was still possible to delete the garden event. On the Almanac events page in the collapsible, the plant section is left empty, and there is an event without a related plant. 
Having used the plant OjectId when creating the event, I decided to search the garden events for the ObjectId before deleting the plant. The app stops the deletion if the ObjectId exists in the garden_events collection. 
When the user now tries to delete a plant with related events, the delete_plant function redirects the user to the plant's page, and a red flash alert informs the user that the app cant delete plants with related events. They first need to delete related event/s, and then the app can delete the plant. This fix maintains the integrity of associated data.
**Issue 2: Delete category with a related event.**
I had the same issue with deleting plants. See Issue 1 above. I needed to prevent users from deleting categories when there is a related event using the category the user wants to delete. I changed the code in the delete_category function to check garden events and prevent the user from deleting the category if there is a related event. The user has two options, update the category in the event to a different one or delete the event/s. Then the app can delete the category. 
  

## USER STORIES REVIEW (Development-Deployment)
[Readme/User Stories](/README.md/#user-stories)

1. **As a hobby gardener:**

	- As a hobby gardener, I want to record yearly changes of individual plants.
	- As a hobby gardener, I want to set up reminders for yearly maintenance tasks (like pruning, pest control, etc.)
	- As a hobby gardener, I'm interested in recording the time of year when plants flower
	- As a hobby gardener, I would like to add my plants to a list of plants containing information relevant to that plant. 
	- As a hobby gardener, I would like to be able to add images of the plants. 
	- As a hobby gardener, I want to edit plants and events when information to improve the records over time.

2. **As a vegetable gardener:**

	- As a vegetable gardener, I would like to set a reminder when the last frost is, so I know when it is safe to plant outside.
	- As a vegetable gardener, I want to set reminders for when to plant particular seeds so they are ready to plant out after the last frost.
	- As a vegetable gardener, I want to record regular or yearly maintenance tasks so I don't forget them.
	- As a vegetable gardener, I want to know when my fruit and vegetable crops are ready to pick.
	- As a vegetable gardener, I want to edit plants and events to improve the records over time.

1.  **As the owner:**
	- I want to engage gardening enthusiasts to build up a user base of registered users.
	- I want to build a base of registered users to develop a social network of users with a similar interest in gardening.
	- I envisage that I will add pages to market a raised garden bed that I designed for growing vegetables.
	- I want users to register and log in to access the journal with garden reminders and tasks.




1. Issue: Collapsible displaying white background when I click the header of an item. Not showing locally. Fix default materializecss CSS style by adding `background-color: none` in style.css.
2. Issue: Add border-top to the collapsible body, so there is a border under the collapsible header when the item opens. 

 