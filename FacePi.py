import fire, os, json
import http.client, urllib.request, urllib.parse, urllib.error, base64
import classes.ClassFaceAPI
import classes.ClassOpenCV

class FacePI:


    def show_opencv(self):
        classes.ClassOpenCV.show_opencv('hint')

    def Signin(self):
        '''
        刷臉簽到
        '''
#        imagepath = '202994853.jpg'
#        imagepath = 'face4.jpg'
#        self.detectLocalImage(imagepath)
#        
        imageurl = 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg'
        imageurl = 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Bill_Gates_2017_%28cropped%29.jpg'
        classes.ClassFaceAPI.Face().detectImageUrl(imageurl)
        imagepath = "Bezos.jpg"
        classes.ClassFaceAPI.Face().detectLocalImage(imagepath)
        
if __name__ == '__main__':
    fire.Fire(FacePI)