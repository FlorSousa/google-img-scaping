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

        
def extract_tar(data):
    pass

def download_chrome_driver(driver_version,os_name):
    url_to_download =  f"https://storage.googleapis.com/chrome-for-testing-public/{driver_version}/{os_name}/chromedriver-{os_name}.zip"
    data = requests.get(url_to_download).content
    unzip("chrome",data)

def get_binary(driver_version,os_name,bits,type_compression):
    if bits == 32:
        url_to_download = f"https://github.com/mozilla/geckodriver/releases/download/v{driver_version}/geckodriver-v{driver_version}-{os_name}.{type_compression}"
        return requests.get(url_to_download).content
    
    os_abr = re.findall(r'(win|macos|linux)',os_name)[0]
    url_to_download = f"https://github.com/mozilla/geckodriver/releases/download/v{driver_version}/geckodriver-v{driver_version}-{os_abr}-aarch64.{type_compression}"
    return requests.get(url_to_download).content

def download_firefox_driver(driver_version,os_name):
    bits_os_version = re.findall(r'(32|64)',os_name)[0]
    data = None
    type_compression = "zip" if re.match(r'win',os_name)[0] == "win" else "tar.gz"
    data = get_binary(driver_version,os_name,bits_os_version,type_compression)
    
    if type_compression == "zip":
        unzip("firefox",data)
        return

    if type_compression == "tar.gz":
        extract_tar("firefox",data)
        return
       
    
    
def download_driver(browser_name,driver_version):
    os_name = check_os()
    if os_name == "":
        print("Error[2]: Your OS is not supported")
        exit(2)

    
    urls_download = {
        "chrome": lambda driver_version,os_name: download_chrome_driver(driver_version,os_name),
        "firefox": lambda driver_version,os_name :download_firefox_driver(driver_version,os_name)
    }
    
    urls_download[browser_name](driver_version,os_name)

def write_image(file_ext,data):
    name_img = f"images/{args.s}/image_{index}.{file_ext}"
    with open(name_img,"wb") as file:
            file.write(data)
  
if __name__ == "__main__":
    from utils.parser_args import parser_args
    from utils.selenium_auto import run
    args = parser_args()
    
    if args.b not in ["firefox","chrome"] :
        print("Error[1]: Select a valid browser")
        exit(1)
    if args.dd == "y":    
       download_driver(args.b,args.d)
    
    images_url = run(url=f"https://www.google.com/search?q={args.s}&tbm=isch",browser_name=args.b)
    
    import os
    if not os.path.exists(f"images"):
        os.mkdir("images")
    
    if not os.path.exists(f"images/{args.s}"):
        os.mkdir(f"images/{args.s}")
       
    for index,url in enumerate(images_url):
        if url == None:
            continue
        file_ext = ""
        regex_base64 = r'data:image/(jpeg|gif|jpg|png|svg);base64'
        if re.match(regex_base64, url):
            encode = url.split(",",1)[1]
            byte_img = base64.b64decode(encode)
            file_ext = re.findall(regex_base64,url)[0]
            if file_ext == "gif":
                continue
            
            write_image(file_ext,byte_img)
            continue
        
        regex_default = r'.(jpeg|jpg|png|svg)'
        if re.match(regex_default,url):
            byte_img = requests.get(url).content
            file_ext = re.findall(regex_default,url)[0]
            write_image(file_ext,byte_img)
            continue
          
        req = requests.get(url)
        byte_img = req.content
        file_ext = "jpg"
        write_image(file_ext,byte_img)