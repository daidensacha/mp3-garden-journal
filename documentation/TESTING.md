# TESTING

 [README](/README.md)

## TESTING PLAN (Pre-development)

[README/Testing](/README.md/#testing)


### DEVELOPMENT

[README/Development](/README.md/#development)

 
#### HTML


#### JavaScript


  

### DEPLOYMENT

[README/Deployment](/README.md/#deployment)


  

### Test for production


#### User Access

 1. **Check unregistered users**
	- Access to restricted pages
		- [x] In the Navbar, there are links to Home, Log In, Register, and Contact. 
		- [x] If I type a non-existing URL, I see a custom 404 Error message, with a link to the homepage. 
		- [x] If I type in an @app.route, i.e. https://mp3-garden-journal.herokuapp.com/get_plants, I am directed to the login page, and an alert message asks me to log in to access the page. 
	- Contact form
		- [x] I click the contact link in the Navbar, and I am directed to the contact page. 
		- [x] I fill in the form, click send, and a success alert appears telling me the message has been sent. **NOTE:** *For more detailed information on the form testing, see:* **(add link to form testing)**
	-  Registration process
		- [x] Enter details in the user registration form, press submit. 
		- [x] I am redirected to the login page, where a success alert message informs me  registration was successful. 
		- [x] I check in the user collection in MongoDB, and a new entry  was created in and is displaying  correct user information. (add Screenshot)
		- [x] I enter user login details in the login form, and login is successful. 
		- [x] When logged in, I am redirected to the user profile page. 

 2. **Check new users** 
    - [x] I log in with new user details, login is successful. 
    - [x] I am redirected to the user profile, an alert message is showing saying "Welcome, dannyboone". A disabled form is displayed showing my registered details, with a "EDIT PROFILE" button.
    - [x] I click the edit profile button, a page with the same inputs and information, not disabled, appears. I change the email, enter my password, and click update information. 
    - [x] I am redirected to the user profile page, a success alert message informs me the details have been updated. This is confirmed in the new details showing in the disabled form. 
    - [x] I check the collection in the MongoDB, where the details have also been updated. 
    - [x] I click on the Navbar Journal link, it redirects to an empty page, with an info alert message informing me to create events and event categories to populate the page. 
    - [x] I click on the Navbar Plants link, it redirects to an empty page, with an info alert message informing me to create plants to populate the page. 
    - [x] I click on the Navbar create category link, it opens an empty page, with an info alert message informing me to create categories to populate the list. 
    - [x] I enter a category, click add category, and one item appears in the list with a tag "Created by: dannyboone". A success alert informs me the category was successfully added. 
    - [x] I click the Navbar "Create Plant" link, am redirected to the add plant page, where a form with inputs is showing. 
    - [x] I enter plant details, click "Add Plant", it instantly redirects me to the plants page, where a success alert informs me the plant was successfully added, and the plant is in the list. 
    - [x] I move my mouse cursor over the plant, a pointer appear, I click on the plant and a modal opens showing me the plant details. 
    - [x] I click on the Navbar "Create Event" link and it opens the "Add Event" page.
    - [x] I enter event details, click "Add Event", and I am redirected to the Events page, where a success alert message informs me the event was successfully added. There is now one event in the list. I open the accordion, and it shows me the plant and event information. 
**NOTE:** More extensive notes for testing of crud functionality for all users in section **CRUD Testing**

 3.  Check for all users

### CRUD Testing

1.  **CREATE**

	 - **Add Category**
	 - [x] I click the add category with an empty input, a red line appears under the input, and a message appears asking to fill in the field. 
	 - [x] I type a category name in the field, the line under the field turns green.
	 - [x] I click the add category button, a success alert appears informing me "New Category Successfully Added". 
	 - [x] The added category appears instantly in the list of categories under the input. 
	 
	 - **Add Plant**
	 - [x] I select create plant in the Navbar, and am redirected to the add plant page. 
	 - [x] I click on the add plant button, and a red line appears under the active input. A validation message appears asking me to fill in the fields. 
	 - [x] I enter plant information, click the add plant button, I am redirected to the plants page and the plant as been added to the list. 
	 
	 - **Add Garden Event**
	 - [x] I click the create Navbar event event link, am redirected to the add event page, and I add events details into the form fields. 
	 - [x] I click save, am redirected to the my events page, a success alert states the event was successfully added. The event is showing in the accordionl. I click on the event and the accordion opens, displaying the event, and related plant information.

2.  **READ**

- **Read Category**
	 - [x] On the create categories page, there is a list displaying only the session users categories. 
	 - [x] I create a category, and it instantly appears in the event category list. 
	 - [x] Only categories created by me are displayed in my category list. I do not have other user categories showing in my category list. 
	
- **Read Plants**
	 - [x] I click on the plant item in the list, a modal opens, showing me the information about the plant. 
	 - [x] Only the plants created by me are displayed on the plants page. I do not have other users plants showing in my plant list.
	
- **Read Garden Events**
	 - [x] I click the Journal link in the Navbar, and am redirected to the my events page where an acccordion header displays the event day, the event category, and the plant name. I click the accordion, it opens showing both the event and related plant information. Both event and plant have edit buttons for easy access to editing. 
	 - [x] Only the events created by me are displayed on the my events page. I do not have other users events showing in my events. 
	
3.  **UPDATE**

 - **Update Category**
	 - [x] Each category item has an edit link.  I click on the edit link for an item, it redirects me to the edit category page, where the category is inserted in a text input with delete, save, and cancel buttons. The list of events is displayed below the input and buttons. 
	 - [x] I change the category name, and click save. 
	 - [x] The category name in the list is updated, and I am still on the edit category page.
	 - [x] I click cancel, and I am returned to the add category page.
	 
- **Update Plant**
	 - [x] I click on the edit button in the modal, I am redirected to the edit plant page. The plant details are displayed in the inputs. 
	 - [x] I change some details, click save, I am redirected back to the plants page, showing the list of plants. 
	 - [x] I click on the plant and confirm the details have been updated.
	 - [x] I check the MongoDB colelction and confirm teh plant details database has also been updated.
	 
- **Update Garden Event**
	 - [x] I click on the edit event button, i am redirected to the edit event page, and the event information is displayed in the form inputs. 
	 - [x] I edit some details, click save, am redirected back to the my events page, a success alert states teh event is successfully updated. I open the event and confirm the details have been updated. 
	 - [x] I check the database and the details have been updated. 
	 
4.  **DELETE**  

- **Delete Category**
	 - [x] I click the edit button on a category. It redirects me to the edit category page, and the category name is in the text input. 
	 - [x] I click the delete button, a model opens, with a banner danger alert stating that deleting category data is irreversible. I am asked if I am sure I want to delete the category. There is a delete, and a cancel button. 
	 - [x] I confirm delete the item, the modal closes, and I am redirected to the add category page. A success alert states category successfully deleted. The item is no longer in the list.
	 - [x] I confirm the change by checking the db collection, it is deleted. 
	 
- **Delete Plant**
	 - [x] I click a plant, the modal window opens, showing the plant details, with an edit button.
	 - [x] I click the edit button, I'm redirected to the edit plant page where the plant details are inserted into the fields.
	 - [x] I click the delete button, a modal opens with a danger alert that states deleting plant data is irriversable. I am asked if I am sure I want to delete the plant. 
	 - [x] I click delete, am redirected to the plants page, a success alert states the plant was successfully deleted. It is no longer in the list. 
	 - [x] I confirm this by checking in the database collection, it has been deleted. 
	 - 
- **Delete Garden Event**
	 - [x] I click on the edit event button in the event accordion. I am redirected to the edit event page, where I click on the delete button. 
	 - [x] A modal opens with a danger alert stating that deleting event data is irriversable. I am also asked if I am sure I want to delete the event.
	 - [x] I click on delete, am redirected to the my events page, and the event has been deleted.
	 - [x] I confirm this by checking in the database, it has been deleted. 




-  **Test local and test live**

- Until this point, the website has been tested on the local server.

- Compare and test deployed version of the website.

- Ensure it is the same and there are no bugs.

- Inputs, forms, features need to display and function as expected.

  

-  **Responsiveness**

- Chrome DevTools:

- Test by screen sizes

- Test by viewing media queries which will specifically include Bootstrap breakpoints.

- Test on different devices, different operating systems, different browsers, screen sizes.

- Share the application to get third party feedback

-  **Function**

- Test on different devices, operating systems, and browsers.

- Test all external links, inputs, forms, navigation links, and features.
---
### Error Messages
**Pages created for the following HTTP errors**
- 404 Page not found
- 405 Method not allowed
- 505 Server error

Images were created in Photoshop illustrator. 
The error pages all have a link to the homepage.

---

### User Experience

-  **User Stories**: Check the application fulfills the needs expressed in the user stories.

 -  **Feedback**: Share the application to get feedback and to test the UI to see how users intuit the process of using the application.

***

***

  

## TESTING CHECKLIST (Development-Deployment)

[README/Testing](/README.md/#testing)

 

  

## Responsive Breakpoints and media queries

### Materialize CSS Breakpoints
| Screen Size | Mobile Devices | Tablet Devices  | Desktop Devices | Large Desktop Devices  |
|:-----------:|:--------------:|:---------------:|:---------------:|:----------------------:|
| Breakpoints| <= 600px | > 600px | > 992px | > 1200px |
| Class Prefix | .s | .m | .l | .xl |

**CSS Media Queries**
Small screens are defined as having a max-width of 600px  `@media {max-device-width: 599px} `
Medium screens are defined as having a max-width of 992px  `@media {min-device-width: 600px}`
Large screen are defined as having a min-width of 993px  `@media {min-device-width: 993px}`
Extra Large screen are defined as having a min-width of 1200px `@media {min-device-width: 1200px}`

**Sass Media Queries**
`@media #{$small-and-down}` {  // styles for small screens and down }
`@media #{$medium-and-up}` {  // styles for medium screens and larger } 
`@media #{$medium-and-down}` {  // styles for medium screens and down } 
`@media #{$large-and-up}` {  // styles for large screens and up } 
`@media #{$extra-large-and-up}` {  // styles for extra large screens and up }
  
--------------------

## Testing Devices


#### **MacBook Pro (15-inch, 2017)**

- Operating System

- macOS Big Sur 11.2.3

- Safari Version 14.0.3 (16610.4.3.1.7)

- Chrome Version 90.0.4430.72 (Official Build) (x86_64)

- Firefox 8 (64-bit)

- Windows 10 Pro (Boot Camp installation)

- Microsoft Edge Version

- Firefox

- Chrome Version

- External Monitors

- 2 x Dell U2419H Monitor 23.8-inch Full HD 1920 x 1080 at 60 Hz


#### **Apple iPad Air** Gen 1 9.7 inches 4:3 ratio

- Operating System

- iOS 12.5.2 (16H30) released March 26

- Screen resolution

- 1536 x 2048 pixels, 4:3 ratio (~264 ppi density)


#### **Apple iPhone 11 Pro**

- Operating System

- iOS 14.4.2

- Screen resolution

- 2436‑by-1125‑pixel resolution at 458 ppi

- 5.8‑inch (diagonal) all‑screen OLED Multi‑Touch display

- Width: 2.81 inches (71.4 mm)

- Height: 5.67 inches (144.0 mm)

  

#### HP ProDesk 600 Desktop PC

- Operating System

- Windows 10 Pro

- Microsoft Edge Version 90.0.818.42 (64-Bit)

- Firefox 78.10.0esr (64-Bit)

- Chrome Version 90.0.4430.85 (64-Bit)

- Monitor

- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz

 
***

## USER STORIES REVIEW (Development-Deployment)

  

[Return to README/User stories](/README.md/#1-strategy)


  
# NOTE TO SELF
Add individual elements list, and checked checkboxes with notes, bugs, unfinished etc
Document testing of user stories with images/ screenshots 

  
  

### Information Section