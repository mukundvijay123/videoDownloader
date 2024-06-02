from flask import Flask,render_template,request,flash,redirect,url_for
from utils import create_profile,get_profile,get_url_metadata,check_profile_integrity,download_video
from time import sleep
import threading
import webbrowser



app=Flask(__name__)
app.secret_key = 'your_secret_key_here'




@app.route('/create_profile',methods=['GET'])
def create_profile_func():
    return render_template('profile.html')




@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    def_dest=request.form['default_destination']
    temp_dest=request.form['temporary_destination']
    create_profile(name,def_dest,temp_dest)
    return render_template('submit.html')


@app.route('/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        vid_format = request.form['format']
        if not check_profile_integrity():
            '''
            error flashing that path isnt correct here
            '''
            return redirect(url_for('create_profile_func'))
        media,metadata=get_url_metadata(url)
        if media=='video':
            print(metadata)
            profile_dict=get_profile()
            t1=threading.Thread(target=download_video,args=(url,profile_dict['default_dest'], vid_format,))
            t1.start()
            return render_template('downloading.html')
        elif media=='playlist':
            pass
        else:
            return render_template('invalid_url.html')
    else:
        return render_template('download_form.html')


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__=='__main__':
    threading.Timer(1,open_browser).start()
    app.run()
