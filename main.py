import pandas as pd
print("Hello, World!")

df = pd.read_csv('Data/Municipality Contact Details.csv')

print(df) 

def main(params):
  name = params.get("name", "world")
  greeting = "Hello " + name + "!"
  

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": greeting,
  }

print ( main({"name": "world"}) )