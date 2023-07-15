# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# return a response


import urllib.request as urllib





def main(url):
    print("Checking connectivity site checker")


    response = urllib.urlopen(url)
    print("Connected to", url, "Succesful")

    print("The response cose was:", response.getcode())

print("This is a site connectivisity checker program")
input_url = input("Input the url of the site you want to check:")

main(input_url)