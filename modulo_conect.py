from requests import get

class Conect():
    
    __apiid=''
    
    def __init__(self):
        self.__apiid='944facd6e8c0e760c0e1c60381c12246'
        
    def get_clima(self, ciudad):
      
        ciudad= ciudad.lower()
        request= get(f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid=944facd6e8c0e760c0e1c60381c12246')
        
        response= request.json()
        print(response)
        return (response["main"]["temp"], response["main"]["feels_like"], response["main"]["humidity"])