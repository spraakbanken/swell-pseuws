pseuws
===

A thin WSGI web service layer for SamirYousuf's rule-based pseudonymizer for Swedish text.

The service lives at `https://ws.spraakbanken.gu.se/ws/larka/pseuws`

Usage
---

Call the service with a POST request and the following data.

| Parameter | Description |
| --------- | ----------- |
| text      | The text to pseudonymize. Punctuation tokens should be separated with a space, e.g. ``Jag heter Arild , och jag bor i Göteborg .``

### Response

The response contains a JSON representation of a list of sentences. Each sentence is a list of token objects, where each token object contains:
- `label`: a list of labels, possibly `[]`
- `string`: if `label` is empty, this is the original token string, otherwise it is a pseudonym

The response data type can be expressed in TypeScript as follows:

```typescript
interface Token {
  string: string
  label: string[]
}
type Sentence = Token[]
type Text = Sentence[]
```

Example
---

```sh
$ curl -d 'text=Ulla åker till London .'  https://ws.spraakbanken.gu.se/ws/larka/pseuws
[[{"label": ["firstname:female", "2"], "string": "Piritta"}, {"label": [], "string": "\u00e5ker"}, {"label": [], "string": "till"}, {"label": ["city", "1"], "string": "Zerba"}, {"label": [], "string": "."}]]
```

Running the server
---

### Requirements

Your mileage may vary.

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install --upgrade setuptools
(venv) $ pip3 install nltk pandas python-Levenshtein gunicorn
(venv) $ python3
>>> import nltk
>>> nltk.download('punkt_tab')
```

### Running

```sh
(venv) $ gunicorn anon:app
```
