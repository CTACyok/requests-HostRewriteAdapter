# requests-HostRewriteAdapter
Simple adapter for requests library to replace host of a request

## Example
```python
import requests
from host_rewrite_adapter import HostRewriteAdapter
session = requests.Session()
session.mount("https://localhost:5000", HostRewriteAdapter(new_host="127.0.0.1"))
r = session.get("https://localhost:5000/api/v1/resource")
```
