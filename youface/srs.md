# Software Requirements Specification for <Project>

Version 1.0 approved

Prepared by <author>
<date created>

## Revision History

- Name, Date, Reason For Changes, Version
-

## 1. Introduction

### 1.1 Purpose

<This project will be a social media platform with the target audience being photographers. This project will be able to let the photographers post their work and have other peers be able to look at them, like them, dislike. This should be a site that can give feedback to the creater of the content, helping them improve on their work or admire others.>



### 1.2 Document Conventions

<This document will be organized in chapters and sections with titles to help organize each section.>

### 1.3 Intended Audience and Reading Suggestions

<This document is intended for the developers of SnapSavvy. The descriptions of this document will go into project requirements, and tell about how this project should work and be implemented. When reading this document it should be read in the order it has been set up, or it is okay to jump to other chapters to get a description of a certain area.>

### 1.4 Product Scope

<Adding on to section 1.1, this project should be an interactive site to which photographers can create and interact with each other. There should be customizable settings for each user and security features such as blocking explicit content.>

### 1.5 References

<For contact of other developers, a wiki has been created with a discord link to contact eachother. For more information contact developer team as this will be the most up to date information on the project.>

## 2. Overall Description

### 2.1 Product Perspective

<Describe the context and origin of the product being specified in this SRS. For
example, state whether this product is a follow-on member of a product family, a
replacement for certain existing systems, or a new, self-contained product. If
the SRS defines a component of a larger system, relate the requirements of the
larger system to the functionality of this software and identify interfaces
between the two. A simple diagram that shows the major components of the overall
system, subsystem interconnections, and external interfaces can be helpful.>

### 2.2 Product Functions

<Summarize the major functions the product must perform or must let the user
perform. Details will be provided in Section 3, so only a high level summary
(such as a bullet list) is needed here. Organize the functions to make them
understandable to any reader of the SRS. A picture of the major groups of
related requirements and how they relate, such as a top level data flow diagram
or object class diagram, is often effective.>

### 2.3 User Classes and Characteristics

<Identify the various user classes that you anticipate will use this product.
User classes may be differentiated based on frequency of use, subset of product
functions used, technical expertise, security or privilege levels, educational
level, or experience. Describe the pertinent characteristics of each user class.
Certain requirements may pertain only to certain user classes. Distinguish the
most important user classes for this product from those who are less important
to satisfy.>

### 2.4 Operating Environment

<Describe the environment in which the software will operate, including the
hardware platform, operating system and versions, and any other software
components or applications with which it must peacefully coexist.>

### 2.5 Design and Implementation Constraints

<Describe any items or issues that will limit the options available to the
developers. These might include: corporate or regulatory policies; hardware
limitations (timing requirements, memory requirements); interfaces to other
applications; specific technologies, tools, and databases to be used; parallel
operations; language requirements; communications protocols; security
considerations; design conventions or programming standards (for example, if the
customer’s organization will be responsible for maintaining the delivered
software).>

### 2.6 User Documentation

<List the user documentation components (such as user manuals, on-line help, and
tutorials) that will be delivered along with the software. Identify any known
user documentation delivery formats or standards.>

### 2.7 Assumptions and Dependencies

<List any assumed factors (as opposed to known facts) that could affect the
requirements stated in the SRS. These could include third-party or commercial
components that you plan to use, issues around the development or operating
environment, or constraints. The project could be affected if these assumptions
are incorrect, are not shared, or change. Also identify any dependencies the
project has on external factors, such as software components that you intend to
reuse from another project, unless they are already documented elsewhere (for
example, in the vision and scope document or the project plan).>

## 3. External Interface Requirements

### 3.1 User Interfaces

<Describe the logical characteristics of each interface between the software
product and the users. This may include sample screen images, any GUI standards
or product family style guides that are to be followed, screen layout
constraints, standard buttons and functions (e.g., help) that will appear on
every screen, keyboard shortcuts, error message display standards, and so on.
Define the software components for which a user interface is needed. Details of
the user interface design should be documented in a separate user interface
specification.>
dark/light button
like and dislike buttons
upload photo button
login button
logout button
messges button that will show messages between you and other people

### 3.2 Hardware Interfaces

