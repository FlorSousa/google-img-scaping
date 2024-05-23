import requests
import re
import base64
def check_os() -> str:
    import platform
    sys_name = platform.system()
    os_acr = {
        "Windows":"win64",
        "Linux":"linx64",
        "Darwin":"mac-x64"
    }
    if sys_name in os_acr.keys():
        return os_acr[sys_name]
    return ""

def unzip(browser_name,data):
    import io
    import zipfile
    zip_content = io.BytesIO(data)
    with zipfile.ZipFile(zip_content, 'r') as zip_ref:
        zip_ref.extractall(f"{browser_name}_driver/")

def download_driver(browser_name,driver_version):
    os_name = check_os()
    if os_name == "":
        print("Error[2]: Your OS is not supported")
        exit(2)

 
    urls_download = {
        "chrome": f"https://storage.googleapis.com/chrome-for-testing-public/{driver_version}/{os_name}/chromedriver-{os_name}.zip",
        "firefox": f":p"
    }
    
    req = requests.get(urls_download[browser_name])
    unzip(browser_name,req.content)

def make_url(search_query):
    return f"https://www.google.com/search?q={search_query}&tbm=isch"
  
if __name__ == "__main__":
    from utils.parser_args import parser_args
    from utils.selenium_auto import run
    args = parser_args()
    
    if args.b not in ["firefox","chrome"] :
        print("Error[1]: Select a valid browser")
        exit(1)
    if args.dd == "y":    
       download_driver(args.b,args.d)
    
    images_url = run(url=make_url(args.s),browser_name=args.b)
    
    import os
    if not os.path.exists(f"images"):
        os.mkdir("images")
    
    os.mkdir(f"images/{args.s}")
       
    for index,url in enumerate(images_url):
        if url == None:
            continue
        regex = r'data:image/(jpeg|png|gif|svg);base64'
        if re.match(regex, url):
            encode = url.split(",",1)[1]
            byte_img = base64.b64decode(encode)
            file_ext = re.findall(regex,url)[0]
        else:
            byte_img = requests.get(url).content
            url_splited = url.split(".")
            file_ext = url_splited[len(url_splited)-1]
            
        if len(file_ext) > 4:
            continue
        path = f"images/{args.s}/image_{index}.{file_ext}"
        
        with open(path,"wb") as file:
            file.write(byte_img)
        
       