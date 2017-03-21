from flask import Flask, render_template, request
from flask import url_for
from scrape import tweets_a, tweets_b, tweets_c
from scrape import tweets_d, tweets_e, tweets_f
from scrape import tweets_g, tweets_h, tweets_i
from scrape import tweets_j, tweets_k, tweets_l
from scrape import tweets_m, tweets_n, tweets_o
from scrape import tweets_p

app = Flask(__name__)

@app.route('/')
def index():
    a = tweets_a()
    b = tweets_b()
    c = tweets_c()
    d = tweets_d()
    e = tweets_e()
    f = tweets_f()
    g = tweets_g()
    h = tweets_h()
    i = tweets_i()
    j = tweets_j()
    k = tweets_k()
    l = tweets_l()
    m = tweets_m()
    n = tweets_n()
    o = tweets_o()
    p = tweets_p()
    return render_template('fss.html', tweets_a=a, tweets_b=b, tweets_c=c,
    tweets_d=d, tweets_e=e, tweets_f=f, tweets_g=g, tweets_h=h, tweets_i=i,
    tweets_j=j, tweets_k=k, tweets_l=l, tweets_m=m, tweets_n=n, tweets_o=o, tweets_p=p,)

if __name__ == "__main__":
    app.run()
