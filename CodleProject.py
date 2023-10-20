from ipycanvas import Canvas
from ipywidgets import Image
import IPython

class superstar():
    def __init__(self):
        self.__canvas = Canvas(width = 600, height = 300)
        self.__canvas.font = "20px serif"
        
        self.__url_map = {
                '봄' : "https://tmn-bucket-materials-all.s3.ap-northeast-2.amazonaws.com/image/dissac/dissac_naver_2_01.png",
                '여름' : "https://tmn-bucket-materials-all.s3.ap-northeast-2.amazonaws.com/image/dissac/dissac_naver_2_02.png",
                '가을' : "https://tmn-bucket-materials-all.s3.ap-northeast-2.amazonaws.com/image/dissac/dissac_naver_2_03.png",
                '겨울' : "https://tmn-bucket-materials-all.s3.ap-northeast-2.amazonaws.com/image/dissac/dissac_naver_2_04.png"
        }
        
    def show(self, season):
        self.__canvas.clear()
        image = IPython.display.Image(self.__url_map[season])
        sprite = Image(value = image.data)
        self.__canvas.draw_image(sprite)
        display(self.__canvas)
    
    def sing(self, song_title):
        self.__canvas.fill_text(song_title, 300, 150)