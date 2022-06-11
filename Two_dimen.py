#importing required libraries
import math
import numpy as np
class Point :
      
   

    def __init__(self,p1,p2):
        
        
        self.x=p1
        self.y=p2
        
    def __str__(self):
        
        
        return "  ({},{})".format(self.x,self.y)
    
    
    def __add__(self,other):
        
        '''This method is uesd to add two 2-D points'''
      
        temp_x=self.x+other.x
        
        temp_y=self.y+other.y
        
        addition =Point(temp_x,temp_y)
        
#creating addition  as a point of 2-D coordinate system

        print(addition)
        
    
    def __sub__(self,other):
        
        '''This method is used to subtract two 2-D points'''
        
        temp_x=self.x-other.x
        
        temp_y=self.y-other.y
        
        subtraction=Point(temp_x,temp_y)
        
#creating subtraction as a point of 2-D coordinate system

        print(subtraction)
    
    
    def Check_quadrant(self):
        
        '''This Method is used to check in which quadrant point lies'''
        
        if(self.x>=0 and self.y>=0):
            print("({},{}) is point of First quadrant".format(self.x,self.y))
            
        elif(self.x<0 and self.y>=0):
            print("({},{}) is point of Second quadrant".format(self.x,self.y))
            
        elif(self.x<0 and self.y<0):
            print("({},{}) is point of Third quadrant".format(self.x,self.y))
            
        else:
            print("({},{}) is point of Fourth quadrant".format(self.x,self.y))
            
            
    def Distance(self,other):
        
        '''This method will give Distance between two points ''' 
    
        return round(math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2),2)
        
       
    def Mid_point(self,other):
        
        '''This method will give mid point for two points given as input'''
    
        mid_x=(self.x+other.x)/2
        
        mid_y=(self.y+other.y)/2
        
        mid=Point(mid_x,mid_y)
        
#creating mid-point as a object of 2-D coordinate system

        print(mid)
    
    
    def Section_formula(self,other):
        
        '''This method is used to find coordinate of a point which 
        divides line segment joining two points in ratio of m:n '''
        
        print("please enter the ratio ")
        
        m=int(input())
        
        n=int(input())
        
        print("""Please select how you want to divide
                 1 for internal division 
                 2 for external division """)
        
        div=int(input())
        
        try:
            
            if div==1:

                point_x=(m*other.x + n*self.x)/(m+n)

                point_y=(m*other.y + n*self.y)/(m+n)
                
                point=Point(round(point_x,2),round(point_y,2))
                
                print(point)

            elif div==2:
                
                point_x=(m*other.x - n*self.x)/m+n
                
                point_y=(m*other.y - n*self.y)/m+n
                
                point=Point(round(point_x,2),round(point_y,2))
                
                print(point)
                
            else:
                
                print("Incorrect divison mentioned")

        except Exception as e:
            
            print("The error we are getting is ",e)

    
    def Area_of_triangle(self,point2,point3):
        
        '''This method will take input of three points and will give Area of triangle fromed 
        from these points as output'''
        

        return 0.5*abs(self.x*(point2.y-point3.y) + point2.x*(point3.y-self.y)+point3.x*(self.y-point2.y))


    
    def Is_collinear(self,point2,point3):
        
        '''This method will take three points as input  and will check for collinarity of three points'''
        
        if(self.Area_of_triangle(point2,point3)==0):
                
            print("These points are Collinear")
            
#calling and using previously defined fuction here using self keyword

        else:
        
            print("These points are not Collinear")
                
                
                
    def Dot_product(self,other):
        
        '''This method will take two points as input and will consider them as vector 
        of i th and j th coordinate and give their dot product as output '''
        
        return self.x*other.x + self.y*other.y
          
        
    def Slope(self,other):
        
        '''This method will calculate slope of a line from two given 2-D points '''
        
        try:
            if((other.x-self.x)==0):
                
                slope=np.Inf
                
            else:
                 slope= (other.y-self.y)/(other.x-self.x)
                
            return round(slope,2)
        
        except Exception as e:
            
            print("the error is caused by",e)
            
       
    def Intercept(self,other):
        
        '''This method will give intercept of line formed by two points '''
        
        try:
            
            intercept=self.Slope(other) * self.x
            
            return round(intercept+self.y,2)
        
        except Exception as e:
            
            print("the error is caused by",e)
            
            
    def Line_from_point(self,other):

         print("Y={}X+{}".format(self.Slope(other),self.Intercept(other)))

            
class Line :
    
    
    def __init__(self,a,b,c):
        
        try:
            self.a=a
            self.b=b
            self.c=c
            if(b==0):
                self.slope=np.Inf
            else:
                self.slope=-a/b
                
            self.intercept=c/b
            
        except Exception as e:
            
            print("The error we are getting is ",e)
            
        
    def __str__(self):
        
        return "{}X+{}Y+{}=0".format(self.a,self.b,self.c)
    
    
    def Point_of_intersection(self,other):
        
        '''This method will take two lines as input and will give point of intersection of lines 
        as output '''
        
        try:
        
            poin_x=round((self.b*other.c-other.b*self.c)/(self.a*other.b-other.a*self.b),2)

            poin_y=round((other.slope*self.intercept-self.slope*other.intercept)/(self.slope-other.slope),2)

            point_of_intersection=Point(poin_x,poin_y)

            print(point_of_intersection)
        
        except Exception as e:
            
            print("The error we are getting is",e)
    
    def Nature_of_lines(self,other):
        
        '''This method will take two lines as input and will give angle between them as output'''
        
 
            
        if((self.slope*other.slope)==-1):
            
            print("The lines are perpendicular")
            
        elif(self.slope==other.slope):
            
            
            print("The lines are parallel")
            
        else:
            try:
            
            
                angle_rad=np.arctan((self.slope-other.slope)/(1+self.slope*other.slope))

                angle= int(math.degrees(abs(angle_rad)))
                print("The lines intersect at an angle of {} degree".format(angle))
                
            except Exception as e:
                print(" the error we are getting is",e)


    def Distance_paralell_lines(self,other):
        
        try:
            
            dist=abs((self.c-other.c)/math.sqrt((self.a)**2+(self.b)**2))
            
            return dist
        
        except Exception as e:
            
            print("The error we are getting is",e)
            
   
        
        
class Line_and_point(Point,Line):
   
        def __init__(self,point,line):
            self.p=point
            self.l=line
            

        def Dist_point_line(self):
            
            try:
        
                return round(((self.p.x*self.l.a) +( self.l.b*self.p.y)+(self.l.c))/math.sqrt((self.l.a)**2+(self.l.b)**2),2)
        
            except Exception as e:
                
                 print("The error we are getting here is ",e)
           