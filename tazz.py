#tazz get path
def fetchProjectImages(projectID, host="http://dtuuviris01.dtu.roche.com/iquant/"):
    #returns images in a given project
    projectIDStr = str(projectID)
    url = host + \
        'rest_api/project/' + projectIDStr + '.json'
    r = requests.get(url)
    project = json.loads(r.text)
    images = project[projectIDStr]["list_images"]
    print(images.keys())
    return images 

def fetchProjectImagePaths(images):
    #returns a dictionary mapping of images and their paths
    imagePaths = {}
    for image in images.keys():
        imagePaths[image]  = images[image]["path"]
    return imagePaths

def buildTazzImagePathsForScanInfo(imagePaths, tazz_base_url = 'http://dtumvims01.dtu.roche.com/tazz/'):
    #returns a dictionary mapping of images and their scan info urls
    #eg. {'L_2_HemII_F05012-11_20171102_3145': 'http://dtumvims01.dtu.roche.com/tazz/?FIF=/IQUANT/images/ReferenceSlides/L_2_HemII_F05012-11_20171102_3145.bif&INFO=SCAN', 
    scan_info_urls = {}
    for image, path in imagePaths.items():
        scan_info_urls[image] = tazz_base_url + \
                                "?FIF=" + path + \
                                "&INFO=SCAN"
    print(scan_info_urls)
    return scan_info_urls

def getImageScanDates(imageURLs):
    #return dictionary of images and their scan dates
    scan_dates = {}
    for image, url in imageURLs.items():
        scan_dates[image] = getScanDate(url)
    print(scan_dates)
    return scan_dates

def getScanDate(tazz_url):
    #returns scan date if available otherwise None
    response = requests.get(tazz_url)
    json_response = json.loads(response.text)
    print(json_response)
    scan_date = jsonpath.jsonpath(json_response, 'iScan.ScanDate')
    if scan_date:
        return scan_date[0]
    else:
        return None

def getProjectScanDates(projectID):
    images = fetchProjectImages(1211)
    imagePaths = fetchProjectImagePaths(images)
    imageURLs = buildTazzImagePathsForScanInfo(imagePaths)
    imageScanDates = getImageScanDates(imageURLs)
    return imageScanDates

print(getProjectScanDates(1211))