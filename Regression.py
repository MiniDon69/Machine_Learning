class LogisticRegression:
    def __init__(self,x:list,y:list):
        
        n = len(x)
        x_mean = sum(x)/n
        y_mean = sum(y)/n
        x_deviation=[i-x_mean for i in x]
        y_deviation=[i-y_mean for i in y]

        deviation_product = [x_deviation[i] * y_deviation[i] for i in range(n)]
        x_deviation_square = [i*i for i in x_deviation]

        self.m = sum(deviation_product)/sum(x_deviation_square)
        self.b = y_mean - (self.m * x_mean)
        print("M:",self.m)
        print("B:",self.b)


    def predict_y(self,x):
        y = self.m * x + self.b
        return y
    
x = [8,10,12]
y = [10,13,16]

obj = LogisticRegression(x,y)

print(obj.predict_y(20))