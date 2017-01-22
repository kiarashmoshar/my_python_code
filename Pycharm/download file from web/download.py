from urllib import request
google_url="http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"

def download_data(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_url.split("\\n")
    dest_url=r'goog.csv'
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_data(google_url)
