# pycsbwrapper
Version 0.0.1

Python wrapper for Central Bureau of Statistics Republic of Latvia pxweb API
https://stat.gov.lv/lv/api-un-kodu-vardnicas/api

Forked from https://github.com/vf42/pycspwrapper, added additional functionality for returning valueTexts
<br />which is forked from https://github.com/kirajcg/pyscbwrapper/, replacing the Sweden API endpoints with the Latvian Central Statistics Bureau ones.

Dependencies: requests>=2.21.0

To install: 
```python
pip install pycsbwrapper
```

To import: 
```python
from pycsbwrapper import CSB
```

For info on usage, see the included notebooks.

## Changelog
News in version 0.0.1:
For wrapper to be better readable by humans and LLMs added parameters for functions that allow returning not just the codes of variables but also texts

get_data - additional parameter added return_text
        <br /> &emsp; :param return_text: If False (default), return only value codes.  {'key': ['LV0056420', '2025'], 'values': ['456']}
                    <br /> &emsp; &emsp;  If True, return codes and texts e.g. {'key': [{'code': 'LV0056420', 'text': '..Piltenes pagasts'}, {'code': '2025', 'text': '2025'}], 'values': ['456']}

get_variables - additional parameter added codes
      <br /> &emsp; :param codes: If True (default), return value codes. 
                   <br /> &emsp; &emsp;  If False, return human-readable texts.
