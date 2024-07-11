# use third-party 'lorem-ipsum' package to generate random words
from lorem_text import lorem

# The `main` function is the entry-point into the function.
# It has one optional argument, which carries all the 
# parameters the function was invoked with.
def main(params):
    words = 10

    # since functions are invoked through http(s), we return an HTTP response
    return {
      "headers": {
        "Content-Type": "text/plain;charset=utf-8",
    },
    "body": lorem.words(words),
}

print (main ("null"))
