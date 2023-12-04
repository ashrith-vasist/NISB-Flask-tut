from flask import Flask,render_template

app=Flask(__name__)
posts=[
    {
        'title':'Apple Iphone16 launch',
        'desc':'Cost infinity'
    },
    {
        'title':'Antriksh',
        'desc':'New CEO of Apple'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',page='home')


@app.route('/profile')
def profile():
    return render_template('profile.html',page='profile')

@app.route('/news')
def news():
    return render_template('news.html',page='news', posts = posts)

if __name__=='__main__':
    app.run(debug=True)