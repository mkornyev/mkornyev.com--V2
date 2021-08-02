from django.core.management.base import BaseCommand
from datetime import datetime
from mkv2.models import Project, Tag, Image


# POPULATE SCRIPT

class Command(BaseCommand):
    args = '<this func takes no args>'
    help = 'Run this script to create sample users.'

    def _createProjects(self):
        """
        sow = User.objects.create_user(username='sow', password='sow', first_name='Max', last_name='K', email='mkornyev@gmail.com')
        sow.is_staff = True 
        sow.is_superuser = False
        sow.save()
        """
        # Create Tags:
        t = Tag.objects.create(name='django')
        t1 = Tag.objects.create(name='heroku')
        t2 = Tag.objects.create(name='rails')
        t3 = Tag.objects.create(name='html')
        t4 = Tag.objects.create(name='javascript')
        t5 = Tag.objects.create(name='ethereum')
        t6 = Tag.objects.create(name='python')
        t7 = Tag.objects.create(name='postgres')
        t8 = Tag.objects.create(name='cobol')
        t9 = Tag.objects.create(name='swift')
        t10 = Tag.objects.create(name='arduino')
        t11 = Tag.objects.create(name='c++')
        t12 = Tag.objects.create(name='aws ec2')
        t13 = Tag.objects.create(name='aws s3')
        t14 = Tag.objects.create(name='aws rds')
        t15 = Tag.objects.create(name='aws sqs')
        t16 = Tag.objects.create(name='aws elasticsearch')
        t17 = Tag.objects.create(name='aws eks')
        t18 = Tag.objects.create(name='kubernetes')
        t19 = Tag.objects.create(name='docker')
        t20 = Tag.objects.create(name='node-js')
        t21 = Tag.objects.create(name='react-js')


        # Create associated Projects:
        p = Project.objects.create(name="""<span class="newera">NewERA412</span>, Consulting Project<br>""",
            short="""A junior year consulting project capstone.
                    <a href="https://cmuisprojects.org/PDFs/s20/newera.pdf"><i>Read the consultant's executive summary here.</i></a>""",
            content="""
                    <br><br>
                    Worked with a local non-profit to develop a custom CRM that tracks their constituent interactions, and helps cater to the org's clients in order to reduce recidivism rates and prevent violence in Allegheny County.
                    The application not only provided our client with unique features, but served as great <i>proof of social impact</i> to potential grantors and partner organizations. 
                    <br><br>
                    <p class='pl-4 lead'>Tooling:</p>
                    <ul>
                        <li>Django 3.0</li>
                        <li>Heroku (for our beta deployment)</li>
                        <li>Digital Ocean (for our production deployment)</li>
                        <li>TwilioSMS Service</li>
                        <li>Whitenoise & GSAP libraries</li>
                    </ul>
                    <br>
                    <p class='pl-4 lead'>Features:</p>
                    <ul>
                        <li>A text notification feature used to send resources to constituents on the go</li>
                        <li>A referral tracking mechanism which checks whether the constituent has opened their custom-generated referral link</li>
                        <li>A publically available resource portal for searching & finding community resources</li>
                    </ul>
                    <br>
                    <p class='lead pl-4 pt-2'>Skills Learned:</p>
                    <ul>
                        <li>Fork-and-Pull methodology</li>
                        <li>Dependency Management via Pip</li>
                        <li>Project Management & Working with Non-Technical Clients</li>
                        <ul>
                            <li>Use of SCRUM</li>
                            <li><a style='float: left;' href='https://github.com/mkornyev/ReEntry412/projects/1'>Kanban</a></li>
                            <li><a style='float: left;' href='https://github.com/mkornyev/ReEntry-Deprecated/wiki'>Iterative Documentation</a></li>
                        </ul>
                    </ul>
                    <br>
                    See the Beta Deployment to play around with the app — use the following logins as needed: admin/admin & sow/sow
                    <br><br>
                    <a href="https://github.com/mkornyev/ReEntry-Deprecated" target="_blank" class="btn btn-primary">Source</a>
                    <a href="http://newera412.com/" target="_blank" class="btn btn-primary">Production Site</a>
                    <a href="https://newera-app.herokuapp.com/" target="_blank" class="btn btn-primary">Beta Deployment</a>""",
            date=datetime(2020, 5, 8, 14, 30, 4, 55),
            imageName='newera.png')
        p.tags.add(t)
        p.tags.add(t1)
        p.save()

        p.project_images.add(Image.objects.create(filename='newera1.png'),
                            # Image.objects.create(filename='newera2.png'),
                            Image.objects.create(filename='newera3.png'), 
                            Image.objects.create(filename='newera4.png'),
                            Image.objects.create(filename='newera5.png'),
                            Image.objects.create(filename='newera6.png'),
                            Image.objects.create(filename='newera7.png'))

        p1 = Project.objects.create(name="<span class='dome'>DoMe</span>, A Collaborative ToDo-List WebApp<br>",
            short="""<span>A Slack-like toDo application. Full stack webapp built with Django 3.0 and deployed on <a href='https://dome-app.herokuapp.com/' style='float: none;'>Heroku.</a></span>""",
            content="""
                <br><br>
                <p class='pl-4 lead'>Libraries Used:</p>
                <ul>
                    <li>Bootstrap 4 (for mobile responsiveness)</li>
                    <li>GSAP TweenMax 2.1 / TimelineMax 2.1 (for transition animations)</li>
                    <li>MomentJS 2.23 / TempusDominus 5.1 (for reactive calendar widgets)</li>
                    <li>SortableJS (for drag / droppable list items)</li>
                </ul>
                <br>
                <a href="https://dome-app.herokuapp.com/" target="_blank" class="btn btn-primary">Production Site</a>""",
            date=datetime(2020, 2, 1, 0, 0, 0, 0),
            imageName='dome.png')
        p1.tags.add(t)
        p1.tags.add(t1)
        p1.save()

        p1.project_images.add(Image.objects.create(filename='dome1.png'),
                            Image.objects.create(filename='dome2.png'),
                            Image.objects.create(filename='dome3.png'), 
                            Image.objects.create(filename='dome4.png'),
                            Image.objects.create(filename='dome5.png'))

        p2 = Project.objects.create(name="<span class='blogbook'>BlogBook</span>, Social Network WebApp<br>",
            short="""<span>A transparent Social network app. Full stack webapp built with Django 3.0 and deployed on <a href="https://blog-book-app.herokuapp.com/" style="float: none;">Heroku.</a></span>""",
            content="""
                    <br><br>
					<p class="pl-4 lead">Implemented Features:</p>
                    <ul>
                        <li><b>Persistent Image Uploads:</b></li>
                        <ul><li>Tied to an AWS S3 Bucket</li><li>With server-side URL signing</li></ul>
                        <li>Subtle feed refresh motivated by AJAX DOM injection</li>
                        <li>User Profiles, Posts, and Comments</li>
                        <li>Global and Follower Post Feeds</li>
                    </ul>
                    <br>
                    <p class="lead pl-4 pt-2">Skills Learned:</p>
                    <ul>
                        <li>Decreasing server load via AJAX-motivated Comments</li>
                        <li>Environment management in Heroku</li>
                        <li>Models & Model Forms in Django</li>
                        <li>Django-style MVC</li>
                    </ul>
                    <br>
                    <a href="https://blog-book-app.herokuapp.com/" target="_blank" class="btn btn-primary">Production Site</a>
                    """,
            date=datetime(2020, 3, 20, 0, 0, 0, 0),
            imageName='blogbook.png')
        p2.tags.add(t, t1, t13)
        p2.save()

        p2.project_images.add(Image.objects.create(filename='blogbook1.png'),
                            Image.objects.create(filename='blogbook2.png'), 
                            Image.objects.create(filename='blogbook3.png'))
                            
        p3 = Project.objects.create(name="""<span class='bakingfactory'>BakingFactory</span>, Rails WebApp<br>""",
            short="""<span>Ecommerce marketplace Webapp built with the Rails framework. Check me out on <a href="https://baking-factory.herokuapp.com/" style="float: none;">Heroku!</a></span>""",
            content="""
                <br><br>
		        <p class="pl-4 lead">Implemented Features:</p>
		        <ul>
		        	<li>Cart sessions, checkouts, and order creation</li>
					<li>A mocked payment gateway for checkouts</li>
					<li>Authentication & Authorization for 4 different types of users</li>
					<li>An informative Admin dashboard</li>
					<li>Baking & Shipping Lists that simulate in-house inventory and fulfilment services</li>
					<li>Models with a bunch of advanced business logic</li>
					<li>Exposed Swagger API</li>
		        </ul>
		        <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>MVC & RESTful Architecture in Rails</li>
		        	<li>Unit Testing Tools (factoryBot, cucumberRails, miniTest)</li>
                    <li>TDD & Code Coverage Tools (simpleCov)</li>
		        	<li>Multiple CSS Frameworks (Bootstrap, Materialize)</li>
		        	<li>Development with SQLite, and Deployment with Postgres</li>
                    <li>Iteratively producing UML diagrams, data dictionaries, & feature schedules, then leveraging these to drive my frontend & backend development</li>
		        </ul>
                <br>
                <a href="https://github.com/mkornyev/BakingFactory" target="_blank" class="btn btn-primary">Source</a>
                <a href="https://github.com/mkornyev/BakingFactoryAPI" target="_blank" class="btn btn-primary">API</a>
                <a href="https://baking-factory.herokuapp.com/" target="_blank" class="btn btn-primary">Site</a>                """,
            date=datetime(2019, 7, 20, 0, 0, 0, 0),
            imageName='baking-factory.png')
        p3.tags.add(t3)
        p3.tags.add(t2)
        p3.tags.add(t1)
        p3.save()

        p3.project_images.add(Image.objects.create(filename='bf1.png'),
                            Image.objects.create(filename='bf2.png'), 
                            Image.objects.create(filename='bf3.png'), 
                            Image.objects.create(filename='bf4.png'))

        p4 = Project.objects.create(name="""<span class="fibpalau">Submission Portal</span>, Consulting Project<br>""",
            short="""A JavaScript & AJAX webapp which uses a permissioned token to facilitate uploads to a document management API.<br><br><i>This website is a small subset of a consulting project I undertook in the summer of 2019, while working for the Palau Foreign Investment Board.</i>""",
            content="""
                    <br><br>
                    <p class="lead pl-4 pt-2">Consulting Project Artifacts:</p>
                    <ul>
                        <li><a href="http://www.fibpalau.com" style="float: left; cursor: not-allowed;" onclick="return false;" target="_blank">Agency Website: fibpalau.com</a>&nbsp;(This site has moved domains <a href="https://fibpalau.github.io" target="_blank">here.</a>)</li>
                        <li><a href="static/mkv2/lib/FinalReport.pdf" style="float:left;" target="_blank">Executive Summary & Final Report</a></li>
                            <ul><li>Read more about my consulting engagement here.</li></ul>
                        <li><a href="static/mkv2/lib/Shortlist.pdf" style="float:left;" target="_blank">DMS Shortlist & Recommendation</a></li>
                            <ul><li>See the project proposal.</li></ul>
                    </ul>
                    <p class="lead pl-4 pt-2">Skills Learned:</p>
                    <ul>
                        <li>JWT and OAuth concepts</li>
                        <li>Deployment to AWS</li>
                        <li>AJAX & Blobs in JavaScript</li>
                        <li>Cross-browser support / scripting</li>
                    </ul>
                    <br>
                    <a href="https://github.com/fibpalau/fibpalau.github.io" target="_blank" class="btn btn-primary">Source</a>
                    <a href="https://fibpalau.github.io" target="_blank" class="btn btn-primary">Production Site</a>
                    """,
            date=datetime(2019, 8, 5, 0, 0, 0, 0),
            imageName='portal.png')
        p4.tags.add(t3)
        p4.tags.add(t4)
        p4.save()

        p4.project_images.add(Image.objects.create(filename='portal1.png'), 
                            Image.objects.create(filename='portal2.png'), 
                            Image.objects.create(filename='portal3.png'), 
                            Image.objects.create(filename='portal4.png'))

        p5 = Project.objects.create(name="""<span class="palauanWarrior">Palauan Warrior</span>, Freelance Work<br>""",
            short="""A freelance website design made for Master War Club Carver Steven Kanai.""",
            content="""
                <br><br>
                <a href="https://github.com/palauanwarrior/palauanwarrior.github.io" target="_blank" class="btn btn-primary">Source</a>
                <a href="https://palauanwarrior.github.io/" target="_blank" class="btn btn-primary">Production Site</a>
                """,
            date=datetime(2019, 6, 1, 0, 0, 0, 0),
            imageName='palau-warrior.png')
        p5.tags.add(t3)
        p5.tags.add(t4)
        p5.save()

        p6 = Project.objects.create(name="""Ethereum Smart Contract<br>""",
            short="""Clever solidity scripting for the Ethereum Blockchain.""",
            content="""
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>Transacting w/Smart Contracts</li>
		        	<li>OOP in the Solidity IDE</li>
		        	<li>Balancing efficiency and Gas cost</li>
		        </ul>
		        Created a computationally-infeasible hash puzzle wager system. The difficulty of the puzzle and the reward amount decrease by a factor of two every hour.<br/><br/>
		        The smart contract is a wager-backed puzzle where a user can win by computing hash function outputs with leading zeroes. The difficulty, indicated by the contract owner, is the number of leading zeroes required for a user to win the wager.<br/><br/>
		        A winning hash (for a difficulty of 4) is computed as such:<br><br/>
		        <strong class="px-4">0x<span class="bakingfactory">0000</span>4fg3108gsln... = SHA256(input)</strong>
                <br><br>
                <a href="https://github.com/mkornyev/EthereumSmartContract" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2019, 2, 2, 0, 0, 0, 0),
            imageName='solidity.png')
        p6.tags.add(t5)
        p6.save()

        p7 = Project.objects.create(name="""<span class="pymusic">PyMusic</span>, Music Learning App<br>""",
            short="""A music learning program leveraging Computer Vision to play images of notes. <a href="https://www.youtube.com/watch?v=8jTTfHMAIsc&t">See a real demo of the software here.</a>
                    <br><br>
                    <i>This project made it to the competition's <a href="http://www.krivers.net/15112-s18/gallery.html">lightning round</a> and ranked in the top 25&#37; of over 400 projects.</i>
                    """,
            content="""
                <br>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>OpenCV</li>
		        	<li>Threading</li>
		        	<li>Numpy</li>
		        	<li>PyAudio/Wave</li>
		        	<li>Simple MVC</li>
                    <li>Functional Programming</li>
		        </ul><br>
		        One of the most ambitious Python projects I've ever built: At first, working with OpenCV was a hit or miss. But, once I got more familiar with the library, the noteReader I designed got much more accurate.
		        Working with makeshift MVC taught me the importance of well organized code, and required me to implement an agile dispatch system.
                <br><br>
                <a href="https://www.youtube.com/watch?v=8jTTfHMAIsc&t" target="_blank" class="btn btn-primary">Video Demo</a>
                """,
            date=datetime(2018, 5, 1, 0, 0, 0, 0),
            imageName='pymusic.png')
        p7.tags.add(t6)
        p7.save()

        p7.project_images.add(Image.objects.create(filename='pymusic1.png'))

        p8 = Project.objects.create(name="""PL/pgSQL DB, Project<br>""",
            short="""
                    A venmo-like transaction database and user store. User functions are implemented entirely using Python and SQL scripts.
                    """,
            content="""
                <br>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>SQL and Python Scripting</li>
		        	<li>Psycopg2</li>
		        	<li>Data Modeling, Normalization, and UML</li>
		        </ul><br>
		        Followed the RDBMS normalization process, from building a data dictionary to drafting a final ERD, and built a resilient data-store in Postgres.
		        Learning to script and motivate the database with Python was invaluable Development experience, and forced me to operate in an environment with no web framework or ORM.
                <br><br>
                <a href="https://github.com/mkornyev/plpgSql_DB" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2018, 12, 5, 0, 0, 0, 0),
            imageName='postgres.png')
        p8.tags.add(t7)
        p8.save()

        p8.project_images.add(Image.objects.create(filename='venmodb1.png'))

        p9 = Project.objects.create(name="""TreasuryDirect CoBOL File Parser, Project<br>""",
            short="""
                    Built a utility to handle Bond datasets on <a href="https://www.treasurydirect.gov/indiv/tools/tools_savingsbondvalues.htm" style="float: none; margin: 0;">TreasuryDirect.gov</a>.
                    """,
            content="""
                <br>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>CoBOL Scripting</li>
		        	<li>inFile/outFile Routines</li>
		        </ul><br>
		        The website is deprecated, and presents users with an unintuitive way to view price histories. This tool provides the user that, along with some descriptive statistics; all motivated by code written in the dataset's native language.
                <br><br>
                <b>&#x23;depracatecobol</b>
                <br><br>
                <a href="https://github.com/mkornyev/BondReader" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2018, 1, 25, 0, 0, 0, 0))
        p9.tags.add(t8)
        p9.save()

        p10 = Project.objects.create(name="""<span class="fibpalau">Big Skinny</span>, Project<br>""",
            short="""
                    Created a new build of the original BigSkinny website (<a href="https://bigskinny.net" style="float: none; margin: 0;">bigskinny.net</a>).
                    """,
            content="""
                <br>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>Bootstrap</li>
		        </ul>
                <br>
                <a href="https://mkcarousel.github.io/" target="_blank" class="btn btn-primary">Site</a>
                <a href="https://github.com/mkornyev/250-TermProject" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2018, 2, 26, 0, 0, 0, 0))
        p10.tags.add(t3)
        p10.save()

        p11 = Project.objects.create(name="""<span class="mqttcontroller">Remote Marble Maze</span>, Embedded Project<br>""",
            short="""
                    Built an iOS application to broadcast Gyroscope data to an Arduino microcontroller. Ported these inputs to the Arduino using a web server, and enabled the remote control of a laser cut marble maze. 
                    """,
            content="""
                <br>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>Connecting iOS clients, a message broker, and Microcontroller components</li>
                    <li>Microcontroller Programming w/C++</li>
                    <li>Sensor processing mechanics (like smoothing and highpass filtering)</li>
                    <li>Managing high latency with multiple global clients</li>
                    <li>Prototyping in Fusion360</li>
		        </ul>
                <br>
                Iterated on the traditional marble maze game and developed a microcontroller that moved a physical laser-cut maze assembly. Also developed unique input schemes to move the two maze axes: 
                One using two sonar sensors to triangulate an object's X & Y position, and one using the high quality qyroscope in your iOS device. Also added a remote input mode
                to the Arduino that could read input from an MQTT broker. This enabled unique remote gameplay between players, who could Zoom and control eachother's mazes. 
                <br><br>
                <a href="https://courses.ideate.cmu.edu/16-223/f2020/work/2020/12/09/handsfree-balance-maze-final-report/" target="_blank" class="btn btn-primary">Project Report</a>
                <a href="https://github.com/mkornyev/MQTT_Controller" target="_blank" class="btn btn-primary">iOS Swift Source</a>
                <a href="https://github.com/mkornyev/MazeMicroController" target="_blank" class="btn btn-primary">Arduino C++ Source</a>
                """,
            date=datetime(2020, 12, 1, 0, 0, 0, 0),
            imageName="mqtt_diagram.png")
        p11.tags.add(t9, t10, t11)
        p11.save()

        p11.project_images.add(Image.objects.create(filename='mqtt1.png'),
                                Image.objects.create(filename='mqtt2.png'),
                                Image.objects.create(filename='mqtt4.png'))

        p12 = Project.objects.create(name="""<span class='dome'>FLP Inventory</span>, Client Project<br>""",
            short="""
                    A senior year tech consulting project for a local non-profit. Our student team arrived at an abstract project path, then iterated on & delivered a production inventory management system to our client in <i>2 months</i>. 
                    """,
            content="""
                <br>
                <br>
                <p class='pl-4 lead'>Tooling:</p>
                <ul>
		        	<li>Django 3.0</li>
                    <li>CI w/GH Actions for linting, static typechecking, and running our test suite</li>
                    <li>CD w/a GH Web Hook for beta deployments on Heroku</li>
                    <li>Docker for packaging the app</li>
                    <li>AWS EC2 for our production deployment</li>
		        </ul>
                <br>
                <p class='pl-4 lead'>Features:</p>
                <ul>
		        	<li>Authentication/Authorization</li>
                    <li>A full set of IMS features for tracking Item Checkin/Checkouts and their associated constituents, staff members, & supporting information</li>
                    <li>Complex form & information staging flows</li>
                    <li>Custom report generation, time-based analytics, and export functionality</li>
                    <li>A weekly CRON job to back up tax-pertinent information to an external server</li>
		        </ul>
                <br>
                <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>Requirements elicitation</li>
                    <li>Project Management</li>
                    <li>Scoping the project within a tight timeframe — we actually leveraged Django's stock DB management site to more quickly iterate on custom features for the system</li>
		        </ul>
                <br>
                See the Source (below) to view the project's Kanban and issue boards, or check out the <a href="https://docs.google.com/document/d/11jZVieWdkskYoGqYnL1vcqemAP6CquMB2xQNZLYfGZY/edit?usp=sharing" target="_blank">system documentation here</a>.
                Also see the Beta Deployment to use the app in a sandbox environment — logins provided!
                <br><br>
                <a href="https://github.com/mkornyev/FLP-Inventory" target="_blank" class="btn btn-primary">Source</a>
                <a href="http://flpinventory.com/" target="_blank" class="btn btn-primary">Production Site</a>
                <a href="http://flp-app.herokuapp.com/" target="_blank" class="btn btn-primary">Beta Deployment</a>
                """,
            date=datetime(2021, 5, 10, 0, 0, 0, 0),
            imageName="flp-landing.png")
        p12.tags.add(t, t1, t12, t19)
        p12.save()

        p12.project_images.add(Image.objects.create(filename='flp-1.png'),
                                Image.objects.create(filename='flp-2.png'),
                                Image.objects.create(filename='flp-3.png'),
                                Image.objects.create(filename='flp-4.png'),
                                Image.objects.create(filename='flp-5.png'))
        
        p13 = Project.objects.create(name="""<span class="eda-template">EDA Template</span><br>""",
            short="""
                    An event-driven architecture template with scripts, code, and other IAC. 
                    <br><br>
                    This is a personal project I evolved into a starter repo for quickly prototyping web-based microservices, extending the architecture w/common AWS tools, and deploying the app to a basic k8s cluster.
                    """,
            content="""
                <br>
                <br>
                <p class='pl-4 lead'>Tooling:</p>
                <ul>
                    <li>Python + Flask</li>
		        	<li>NodeJS + Express</li>
                    <li>Docker + Kubernetes</li>
                    <li>AWS EKS, RDS, ES, and SQS</li>
                    <li>Vagrant & Bash Scripts for setting up clean Dev and Test environments</li>
		        </ul>
                <br>
                <p class='pl-4 lead'>Features:</p>
                <ul>
		        	<li>2 sample BFFs (backend-for-frontends)</li>
                    <li>2 independently scalable Node servers</li>
                    <li>1 Circuit Breaker</li>
                    <li>Command Query Responsibility Segregation w/RDS & ES</li>
                    <li>K8s config files for orchestrating the deployment as a set of services</li>
		        </ul>
                <br>
                See the github source below for more info!
                <br>
                <br>
                <a href="https://github.com/mkornyev/EDA-Template" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2021, 4, 1, 0, 0, 0, 0),
            imageName="eda-diagram.png")
        p13.tags.add(t14, t15, t16, t17, t18, t19, t20)
        p13.save()

        p13.project_images.add(Image.objects.create(filename='../eda-diagram.png'))

        p14 = Project.objects.create(name="""<span class='fibpalau'>AlarmClock!</span>, React App<br>""",
            short="""
                    A quick side-project built with React: an Alarm Clock with an ergonomic UI.
                    """,
            content="""
                <br>
                <br>
                <p class='pl-4 lead'>Tooling:</p>
                <ul>
		        	<li>React 17.0.2</li>
                    <li>NodeJS v16.5.0</li>
		        </ul>
                <br><br>
                <a href="https://github.com/mkornyev/ReactiveAlarmClock" target="_blank" class="btn btn-primary">Source</a>
                <a href="https://ez-alarm.herokuapp.com/" target="_blank" class="btn btn-primary">Site</a>
                """,
            date=datetime(2021, 7, 27, 0, 0, 0, 0),
            imageName="alarmclock.png")
        p14.tags.add(t1, t20, t21)
        p14.save()

        p14.project_images.add(Image.objects.create(filename='alarmclock1.png'))
        

        print("\n{} Tags, {} Images, and {} Projects Created.\n".format( Tag.objects.count(), Image.objects.count(), Project.objects.count()))

    def handle(self, *args, **options):
        self._createProjects()