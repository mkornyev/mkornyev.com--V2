from django.core.management.base import BaseCommand
from datetime import datetime
from mkv2.models import Project, Tag


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
        
        t1.save()
        t2.save()
        t3.save()
        t4.save()
        t5.save()
        t6.save()
        t7.save()
        t8.save()


        # Create associated Projects:
        p = Project.objects.create(name="""<span class="newera">NewERA412</span>, Consulting Project<br>""",
            short="""A Junior year consulting project capstone culminating my third year at Carnegie Mellon.
                    <br><a href="https://cmuisprojects.org/PDFs/s20/newera.pdf"><i>Read the consultant's executive summary here.</i></a>""",
            content="""
                    <br><br>
                    <p class='pl-4 lead'>Libraries Used:</p>
                    <ul>
                        <li>TwilioSMS Service</li>
                        <li>GSAP TweenMax 2.1 / TimelineMax 2.1 (for transition animations)</li>
                        <li>MomentJS 2.23 / TempusDominus 5.1 (for reactive calendar widgets)</li>
                        <li>SortableJS (for drag / droppable list items)</li>
                    </ul>
                    <p class='lead pl-4 pt-2'>Skills Learned:</p>
                    <ul>
                        <li>Fork-and-Pull methodology</li>
                        <li>Production Deployment to Digital Ocean</li>
                        <li>Dependency Management via Pip</li>
                        <li>Project Management Best Practices</li>
                        <ul>
                            <li>Use of SCRUM</li>
                            <li><a style='float: left;' href='https://github.com/mkornyev/ReEntry412/projects/1'>Kanban</a></li>
                            <li><a style='float: left;' href='https://github.com/mkornyev/ReEntry-Deprecated/wiki'>Iterative Documentation</a></li>
                        </ul>
                    </ul>
                    <br>
                    <a href="https://github.com/mkornyev/ReEntry-Deprecated" target="_blank" class="btn btn-primary">Source</a>
                    <a href="http://newera412.com/" target="_blank" class="btn btn-primary">Site</a>""",
            date=datetime(2020, 5, 8, 14, 30, 4, 55),
            imageName='newera.png')
        p.tags.add(t)
        p.tags.add(t1)
        p.save()

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
                <p class='lead pl-4 pt-2'>Skills Learned:</p>
                <ul>
                    <li>Decreasing server load via AJAX-motivated Comments</li>
                    <li>Environment management in Heroku</li>
                    <li>Models & Model Forms in Django</li>
                    <li>Django-style MVC</li>
                </ul>
                <br>
                <a href="https://dome-app.herokuapp.com/" target="_blank" class="btn btn-primary">Site</a>""",
            date=datetime(2020, 3, 20, 0, 0, 0, 0),
            imageName='dome.png')
        p1.tags.add(t)
        p1.tags.add(t1)
        p1.save()

        p2 = Project.objects.create(name="<span class='blogbook'>BlogBook</span>, Social Network WebApp<br>",
            short="""<span>A transparent Social network app. Full stack webapp built with Django 3.0 and deployed on <a href="https://blog-book-app.herokuapp.com/" style="float: none;">Heroku.</a></span>""",
            content="""
                    <br><br>
					<p class="pl-4 lead">Implemented Features:</p>
                    <ul>
                        <li><b>Persistent Image Uploads:</b></li>
                        <ul><li>Tied to an AWS S3 Bucket</li><li>With server-side URL signing</li></ul>
                        <li>Subtle feed refresh motivated by JS DOM manipulation</li>
                        <li>User Authentication</li>
                        <li>User Profiles, Posts, and Comments</li>
                        <li>Global and Follower Post Feeds</li>
                    </ul>
                    <p class="lead pl-4 pt-2">Skills Learned:</p>
                    <ul>
                        <li>Decreasing server load via AJAX-motivated Comments</li>
                        <li>Environment management in Heroku</li>
                        <li>Models & Model Forms in Django</li>
                        <li>Django-style MVC</li>
                    </ul>
                    <br>
                    <a href="https://blog-book-app.herokuapp.com/" target="_blank" class="btn btn-primary">Site</a>
                    """,
            date=datetime(2020, 2, 1, 0, 0, 0, 0),
            imageName='blogbook.png')
        p2.tags.add(t)
        p2.tags.add(t1)
        p2.save()

        p3 = Project.objects.create(name="""<span class='bakingfactory'>BakingFactory</span>, Rails WebApp<br>""",
            short="""<span>Ecommerce marketplace Webapp built with the Rails framework. Check me out on <a href="https://baking-factory.herokuapp.com/" style="float: none;">Heroku!</a></span>""",
            content="""
                <br><br>
		        <p class="pl-4 lead">Implemented Features:</p>
		        <ul>
		        	<li>Cart, checkout, and order creation</li>
					<li>Payment Gateway Simulation</li>
					<li>Authentication & Authorization for 4 different types of users</li>
					<li>Informative Admin Dashboards</li>
					<li>Baking & Shipping Lists that simulate in-house inventory and fulfilment services</li>
					<li>Models with a bunch of advanced business logic</li>
					<li>API w/a SwaggerDocs UI</li>
		        </ul>
		        <p class="lead pl-4 pt-2">Skills Learned:</p>
		        <ul>
		        	<li>MVC</li>
		        	<li>RESTful Architecture</li>
		        	<li>TDD</li>
		        	<li>Test Coverage Tools (simpleCov)</li>
		        	<li>Unit Testing Tools (factoryBot, cucumberRails, miniTest)</li>
		        	<li>CSS Frameworks (Bootstrap, Materialize)</li>
		        	<li>Development with SQLite, and Deployment with Postgres</li>
		        </ul>
                <br>
                <a href="https://github.com/mkornyev/BakingFactory" target="_blank" class="btn btn-primary">Source</a>
                <a href="https://github.com/mkornyev/BakingFactoryAPI" target="_blank" class="btn btn-primary">API</a>
                <a href="https://baking-factory.herokuapp.com/" target="_blank" class="btn btn-primary">Site</a>                """,
            date=datetime(2019, 5, 1, 0, 0, 0, 0),
            imageName='baking-factory.png')
        p3.tags.add(t3)
        p3.tags.add(t2)
        p3.tags.add(t1)
        p3.save()

        p4 = Project.objects.create(name="""<span class="fibpalau">Submission Portal</span>, Consulting Project<br>""",
            short="""A JavaScript and AJAX motivated webapp which uses a permissioned token to upload to an external API.<br><br><i>This website is a small subset of a consulting project I undertook in the summer of 2019, while working for the Palau Foreign Investment Board.</i>""",
            content="""
                    <br><br>
                    <p class="lead pl-4 pt-2">Consulting Project Artifacts:</p>
                    <ul>
                        <li><a href="http://www.fibpalau.com" style="float: left;" target="_blank">Agency Website: fibpalau.com</a></li>
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
                    <a href="http://fibpalau.com/" target="_blank" class="btn btn-primary">Site</a>
                    """,
            date=datetime(2019, 8, 5, 0, 0, 0, 0),
            imageName='portal.png')
        p4.tags.add(t3)
        p4.tags.add(t4)
        p4.save()

        p5 = Project.objects.create(name="""<span class="palauanWarrior">Palauan Warrior</span>, Freelance Work<br>""",
            short="""A freelance website design made for Master War Club Carver Steven Kanai.""",
            content="""
                <br><br>
                <a href="https://github.com/palauanwarrior/palauanwarrior.github.io" target="_blank" class="btn btn-primary">Source</a>
                <a href="https://palauanwarrior.github.io/" target="_blank" class="btn btn-primary">Site</a>
                """,
            date=datetime(2019, 7, 20, 0, 0, 0, 0),
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

        p7 = Project.objects.create(name="""Python Application: <span class="pymusic">PyMusic</span><br>""",
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
		        	<li>Data Modeling, Noralization, and UML</li>
		        </ul><br>
		        Followed the RDBMS normalization process, from building a data dictionary to drafting a final ERD, and built a resilient data-store in Postgres.
		        Learning to script and motivate the database with Python was invaluable Development experience, and forced me to operate in an environment with no web framework.
                <br><br>
                <a href="https://github.com/mkornyev/plpgSql_DB" target="_blank" class="btn btn-primary">Source</a>
                """,
            date=datetime(2018, 12, 5, 0, 0, 0, 0),
            imageName='postgres.png')
        p8.tags.add(t7)
        p8.save()

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
		        Built a utility to handle Bond datasets on <a href="https://www.treasurydirect.gov/indiv/tools/tools_savingsbondvalues.htm" style="float: none; margin: 0;">TreasuryDirect.gov</a>.<br>
		        The website is deprecated, and presents users with an unintuitive way to view price histories. This tool provides the user that, along with some descriptive statistics; all motivated by code written in the dataset's native language.
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
        
        print("\n{} projects and {} tags created.\n".format( Project.objects.count(), Tag.objects.count()))

    def handle(self, *args, **options):
        self._createProjects()