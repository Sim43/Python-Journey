from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def send_email(name, email, phone, message):
    message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ['EMAIL'], password=os.environ['PASSWORD'])
        connection.sendmail(from_addr=os.environ['EMAIL'], to_addrs=os.environ['EMAIL'], msg=message)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        send_email(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['message']
            )
        return render_template("contact.html", status=True)
    return render_template("contact.html", status=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
