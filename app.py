from fileinput import isfirstline
from urllib import response
from flask import Flask,render_template,Response
from camera import showVideo
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return'Hello,World!'

@app.route('/index')
def load_index():
    return render_template('index.html')

#### exercise programs ####
@app.route('/bodybuilding-program')  
def load_bodybuilding_program():
    return render_template('bodybuilding-program.html')
    


@app.route('/staminabuilding-program')   
def load_overallworkout_program():
    return render_template('staminabuilding-program.html')

@app.route('/overallworkout-program')   
def load_staminabuilding_program():
    return render_template('overallworkout-program.html')

#### squats start #####
@app.route('/squats')
def loadsquat():   
    embedid_video="https://www.youtube.com/embed/LGsLB4RqiTY"

    exercisetype="/squatvideo"
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/squatvideo')
def squatvideo():
    mode='squats'
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame')
##### squats end ####

### tricep start #####
@app.route('/tricep')
def loadtricep():   
    embedid_video="https://www.youtube.com/embed/FqLa4rILR_c"
    exercisetype="/tricepvideo "
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/tricepvideo')
def tricepvideo():
    mode='tricep'
   
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame')
##### tricep end #####

##### jumping jack start ####
@app.route('/jumping_jack')
def loadjumping_jack():   
    embedid_video="https://www.youtube.com/embed/vd1s5_ywXgY" 
    exercisetype="/jumping_jackvideo"
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/jumping_jackvideo')
def jumping_jackvideo():
    mode='jumping_jack'
   
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame')
#### jumping jack end ####

#### bicep curls start ####
@app.route('/bicep_curls')
def loadbicep_curls():   
    embedid_video="https://www.youtube.com/embed/9t0I73kg7ho" 
    exercisetype="/bicep_curlsvideo"
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/bicep_curlsvideo')
def bicep_curlsvideo():
    mode='bicep_curls'
   
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame')  
#### bicep curls end######

#### pushup start #####
@app.route('/pushup')
def loadpushup():   
    embedid_video="https://www.youtube.com/embed/n9kfxT-ttjA" 
    exercisetype="/pushupvideo"
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/pushupvideo')
def pushupvideo():
    mode='pushup'
   
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame') 

### PUSHUP END ###

#### pullup start #####
@app.route('/pullup')
def loadpullup():   
    embedid_video="https://www.youtube.com/embed/qHsxfz1Pf0A" 
    exercisetype="/pullupvideo"
    return render_template('exercise.html',embedid_video=embedid_video,exercisetype=exercisetype)

@app.route('/pullupvideo')
def pullupvideo():
    mode='pullup'
   
    return Response(gen(showVideo(),mode),
    mimetype='multipart/x-mixed-replace; boundary=frame') 
### pullup end###

#### genratng camera start ######
def gen(camera,mode):
    camera.makecount_zero()
    while True:
        
        frame=camera.get_frame(mode)
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(showVideo()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)


