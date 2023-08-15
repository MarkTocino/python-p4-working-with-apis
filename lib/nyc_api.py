
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    programs_list = []
  # json.loads turn the response into a dictionary rather than a byte string
  # byte string b'[\n  {\n    "name": "Flatiron School Manhattan",\n    "address": "11 Broadway, New York, NY 10004",\n    "coordinates": {\n      "latitude": "40.704521",\n      "longitude": "-74.012833"\n    }\n  },\n  {\n    "name": "Flatiron School Austin",\n    "address": "316 W 12th St, Austin, TX 78701",\n    "coordinates": {\n      "latitude": "30.275080",\n      "longitude": "-97.743700"\n    }\n  },\n  {\n    "name": "Flatiron School Denver",\n    "address": "3601 Walnut St 5th Floor, Denver, CO 80205",\n    "coordinates": {\n      "latitude": "39.743510",\n      "longitude": "-105.011360"\n    }\n  },\n  {\n    "name": "Flatiron School Seattle",\n    "address": "1411 4th Ave 13th Floor, Seattle, WA 98101",\n    "coordinates": {\n      "latitude": "47.684879",\n      "longitude": "-122.201363"\n    }\n  },\n  {\n    "name": "Flatiron School London",\n    "address": "131 Finsbury Pavement, Finsbury, London EC2A 1NT, UK",\n    "coordinates": {\n      "latitude": "51.520480",\n      "longitude": "-0.087190"\n    }\n  }\n]'


  # json.loads:
  # [
  #    {
  #       "name":"Flatiron School Manhattan",
  #       "address":"11 Broadway, New York, NY 10004",
  #       "coordinates":{
  #          "latitude":"40.704521",
  #          "longitude":"-74.012833"
  #       }
  #    },
  #    {
  #       "name":"Flatiron School Austin",
  #       "address":"316 W 12th St, Austin, TX 78701",
  #       "coordinates":{
  #          "latitude":"30.275080",
  #          "longitude":"-97.743700"
  #       }
  #    },
  #    {
  #       "name":"Flatiron School Denver",
  #       "address":"3601 Walnut St 5th Floor, Denver, CO 80205",
  #       "coordinates":{
  #          "latitude":"39.743510",
  #          "longitude":"-105.011360"
  #       }
  #    },
  #    {
  #       "name":"Flatiron School Seattle",
  #       "address":"1411 4th Ave 13th Floor, Seattle, WA 98101",
  #       "coordinates":{
  #          "latitude":"47.684879",
  #          "longitude":"-122.201363"
  #       }
  #    },
  #    {
  #       "name":"Flatiron School London",
  #       "address":"131 Finsbury Pavement, Finsbury, London EC2A 1NT, UK",
  #       "coordinates":{
  #          "latitude":"51.520480",
  #          "longitude":"-0.087190"
  #       }
  #    }
  # ]

    programs = json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program["agency"])
    return programs_list

# programs = GetPrograms().get_programs()
# print(programs)
programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
  print(school)
