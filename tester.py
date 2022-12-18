import requests

body = "ewogImFuc3dlcnMiOiB7ItCi0LXQvNCwINCy0LDRiNC10LPQviDQvtCx0YDQsNGJ0LXQvdC40Y8iOiAi0JrQvtC80LzQtdC90YLQsNGA0LjQuSIsICLQodC+0L7QsdGJ0LXQvdC40LUiOiAiZmFzZGZhZHNmYWRmIiwgItCf0YDQuNGB0L7QtdC00LjQvdC40YLRjCDRhNCw0LnQuzoiOiAi0J3QtdGCINC+0YLQstC10YLQsCIsICLQktCw0YjQtSDQuNC80Y8iOiAic2RmYXNkIiwgItCS0LDRiCBlbWFpbCI6ICJrb241Z29yQHlhbmRleC5ydSJ9LAogImRhdGUiOiAxOC4xMi4yMDIyCn0="

form1 = {
    "header1": "world",
    "header2": "Im"
}

form2 = {
    "header1": "mike",
    "header2": "nice little doggy"
}

form3 = {
    "header1": "world",
    "header2": "Im",
    "header3": " opsie new header"
}

form4 = {
    "header1": "world",
    "header3": "header deleted"
}

url = "http://localhost:8080/1GvxHnRLOnsUZZg_cUm7NUKdmCVGrZyWj9XkAo-3q36Q"
for form in form1, form2, form3, form4:
    body = {
        "answers": form
    }
    requests.post(url, json=body)
