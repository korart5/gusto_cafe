from django.shortcuts import render

from django.http import HttpResponse

def main(request):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Korart</title>
    <link rel="shortcut icon" href="favicon.ico" type="ico">
</head>
<body>
    <style>
    #menu__toggle {
    opacity: 0;
  }
  /* стилизуем кнопку */
  .menu__btn {
    display: flex; /* используем flex для центрирования содержимого */
    align-items: center;  /* центрируем содержимое кнопки */
    position: fixed;
    top: 20px;
    left: 20px;
    width: 26px;
    height: 26px;
    cursor: pointer;
    z-index: 1;
  }
  /* добавляем "гамбургер" */
  .menu__btn > span,
  .menu__btn > span::before,
  .menu__btn > span::after {
    display: block;
    position: absolute;
    width: 100%;
    height: 2px;
    background-color: #616161;
  }
  .menu__btn > span::before {
    content: '';
    top: -8px;
  }
  .menu__btn > span::after {
    content: '';
    top: 8px;
  }
  /* контейнер меню */
.menu__box {
    display: block;
    position: fixed;
    visibility: hidden;
    top: 0;
    left: -100%;
    width: 300px;
    height: 100%;
    margin: 0;
    padding: 80px 0;
    list-style: none;
    text-align: center;
    background-color: #1c1d22;
    box-shadow: 1px 0px 6px rgba(0, 0, 0, .2);
  }
  /* элементы меню */
  .menu__item {
    display: block;
    padding: 12px 24px;
    color: #333;
    font-family: 'Roboto', sans-serif;
    font-size: 20px;
    font-weight: 600;
    text-decoration: none;
  }
  .menu__item:hover {
    background-color: #CFD8DC;
  }
  #menu__toggle:checked ~ .menu__btn > span {
    transform: rotate(45deg);
  }
  #menu__toggle:checked ~ .menu__btn > span::before {
    top: 0;
    transform: rotate(0);
  }
  #menu__toggle:checked ~ .menu__btn > span::after {
    top: 0;
    transform: rotate(90deg);
  }
  #menu__toggle:checked ~ .menu__box {
    visibility: visible;
    left: 0;
  }
  .menu__btn > span,
.menu__btn > span::before,
.menu__btn > span::after {
  transition-duration: .25s;
}
.menu__box {
  transition-duration: .25s;
}
.menu__item {
  transition-duration: .25s;
}
@import url("https://fonts.googleapis.com/css?family=Varela+Round");
html {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}

*,
*:before,
*:after {
  -webkit-box-sizing: inherit;
          box-sizing: inherit;
  padding: 0;
  margin: 0;
  letter-spacing: 1.1px;
}

body,
html {
  width: 100%;
  height: 100%;
  background: #1c1d22;
  font-family: "Varela Round", sans-serif;
}



.humani {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  max-width: 600px;
  height: 100%;
  margin: 0 auto;
}

.humani a {
  text-decoration: none;
  font-size: 25px;
  color: #ddd;
  position: relative;
  margin-bottom: 50px;
  -webkit-transition: all .2s;
  transition: all .2s;
  overflow: hidden;
}

.humani a:hover {
  color: #fff;
}

.humani a:last-child {
  margin-bottom: 0px;
}

.humani a::before {
  content: "";
  position: absolute;
  top: 0px;
  left: -100%;
  width: 100%;
  height: 100%;
  background: #eb2141;
  z-index: 99;
  -webkit-transition: all 0.4s cubic-bezier(0.7, 0, 0.3, 1);
  transition: all 0.4s cubic-bezier(0.7, 0, 0.3, 1);
}

.humani a:hover::before {
  left: 100%;
}

.humani a::after {
  content: "";
  position: absolute;
  top: 50%;
  margin-top: -2px;
  left: 100%;
  width: 100%;
  height: 4px;
  background: #eb2141;
  -webkit-transition: all .3s;
  transition: all .3s;
  -webkit-transition-delay: .4s;
          transition-delay: .4s;
}

.humani a:hover::after {
  left: 0%;
}

.videopos{
  justify-content: center;
  text-align: center;
  margin-top: 4%;
}
    </style>
    <div class="hamburger-menu">
        <input id="menu__toggle" type="checkbox" />
        <label class="menu__btn" for="menu__toggle">
          <span></span>
        </label>
        <ul class="menu__box">
          <div class='humani'>
            <a target="blank", href="https://pypl.github.io/PYPL.html">
              <span>Python</span>
            </a>
            <a target="blank", href="https://discord.com/">
              <span>Javascript, CSS, HTML</span>
            </a>
            <a target="blank", href="https://www.tiobe.com/">
              <span>С++, C, C#</span>
            </a>
            <a target="blank", href="https://www.youtube.com/">
              <span>Kotlin, Go, Swift</span>
            </a>
          </div>
        </ul>
      </div>
      <div class="videopos"><video src="El.mp4" controls="controls" >
    </video></div>
      
</body>
</html>
    """
    return HttpResponse(html)