from django.shortcuts import render,redirect
from .mazetest import Maze
from .solutiondata import sols
import time,os
# floor1checkpoint = {"kitchen":(138, 23), "bedroom1":(48, 24), "emptyroom":(59, 41), "bath":(31, 44), "stairentry":(106, 45), "bath2":(58, 50), "room":(188, 50),"stairexit":(106, 53),"familyroom":(63, 67), "formaldining":(100, 68),"office":(139, 71), "exit":(79, 76)}
# floor2checkpoint = {"bedroom1":(56,24), "familyroom":(119, 37), "bath":(32, 45), "stairentry":(143, 45), "emptyroom":(73, 51),"stairexit":(142, 51), "bedroom3":(146, 62),"bedroom2":(74, 63),"Bathroom":(107, 72)}

locations={'Hall':(55,86),'Bedroom 1':(26,36),'Bedroom 2':(67,35),'Bedroom 3':(78,94),'Bedroom 4':(57,171),'Sitting Area':(14,112),'Balcony':(15,140),'Master Bath':(27,151),'Master Bedroom':(26,98),'Bath':(54,27),'W.I.C':(34,133)}
# this is for the first floor
floor1checkpoint = {"kitchen-1st floor":(138, 23), "bedroom1-1st floor":(48, 24), "empty-1st floor":(59, 41), "bath-1st floor":(31, 44), "stairentry-1st floor":(106, 45), "bath2-1st floor":(58, 50), "room-1st floor":(188, 50),"stairexit-1st floor":(106, 53),"familyroom-1st floor":(63, 67), "formaldinnning-1st floor":(100, 68),"office-1st floor":(139, 71), "exit-1st floor":(79, 76)}
# this is for the second floor
floor2checkpoint = {"bedroom1-2nd floor":(56,24), "familyroom-2nd floor":(119, 37), "bath-2nd floor":(32, 45), "stairentry-2nd floor":(143, 45), "empty-2nd floor":(73, 51),"stairexit-2nd floor":(142, 51), "bedroom3-2nd floor":(146, 62),"bedroom2-2nd floor":(74, 63),"bathroom-2nd floor":(107, 72)}
floors = [floor1checkpoint,floor2checkpoint]
floor1 = False
floor2 = False
# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request,'inmapapp/index.html',{'image':"inmapapp/MAP.png",'time':'','update':False})    
    else:
        then = time.time()
        FromAuto = request.POST.get('fromLocation')
        ToAuto = request.POST.get('To')
        FromMan = request.POST.get('manualFrom')
        ToMan = request.POST.get('manualTo')
        if FromAuto and ToAuto:
            From = FromAuto
            To = ToAuto
        else:
            From = FromMan
            To = ToMan
        if From in floor1checkpoint and To in floor1checkpoint:
            From_x,From_y = floor1checkpoint[From]
            To_x,To_y = floor1checkpoint[To]
            m = Maze(os.path.abspath('inmapapp/static/inmapapp/floor1.txt'),From_x,From_y,To_x,To_y,"floor1.png")
            m.solve()
            m.output_image()
            floor1 = True
            floor2 = False
            return render(request,'inmapapp/result.html',{'floor1':floor1,'floor2':floor2,'time':time.time()-then,'update':True})
        if From in floor2checkpoint and To in floor2checkpoint:
            From_x,From_y = floor2checkpoint[From]
            To_x,To_y = floor2checkpoint[To]
            m = Maze(os.path.abspath('inmapapp/static/inmapapp/floor2.txt'),From_x,From_y,To_x,To_y,"floor2.png")
            m.solve()
            m.output_image()
            floor1=False
            floor2 = True
            return render(request,'inmapapp/result.html',{'floor1':floor1,'floor2':floor2,'time':time.time()-then,'update':True})
        if From in floor1checkpoint and To in floor2checkpoint:
            From_x,From_y = floor1checkpoint[From]
            To_x,To_y = floor2checkpoint[To]
            m = Maze(os.path.abspath('inmapapp/static/inmapapp/floor1.txt'),From_x,From_y,106,53,"floor1.png")
            m.solve()
            m.output_image()
            n = Maze(os.path.abspath('inmapapp/static/inmapapp/floor2.txt'),143,45,To_x,To_y,"floor2.png")
            n.solve()
            n.output_image()
            floor1=True
            floor2=True
            return render(request,'inmapapp/result.html',{'floor1':floor1,'floor2':floor2,'time':time.time()-then,'update':True})
        if From in floor2checkpoint and To in floor1checkpoint:
            From_x,From_y = floor2checkpoint[From]
            To_x,To_y = floor1checkpoint[To]
            m = Maze(os.path.abspath('inmapapp/static/inmapapp/floor2.txt'),From_x,From_y,142,51,"floor2.png")
            m.solve()
            m.output_image()
            n = Maze(os.path.abspath('inmapapp/static/inmapapp/floor1.txt'),106,45,To_x,To_y,"floor1.png")
            n.solve()
            n.output_image()
            floor1=True
            floor2=True
            return render(request,'inmapapp/result.html',{'floor1':floor1,'floor2':floor2,'time':time.time()-then,'update':True})
            # print(From_x,From_y,To_x,To_y)
            
            # /home/sooraj/Documents/PROJECTS/INMAPWEB/inmapproject/inmapapp/static/inmapapp/map.txt
            # '/home/sooraj/Documents/PROJECTS/INMAPWEB/inmapproject/static/inmapapp/map.txt'
            # print("Maze:")
            # # m.print()
            # print("Solving...")
            # m.solve()
            # # print("States Explored:", m.num_explored)
            # # print("Solution:")
            # m.print()
            # m.output_image()
        now = time.time()   
        return render(request,'inmapapp/index.html',{'image':"inmapapp/result.png","time":now-then,"update":True})       
        
def result(request):
    return render(request,'inmapapp/result.html')

def sample(request):
    ans=""
    for sol in sols:
        ans+=f'''<div style="width:10px;height:10px;border:5px solid black;position: absolute;top: {sol[1]*4.2}px;left: {sol[0]*4.7}px;"> </div>'''
    return render(request,'inmapapp/sample.html',{"data":ans})
def test(request):
    From = request.POST.get('fromLocation')
    To = request.POST.get('To')
    FromMan = request.POST.get('manualFrom')
    ToMan = request.POST.get('manualTo')
    print(From,To)
    print(FromMan,ToMan)
    
    return render(request,'inmapapp/prev_index.html')