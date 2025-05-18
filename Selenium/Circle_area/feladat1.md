#1. Task: Find the area of ​​a circle

Create a python application (a single python file) that uses selenium. Use the pytest framework for testing, and it is important to use assert comparisons!

The program should load the Circle Area app:
https://high-flyer.hu/zvkrs47p/feladat1_kor.html

Your task is to automate the testing of the following functions of the application:

## TC01: Correct filling
* Check the operation of the application with the following test data:
* r: 10
* Result: 314

## TC02: Filling in with non-numbers
* Check the operation of the application with the following test data:
* r: kiscita
* Result: NaN

## TC03: Blank filling
* Check the operation of the application with the following test data:
* r: <blank>
* Result: NaN

### Submit the solution
* Put your solution in the `Selenium` folder, named `test_feladat1_kor_terulet.py`.
* First commit your locally developed solution with `git commit`,
* then don't forget to send it to the Github server with `git push`.
* Submit your solution even if you are not completely sure about it, because submitting any code related to the subject will be worth points.
* Write comments in the solution file explaining the code you have written (don't overdo it, but don't submit the file without comments either).