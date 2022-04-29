import requests
input = input(("단어"))
url = 'https://wordsapiv1.p.rapidapi.com/words/{}/synonyms'.format(input)

headers = {
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
	"X-RapidAPI-Key": "d01476a2e3msh99aaa889250ff07p1b9ecdjsn79f4a330e88a"
}
response = requests.request("GET", url, headers=headers)

print(response.text)