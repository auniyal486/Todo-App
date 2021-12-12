from __init__ import db,create_app,bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from forms import Signupform, LoginForm
from flask import redirect, url_for,render_template,flash,request,Blueprint
from models import User,Post

routes = Blueprint('routes', __name__)

@routes.route("/",methods=['GET','POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    reg_form=Signupform()
    login_form=LoginForm()
    if reg_form.validate_on_submit():
        user = User.query.filter_by(email=reg_form.email.data).first()
        if user:
            flash("That email is taken. Please choose a different one.")
            return redirect(url_for('routes.index'))
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode('utf-8')
        user = User(first_name=reg_form.first_name.data, last_name=reg_form.last_name.data,email=reg_form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user,remember=reg_form.remember)
        flash('Account has been created')
        return redirect(url_for('routes.home'))
    elif login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            flash('Login Successful')
            return redirect(url_for('routes.home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
            return redirect(url_for('routes.index'))
    return render_template("index.html",reg_form=reg_form,login_form=login_form)

@routes.route('/home',methods=['GET','POST'])
@login_required
def home():
    if(request.method=="POST"):
        task=request.form["Task"]
        desc=request.form["Description"]
        obj=Post(user_email=current_user.email,task=task,description=desc)
        db.session.add(obj)
        db.session.commit()
        flash("Task has been added")
        return redirect(url_for("routes.home"))
    todo=Post.query.filter_by(user_email=current_user.email).all()
    return render_template("home.html",all_todo=todo,current_name=current_user.first_name)

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@routes.route("/update/<int:id>",methods=["POST","GET"])
@login_required
def updated(id):
    todo=Post.query.get_or_404(id)
    if(request.method=="POST"):
        desc=request.form["Description"]
        todo.description=desc
        db.session.commit() 
        flash("Task has been updated")
        return redirect(url_for("routes.home"))
    return render_template("update.html",todo=todo,current_name=current_user.first_name)
    

@routes.route("/delete/<int:id>")
@login_required
def delete(id):
    todo=Post.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash("Task has been deleted")
    return redirect(url_for("routes.home"))

app = create_app() 
if __name__ == '__main__':
    app.run(debug=False) 