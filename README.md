# loadtest

Load tester and benchmark tool for Python programmers.

## Installation:
```bash
pip install loadtest
```
## Basic usage

```python
def request_func():
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    if response.status_code != 200:
        print(response.status_code)
    else:
        sample = {
          "userId": 1,
          "id": 1,
          "title": "delectus aut autem",
          "completed": False
        }
        if response.json() != sample:
            print(response.json())
    return response

from loadtest import LoadTester
load_tester = LoadTester(n_jobs=10, worker=request_func, count=100)
load_tester.start()
```
