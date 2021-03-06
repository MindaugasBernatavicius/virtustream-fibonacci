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
- The full service has a 2 tier design with 4 components:
   - An nginx proxy server in front communicating with 
   - The backend python service.
- The 4 components and justification for using them:
   - nginx - web server / proxy: provides caching to offload requests from the backend;
   - uswgi - way to communicate with python backed: simple and well supported;
   - flask - python framework: lightwight, easilly extendable for future needs and easilly testable;
   - python - popular, user frienly language with a lot of libraries;
   
- The full request flow:
  
  ```User --(network)--> nginx --> uwsgi --> flask (router) --> python model (business logic).```
  
- Folder structure:
```
root
├── config
│   ├── vs-fib-nginx.conf
│   └── vs-fib.ini
├── models
│   └── fibonacci_generator.py   // memoized fibonacci algorithm
├── routers
│   └── fibonacci_service.py     // entrance point for the request, router invokes necessary model based on the URL accessed
├── run.sh
├── setup.sh
└── tests
    ├── end2end
    ├── integration
    │   ├── conftest.py
    │   └── test_fibonacci_service.py
    ├── performance
    ├── security
    └── unit
        └── test_fibonacci_generator_model.py
```

## Deployment procedure:
```
git clone https://github.com/MindaugasBernatavicius/virtustream-fibonacci.git
cd virtustream-fibonacci
./setup.sh
```
This will install all the packages that can be found in the setup.sh script. Expected end of output, please inspect the full output for possible errors:
![image](https://user-images.githubusercontent.com/7895269/45942519-6b1bbd80-bfeb-11e8-86dc-f8f97a189507.png)

## Launch procedure:

Inside virtustream-fibonacci:
```
./run.sh
```
This launches nginx and uwsgi, which in turn initializes flask backend, expected output:
![image](https://user-images.githubusercontent.com/7895269/45942455-1b3cf680-bfeb-11e8-94e2-dc59b50cbdfb.png)


## Launching automated tests:

Inside virtustream-fibonacci:
```
pytest -sv
```
his launches this initialized flask app (no nginx) and runs tests with pytest, expected output:
![image](https://user-images.githubusercontent.com/7895269/45942408-ed57b200-bfea-11e8-9b1e-5ec24c8396a1.png)

## Usage and simple debugging:

After launch the application will be available via port 8080 (nginx configured to listen on that port), expected curl output:
![image](https://user-images.githubusercontent.com/7895269/45943299-660c3d80-bfee-11e8-9e2a-6dff062fe250.png)

The output of the run script will show requests (when nginx cache is not hit):
![image](https://user-images.githubusercontent.com/7895269/45943214-1f1e4800-bfee-11e8-9fa6-63fd32bd0ede.png)

Nginx logs are available:
![image](https://user-images.githubusercontent.com/7895269/45943192-0f9eff00-bfee-11e8-8f0b-917b98a1a275.png)

There is also the ability to observe how the cache (or memoization) of the fibonacci algorithm itself works, launching the request with ```&debug=True``` query parameter:
![image](https://user-images.githubusercontent.com/7895269/45943458-07938f00-bfef-11e8-95c2-5a217adccca0.png)

What is displayed in the logs:
![image](https://user-images.githubusercontent.com/7895269/45943484-272ab780-bfef-11e8-980e-a0bc03f776b8.png)
