from flask import Flask, render_template,request,redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import asyncio
from im import img


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://kwssykuhixsvbw:033b3a1ce45215ffb610033d3cbfa58a08b32e7a673c73821a5080c56bae0cc0@ec2-54-164-22-242.compute-1.amazonaws.com:5432/dqkleovt9di82'
db = SQLAlchemy(app)


class Painter(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/home', methods=['POST', 'GET'])
def index():
    db.create_all ()
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Painter(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
    # Through link
            import requests
            r = requests.post(
                "https://api.deepai.org/api/colorizer",
                data={
                    'image': {task_content},
                },
                headers={'api-key': 'd98c8a77-a695-42a1-8f50-c08bb46509e1'}
            )

            res = r.json()
            output = res['output_url']
            
            tasks = Painter.query.order_by(Painter.date_created).all()
            return render_template('index.html',tasks=tasks,output=output)
        except:
            return ' ERROR !!'
    else:
        tasks = Painter.query.order_by(Painter.date_created).all()
        return render_template("index.html",tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Painter.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/home')
    except:
        return 'Not deleted'

@app.route('/',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        return redirect('/home')
        
    return render_template('signin.html')



if __name__ =="__main__":
    app.run(debug=True)
