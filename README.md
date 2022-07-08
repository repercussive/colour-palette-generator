# Colour Palette Generator
## Liam Robertson

This repo includes my deliverable files for the QA DevOps Core Practical Project.

## Contents
1. [Project requirements](#project-requirements)
2. [Design](#design)
3. [The app](#the-app)
4. [Project tracking](#project-tracking)
5. [Risk assessment](#risk-assessment)
6. [Development process](#development-process)
7. [Testing](#testing)
8. [Automation](#automation)
9. [Challenges faced](#challenges-faced)
10. [Future developments](#future-developments)
11. [Acknowledgements](#acknowledgements)

## Project requirements

The objective of this project was to develop an application using a service-oriented architecture comprising 4 services. These are to work together to randomly generate an object of some kind. The application must take advantage of a CI/CD pipeline for automated testing, building and deployment. The project must satisfy the following requirements:

- 4 interacting services, developed in Python
- code integrated into a version control system using the feature-branch model
- kanban board for project tracking
- Jenkins as a CI server, which oversees the rebuilding and redeployment of the application in response to webhooks
- Ansible for configuration management (provisions the environment needed for the application to run)
- Google Cloud Platform virtual machines as cloud-based servers
- Docker for containerisation
- Docker Swarm for container orchestration
- Nginx as a reverse proxy

## Design

I have chosen to create an application that randomly generates colour palettes by applying colour harmony principles. To add some context before explaining how the overall application design follows the service-oriented architecture, here’s a small summary of colour harmony.

| ![image](https://user-images.githubusercontent.com/7796522/177792153-ac44695e-24c2-4f08-b85a-3bb355869fe8.png) | 
|:--:| 
| *There are lots of ways to combine colours, but a simple way to create pleasing combinations is to use certain formulas - for example, complementary colours are found on opposite sides of the colour wheel, while analogous colours are found close together on the wheel. Artists and designers have been using these principles throughout history.* |

### Services

With this in mind, these are the functions of the 4 main services:

#### Base colour API
> This service generates a random colour, to be used as the palette’s base colour.

#### Palette type API
> This service outputs a colour harmony rule (e.g. complementary, analogous, split-complementary), randomly selected from an array.

#### Create palette API
> This service takes in a base colour and a palette type, and from that creates the final palette. This is not random; if this service were to receive the same combination of base colour and palette type, it would give the same output. Using the appropriate formula, it generates a list of colours in the palette.

#### Front end
> This service gets data from the base colour API and palette type API, then sends that data to the create palette API which will send the final palette data back to the front end. This service will then generate and serve an HTML document based on the palette data.

A final service was implemented, namely a reverse proxy using Nginx. This forwards incoming requests from port 80 on the host machine to port 5000 on the front-end service (which is where the user-facing app is running).

The diagram below illustrates how the various services interact.

![image](https://user-images.githubusercontent.com/7796522/178023211-1427adc3-0485-4306-8891-87b30a4178df.png)

### UI design

As part of the design process, I created a simple mockup for the front-end view using Figma. After designing a very simple initial idea for the interface, I decided to include a colour wheel diagram to visually demonstrate the colour harmony formulas. The designs (before and after the colour wheel feature) can be seen [here](https://www.figma.com/file/Gl5pMdldXuBQskymPYqya6/palette-generator-mockup?node-id=0%3A1).

## The app

Here is the result of transforming the design above into the final working application.

| ![image](https://user-images.githubusercontent.com/7796522/177987517-5f1b7370-88f2-4629-bc72-5b064eecfa02.png) | 
|:--:| 
| *When the app is loaded, a colour palette is generated with 5 colours.* |

| ![image](https://user-images.githubusercontent.com/7796522/177987646-684f14d7-1c76-4256-b834-a4fc6cfb861b.png) | 
|:--:| 
| *After clicking the “Generate a new palette” button, a new palette is created.* |

| ![image](https://user-images.githubusercontent.com/7796522/178018509-a022b1a1-3b9f-4af0-a8a1-dbcc1aec1300.png) | 
|:--:| 
| *The hex values for each colour are displayed. Also shown are the palette’s base colour, the palette type (in this case, split-complementary) as well as a visual representation of how the colours are positioned on the colour wheel.* |

## Project tracking

I used Jira to track the progress of the project. The kanban feature allowed me to plan out all of the tasks involved in the development of the application, and track them as they move from being incomplete, to in progress, to complete. The image below shows the state of the Jira board in the middle-to-end stages of development.

![image](https://user-images.githubusercontent.com/7796522/177855585-88ae89e8-d2e4-4043-a2d4-19fc1c4575c3.png)

## Risk assessment

I performed a risk assessment outlining some hazards associated with this project. [This risk assessment matrix](https://www.researchgate.net/profile/Gulsum-Kaya/publication/323570642/figure/fig7/AS:625770716217345@1526206773610/A-standard-risk-matrix.png) illustrates the system used. For each hazard, the likelihood and impact are rated on a scale from 1 to 5, and the priority level is calculated as the product of these two ratings.

![image](https://user-images.githubusercontent.com/7796522/177998917-27ec72b0-d202-4296-95cb-45898f4436e0.png)

## Development process

Version control (with git) was used throughout the development of the project. I made use of the feature-branch model. The `dev` branch acts as the primary branch used for development. When developing a new feature, I would make changes in a separate feature branch. When the feature was completed the changes were merged into the `dev` branch. This keeps the `dev` branch stable and prevents semi-completed features from being deployed. Upon reaching a major version the dev branch is merged into `main`.

The project repo is hosted on GitHub. It not only acts as a backup for the project files, but also provides additional features, such as webhooks, which are a necessary part of the CI pipeline.

The four primary services are written in Python. The web micro-framework Flask was used to implement the various APIs. I made heavy use of the [`colour`](https://pypi.org/project/colour/) module as this allows for easy manipulation of colours. I have used best practices to reduce code complexity and improve readability, such as loops and helper functions. See [the implementation for the create palette API](https://github.com/repercussive/colour-palette-generator/blob/1afbbe1729c148aa0894f72334bceea0a4ab5822/service-4-create-palette-api/application_4/routes.py). Notice that the colour harmony formulas have been implemented with extensibility in mind - if you wanted to add another formula, all you would have to do is add an entry to the `palette_offsets` dictionary.

Automatic testing, building and deployment were handled with Jenkins and Ansible; these will be covered in more detail later.

## Testing

Unit tests were written for the 4 main services. Pytest was used as the testing library for this project. The output of a successful test run is shown below.

![image](https://user-images.githubusercontent.com/7796522/177988598-f25c0093-5da0-45ff-9076-281365b09577.png)

## Automation

This project demonstrates the use of a CI/CD pipeline. 

On a virtual machine running Jenkins, a Pipeline project was set up. When changes are pushed to the dev branch, this will trigger a GitHub webhook, which is delivered to Jenkins. This will cause the stages in [the Jenkinsfile](https://github.com/repercussive/colour-palette-generator/blob/dev/Jenkinsfile) to run (test, build and deploy).

- Firstly, Jenkins will automatically run the unit tests. If any of the tests fail, the build will be aborted, which prevents faulty versions of the application from being deployed.
- The next stage in the pipeline involves building the container images for the various services. After the images are built, it logs into Docker Hub (using the encrypted credentials entered into Jenkins) and pushes the newly built images there.
- The final stage is deployment. Jenkins will run a script that triggers [this Ansible playbook](https://github.com/repercussive/colour-palette-generator/blob/dev/ansible/playbook.yaml), which provisions the environment for the application to run and deploys the app with any changes made. This will be covered in more detail later.

Here are example console outputs from successful builds:
- [before Docker is installed on the swarm machines](https://gist.github.com/repercussive/2b1164f7b422a5bad0046d099937ee16)
- [when Docker is already installed on the swarm machines](https://gist.github.com/repercussive/5ae90f6940c2411c871b8a3ebcc81f24)

### Ansible

The Ansible playbook performs the following tasks:

- First, it installs Docker (and other necessary dependencies) onto the relevant VMs - in this case, that would be the VM for the Docker swarm manager and the VM for a swarm worker. This is achieved using an [Ansible role](https://github.com/repercussive/colour-palette-generator/tree/dev/ansible/install-docker). If the dependencies are already installed, nothing will be changed.
- Secondly, it instructs the swarm manager VM to initialise a swarm.
- Next, the stack is deployed to the swarm (thus deploying the application). [This docker-compose file](https://github.com/repercussive/colour-palette-generator/blob/dev/docker-compose.yaml) is used to configure the stack (the service images are pulled from Docker Hub, where we had pushed them previously)
- Finally, it instructs the swarm worker to join the swarm. This allows the application’s workload to be automatically distributed between the manager and worker machines. 

### Note on swarm workers

In my case I have only added a single swarm worker machine. It would be easy to add any arbitrary number of workers to the swarm, simply by adding more VMs and including them in the `swarm-workers` hosts list within the [Ansible inventory file](https://github.com/repercussive/colour-palette-generator/blob/dev/ansible/inventory.yaml). This would allow the application to scale up to avoid performance issues as demand increases.

### Summary of CI/CD process

The diagram below illustrates the entire CI/CD system used in the project.

![image](https://user-images.githubusercontent.com/7796522/178021572-6e8fcbce-818f-4628-b4af-17fc11a124fc.png)

## Challenges faced

The main challenge with this project was my own lack of familiarity with certain tools, in particular Docker and Ansible. Although I had been introduced to these tools by my trainers, this was my first time using them independently and in a more practical context. Being thrown into a project like this forced me to understand the underlying concepts. After applying these concepts in the context of a working application, I feel like I have a much stronger grasp of the principles behind containerisation, microservices, and automated CI/CD systems in general. I can see how the concepts I’ve used could be expanded upon in the development of real-world applications.

To give a more concrete example, something that I found tricky was deciphering logs to find, understand and fix errors in the build/deployment process. I didn’t expect my first attempt at deploying the app to work. I was correct. There were many issues that needed to be fixed; this involved closely inspecting logs for errors, researching them, and taking the right steps to fix them. Although this process could be confusing and frustrating at times, solving the problems helped me to better understand my tools, and seeing my app successfully deploy for the first time was very satisfying.

## Future developments

I have only implemented 4 colour harmony formulas (monochromatic, analogous, complementary and split-complementary), but others exist (such as triadic or tetradic). One simple way to develop this app further would be to implement these other types of colour palettes.

A more ambitious development could involve the use of an SQL database to store the palettes that are generated. If this were combined with a user accounts system, users would be able to save palettes to be accessed later.

## Acknowledgements

Thanks to Earl, Adam and Leon for their guidance on the tools used in this project.
