# microservices

In order to request data from the microservice, your program must assemble a dictionary of character data.
This dictionary should be converted to json using the "json.dumps" command and written to the txt file: "getSheet.txt".
An example request is shown below.

After the request has been sent ,your program should wait for a response from the service containing the file path to your sheet.
The character sheet should be found in the same directory as all of the other files mentioned here (getSheet.txt, sheetGen.py).
An example of how your program should await a reponse is shown below.

# example microservice request call
```
  import json
  character = {"name":"Brandomonkey",
               "class":"Ranger",
               "level":"20",
               "str":"10",
               "dex":"22",
               "con":"16",
               "int":"14",
               "wis":"30",
               "cha":"1"}
  
  file = open(r"getSheet.txt","w+")
  json_char = json.dumps(character) 
  file.write(json_char)
```
# example microservice response call
```
  output = ""
  while output == "":
      output = file.readline()
```
![Sequence diagram (1)](https://github.com/BrandonNguyenOSU/microservices/assets/135754216/66281efa-d9c1-46c5-96e8-90409bc1ed84)
