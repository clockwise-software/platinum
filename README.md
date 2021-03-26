# base-environment

This is the base environment for the CLOCKWISE 2021 Software Engineering Bootcamp!

## About CLOCKWISE SE Bootcamp

This bootcamp is a collaborative pilot initiative between the Wyoming Innovation Network of partners and Cardiff University. WIN "calls for closer collaboration between the University of Wyoming and the state’s community colleges and an emphasis on developing innovative solutions that will support and enhance Wyoming’s economy and workforce." [1](https://governor.wyo.gov/media/news-releases/2021-news-releases/governor-unveils-higher-education-initiative-with-new-approach) 


## Industry Challenge

The final project will be the development of a system for identifying employees based upon their project areas. At the end, the final product will be a product that allows for matching people with specific skills to matching proposal requirements.

### Background
[![Trihydro](https://www.trihydro.com/images/default-source/layout-images/logo.png)](https://www.trihydro.com)

Trihydro Corporation (Trihydro) is an engineering and environmental consulting firm based out of Laramie, Wyoming. Trihydro has nearly 475 employees across the United States. We offer a wide range of services including air quality and process management; engineering and surveying; environmental; health and safety; information technology; and water resources.

### Problem
Over the last 5 years, Trihydro has completed an average of 850 proposals per year. Proposal amounts range from $1,000 to over a million dollars. A couple questions that continuously arise during the proposal effort is “Who has project experience that live near the project location?” and “Who has relevant experience related to this proposal?” To answer those questions, a company-wide e-mail is sent requesting expertise in the line of work and project area. Employees can call the marketing team to determine relevant project experience, rely on other staff to respond (e.g., long-term employees), or maintain their own Excel file containing a list of staff and their areas of expertise.

### Goal

Trihydro desires a system of identifying employees, within the project area, that possess skills matching proposal requirements.

## Environment
This environment supports automated deployment through GitPod and produces a base FLASK + SQLITE + BOOTSTRAP stack.

### Development 

Basic details surrounding GitPod can be found here (in their 10 minutes of primer videos https://www.gitpod.io/screencasts/) environment 

The environment features several extensions including:
   * SQLITE database viewer / browser
   * Python Linting, Debugging

Project wide configuration parameters are controlled by the `.gipod.yml`, `.gitpod.Dockerfile`, and `requirements.txt` file. It is not necessary or recommended that you change any of these.

### Key Elements

  * Database: /bootcamp.sqlite : you may wish to make changes to the DB schema, it is recommended that you keep the orginal and create another copy (you can interact with the DB directly via the terminal `sqlite bootcamp.db`, or by right clicking on the db `Open Database` or using `F1 > SQLite: <cmd>`)
  * src/  -- all components of the project except the database
    * static/  - all the bootstrap styling and front-end javascript
    * templates/ - the default html templates using the [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) templating language; all pages currently inherit from `src/templates/generalPageStyled.html`
    * SimpleServer.py - the Python Server running on port 5000, serving up a [Flask-based](https://flask.palletsprojects.com/en/1.1.x/) site that enables one to search the database using employee last names.




### Resources

 * [Flask Tutorial (without DB)](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
 * [Flask Tutorial Collection](https://realpython.com/tutorials/flask/)
 * [Example Projects](https://www.fullstackpython.com/flask.html)



## Getting Started

1. Define a team contract (template provided ) 
   * Establish expectations, goals, and committment both as a group and as individuals.
1. Create a branch of your team's project called `yourlastname-gitpod-exploration`
1. Familiarize yourself with the gitpod environment, in your open branch, launch gitpod (use Chrome or Firefox for ease of use; [browser extensions](https://www.gitpod.io/docs/browser-extension/))
1. Look over the Industry need/challenge and brainstorm in your group what you can do and how you can extend this base environment
1. Sketch out a skelton set of ideas and questions for the industry partner (Trihydro) 
1. Engage with and gather requirments/details fromthe industry partner (Trihydro) 
1. Plan out major milestones and tasks
1. Collaboratively work, itterate, and present!

## Support
1. Saturday Events:
   * Near Peer Mentor - PhD Students (~10:30AM-2:30PM)
   * Lunch and Learn Session - ~12-1 PM 
1. Week-long Access:
   * Slack CLOCKWISE Bootcamp:
      * [Invite Link](https://join.slack.com/t/clockwise-bootcamp/shared_invite/zt-nu2mzbza-uvGPV1pXr0lHbJskgr_Y~Q)
      * [clockwise-bootcamp.slack.com](clockwise-bootcamp.slack.com) 
    * Office Hours (TBA)
    * Drop-in Sessions (TBA)

 
 ## What/Who is CLOCKWISE?

 CLOCKWISE (Creating Lasting Opportunities with Cardiff to Kindle Wyoming's Interests in Software Engineering) is comprised of several dozen faculty and administrators from Wyoming's public insitutions of higher education
   * [University of Wyoming](www.uwyo.edu), 
   * [Casper College](http://www.caspercollege.edu/), 
   * [Central Wyoming College](http://cwc.edu/), 
   * [Eastern Wyoming College](https://ewc.wy.edu/), 
   * [Sheridan College](http://www.sheridan.edu/) / [Gillette College](http://www.sheridan.edu/about/gillette), 
   * [Laramie County Community College](http://www.lccc.wy.edu/), 
   * [Northwest College](http://www.nwc.edu/), 
   * [Western Wyoming Community College](http://www.westernwyoming.edu/) 

and [Cardiff University](https://www.cardiff.ac.uk/).

[<img src="https://upload.wikimedia.org/wikipedia/commons/1/18/University_of_Wyoming_logo.svg" alt="Uwyo" title="Uwyo" width="150" />](http://www.uwyo.edu) [<img src="https://upload.wikimedia.org/wikipedia/commons/e/ee/Casper_College_wordmark.svg" alt="Casper College" title="Casper College" width="150" />](http://www.caspercollege.edu)[<img src="https://www.cwc.edu/media/marketing-files/cwcedu/style-assets/icons/cwc-logo-blue@2x.png" alt="CWC" title="CWC" width="150" />](http://www.cwc.edu)[<img src="https://uqwf03nohzf4b5l9s1r9ke214de-wpengine.netdna-ssl.com/wp-content/uploads/2020/10/EWC_LogoBlackB.png" alt="EWC" title="EWC" width="150" />](http://https://ewc.wy.edu/)

[<img src="https://www.sheridan.edu/wp-content/uploads/2015/12/SC-NWCCD-GC_large.png" alt="Sheridan/Gillette" title="Sheridan/Gillette" width="300"/>](https://www.sheridan.edu) [<img src="https://upload.wikimedia.org/wikipedia/en/3/3c/Laramie_County_CC_logo.jpg" alt="LCCC" title="LCCC" width="150"/>](http://www.lccc.wy.edu)

[<img src="http://www.uwyo.edu/acadaffairs/degree-plans/_files/images/comm-colleges/nwc_logo_605x206.gif" alt="NWC" title="NWC" width="150" />](http://www.nwc.org) [<img src="https://www.mtsacc.org/colleges/uploads/2017/10/Western-Wyoming-Community-College-300x142.jpg" alt="WWCC" title="WWCC" width="150"/>](http://www.westernwyoming.edu/)

[<img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Cardiff-university-vector-logo.svg" alt="Cardiff" title="Cardiff" width="150"/>](https://www.cardiff.ac.uk/)


Infrastructure and neer-peer support is provided by the [Cybersecurity Education and Research Center](http://www.uwyo.edu/CEDAR).
