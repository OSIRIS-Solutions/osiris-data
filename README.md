
# Setup optional jobs

This library need Python to be installed. Please look up [how to install](https://wiki.python.org/moin/BeginnersGuide/Download) the latest Python version on your OS. You will also need `pip` to install packages.

When you have Python installed, you can create an virtual environment (see [here](https://docs.python.org/3/library/venv.html) for more information on python virtual environments). 

This command will create a folder named 'venv' and all needed files for the virtual environment with in the folder:

```bash
python3 -m venv ./venv
```

Next step is to start the virtual environment:

```bash
source ./venv/bin/activate
```

## Set up osirisdata

Now you can install the python library **osirisdata** and all dependencies. Therefore you can  run:

```bash
make install
```

Additionally, you have to copy the **configuration file** `config.default.ini` and rename it to `config.ini`. 
In this file, you must modify the values according to your needs. 


### Prepare

To set up this feature, you must change the OpenAlex-ID of your institute in the `config.ini` file.

```ini
[OpenAlex]
Institution = I7935750
```
