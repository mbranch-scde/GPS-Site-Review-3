<!--
SITE CONTENT: edit any text here, then run:   python build.py
How this file works
- "# name" starts a page (global, index, teacher, admin, library, viewer).
- "## key" starts one piece of text. Everything under it, until the next heading, belongs to it.
- Inline formatting: **bold**, [link text](url). A blank line starts a new paragraph.
- Lines that start with "- " become a list. Where a list shows "a | b | c", the " | " (space, bar, space) separates the fields.
- Text in these HTML comments is ignored.

SOURCES (every statement on the site should trace to one of these)
- OP  = the one-pagers in "Site Training Materials/One Pagers"
- DG  = Teacher and Administrator Navigator interactive guide (District version)
- OIS = Administrator Navigator Early Learning guide (OIS)
- PDF = "How to Access the GPS Platform" PDF
- ORIG = the original GPS Navigator Hub (library titles, descriptions, topics)
- SPEC = the page hooks and demo questions you supplied
- SURVEY = the time-savings survey CSV (64 respondents, 20 districts)
-->

# global

## site.name
GPS · Navigator Hub

## site.tagline
Resources for South Carolina educators

## banner.label
Resource site

## banner.text
The home and learning center of GPS. To use a Navigator, log in through the [EA Portal](https://portal.edanalytics.app/).

## footer.org
**Growing Pathways for Students**
South Carolina Department of Education

## footer.contact
Questions or suggestions? Email [gps@ed.sc.gov](mailto:gps@ed.sc.gov).

## footer.access
Need access? Contact your district user administrator, or use the [access request form](index.html#access).

## portal.url
https://portal.edanalytics.app/

## nav
- index.html | Home
- teacher-navigator.html | Teacher Navigator
- admin-navigator.html | Administrator Navigator
- library.html | Guide Library

# index

<!-- hero lead: ORIG home page. -->
## hero.eyebrow
GPS · Navigator Hub

## hero.title
Find your way with GPS.

## hero.lead
Practical guides for South Carolina educators using Teacher Navigator and Administrator Navigator.

## hero.button1
Choose your Navigator →

## hero.button2
How do I get started?

## hero.video.caption
GPS Overview

## hero.photo.alt
Educators working together around a laptop

## hero.photo.credit
Illustrative photo · Stiven Rivera / Pexels

<!-- DG intro; OP "Teacher nav overview" What it is. Teacher Navigator has no behavior tab for SC, so behavior is not listed. -->
## what.eyebrow
What is GPS?

## what.title
Two Navigators, one set of student-success data.

## what.cards
- Administrator Navigator | Administrator Navigator gives district and school administrators a holistic view of the metrics that drive student success, in one platform: over 20 dashboards, curated and designed to fit within an existing workflow. It provides high-level overviews while also diving into subgroup and student-level data.
- Teacher Navigator | Teacher Navigator is the GPS ecosystem's classroom-facing view of student attendance, assessments, and well-being. It organizes everything into three nested levels so you can start with a whole grade and drill down to a single student.

<!-- Roles: OP "For:" lists (Teacher nav overview, Groups & interventions, Metrics, ADM, On-Track & CCR, Predictions) and OIS "Built for district level and school level administrators and educators." -->
## who.eyebrow
Who is it for?

## who.title
District and school staff.

## who.teacher.label
Teacher Navigator

## who.teacher
- Teachers
- Counselors
- Instructional coaches
- Principals and other school and district administrators
- MTSS coordinators and interventionists

## who.admin.label
Administrator Navigator

## who.admin
- District and school administrators
- Principals and school leaders
- District accountability staff and data coordinators
- District finance and data teams
- PowerSchool administrators
- Counselors

<!-- Framing is yours: a data-driven look at students; a backup for teachers and administrators; time back. "Next day" is OP Metrics dashboard. -->
## why.eyebrow
Why use it?

## why.title
Your data, ready when you need it.

## why.list
- A data-informed look at your students, from a district view, school view, down to a single student.
- An immediate, accessable resource for teachers and administrators.
- A free holistic comprehensive view of student data in your district. 

<!-- SURVEY: how long each task takes WITHOUT GPS, from 64 staff in 20 districts.
Hours a year = each person's time answer x how often they do the task, using the midpoint of each answer range
(3 hours for "more than 3 hours"), averaged over the staff who do the task. 30+ minutes = share of those staff.
Row: task | hours a year (average per person) | share who say it takes 30 minutes or more each time | staff who do the task
Total = sum of the four averages. -->
## stats.title
How much time can GPS give back?

## stats.intro
We asked 64 education staff across 20 districts how long four common data tasks take them without GPS. All four can be done in GPS.

## stats.total
about 60 hours

## stats.total.label
a year, for someone who does all four tasks. That is more than a full work week.

## stats.rows.label
hours a year, on average

## stats.rows
- Find students who are chronically absent or close to it | about 9 | 10% | 48
- Pull a school's assessment results by student group | about 14 | 35% | 54
- Identify students who are off track for graduation or readiness | about 15 | 33% | 43
- Put together data for a school improvement or coaching meeting | about 23 | 61% | 51

## stats.row.detail
{pct} of staff say it takes 30 minutes or more each time (n = {n})

## stats.note
How we calculated this: each person's answer to "how long does this take you?" multiplied by "how often do you do it?", using the middle of each answer range (3 hours for "more than 3 hours"), averaged across the staff who do that task. The total adds the four averages. These are the times staff report without GPS.

<!-- Hooks are SPEC. Features are the topic names in ORIG / DG. -->
## navigators.eyebrow
Find your Navigator

## navigators.title
Choose your Navigator.

## navigators.body
Each Navigator has its own page with an introduction video and step-by-step instructions.

## pane.teacher.label
Teacher Navigator

## pane.teacher.hook
Your home for understanding student progress, attendance, assessment performance, and which students may need more support.

## pane.teacher.who
- Teachers
- Counselors
- Instructional coaches
- Principals and other school and district administrators
- MTSS coordinators and interventionists

## pane.teacher.features
- Grade
- Class
- Student
- Group
- Assessments
- Performance over time

## pane.teacher.access
Log in through the EA Portal and select Teacher Nav. To get access, contact your district user administrator.

## pane.teacher.learn
Learn Teacher Navigator →

## pane.admin.label
Administrator Navigator

## pane.admin.hook
Home for 20+ comprehensive dashboards covering a high-level view of assessments, course grades, college and career readiness, and predictions and growth targets, and much more.

## pane.admin.who
- District and school administrators
- Principals and school leaders
- District accountability staff and data coordinators
- District finance and data teams
- Counselors

## pane.admin.features
- Metrics
- Assessments
- Course grades
- College and career readiness
- Predictions and targets
- Growth
- Attendance

## pane.admin.access
Log in through the EA Portal and select Admin Nav. To get access, contact your district user administrator.

## pane.admin.learn
Learn Administrator Navigator →

<!-- PDF "How to Access the GPS Platform". -->
## start.eyebrow
How do I get started?

## start.title
Getting into the Navigators.

## start.steps
- **Go to the EA Portal.** To log into any of the GPS platforms, your starting place is always the EA Portal, the hub where all GPS products live. [Open the EA Portal →](https://portal.edanalytics.app/)
- **Log in with single sign-on (SSO).** Click the login button. If you work in a school or a school district, log in with **Classlink**. If you are a state employee working for SCDE, or you do not work for a school district or school, log in with **Microsoft Azure**. Each user has their own login settings, so this may differ for you.
- **Select your application.** The portal shows every application you have been granted access to. Select Admin Nav or Teacher Nav. To open a platform again, log in to the EA Portal, select your application, and start working in the data.

## start.help
If you run into issues logging in or need access, reach out to your district user administrator. For help understanding the dashboards, or for suggestions or questions, email [gps@ed.sc.gov](mailto:gps@ed.sc.gov). In the EA Portal, the drop-down next to your initials has Help Guides and the EA Support Portal, where you can make a ticket.

## start.pdf
Step-by-step access guide (PDF)

## access.title
Don't have access yet?

## access.body
Select your district and your email program will open a message to your district's user administrator, with the request already written.

## access.select.label
Your district

## access.select.placeholder
Choose your district…

## access.button
Email my district user administrator →

## access.none
Your district isn't listed. Email [gps@ed.sc.gov](mailto:gps@ed.sc.gov).

## access.mail.subject
Request for GPS Navigator access

## access.mail.body
Hello,

I would like access to the GPS Navigator(s) for my district:
[ ] Teacher Navigator
[ ] Administrator Navigator

My name:
My school or office:
My role:
My work email:

Thank you!

# teacher

<!-- Hero lead is the SPEC hook. What it is: OP "Teacher nav overview". -->
## hero.eyebrow
Teacher Navigator

## hero.title
Your students, classes, and groups.

## hero.lead
Your home for understanding student progress, attendance, assessment performance, and which students may need more support.

## hero.image
assets/images/teacher-nav-grade-overview.png

## hero.image.alt
Teacher Navigator grade view showing the left navigation and stats at a glance

## hero.image.caption
Teacher Navigator · Grade view

## what.title
What is it?

## what.body
Teacher Navigator is the GPS ecosystem's classroom-facing view of student attendance, assessments, and well-being. It organizes everything into three nested levels so you can start with a whole grade and drill down to a single student.

- **Grade:** a whole grade at a school. Spot cohort-wide patterns.
- **Classroom:** one course section. Compare your class to the district average.
- **Student:** one child's full picture, including programs and CCR.

## who.title
Who is it for?

## who.body
- Teachers
- Counselors
- Instructional coaches
- Principals and other school and district administrators
- MTSS coordinators and interventionists

What you see is based on your access. If you are missing a grade, class, or student, it is usually an access or roster question. Route it to your school's GPS contact.

## access.title
How to access

## access.steps
- Open the [EA Portal](https://portal.edanalytics.app/).
- If you work in a school or school district, log in with **Classlink**.
- Select **Teacher Nav**.

## access.note
Need access? Reach out to your district user administrator, or use the [request form](#access).

## start.eyebrow
Getting started

## start.title
Introduction to Teacher Navigator

## video.title
Teacher Navigator introduction

## video.points.title
In this video

## video.points
- Class
- Group
- Student
- Grade
- Assessments
- Predictions over time

<!-- DG Teacher Navigator: Grade / Class / Student / Group definitions; OP "Teacher nav overview": "Learn one level and the others feel familiar." -->
## video.blurb
Teacher Navigator organizes everything into three nested levels, Grade, Classroom, and Student. Learn one level and the others feel familiar.

## login.button
Log in to Teacher Navigator →

## request.link
Don't have access yet?

## guides.buttons
- teacher-nav-overview | one-pager | Getting-started one-pager
- teacher-nav-group | one-pager | Groups and interventions one-pager

<!-- Questions are SPEC. Every step is from OP "Teacher nav overview" (Quick start, The drill-down move, Tabs), DG Teacher Navigator, or OP "Teacher Nav - groups and interventions" (Quick steps - Admin role). Format: question | steps separated by ";" | guide slug | link label -->
## questions.eyebrow
Start with a question

## questions.title
Step-by-step instructions for common questions.

## questions
- How did Grade 5 perform on previous assessments? Who needs more help before moving on to 6th grade? | Click Teacher Navigator. You open to your grade levels.; Use the left rail to move: find a… (search), grade, class, student, group.; Open a level and pick a tab, such as assessments.; Go wide to narrow. Grade: is there a pattern across the cohort? Classroom: compare this class to the district average. Student: check subscores for which skills, and performance over time for the trend. | teacher-nav-overview | Getting-started one-pager
- How are my students predicted to grow? | Click Teacher Navigator and select a school or class, then select a student.; Open the Performance over Time tab. It is available at the student level only.; Performance over time shows predicted AVT based on historical assessments.; State equivalent puts different tests on one yardstick. It is the scale the performance over time chart uses. | teacher-nav-overview | Getting-started one-pager
- How do I create a group of students for an intervention? | Click the group icon in the left sidebar, alongside find a…, grade, class, and student.; Click + add group. Name it, and pick school or district scope.; Add students and staff on the two tabs. Filter by name, classroom, grade, or school, check, then add to group.; Click view group. The group's data view has four tabs: at a glance, updates, assessments, and well-being.; Open Updates and click + Add New under interventions. Enter a name, description, content area, and start and end dates. | teacher-nav-group | Groups and interventions one-pager

## questions.note
 **FERPA caution:** Adding a staff member to a group gives them student-level access to the students in it. Granting school or district admin rights gives them access to every student in that scope, not just the group.

# admin

<!-- Hero lead is the SPEC hook. What it is: DG introduction + OIS. -->
## hero.eyebrow
Administrator Navigator

## hero.title
A view across schools and students.

## hero.lead
Home for 20+ comprehensive dashboards covering a high-level view of assessments, course grades, college and career readiness, and predictions and targets, and more. Every chart, table, and visualization is available to be exported.

## hero.image
assets/images/admin-nav-average-daily-attendance.png

## hero.image.alt
Administrator Navigator Average Daily Attendance dashboard with filters, district metrics, and attendance charts

## hero.image.caption
Administrator Navigator · Average Daily Attendance dashboard

## what.title
What is it?

## what.body
Administrator Navigator gives district and school administrators a holistic view of the metrics that drive student success, in one platform: over 20 dashboards, curated and designed to fit within an existing workflow.

It provides high-level overviews while also diving into subgroup and student-level data. The highlighted dashboards each drill from a district-wide roll-up down to a single student.

## who.title
Who is it for?

## who.body
- District and school administrators
- Principals and school leaders
- District accountability staff and data coordinators
- District finance and data teams
- PowerSchool administrators
- Counselors

## access.title
How to access

## access.steps
- Open the [EA Portal](https://portal.edanalytics.app/).
- If you work in a school or school district, log in with **Classlink**. If you are a state employee working for SCDE, log in with **Microsoft Azure**.
- Select **Admin Nav**.

## access.note
Need access? Reach out to your district user administrator, or use the [request form](#access).

## start.eyebrow
Getting started

## start.title
Introduction to Administrator Navigator

## video.title
Administrator Navigator introduction

## video.points.title
In this video

## video.points
- Metrics Dashboard
- On-track and career readiness
- Assessments
- Behavior
- Predictions and targets
- Many more…

## video.blurb
Administrator Navigator provides high-level overviews while also diving into subgroup and student-level data.

## login.button
Log in to Administrator Navigator →

## request.link
Don't have access yet?

## guides.buttons
- metrics-dashboard | one-pager | Metrics Dashboard one-pager
- on-track-and-ccr | one-pager | On-Track and CCR one-pager
- predictions-and-targets | one-pager | Predictions and Targets one-pager
- assessment | one-pager | Assessment one-pager

<!-- Questions are SPEC. Every step is from the matching OP: Metrics dashboard (Quick steps), Predictions and targets (Quick steps), Assessment (Recommended filter order). -->
## questions.eyebrow
Start with a question

## questions.title
Step-by-step instructions for common questions.

## questions
- How do I understand what percent of my students are proficient in ELA or Math? | Open Administrator Navigator.; In the left menu, expand Accountability and select Metrics Dashboard. The dashboard shows proficiency percentages, the % of students that pass certain exam thresholds.; Set filters and apply: School Year, Metric Category, District/School Level Metric, then Apply Filters.; Move through the three views: District, School, Student, to zoom from roll-up to roster. | metrics-dashboard | Metrics Dashboard one-pager
- How do I learn how my students are progressing against their growth targets? | Open Administrator Navigator. In the left menu, select Predictions and Targets (just below Growth).; Set filters and apply: School Year, School, Target Type, Subject, Prediction Type, then Apply Filters.; Read the headline: the Percent Predicted card and the by-target-type and by-prior-proficiency charts.; To build a watch-list, open the student table, filter to Predicted to Meet Target = "no", and export via the three-dot menu.; Percent Met is empty until summatives arrive. Before the current year's SC READY summative, the Percent Met card shows No data. | predictions-and-targets | Predictions and Targets one-pager
- How did students perform on assessments? | Open the Assessment dashboard in Administrator Navigator.; Set the year. Clear all first if results look wrong.; Select assessment and subject. Keep the test definition consistent.; Select grade. Cut scores often differ by grade.; Select season(s) to compare like administrations and see trends over time.; Add school or student group. Narrow only after the base slice is valid. | assessment | Assessment one-pager

<!-- Questions 1-2 are yours; the rest are worked examples quoted from the matching one-pager. Row: question | dashboard | guide slug -->
## more.title
More questions GPS can help answer

## more
- Which subgroups need the most support to be on track to graduate? | On Track and College and Career Readiness Dashboard | on-track-and-ccr
- How is my school doing in a certain metric compared to other schools in my district? | Metric Comparison | metric-comparison-dashboard
- What percentage of district students scored a B or higher in English 2, Semester 1? | Course Grades: Snapshot | course-grades
- Which sections have the highest chronic absence? | Sections Dashboard | sections

# library

<!-- Everything here follows the original hub's library page (ORIG): hero text, filters, and each guide's description and topic. {count} is filled in automatically. -->
## hero.eyebrow
The resource library

## hero.title
Find your guide.

## hero.lead
Browse {count} resources. Start with an individual dashboard guide, or choose an interactive walkthrough. Filter by Navigator, topic, or format.

## topics.title
Browse by topic

## topics.all
All topics

## search.label
Search resources

## filter.navigator
Navigator

## filter.navigator.all
All Navigators

## filter.format
Format

## filter.format.all
All formats

## filter.reset
Reset filters

## count.text
{shown} of {total} resources

## open.link
Open guide →

## empty
No resources match these filters. Try a different search, or reset the filters.

<!-- slug | Navigator | Format | Topic | Title | Description (all ORIG) -->
## guides
- interactive-district | GPS | Interactive walkthrough | Getting started | Introduction to Administrator and Teacher Navigator | Starting guide to understanding how to navigate and understand the data within the GPS Navigators
- interactive-ois | Administrator Navigator | Interactive walkthrough | Early learning | Administrator Navigator Guide, made for OIS | Guide created for Admin Nav, focusing on Early Childhood Education use cases. Applicable for all users.
- assessment-student-detail | Administrator Navigator | One-page guide | Assessment | Assessments: Student Detail | Guide for navigating the Assessments: Student Detail dashboard on Administrator Navigator
- assessment | Administrator Navigator | One-page guide | Assessment | Assessment Dashboard | Guide for using the Assessment Dashboard in Admin Navigator
- adm | Administrator Navigator | One-page guide | Enrollment | Average Daily Membership (ADM) | Guide for using the ADM in Admin Navigator
- course-grades | Administrator Navigator | One-page guide | Course grades | Course Grades | Guide for using the Course Grades dashboard and Course Grade: Student Detail dashboard in Admin Navigator
- growth-dashboard | Administrator Navigator | One-page guide | Growth | Growth Dashboard | Guide for using the Growth Dashboard in Admin Navigator
- growth-roster-verification | Administrator Navigator | One-page guide | Growth data quality | Growth Roster Verification | Guide for verifying student roster data within the Growth Dashboard in Admin Navigator
- growth-student-progress | Administrator Navigator | One-page guide | Growth | Growth Student Progress | Guide for monitoring individual student growth and progress metrics in Admin Navigator
- high-school-cohort-verification | Administrator Navigator | One-page guide | Cohort verification | High School Cohort Verification | Guide for reviewing and verifying student cohort assignments in Admin Navigator
- metric-comparison-dashboard | Administrator Navigator | One-page guide | Metrics | Metric Comparison Dashboard | Guide for comparing performance metrics across schools, groups, and reporting periods in Admin Navigator
- metrics-dashboard | Administrator Navigator | One-page guide | Metrics | Metrics Dashboard | Guide for using the Metrics Dashboard to analyze key performance indicators in Admin Navigator
- on-track-and-ccr | Administrator Navigator | One-page guide | College and career readiness | On Track and CCR | Guide for using the On Track and College & Career Readiness dashboards in Admin Navigator
- predictions-and-targets | Administrator Navigator | One-page guide | Predictions and targets | Predictions and Targets | Guide for viewing predictions and performance targets in Admin Navigator
- sections | Administrator Navigator | One-page guide | Course sections | Sections Dashboard | Guide for using the Sections Dashboard to review course and section-level performance data in Admin Navigator
- teacher-nav-overview | Teacher Navigator | One-page guide | Getting started | Teacher Nav Overview | Getting-started reference for Teacher Navigator's student, group, and intervention views.
- teacher-nav-group | Teacher Navigator | Use case | Groups and interventions | Teacher Nav - Groups and Interventions | Guide for creating, editing, and applying groups and interventions in Teacher Navigator.

# viewer

## back
← Back to Guide Library

## newtab
Open in a new tab ↗

## missing
We couldn't find that guide. [Return to the Guide Library](library.html).
