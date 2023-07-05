import imgkit
from jinja2 import Template

# HTML template
template = Template('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700&family=Roboto:wght@400;700&display=swap');
      body {
        padding: 0;
        margin: 0;
        background-color: #f7f7f7;
        font-family: Arial, sans-serif;
        text-align: center;
      }
      .book-cover {
/*        margin: 50px auto;*/
        /*width: 686px;
        height: 379px;*/
        width: 1920px;
        height: 1080px;
        background-color: #fff;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: center;
        align-items: center;
        display: flex;
      }
      .book-cover img {
        width: 80%;
        height: auto;
      }
      .book-details {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        margin: 3rem 0;
      }
      body {
        background-color: #F5F5F5;
      }

.frame {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 1080px;
  flex: 0.4;
  margin: 0 auto;
}

.book-container {
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 2000px;
  margin-top: 100px;
  margin-bottom: 100px;
  width: 80%;
  height: auto;
  margin-left: auto;
  margin-right: 25%;

}

.book-image {
  max-width: 900px;
  height: auto;
  position: relative;
  z-index: 100;
}


@keyframes initAnimation {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(-30deg);
  }
}

.book {
  width: 500px;
  height: 800px;
  position: relative;
  transform-style: preserve-3d;
  transform: rotateY(-30deg);
}


.book > :first-child {
  position: absolute;
  top: 0;
  left: 0;
  background-color: red;
  width: 500px;
  height: 800px;
  transform: translateZ(25px);
  background-color: #01060f;
  border-radius: 0 2px 2px 0;
  box-shadow: 5px 5px 20px #666;
}

.book::before {
  position: absolute;
  content: ' ';
  background-color: blue;
  left: 0;
  top: 3px;
  width: 48px;
  height: 100%;
  transform: translateX(470px) rotateY(90deg);
  background: linear-gradient(40deg, 
    #fff 0%,
    #f9f9f9 5%,
    #fff 10%,
    #f9f9f9 15%,
    #fff 20%,
    #f9f9f9 25%,
    #fff 30%,
    #f9f9f9 35%,
    #fff 40%,
    #f9f9f9 45%,
    #fff 50%,
    #f9f9f9 55%,
    #fff 60%,
    #f9f9f9 65%,
    #fff 70%,
    #f9f9f9 75%,
    #fff 80%,
    #f9f9f9 85%,
    #fff 90%,
    #f9f9f9 95%,
    #fff 100%
    );
}

.book::after {
  position: absolute;
  top: 0;
  left: 0;
  content: ' ';
  width: 500px;
  height: 800px;
  transform: translateZ(-25px);
  background-color: #01060f;
  border-radius: 0 2px 2px 0;
  box-shadow: -10px 0 50px 10px #666;
}
.left {
  flex: 0.6;
  height: 100%;
}
.txt-yellow {
  color: #FF7A00;
}
.company {
  font-family: 'Cairo', sans-serif;
  font-weight: 700;
  font-size: 40px;
}
.desc {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  font-size: 100px;
}
.title {
  font-family: 'Robot', sans-serif;
  font-weight: 400;
  font-size: 100px;
}
.author {
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  font-size: 50px;
  margin-top: -8px;
}
    </style>
  </head>
  <body>
    <div class="book-cover">
      <div class="left">        
        <div class="book-details">
          <p class="company"><span class="txt-yellow">Snap</span>Tale</p>
          <h1 class="desc">Free AudioBook <span class="txt-yellow">Summary</span></h1>
          <h1 class="title">{{title}}</h1>
          <p class="author">by {{author}}</p>
        </div>
      </div>
      <div class="frame">
        <div class="book-container">
          <div class="book">
            <img
              class="book-image"
              alt="book-cover"
              src="{{image}}"
            />
          </div>
        </div>
      </div>
    </div>

  </body>
</html>
''')

# Parameters
title = "The Great Gatsby"
author = "F. Scott Fitzgerald"
image = "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1599569204i/55051662.jpg"

# Render HTML template
html = template.render(title=title, author=author, image=image)

# Generate image
imgkit.from_string(html, 'book_cover.jpg', options={'width': 1920, 'height': 1080})
