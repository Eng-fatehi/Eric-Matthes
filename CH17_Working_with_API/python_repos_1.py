import requests   # requests is a third-party module that makes HTTP (Hypertext نص تشعبيTransfer Protocol) requests.
''' 
The requests module allows you to send HTTP requests using Python. 
The HTTP request returns a Response Object with all the response data 
(content, encoding, status, etc).
'''

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"  # The main part of the URL 
# https://api.github.com/   directs the request to the part of GitHub that responds to API calls.
# search/repositories       tells the API لاجرا بحث to conduct a search through all the repositories on GitHub.

url +="?q=language:python+sort:stars+stars:>10000"  #  الاستعلام الاستفسارThe query part of the URL

'''
the question mark, tell that we're about to pass an argument.
علامة الاستفهام، تخبرنا أننا على وشك تمرير حجة.
the q stands for query.
يشير الحرف q إلى الاستعلام.
the equal sign (=), lets us begin specifying a query (q=).
علامة التساوي (=)، تتيح لنا البدء في تحديد الاستعلام (q=).
language:python, we indicate that we want information only on repositories that have Python as hte primary language.
نشير إلى أننا نريد معلومات فقط عن المستودعات التي تحتوي على لغة بايثون كلغة أساسية.
+sort:stars, sorts the projects by the number of stars they've been given.
+sort:stars، يقوم بفرز المشاريع حسب عدد النجوم التي تم منحها لها.
stars:>10000, tells GitHub to only look for Pythons repositories that have more than 10,000 stars.
يخبر (جيت هب) بالبحث فقط عن مستودعات بايثون التي تحتوي على أكثر من 10000 نجم.
'''

# ملاحظة لو حذفت الهيدرس لن يتغير شي
headers = {"Accept": "application/vnd.github.v3+json"} # the headers for the API call in dictonary by key and value.
# # Set the content type based on your API requirements. تحدد طبيعة ونمط البيانات المطلوبة.
# ask to this version of the API and return  the results (response) in json format.
r = requests.get(url, headers=headers) # r is a response object 
print(f"status code: {r.status_code}")  #  if the requst is successful, the status code will be 200.

# Convert the response object to a dictionary.
response_dict = r.json() # use json() method on the response object to parse the response content as json.

# Process results.
print(response_dict.keys())


'''  https://api.github.com/search/repositories?q=language:python+sort:stars  '''

''' https://www.youtube.com/watch?v=9Kwnq4y7hzY&list=PLVCtnldBSr4-hJ6y3eLJqzdbP_wlagjAG&index=10 '''

''' https://www.youtube.com/watch?v=FW8NdB18AYM '''