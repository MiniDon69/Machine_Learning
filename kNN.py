class Movie:
    def __init__(self,rateing:float,duration:int,genre:str):
        self.rating = rateing
        self.duration = duration
        self.genre = genre

class KNN:
    def __init__(self,arr:list,rating:float,duration:int):
        self.rate = rating
        self.duration = duration
        self.closest = arr[0]
        
        for i in arr:
            if self.distance(i) < self.distance(self.closest):
                self.closest = i

        print(self.closest.genre)

    def distance(self,Movie:Movie):
        
        return ((self.rate-Movie.rating)**2+(self.duration-Movie.duration)**2)**0.5


movie1 = Movie(8.0,160,"Action")
movie2 = Movie(6.2,170,"Action")
movie3 = Movie(7.2,168,"Comedy")
movie4 = Movie(8.2,155,"Comedy")

obj = KNN([movie1,movie2,movie3,movie4],7.4,114)


