from . import session
import json

class CSB(object):
    """ Version 0.0.1 """
    def __init__(self, lang, *args):
        self.ids = list(args)
        self.url = 'https://data.stat.gov.lv/api/v1/{}/OSP_PUB/'.format(lang)
        self.url_out = 'https://data.stat.gov.lv/pxweb/{}/OSP_PUB/START__'.format(lang)
        self.query = {"query": [], 
                      "response": {"format": "json"}
                      }

    def info(self):
        """ Returns the metadata associated with the current folder. """
        response = session.get(self.url + '/'.join(self.ids))
        return response.json()

    def go_down(self, *args):
        """ Goes deeper in the hierarchical metadata structure. """
        self.ids += list(args)

    def go_up(self, k=1):
        """ Goes k levels up in the hierarchical metadata structure. """
        self.ids = self.ids[:-k]

    def get_url(self):
        """ Returns the url to the current folder. """
        if len(self.ids[-1]) >= 3:
            try:
                int(self.ids[-1][3])
            except ValueError:
                return self.url_out + '__'.join(self.ids[:-1]) + '/' + self.ids[-1]
        return self.url_out + '__'.join(self.ids)

    def get_variables(self, codes=True):
        """
        Returns a dictionary of variables and their ranges for the bottom node.

        :param codes: If True (default), return value codes. 
                      If False, return human-readable texts.
        """
        response = self.info()
        val_dict = {}
        try:
            variables = response['variables']
        except (TypeError, KeyError):
            print("Error: You are not in a leaf node.")
            return val_dict

        for item in variables:
            if codes:
                val_dict[item['code']] = item.get('values', [])
            else:
                val_dict[item['code']] = item.get('valueTexts', [])
        return val_dict


    def clear_query(self):
        """ Clears the query. Mostly an internal function to use in others. """
        self.query = {"query": [], 
                      "response": {"format": "json"}
                      }

    def set_query(self, **kwargs):
        """ Forms a query from input arguments (codes only). """
        self.clear_query()
        response = self.info()
        variables = response['variables']
        for kwarg in kwargs:
            for var in variables:
                if var["code"] == kwarg:  # match by code, not text
                    self.query["query"].append({
                        "code": var['code'],
                        "selection": {
                            "filter": "item",
                            "values": [v for v in kwargs[kwarg] if v in var['values']]
                        }
                    })


    def get_query(self):
        """ Returns the current query. """
        return self.query

    def get_data(self, return_text=False):
        """ Returns the data from the constructed query. 
        
        :param return_text: If False (default), return only value codes.  {'key': ['LV0056420', '2025'], 'values': ['456']}
                      If True, return codes and texts e.g. {'key': [{'code': 'LV0056420', 'text': '..Piltenes pagasts'}, {'code': '2025', 'text': '2025'}], 'values': ['456']}
        """
        response = session.post(self.url + '/'.join(self.ids), json=self.query)
        response_json = json.loads(response.content.decode('utf-8-sig'))

        if not return_text:
            return response_json

        # Build mapping from metadata
        meta = self.info()
        code_to_text = {
            var["code"]: dict(zip(var["values"], var["valueTexts"]))
            for var in meta["variables"]
        }

        # Enrich keys with texts
        enriched_data = []
        for row in response_json.get("data", []):
            enriched_key = []
            keys = row.get("key", [])
            for idx, code_val in enumerate(keys):
                col_code = response_json["columns"][idx]["code"] if idx < len(response_json["columns"]) else f"VAR{idx}"
                text_val = code_to_text.get(col_code, {}).get(code_val, code_val)
                enriched_key.append({"code": code_val, "text": text_val})
            enriched_data.append({
                "key": enriched_key,
                "values": row.get("values", [])
            })


        response_json["data"] = enriched_data
        return response_json