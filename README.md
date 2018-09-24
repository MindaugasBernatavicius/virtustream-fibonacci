# virtustream-fibonacci

## Problem statement:
Please provide a sample project for review:
1. The project should provide a web service.
   1. It accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. i.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
   2. Given a negative number, it will respond with an appropriate error.
2. Include whatever instructions are necessary to build and deploy/run the project, where "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. Include some tests.
4. While this project is admittedly trivial, approach it as representing a more complex problem that you'll have to put into production and maintain for several years, with production quality code.

## Constraints and assumptions:
- The design goals for the solution to this problem are:
   - Performance - ability to serve 1 query as fast as possible.
   - Scalability - non-degrading performance when the query count increases.
   - Extensibility and ease of future development and support.
- The service is left open - so the ovearloading of it is possible.

## Design and implementation:
- The full service has a 2 tier design w/ 4 components:
   - An nginx proxy server in front communicating with 
   - The backend python service.
   
- The full request flow:
  
  ```User --(network)--> nginx --> uwsgi --> flask (router) --> python model (business logic).```

## Deployment procedure:

## Launch procedure:

## Launching automated tests:
