# Automated Tests E-Commerce Site
## Description
Automated tests using Python & PyTest for an ecommerce site. The site under test is created using WordPress, Woocommerce and the StoreFront theme.
Example site for testing: http://demostore.supersqa.com/



## Prerequisites to run the tests
* You must have the E-Commerce site running
* The site must be created with WordPress & WooCommerce
* The site must be using the "StoreFront" theme
* For a tutorial on how to create a site to run these tests on, watch these videos
  * [Creating Ecommerse Site for Testing - Part 1](https://www.youtube.com/watch?v=KhLGXIxeJLI&t=1s&ab_channel=SuperSQA)
  * [Creating Ecommerse Site for Testing - Part 2](https://www.youtube.com/watch?v=w47JR3aoTNw&ab_channel=SuperSQA)
  * [Creating Ecommerse Site for Testing - Part 3](https://www.youtube.com/watch?v=qwCY8UEWqqM&ab_channel=SuperSQA)

## Steps for setting up the framework and running tests

### Clone the code
```
git clone https://github.com/supersqa1/qa-bootcamp-framework.git
```

Navigate to the cloned directory
```
cd qa-bootcamp-framework
```

### Create virtual environment and install requirements
Create a virtual environment
```
python3 -m venv ssqatest_venv
```

### Activate the virtual environment 
  - On Mac/Linux
    ```commandline
    $ source  ssqatest_venv/bin/activate
    ```

  - On 'Windows CMD'
    ```commandline
    C:\..\Scripts\activate.bat
    ```

  - On 'Windows PowerShell'
    ```commandline
    C:\..\Scripts\Activate.ps1
    ```
### Install requirements in the virtual environment
```commandline
python3 -m pip install -r requirements.txt
```

### Set environment variables
There are variables required by the framework. 
Some of these value can be changed directly in the code instead of setting environment variables 
but setting the environment variables is the easiest option.
To change values in the code change them here: qa-bootcamp-framework/ssqatest/src/configs/MainConfigs.py

The Easiest way to set the variables is to set them in a file and run/source the file.
For 'Mac/Linux' systems, update and run the 'variables_local.sh' file.

```
source variables_local.sh
```

For 'Windows' using 'CMD' run the '' file.
```commandline
C:\..\variables_local.bat
```

Here are the variables that must be set
(For Windows on CMD replace 'export' with 'set')
```commandline
export BASE_URL=<your website url>
export BROWSER=<browser type>
export RESULTS_DIR=$(pwd)/results
export DB_PORT=<your database port>
export DB_HOST=<your database host>
export DB_DATABASE=<your site's database/schema name>
export DB_TABLE_PREFIX=<your site's tables prefix>

# credentials (these should not be kept in source controle like GitHub)
export WOO_KEY=<your woocommerce api key>
export WOO_SECRET=<your woocommerce api secret>
export DB_USER=<your database user>
export DB_PASSWORD=<your database password>
```

Example:
```commandline
export BASE_URL=http://localhost:8888/localdemostore/
export BROWSER=chrome
export RESULTS_DIR=$(pwd)/results
export DB_PORT=8889
export DB_HOST=localhost
export DB_DATABASE=localdemostore
export DB_TABLE_PREFIX=wp_
# credentials (these should not be kept in source controle like GitHub)
export WOO_KEY=ck_173049470988979798abedf1b34979a6fc437bd2da634
export WOO_SECRET=cs_38fc1985b37f17ffcoi987adf098adf65adf01c347
# credentials for the wordpress/mysql database
export DB_USER=root
export DB_PASSWORD=root
```

## Run tests
#### To run all tests
** Make sure virtual environment is active
** Explore the 'runner.sh' (For Mac/Linux) and consider using it.

```commandline
cd ssqatest
python3 -m pytest tests
```

#### To run frontend tests
```commandline
cd ssqatest
python3 -m pytest tests/frontend
```
#### To run backend tests
```commandline
cd ssqatest
python3 -m pytest tests/backend
```

#### To run specific test by id
```commandline
cd ssqatest
python3 -m pytest tests -m tcid33
```
