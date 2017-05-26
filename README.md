**Project Wake-up Time**
===
by using Neural Network



Description
---

The main object of this project is determining when should wake up the user. It uses neural network to do this. Inputs are waking up time of one day ago, tiredness, need to sleep late and day. Output consists of 4 decision classes as 06.00, 07.00, 08.00, 09.00.

* **Waking up time :** 1 early , 0 late.
* **Tiredness :** 1 tired, 0 not tired.
* **Need for sleep :** 1 yes, 0 no.
* **Day:** 1 weekdays, 0 weekend.

Neural network shown below.

![alt text](https://github.com/HarunGlec/Wake-up-time-AI/blob/master/Project_Diagram.png)

Functionalities
---
Program loads data from excel file. Then data divided automatically input and output. As activation function, it uses sigmoid function. Training process continues until the expected error value is reached. In training process program uses gradient descent as back propagation algorithm. During this process, it shows error rate every 100 steps. At the end of training process shows predictions and check accuracy of results. Program also shows effectivenes and efficiency of algorithm.

Dependencies
---
Python 2.7.13 has used as programming language. To read data from excel file, pandas module version 0.19.2 and to handle with data, numpy module version
1.11.3 have used. Also time module that is one of the standart modules, was added to calculate efficiency.

Installation
---
**Windows**
* Download Python 2.7 from this site and install.
https://www.python.org/downloads/windows/


* Download available Numpy version from this site and install.
https://pypi.python.org/pypi/numpy


* Download Pandas from this site and install.
http://pandas.pydata.org/getpandas.html

Also you can download through PIP. It is explained below Linux.

**Linux**
* Most of Linux distribution has Python 2.7 as default, but if not, you can
install by typing the following in the command prompt.

*On Debian-like Linux*

	$ sudo apt-get install python2.7
    
*On CentOS-like Linux*

	$ sudo yum install python
    
* We will install other modules via PIP. It is a package managementsystem for Python. Firstly, download it from this site.

	https://bootstrap.pypa.io/get-pip.py
    
    Then, type the following in the command prompt.

		$ python get-pip.py
 
* Type the following to install pandas and numpy modules.

		pip install numpy
    	pip install pandas

**Running Neural Network**

If all this installations completed smoothly, you can run easily neural network by
typing following in the command prompt.

	$ python NeuralNetwork.py
    
References and Thanks
---
* http://iamtrask.github.io/2015/07/12/basic-python-network/

I would like to express my gratitude to *Rabia Bilen* for his contribution to the generation of training data.
