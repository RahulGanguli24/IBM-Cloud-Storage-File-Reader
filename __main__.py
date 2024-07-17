import pandas as pd
#print("Hello, World!")

df = pd.read_csv('Data/Municipality Contact Details.csv')

#print(df) 

def main(params):
  name = params.get("name", "world")
  greeting = "Hello " + name + "!"
  
  df = pd.read_csv('Data/Municipality Contact Details.csv')

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": "Total Rows: " + str(pd.options.display.max_rows)+ " --> " + greeting + " --> " ,
  }

#print ( main({"name": "world"}) )
