<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/group-three-sda/final-project">
    <img src="final_project/static/snapvisite/images/logo_color.png" alt="Logo" width="80" height="20">
  </a>

<h3 align="center">SnapVisite</h3>

  <p align="center">
    Final project of SDA python course: ZDPYTpol45
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a credit project for Software Development Academy courses. <br> 
A website was created to connect customers with service providers in the field of beauty and personal care services. 
The site allows the service provider to show available appointments and individual customers to find the right service at the right time. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [python](https://www.python.org/)
* [django](https://www.djangoproject.com/)
* [python-decouple](https://pypi.org/project/python-decouple/)
* [Pillow](https://pillow.readthedocs.io)
* [django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/)
* [phonenumbers](https://pypi.org/project/phonenumbers/)
* [bootstrap](https://pypi.org/project/bootstrap-py/)
 
 <p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

Here are instructions on how to run the SnapVisite project locally. <br>
Describes how to get a local copy, what you need to run it and how to run it. 

### Prerequisites

This is list of software that you need to run SnapVisite project and how to install this software.
* python 3.6 or newer
  ```sh
  install version 3.6 or newer from webside: https://www.python.org/
  ```
* django 4.0.4 on newer
  ```sh
  install django famework to your virtual enviroment using terminal with command:
  pip install django
  ```
  



### Installation

1. Clone the repo with command:
   ```sh
   git clone https://github.com/group-three-sda/final-project.git
   ```
2. Install python packages using terminal with command:
   ```sh
   Easy method:
   pip install -r requirements.txt
   
   Detailed method:
   pip install python-decouple
   
   python3 -m pip install --upgrade Pillow
   
   pip install django-phonenumber-field[phonenumbers]
   
   pip install phonenumbers
   
   pip install bootstrap-py
   ```
3. Make your secret key in settings.py     
   ```js
   In final-project folder create .env file.
   
   Add to .env file variables used in settings.py config: 
       SECRET_KEY = example_name
       DEBUG = False
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE -->
## Usage

The "SnapVisit" service is designed to make it easier for service providers to connect with their customers by speeding up the appointment booking and payment process. The service provider will be able to register their business, set services and their price list, create a calendar to manage appointments. The customer will have the freedom to choose appointments with the selected service provider based on their needs.


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- FEATURES -->
## Features

- [ ] Registration of new service providers
- - [ ] Accepting registered service providers
- - [ ] Removing users as a service provider 
- - [ ] Creation of a corporate account management panel
- - [ ] Personalization of the service provider panel
- - [ ] Adding a list of services and a price list
- - [ ] Adding a location and address
- - [ ] Editing the schedule
- - [ ] Confirming appointments
- - [ ] Check date and time details
- - [ ] Feedback system
- [ ] Registration of users as recipients of services 
- - [ ] Deleting users as a recipient of services 
- - [ ] Edit individual account management panel
- - [ ] Adding and editing comments for companies
- - [ ] Adding company reviews
- - [ ] Booking appointments with a provider
- - [ ] Option to pay for the service
- - [ ] Ability to view future visits
- - [ ] Finding service providers
- - [ ] Cancellation of appointment
- [ ] Accepting registered service providers
- - [ ] Removing users as a service provider 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

No license.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [group-three-sda](https://github.com/group-three-sda) - example-group-three-mail@gmail.com

Project Link: [https://github.com/group-three-sda/final-project](https://github.com/group-three-sda/final-project)
<p align="right">(<a href="#top">back to top</a>)</p>






