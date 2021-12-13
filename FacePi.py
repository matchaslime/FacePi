import fire, os, json
import http.client, urllib.request, urllib.parse, urllib.error, base64
basepath = os.path.dirname(os.path.realpath(__file__))
headers = os.path.join(basepath,'Config.json')

class FacePi:
    def detectLocalImageUrl(self, imagepath):
        headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.readConfig()['api_key'],
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender',
            #'recognitionModel': 'recognition_04',
            'returnRecognitionModel': 'false',
            'detectionModel': 'detection_01',
            'faceIdTimeToLive': '86400',
        })

        print('imageurl=', imagepath)
        requestbody = open(imagepath, "rb").read()
        try:
            conn = http.client.HTTPSConnection(self.readConfig()['host'])
            conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody, headers)
            response = conn.getresponse()
            data = response.read()
            json_face_detect = json.load(str(data, 'UTF-8'))
            print("detectLocalImage:",f"{imagepath}偵測到{len(json_face_detect)}個人")
            return json_face_detect
        
        except Exception as e:
            print("[Errno {0}]連線檢查失敗！請檢察網路設定。 {1}".format(e.errno, e.strerror))

    def detectImageUrl(self, imageurl):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.readConfig()['api_key'],
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender',
            #'recognitionModel': 'recognition_04',
            'returnRecognitionModel': 'false',
            'detectionModel': 'detection_01',
            'faceIdTimeToLive': '86400',
        })

        print('imageurl=', imageurl)
        requestbody = '{"url":"' + imageurl + '"}'
        try:
            conn = http.client.HTTPSConnection(self.readConfig()['host'])
            conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody, headers)
            response = conn.getresponse()
            data = response.read()
            json_face_detect = json.load(str(data, 'UTF-8'))
            print("detectLocalImage:",f"{imageurl}偵測到{len(json_face_detect)}個人")
            return json_face_detect
        
        except Exception as e:
            print("[Errno {0}]連線檢查失敗！請檢察網路設定。 {1}".format(e.errno, e.strerror))

    def Indntify(self, imagepath):
        '''
        傳入圖片路徑，url 並進行辨識
        '''
        self.detectLocalImage(imagepath)

    def Signin(self):
        '''
        刷臉簽到
        '''
        imageurl = 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg'
        imageurl = 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Bill_Gates_2017_%28cropped%29.jpg'
        self.detectLocalImageUrl(imageurl)


if __name__ == '__main__':
    fire.Fire(FacePi)