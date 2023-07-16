#Импорт
from flask import Flask, render_template, request
from time import sleep


app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')
#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    file = open('form.txt', 'w', encoding="utf-8")

#    with open('form.txt', 'w', encoding="utf-8") as f:
    file.write(name + '\n')
    print('Name written! ' + name)
    sleep(0.1)
    file.write(email + '\n')
    print('Email written! ' + email)
    sleep(0.1)
    file.write(address + '\n')
    print('Address written! ' + address)
    sleep(0.1)
    file.write(date + '\n')
    print('Date written! '  + date)
    sleep(0.1)
    file.close()                

    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           email=email,
                           date=date,
                           address=address,
                           )

app.run(debug=True)
