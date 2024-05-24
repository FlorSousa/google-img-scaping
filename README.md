# Google images scaprapper

```
python main.py -s <your+search> -b <your_browser> -dd <y or n to download driver> -d <if yes the version>
```

| CLI     | Mean |
| -------- | ------- |
| -s  | Search query    |
| -b |  Browser     |
| -dd    | Download driver (y or n)    |
| -d    | Driver version (if downloading)   |


## Save white mice images 🐭
```
python main.py -s white+mice -b firefox
```

## Save dogs images and download firefox driver 🐶
```
python main.py -s cute+dogs -b firefox -- dd y -d 0.34.0
```

## Save cats imagens and download chrome driver 🐱‍🚀
```
python main.py -s badass+cats -b chrome -- dd y -d 125.0.6422.78
```

### or
Chrome is the default option 😛
```
python main.py -s badass+cats -- dd y -d 125.0.6422.78
```


# Alert ⚠️

This is an experimental repository for academic purposes

## Problems or others 😕
- Only driver downloads for x64 architecture are tested
- Refactoring of some methods is needed
- Chromedriver unzip creates a folder. You'll need to manually move/copy chromedriver.exe (a bug to be fixed)