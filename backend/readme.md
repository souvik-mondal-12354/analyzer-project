# Backend for analysis-project

## Setup

1. clone the repository
2. create a virturn environment
```
python3 -m venv environ
```

Note : in windows if `python3` does not work try `py` only

3. activate the virtural environment

- windows

```
./environ/Scripts/activate
```

- linux
```
source ./environment/bin/activate
```

4. Install required libraries
```
pip3 install -r requirements.txt
```

Note: for windows the command will be `pip` insteed of `pip3`

5. run the server (dev mode)
```
fastapi dev ./src/app.py
```