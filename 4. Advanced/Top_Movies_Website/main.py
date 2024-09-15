from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import requests

TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MzI4ZGUyYTVmOWQ2YWI0Yjc5YjU1OTliY2YyNzkwMCIsIm5iZiI6MTcyNjM5NzU3Mi43MjMyMjcsInN1YiI6IjY2ZTZiOWYzZTgyMTFlY2QyMmIwNzlhYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aa_bL7DchxYzBmXB9RaiY4tmvIMxq4qobT5hu9USgy0"
API_KEY = "8328de2a5f9d6ab4b79b5599bcf27900"
tmdb_url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
get_movie_url = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

    

class EditForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    review = StringField(label='Your Review', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField(label="Done")

class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    # Read
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = result.scalars().all()
        with app.app_context():
            for i in range(len(all_movies)):
                all_movies[i].ranking = len(all_movies) - i
            db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = EditForm()
    if form.validate_on_submit():
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
            movie_to_update.rating = request.form["rating"]
            movie_to_update.review = request.form["review"]
            db.session.commit() 
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            'query': request.form['title'].title()
        }
        response = requests.get(tmdb_url, headers=headers, params=params)
        return render_template("select.html", movies=response.json()['results'])
    return render_template("add.html", form=form)


@app.route("/find/<int:id>")
def find(id):
    if id:
        params = {"api_key": API_KEY, "language": "en-US"}
        response = requests.get(f"{get_movie_url}{id}", params=params)
        response = response.json()
        new_movie = Movie(
            year=response['release_date'][:4],
            title=response['title'],
            description=response['overview'],
            img_url=f"{MOVIE_DB_IMAGE_URL}{response['poster_path']}",
        )
        with app.app_context():
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