<Describe the logical and physical characteristics of each interface between the
software product and the hardware components of the system. This may include the
supported device types, the nature of the data and control interactions between
the software and the hardware, and communication protocols to be used.>
it will be supported on web browsers first then on  mobile devices after all main features are implemented.

### 3.3 Software Interfaces

N/A

### 3.4 Communications Interfaces


communcation with email to send a code to verify email adress


## 4. System Features

<This template illustrates organizing the functional requirements for the
product by system features, the major services provided by the product. You may
prefer to organize this section by use case, mode of operation, user class,
object class, functional hierarchy, or combinations of these, whatever makes the
most logical sense for your product.>

<You may modify the structure of this secture according to the software process
you are using for this project. For example, if you are using agile (or some of
its derivations) and you need to format the features in terms of user stories,
you may replace the format below with your own adaptation for each user story.>


### 4.1 System Feature 1

<Don’t really say "4.1 System Feature 1" for the heading here. Rewrite the
heading as the feature name in just a few words.>

### 4.1.1 Description and Priority

<Provide a short description of the feature and indicate whether it is of High,
Medium, or Low priority. You could also include specific priority component
ratings, such as benefit, penalty, cost, and risk (each rated on a relative
scale from a low of 1 to a high of 9).>

### 4.1.2 Stimulus/Response Sequences

<List the sequences of user actions and system responses that stimulate the
behavior defined for this feature. These will correspond to the dialog elements
associated with use cases.>

### 4.1.3 Functional Requirements

<Itemize the detailed functional requirements associated with this feature.
These are the software capabilities that must be present in order for the user
to carry out the services provided by the feature, or to execute the use case.
Include how the product should respond to anticipated error conditions or
invalid inputs. Requirements should be concise, complete, unambiguous,
verifiable, and necessary. Use "TBD" as a placeholder to indicate when necessary
information is not yet available.>

<Each requirement should be uniquely identified with a sequence number or a
meaningful tag of some kind.>

- REQ-1:
- REQ-2:

### 4.2 System Feature 2 (and so on)

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements

<If there are performance requirements for the product under various
circumstances, state them here and explain their rationale, to help the
developers understand the intent and make suitable design choices. Specify the
timing relationships for real time systems. Make such requirements as specific
as possible. You may need to state performance requirements for individual
functional requirements or features.>

### 5.2 Safety Requirements

<Specify those requirements that are concerned with possible loss, damage, or
harm that could result from the use of the product. Define any safeguards or
actions that must be taken, as well as actions that must be prevented. Refer to
any external policies or regulations that state safety issues that affect the
product’s design or use. Define any safety certifications that must be
satisfied.>

### 5.3 Security Requirements

<Specify any requirements regarding security or privacy issues surrounding use
of the product or protection of the data used or created by the product. Define
any user identity authentication requirements. Refer to any external policies or
regulations containing security issues that affect the product. Define any
security or privacy certifications that must be satisfied.>

### 5.4 Software Quality Attributes

<Specify any additional quality characteristics for the product that will be
important to either the customers or the developers. Some to consider are:
adaptability, availability, correctness, flexibility, interoperability,
maintainability, portability, reliability, reusability, robustness, testability,
and usability. Write these to be specific, quantitative, and verifiable when
possible. At the least, clarify the relative preferences for various attributes,
such as ease of use over ease of learning.>

### 5.5 Business Rules

<List any operating principles about the product, such as which individuals or
roles can perform which functions under specific circumstances. These are not
functional requirements in themselves, but they may imply certain functional
requirements to enforce the rules.>

## 6. Other Requirements

<Define any other requirements not covered elsewhere in the SRS. This might
include database requirements, internationalization requirements, legal
requirements, reuse objectives for the project, and so on. Add any new sections
that are pertinent to the project.>

## Appendix A: Glossary

<Define all the terms necessary to properly interpret the SRS, including
acronyms and abbreviations. You may wish to build a separate glossary that spans
multiple projects or the entire organization, and just include terms specific to
a single project in each SRS.>

## Appendix B: Analysis Models

<Optionally, include any pertinent analysis models, such as data flow diagrams,
class diagrams, state-transition diagrams, or entity-relationship diagrams.>

## Appendix C: To Be Determined List

<Collect a numbered list of the TBD (to be determined) references that remain in
the SRS so they can be tracked to closure.>
