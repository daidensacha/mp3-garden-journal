



# Welcome

## Code Institute: Milestone Project 3

### Garden Almanac - Daiden Sacha - Full Stack Web Developer

View the [Garden Almanac](https://mp3-garden-journal.herokuapp.com/) on Heroku.

[Testing.md](/documentation/TESTING.md) outlines my testing strategy, development, deployment and post deployment.

## UX DESIGN

### 1. Strategy
**User Stories:**


1. **As a hobby gardener:**

	- As a hobby gardener, I want to record yearly changes of individual plants.
	- As a hobby gardener, I want to set up reminders for yearly maintenance tasks (like pruning, pest control, etc.)
	- As a hobby gardener, I'm interested in recording the time of year when plants flower
	- As a hobby gardener, I would like to add my plants to a list of plants containing information relevant to that plant. 
	- As a hobby gardener, I would like to be able to add images of the plants. 
	- As a hobby gardener, I want to edit plants and event information to improve the records over time.

2. **As a vegetable gardener:**

	- As a vegetable gardener, I would like to set a reminder when the last frost is, so I know when it is safe to plant outside.
	- As a vegetable gardener, I want to set reminders for when to plant particular seeds so they are ready to plant out after the last frost.
	- As a vegetable gardener, I want to record regular or yearly maintenance tasks so I don't forget them.
	- As a vegetable gardener, I want to know when my fruit and vegetable crops are ready to pick.
	- As a vegetable gardener, I want to edit plants and events to improve the records over time.

1.  **As the owner:**
	- I want to engage gardening enthusiasts to build up a user base of registered users.
	- I want to build a base of registered users to develop a social network of users with a similar interest in gardening.
	- I envisage adding pages to market a raised garden bed that I designed for growing vegetables.
	- I want users to register and log in to access the journal with garden reminders and responsibilities.

### 2. Scope

**Required Features**
- **All Users:**
	- **Home page** The landing page will be light and fresh, with images of nature and plants.
		- **Search Filter** A search input above the collapsible on the almanac page searches the events, categories, months, plants. 
		- **Image slider** will be the main eye-catching feature of the landing page, visible as soon as users arrive at the landing page. 
		- **Material Box** Material Design implementation of the Lightbox plugin to display images. I used it to show pictures of nature, to inspire and connect with users. 
		- **Navbar**
			- **Contact Form Link** will link users to the contact form.
			- **Log in link** will open the login form for users to log in. 
			- **Register link** will open the registration form for users to register. 
		- **Footer** Will hold the social links and contact icon link. 
			- **Social Icons** in the footer so users can open my GitHub and LinkedIn profiles. 
	- **Contact page** Will display the contact form. 
		- **Contact form** for users to send messages to site admin.
	- **Login Page** with the login form. 
		- **Login Form** for users to log in. 
	- **Register Page** with the registration form.
		- **Register Form** for users to register.


- **Registered Users:**
	- **Navbar** - The Navbar for registered users who log in will display additional links to the journal page, plants page, add garden event page, add plants page, and add categories page. 
	- **Journal page** - To display the session user's garden events in the Material Design Collapsible.
		-	**Materializecss Collapsible** - For viewing Garden Events. The header will display the event date in month/ day format. It will show the event name.
		 - **Edit button** - So users can open the edit garden event and edit plant forms.
	- **Plants page** - To display the session user's plants in the Material Design styles collection (list)
	- **Profile page** - To display the session user's profile in the disabled form inputs.
	- **Materializecss Collection** - A Material Design style list for displaying the plants. 
		 - **Edit button** so that users can open the edit garden event and edit plant forms.

	- **Forms**
		- **Create plant** -  So users can create and add their plants
		- **Create Garden Event** - So users can add garden events
		- **Create Category** - So users can create event categories.
		- **Update plant** - So users can edit and update plant information.
		- **Update Garden Event** - So users can edit and update garden event information. 
		- **Update Category** - So users can edit and update garden event categories.  
		- **User Profile Form** (disabled for viewing only) - To display the user profile. 
		- **Update Profile Form** - So users can update select profile information.

	- **Modals**
		- **View Plant Modal** - Will open when the user clicks on the plant in the list. It will display the plant information and have an edit button. 
			- **Edit button** - When the user clicks the button, they will be redirected to the edit plant page, displaying the plant information in the update plant form.
		- **Delete Plant Modal** - The modal will open when the user has clicked to delete a plant. It will display a danger alert, informing the user that the action is irreversible. 
			- **Delete Button** By clicking this button, the user confirms they want to delete the plant data, deletes plant data, and the app redirects them to the plant's page. 
			- **Cancel Button** When the user clicks this button to cancel their intention to delete the plant, the modal will close and redirect the user to the plant's page. 
		- **Delete Garden Event Modal** - The modal will open when the user has clicked to delete a garden event. The modal will display a danger alert, informing the user that deleting data is irreversible.  
			- **Delete Button** By clicking this button, the user confirms they want to delete the garden event data, deletes event data, and is redirected to the journal page. 
			- **Cancel Button** When the user clicks this button to cancel their intention to delete the garden event, the modal will close and redirect the user to the journal page. 
		- **Delete Category Modal** - The modal will open when the user has clicked to delete an event category. The modal will display a danger alert, informing the user that deleting data is irreversible.  
			- **Delete Button** By clicking this button, the user confirms they want to delete the event category, deletes the category, the modal closes, and redirects the user to the add category page. 
			- **Cancel Button** When the user clicks this button to cancel their intention to delete the event category, the modal closes and redirects the user to the add category page. 

- **Admin Users**
	- **Navbar** The Navbar for admin will display an additional link to the messages page.  
		- **Messages page** to display the session user messages.
			- **Materialize Collapsible** for viewing messages. The header of the collapsible has a delete button that will open the confirm delete modal when clicked.
				- **Delete button** - So admin can delete the user messages.
			- **Delete Message Modal** - The modal will open when the user has clicked to delete a message. The modal will display a danger alert, informing the user that deleting the message is irreversible.  
				- **Delete button** - So admin can confirm deletion of the user message.
				- **Send Email button** - To reply to the user in the computer's default email app. 

**Functional Requirements**
- **Image slider** It will have four images and will automatically scroll at intervals of around 10 seconds, enough time for the user to view the image. The transition of the photos, each representing a season, relates to the cyclical nature of existence and events. The images will give the impression of looking through a window.
- **Material Box** Images in the Lightbox plugin will expand when clicked and revert to their initial display when the user clicks a second time. The images are to illustrate the beauty of nature. 
- **Navbar** The Navbar for non-session users will display links to the login page, register page, and contact page.
- **Contact Form** The form inputs will have multiple levels of validation. 
	- **Browser side validation** will utilize the Material Design class `validate`. If a user clicks fields without filling them in, a red line will appear under the input. If the user has not filled in the information, a tooltip message will appear asking to fill in the input. 
	When the form validates, the app displays a flash message success alert notifying the user their message has been sent.
	- **Server Side Validation** is handled by Flask-WTForms, and defined in the form class. Inputs that fail validation will display a red message under the form input, informing the user what is needed for the form input to pass validation. An error alert will appear, telling the user validation has failed. 
- **Login Page** The user will be required to enter their username and password to log in. If they enter correctly, the app redirects them to the profile page, and the additional functionality will be available for the user. If they enter incorrect information, an error alert appears, informing the user the details were wrong. 
- **Registration Page** The user registers by completing all the fields in the registration form. The browser validates the form fields, and a tooltip appears with a validation message if a form field fails validation. If the registration form passes validation, the user is logged in and redirected to the profile page.
-  **Materializecss Collapsible** The collapsible is closed by default, and the user clicks the header to open the accordion. The app displays   "Month/ Day", event category, and event name in the collapsible header. When the user opens the collapsible, the user can view the event and plant information. An edit button for the plant, and one for the event, link to the respective edit pages. 
- **Search Filter** They can filter events by events name, category, month to quickly find required events.  

**Content Requirements**
The garden almanac revolves around creating a record of recurring events in the garden. The goal of the almanac is to develop and improve knowledge based on historical experience recorded in the garden events, plants, and categories of the application. The app collates data to display a yearly event calendar to manage and get the most out of the garden. The app requires some fields in the forms for entering the data to show the events and plants. Other form fields are optional, so the user can enter this content if it suits them. 

### 3. Structure
**Interaction Design**
**ALL USERS:** The site is one page with a contact form, with a link to it in the Navbar. 
Unregistered users are limited to viewing the Homepage, with an option to register via the link in the Navbar. They can also send a message via the contact form. 
- ***Contact Page:*** Users will be able to contact me to give feedback or to ask for support or feature requests. Contact easily accessible from the main Navbar or a link in the footer. 

**REGISTERED USERS:** Registered users can log in, and this enables additional links in the Navbar to a Journal page and Plants page. 
- ***Journal page:*** 
	- A search filter will is positioned above the accordion on the page so that the user can enter the month, plant name, event category to quickly filter the events. It will improve UX as the list of events grows. 
	- An accordion will display the events, and all list items in the accordion will be closed by default and ordered by date. Users can click on an event, and the accordion item will open, displaying the event and related plant, with edit buttons to directly open and edit either. 
	
- ***Plant Page:*** 
	- The plant page displays a list of the user's plants. 
	- The user can click on a plant, which will open a modal displaying the user's plant information. 
	- The modal will have an edit button that will link to an update plant page, where the user can update or delete the plant information.
	
- ***Profile Page:*** 
	- A disabled form on the page will display the registered user's information. An edit button will open an edit profile page, with some fields editable so the user can update their information.

**Information Architecture** 
 There will be three pages for the site, with only the Homepage being accessible to users that are not registered or logged in. 
 
 **CRUD Update forms** 
 - ***Forms:*** display information for each user and contain edit links that redirect to the update/edit page, where the user can update information. Some fields in the related forms will be required, and others are optional but clearly labeled. The user will change and update the information quickly and redirect the user back to the related item group. The update forms will have a save, delete, and cancel button for the user. 

**CRUD Delete structure** 
- ***Forms and delete process*** The user can click the delete button on the update item page, which will open a modal with a danger alert, informing the user that deleting the data is irreversible. They can choose from the delete, or cancel buttons, to delete or cancel and return to the related items group page. 
   
- **Visible to all users**
   - ***Homepage***
	   - Home page navigation will link to the contact form at the bottom of the page, also the login/ registration form. 
	   - There will be a slider with images relating to the four seasons. These images are a feature, and I kept them in the base template to view them on all pages. 
	   - A collection of images to inspire interest in gardening. 
	   
- **Additional pages visible to registered and logged in users** 
   - ***Journal page***
	   - Will display the events for the user's garden.
	   - Event name and plant name will be links that will open the corresponding entry to view, update or delete it.  
   - ***Plants Page***
	   - Will display a list of the plants entered by the user.
	   - The plant name in the list will be a link that opens the plant profile in a modal window to view, update or delete it.
	   
### MongoDB  

I decided to create separate collections for users, event categories, and plants. The fourth collection will be the garden events, which will contain information about the event. Within the garden event entry, I will record the plant id, the user id, and the category to make it easy to filter the database for the information. During development, I had the idea of creating a message feature for the admin and displaying sent messages in the back end. To this end, I made one more MongoDB collection for messages. 

**MongoDB Schema**

![MongoDB Schema](documentation/images/almanac_schema-a2.jpg)  

**Crucial considerations in designing the above schema**

1. ***Users will create events related to plants.***
The user is required to select a plant from the list of their created plants to create an event. The plant ObjectId is then saved in the ```garden_event``` collection as the 	```event_plant_id```. It was necessary because the ObjectId is immutable, whereas if I used the plant name, the user could update and change that, then it would be more complex the maintain the connection between the event and plant. 

2. ***Users will be able to group types of events by category.***
Events are many, but users can group them into few categories. THose categories often relate to seasons, so it is easy to see the types of approaching events by filtering by category. For this reason, I've created the category collection so users can create and edit or delete categories. When creating an event, users can choose the categories from a select input. 

3. ***Plants, events, and categories will be associated with the creator of them.***
Once registered, the user cannot change the user name, and all plants, categories, and events created by the user will contain the field ```created_by```. In this way, I am easily able to filter the collections for items created by the user.

4. ***Plants, events, and categories will be only viewable by that user.***
I have used the user name as the session cookie to identify the user and filter out the displayed items for that user. I felt this was important, as the list of events will grow exponentially. If the list of plants, events, and categories contains other users' items, it will diminish the user experience.

5. ***Admin can view messages sent from the site's contact form.***
For the sake of the learning experience and in step with the project's learning objectives, I specifically chose not to use JavaScript to process and send the contact form messages. I wanted to use Python, and this solution came to me after I created the Flask-WTForms form. I realized how easy it would be to create a MongoDB collection and POST the message data to the database. From there, it's a simple task of building the HTML template to display the messages. 
6. ***Dates in MongoDB are in ISODate format.***
I'll be honest and say this was a dive into learning something very new for me. The Material Design date picker is responsive and works well. However, it serves the date in string format, which I discovered when posting the form date to the database collections. I chose to convert the date to ISODate format to store in the database, and it's pretty straightforward once you get used to it. 


I decided on the following schema, using collections to separate data groups, users, plants, categories (event), garden_events, and messages. 



***Users***
Users and garden events are central to the application.  The ```username``` is what links plants, events and categories. When the user creates a new item for plants, events, or categories, the application inserts  `user_name` as a reference key `created_by`. I can match the session user with the ```username```  key in the collections to retrieve the user's data from the database. 
```  
	users  {
			_id: 			<ObjectId>
			username: 		<string>
			email: 			<string>
			registered: 		<date>
			firstname: 		<string>
			lastname: 		<string>
			password: 		<string>
       }
```


***Plants***
The ```created_by``` key is the ```usename``` of the user and what I use to link the plant entry to the user. The remaining combination of fields is for gathering relevant information to fulfill the needs of the user. Some fields are required. A minimum amount of data is needed to populate the pages with something suitable for the user. Other form fields are optional so that the user can cater to various plants, ornamental or productive. 
```   
	plants  {
			_id: 			<ObjectId>
		    type: 			<string>
		    name: 			<string>
		    sow_at: 			<date>
		    plant_at: 			<date>
		    harvest_from: 		<date>
		    harvest_to: 		<date>
		    fertilise: 			<string>
		    fertiliser: 		<string>
		    notes: 			<string>
		    created_by: 		<string>  
     }
```   
***Categories***
The user has total discretion to group the types of events they prefer, which will suit their needs and desire to search or filter information. The user can add, edit, update or delete categories displayed in a select input in the add or edit ```garden_event``` forms. The user is required to select a category when creating an event. 
```  
	categories  {
		     _id: 			<ObjectId>
		     category: 			<string>
		     created_by: 		<string>
	 }
```
***Garden Events***
The pivot of the whole application concept hinges on relationships to categories and plants.  I used the plant ObjectId as the pseudo foreign key to link events with the related plant. The ObjectId is unique to the plant and immutable, enabling me to maintain the link without complications if I use a field that users can edit. Some fields are required, and other optional, similar reasons for the same in the plant's collection. I stored dates in ISODate format. I also saved the date in month string format and included them in the indexing of the database so users can enter month names to filter events by month.  
``` 
	garden_events {
			 _id: 			<ObjectId>
			 category: 		<string>
			 event_plant_id: 	<ObjectId>
			 name: 			<string>
			 repeats: 		<string>
			 occurs_at: 		<date>
			 month: 		<string>
			 notes: 		<string>
			 created_by: 		<string>
	 }
```
***Messages***
It was not in my initial plan but inspired when I worked out what to do with my contact form data. For the sake of the learning process, I resisted using JS to handle the form and send it via a third party. I used `flask-wtf` forms to build the contact form and validation. In a moment of clarity, I had the idea to create the collection to store the message data, and I coded an Admin Message Inbox to display the messages. 
``` 
	messages  {
		     _id: 			<ObjectId>
		     firstname: 		<string>
		     lastname: 			<string>
		     email: 			<string>
		     message: 			<string>
		     created_at: 		<date>
	 }
```
**Database Issues and Notes**
1. ***Linking garden_events with plants*** As explained, I used the plant ```ObjectId``` and store it as an ```ObjectId``` in the ```garden_event``` collection under the key name ```event_plant_id```. I initially tried using the plant ```name``` field but encountered complications. I stored the plant ```name``` in the ```garden_event``` collection and used it to link the two.  When the plant ```name``` was changed and updated, that method required coding changes to the reference field in ```garden_event```. It was my first lesson on why I should use an immutable field for such linking. Consequently, I changed to using the plant ```ObjectId```. 
It was a little complicated because there is very little information written in simple terms for someone learning. I  used the string format of the ```ObjectId``` in the forms select option, retrieve that when the form is posted, insert it in ```event_plant_id:ObjectId("string_format")``` and store it as the ```ObjectId``` in the ```garden_events``` collection. This way, it is easy to loop through and compare items from the two collections to find a match for the ```ObjectId```.
2. ***Time format*** I'm sure every developer encounters this and has to learn it.
Materialize Design date picker allows you to format the required date however you want to get it. However, it creates a date string, and if you (like me) specified the date field type in MongoDB, it overwrites that and stores the string in the database collection field. When you're expecting a date format and display it in your HTML template, you will encounter Jinja errors. 
In the jQuery function for the date picker, my chosen format to display the date was ```format: "mmmm dd, yyyy",``` i.e., February 10, 2021. My solution was as follows. 
-	Step 1. Store string in variable. ```date_string = request.form.get("occurs_at")```
-	Step 2. Convert string to ISODate ```date_object = pd.to_datetime(date_string)```
	-	Note that I used Pandas here, for simplicity, as with datetime, you need to specify the date format of the date string to be converted, i.e. ```date_object = datetime.strptime(date_string, '%B %d, %Y')``` . View [Documentation for strptime() Behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)  along with a list of the Format codes.
- Step 3. Upload the date to MongoDB. The date was converted from ```"February 10, 2021"``` to ```2021-02-10T00:00:00.000+00:00```.

	As I worked through the project, I had to use the datetime format codes to display the date as I wanted, so I got used to it and realized that it is easy to show the date in whatever format you wish. I stored all my dates in ISODate format in MongoDB unless I wanted to keep it as a string. I saved the month name in the garden_events collection for indexing, so users can search and filter by month name.

### 4. Skeleton

**Wireframing:**
I completed the wireframes in Adobe XD, and I kept them simple to display the layout of the required components. I have used Materializecss as the framework and based my work around a simple free template I found at [materializecss themes](http://swarnakishore.github.io/MaterializeThemes/#themes). 

#### Home page wireframes  
![Home Page](documentation/images/wireframes/wireframe-homepage.jpg)

#### Journal page wireframes  
![Journal Page](documentation/images/wireframes/wireframe-journal.jpg)

#### Plants page wireframes  
![Plants Page](documentation/images/wireframes/wireframe-plants.jpg)

### 5. Surface

**Visual Design:**
I selected four stock images to represent each season and display them in a carousel slider directly under the navigation. The image carousel changes images every 10 seconds automatically so that the user can view each photo. This feature will be visible on all pages, along with the Navbar. 

I included links to the contact form in the Navbar and at the bottom of the page, so it's easy for users to contact me. 

I included images of fruit and vegetables to inspire users to make use of the application. Event names and plant names open related events and plant profiles, so users can easily view, update, or delete them. 

The app has a  fixed Navbar, so it's easily accessible and always visible. The site is simple, and the styling and functions are consistent across pages. 

## TECHNOLOGIES USED

**Languages Used**
1.  HTML
2.  CSS3
3.  SCSS
4.  JavaScript
5.  jQuery
6.  Python
7.  Jinja
8.  Markdown

**Frameworks, Libraries, Programs used**

1. [Material Design Framework](https://materializecss.com/getting-started.html)
	It is my chosen responsive framework for this project.
2. [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) 
     Used to display data from MongoDB in the front-end templates.
3. [Heroku](https://www.heroku.com/home)
	Hosting the project.
4. [MongoDB](https://www.mongodb.com/)
5. NoSQL database used to store non-relational data of the website.
6. [Flask-WTForms](https://flask-wtf.readthedocs.io/en/0.15.x/) 
    A simple integration of Flask and WTForms, offering validation and implementation using Jinja. 
7. [Font Awesome](https://fontawesome.com/)
	Icons used in the website.
8. [GitHub](https://github.com/)
	Used to host project repository and to deploy the project live via 	GitHub Pages
9. [Git Version Control](https://git-scm.com/)
	I used it to commit blocks of work to the GitHub repository and create branches to work on specific changes or testing.
10. [Gitpod](https://gitpod.io/workspaces)
	Editor used to work on project.
11. [Adobe XD](https://www.adobe.com/products/xd.html) 
	Used to create wireframes
12. [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
	Used to edit images for the site.
13. [Adobe Illustrator](https://www.adobe.com/de/creativecloud.html?mv=search&mv=search&sdid=MQH8S7GK&ef_id=Cj0KCQjwgtWDBhDZARIsADEKwgPZA7lnHvCbzk4T9-Q7HVENkRXnk1GxIseaWipJrYnWF0LQvFTw21MaAlQ6EALw_wcB:G:s&s_kwcid=AL!3085!3!392740825380!b!!g!!%2badobe!1419110055!55481570853&gclid=Cj0KCQjwgtWDBhDZARIsADEKwgPZA7lnHvCbzk4T9-Q7HVENkRXnk1GxIseaWipJrYnWF0LQvFTw21MaAlQ6EALw_wcB)
	I used it to create my 404, 405, and 500 error images to display if users encounter missing or broken page links.
14. [Squoosh](https://squoosh.app/)
	I used it to compress images to optimize load performance.
15. [Quire](https://quire.io/)
It is a free project and task planning application used for adding and planning tasks for the project.
16. [Depositphotos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE)
It is my source of choice for stock images.
17. [StackEdit](https://stackedit.io/)
	It's a free, online note-taking and markdown application. I used it to create the README file for GitHub.
18. [Webmaker App](https://webmaker.app/app/) It is a free application similar to codepen, used to create and save the work locally. I use it to implement and experiment with using components of different frameworks that I am using, so I am familiar with how to use them when I come to implementing them in my work. 

## TESTING

See: [Testing.md](/documentation/testing.md)  

### Research
---
Having decided to use Materializecss, I became familiar with the framework, syntax, and available components. I needed to see what is available to meet my needs to implement my design requirements how I needed them to be.
I test and experiment locally using [Webmaker App](https://webmaker.app/app/), as it's free, works well, and I can create codepen examples of what I want to implement with select components. I can save these examples to an HTML document to share with clients. 
- ***Grid*** It's pretty straightforward and similar in many ways to bootstrap. Some class names are similar, i.e. ```.row``` and ```.col```. The grid class syntax is also pretty simple to grasp. 
- ***Collapsible*** The Material Design name for what is better known as an accordion. I needed to research how to implement the accordion and decide how to display the garden event information. 
- ***Collection*** Material Design name for a list. I wanted to use it for displaying the list of plants and also the list of categories. 
- ***Tabs	(conflict)*** My initial plan was to display the events by month in tabs, but Materializecss uses the image carousel css in the tabs, which created a conflict with the image slider. The tabs automatically scrolled. Furthermore, as I needed time to sort the issues, and my time was limited, I decided to go an easier route. I didn't use tabs in my project, and overall I'm happy I went the "Collapsible" route.
- ***Image slider*** I wanted to have this as the main feature when the user lands on the Homepage. One image relating to each season, Spring, Summer, Autumn, Winter. I found my pictures on Deposit photos and created the slider images from the stock images.
- ***Forms*** I needed to look at the form elements, see the implementation procedure, to know in advance what I was going to implement before I came to it. 
- ***Modal*** The plan was to use modals to display plant information and the contact form. I changed the contact form from HTML to Flask-WTForms, in the end, to stay with Python, so I did away with the form modal. I used modals for the delete confirmation messages.

- ***Material Design Template*** I wanted to use the Material Design framework, so I spent a little time looking at what was online concerning templates. I came across [Materialize Themes](http://swarnakishore.github.io/MaterializeThemes/#themes) and found inspiration in what I saw. The theme I chose was using an older version of materializecss, so I needed to go through it from top to bottom as some things needed to be updated to work with the latest release. I customized it how I wanted it, kept some things, and started my project. 
- ***Stock images*** [Deposit Photos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE), my first stop for stock images when I need them. I found the pictures I needed for the image slider and also for the parallax. 

- ***Mongo DB Schema design*** With zero experience designing or working with building any database, apart from the Code Institute code along project, I was overwhelmed. I read so much information, watched so many youtube videos. I had all the info, but it was abstract without a reference point of experience to understand it in real terms. I heard it often that the database design pretty much depended on the needs of the applications. I got it. But how to design it? I spent the first week researching just this, and I decided to jump in and learn in the end. For the most part, the finished product is very close to what I planned, apart from a few changes I made to improve things (to meet the application's needs). 

### Development
---

#### Create Mongo DataBase
1. Navigate to mongodb.com, register, and create an account. 
2. Create a free shared cluster 
3. Select a cloud service. I chose AWS.
4. Select the closest region to you offering a free service. I chose Frankfurt.
5. Choose the cluster tier, M0 Sandbox (free forever)
6. Scroll down and select Cluster Name, and name your cluster.
7. Click on the "Create Cluster" button.
8. Click on Database Access in the menu on the left.
9. CLick on "Add New Database User".
10. Create a user name and password using only a combination of letters and numbers.
11. Set User Privileges to "Read and write to any database".
12. Click Add User.
13. Click on Network Access in the menu on the left-hand side.
14. Click Add IP Address, and here you can click "Add Current IP Address" to limit access to the database, or click "Allow Access From Anywhere" if you want to access from different locations. 
15. Click Clusters in the menu on the left, and click on "Collections".
16. Click "Add My Own Data", and here you can create your database and add your first collection name. Click Create. It can take a few minutes. 
17. Click on "Create Document" to create your first document of key-value pairs. (I created example values to start with) Also, select the type of field. 
18. Once complete, click "Insert" to insert the document into the collection. 

#### Create Project

- **Create Project Repository** I used the Code Institute [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template). I clicked on "Use this template" and created my project repository name "mp3-garden-journal". I then opened this in GitPod to start the project. 

-   **Initialise Git**  To begin my project, I started with  `git init`  to initialize git within the project.
    
-   **Git Ignore**  I created a  **.gitignore**  file to add files and directories I didn't want to upload to GitHub.
    
    `git echo "file_name" >> .gitignore`  is the terminal command I used to add files and directories to  **.gitignore**.

- **Implement Flask app and templates**
 I won't explain how to set up Flask for this section, as there is plenty of clear information online. Also, I can only give partial information, as some are confidential, and I think it could lead to confusion. 
At this point, I implemented Flask and created my base template with the Materialize Theme. I began building the HTML templates using Jinja and extending the templates from the base.html. 
 
- **Connect with Mongo DB** I connected my MongoDB with the Flask app. 

**Incremental Development and Simultaneous Testing**
The development process was incremental, piece by piece, checking as I went for breaks or mistakes in the code and fixing them along the way. With ```debug=True``` Jinja showed me the errors as I progressed, so I could quickly locate where I made a mistake, and it was then just a process of troubleshooting it. 

I created three accounts, my own, an admin, and a third fictitious user to test features. I created plants, categories, events by different users, updated them, deleted them, trying as many scenarios as possible to see what happens and if the behavior was expected or unexpected. 
At one point, I created a custom 404 error page for when users might encounter a broken link, and I experienced a 500 error. I then created a custom 500 error page and threw in a customer 405 error page as well. At that point, I was trying to find ways or scenarios that would show me where the code needed to be improved or made more secure. 

I deployed my project to Heroku early, to be so I had a live version to check and compare to what I was seeing in my local server. 

I tested in Chome Dev Tools, and I checked the application's performance in multiple browsers, operating systems, computers, and devices. 

See [Testing.md](/documentation/TESTING.md) for more detail.

### Deployment

**Deploy to Heroku**
1. Setup pages required by Heroku to run the app.
	- In the console  I run `pip3 freeze --local > requirements.txt` . It creates the file `requirements.txt` and lists all the dependencies needed to run the application. 
	- in the terminal, I create the Procfile by typing `echo web: python app.py > Procfile`. Heroku looks for this file to know what is needed to run the app and how to run it.
	- I remove the blank line at the bottom of the Procfile, which can cause problems running the app on Heroku.
2. I go to heroku.com, 
	-  I log in, and in the user dashboard, click "create new app". 
	- I create a unique app name using lower case, dashes, and or underscores. 
	- I select the region closest to me (Europe) and click "create app",
3. Setup automatic deployment from my GitHub repository.
	- With my GitHub username displayed, I enter the repository name and click search.
	- It finds my repo, and I click "connect to this app".
4. Add environment variables in a hidden file env.py that is not committed and pushed to GitHub with the app.
	- I click on the "Settings" tab for my app and click on "Reveal Config Vars".
	- I enter the key-value pairs, minus quotes.
	- I leave the MONGO_URI value empty as I don't have that yet.
	- Before deploying, I commit and push my two new files to the repository. 
	- I complete the git command, `git status`, `git add .`, `git commit -m "add requirements.txt and Procfile"`, then `git push`. 
5. Back in Heroku, I click "deploy branch."
6. After about short wait, Heroku has received the code from GitHub, built the app, and a message says, "Your app has been successfully deployed".
7. To confirm, I click "View" to launch the app.

### Feedback


### Credits
***Flask App*** 
Without the Code Institute code along [Task Manager project](https://github.com/Code-Institute-Solutions/TaskManagerAuth) as a reference, I feel this project would have been far more complex. Time and time again, I referred back to examples in the Task Manager project to grasp a concept or find my way through a situation.  
***Theme inspiration*** 
I came across some [materializecss themes](http://swarnakishore.github.io/MaterializeThemes/#themes) and used them to develop my theme template. I had to update the markup for the latest version of marterializecss and customize the theme to my own needs. But analyzing these themes helped me to get a grasp of the structure and function of materializecss elements. 

## NOTES


## IMPROVEMENTS/ FUTURE FEATURES
**Admin**
- **User Groups**
With limited time to complete my project, I have had to exclude developing the admin panel to how I would like it. It's a learning process, but in working on limiting users' accessibility, having users with different permissions, it's clear that planning for and assigning user group permissions is a good idea. 
	- **User Management** 
	I would like to have a page in the admin profile to list all users and monitor their activity. It would also be good to be able to change the group permissions from this page. I plan on changing and adding this to the site. 
- **Interest Groups** 
I see potential to develop this into a social platform, where users with similar interests can connect and share their events, plants, and information. It would be invaluable as an almanac, as it depends on experience. The broader the user base of knowledge being input and contributed, the more accurate and helpful the information. 

## BUGS and ISSUES
- **MongoDB Schema**

On the almanac page, I display the events and plant information. Initially, I used the plant name in the ```garden_event```  as a key ```plant_id: "plant_name" ```collection, to identify the plant and display the info. When I came to updating plant information, I became aware this was not a good way when users changed the plant name, and then my code couldn't match the plant with the stored plant name in the garden event collection. I needed a way to identify the plant with the corresponding event. 
I had some issues then, which took me a while to work out, like comparing the ObjectId string with the ObjectId. I decided to use the plant ObjectId instead, as it's immutable and unique. In my add/ edit_event routes, I used the Material Design select as follows.
```
<select id="event_plant_id" name="event_plant_id" class="validate" required>
	<option value="" disabled selected>Choose Plant</option>
	{% for plant in user_plants %}
	<!-- Here the plant ObjectId is used in value as sudo foreign key -->
	<option value="{{ plant._id }}">{{ plant.plant_name }}</option>
	{% endfor %}
</select>
```
I then called the ObjectId string value in my function like so. 
```
event_plant_id = request.form.get("event_plant_id")
```
The ObjectId string is then converted back to the ObjectId for sending to MongoDB to store in the ```garden_events```  collection. 
 ```"event_plant_id": ObjectId(event_plant_id)```
Once I was able to convert the string format to its ObjectId format, I looped through the plants to find the matching ObjectId and then display the related plant information alongside the garden event.

- **Edit Categories**

I clicked on the edit category, and the app redirected me to the edit category page. The category _id was showing in the browser URL, but the category name displaying in the input was incorrect and always the same. 
I created my cursor in the ```app.route``` for categories as follows.

```
categories = list(mongo.db.categories.find().sort("event_category"))
```
I then filtered that list to item for the session user or admin,
```
user_categories = []
for category in categories:
	if (category["created_by"] == session["user"] or session["user"] == "admin"):
		user_categories.append(category)
```
It worked on the plants and almanac pages, but it was playing up here for some reason. 
I changed the code to reduce duplication and only get the ```session["user"]``` items.

```
categories = []
# Distinguish if admin or normal user and filter list accordingly
if session["user"] == "admin":
	categories = list(mongo.db.categories.find().sort("event_category"))
else:
	categories = list(
			mongo.db.categories.find(
				  {"created_by": session["user"]}).sort("event_category"))
if  not categories:
flash("Create event categories to populate this list.", "info")
```
The change has simplified my coding, as I now use the same list name for ```categories``` instead of creating a new list ```user_categories``` and then using that in my template.  
The bug disappeared, and my code was more straightforward. I repeated these changes in the app.py for plants and events. 
