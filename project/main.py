import webbrowser
from configuration import *
import processing
import sys, traceback, os
import paths_
from typing import List, Dict, Union, Optional



from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from sqldb.dbs import *
from sqldb.user_ import *
import  short_full

'''
email='232@gmail.com'
getted_lendth, getted_users = user_get(email)
print('getted_users=',getted_users)
print('getted_lendth=',getted_lendth)
getted_user=getted_users[0]
print(getted_user[2])
input('222')

'''

''' 
import obtain
ans=obtain.go()
print(ans)
score=processing.go(ans)
user=User();
user.setpr(name='Dim',email='vvv@gmail.com',score= score);
user_add(user)
input('user added')
'''


BASE_PATH = paths_.Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
app = FastAPI(title="API")
app = FastAPI()
from fastapi.staticfiles import StaticFiles
staticfiles = StaticFiles(directory="templates")
folder = os.path.dirname(__file__)
app.mount("/templates", StaticFiles(directory="templates"), name="static2")

app.mount("/templates/particle", StaticFiles(directory="templates/particle"), name="static6")
app.mount("/templates/particle", StaticFiles(directory="templates/particle"), name="static3")
app.mount("/templates/particle", StaticFiles(directory="templates/particle"), name="static4")
app.mount("/templates/particle", StaticFiles(directory="templates/particle"), name="static5")
app.mount("/templates/particle", StaticFiles(directory="templates/particle"), name="static7")

app.state.ans={ }
app.state.user_name=''
app.state.user_email=''

print('before app')


#-------------------------------------------------------------------

@app.get("/")
def do_login (request: Request):
    # показывает страницу регистрации (ввод имя, email)
    title:str = expl
    step=1
    question = questions[step - 1]
    result_text = ''
    app.state.ans={ }
    return templates.TemplateResponse("login.html", {"request": request, "title": title, "question": question,"step": step,  "result_text": result_text})

#-------------------------------------------------------------------

@app.post("/")
def do_redirect (request: Request, name:str=Form(default="0"), email:str=Form(default="0"), ):
    # получает из формы данные (ввод имя, email)
    if email!='0':

        getted_lendth, getted_users = user_get(email)

        if getted_lendth>0:
            # если user уже в БД - берет из БД его результат и показывает
            getted_user = getted_users[0]
            title=f'{name}, Вы уже проходили тест... <br/>Ваш результат:<br/>'

            result_text=short_full.sf(getted_user[3])
            return templates.TemplateResponse("registed.html",
                                              {"request": request, "title": title,
                                               "result_text": result_text})


        else:
            # если user  нет в БД - идет в тест
            app.state.user_name=name
            app.state.user_email = email
            title=f'Вы зарегистрированы, {name} {email} !'
            result_text=f'''
    <form action="/quest" method="post">    
    <input type="hidden" id="step" name="step" value="0">
    <input type="submit" value="ПРОЙТИ ОПРОС ">
  </form>
            '''
            return templates.TemplateResponse("registed.html", {"request": request, "title": title,  "result_text": result_text})

#-------------------------------------------------------------------

@app.post("/quest")
def do_retrieve(request: Request, ans: str = Form(default="0"), step: int = Form(default=-1), ):
    # проход по всем вопросам теста
    app.state.ans[step] = ans
    step = step + 1
    print("step=", step, "len(questions)=",len(questions))
    if step>-1 and step<71 :
        print("/quest", app.state.user_name)
        print("/quest", app.state.user_email)
        print("/quest step", step )

        question = questions[step]
        title = "Вопрос"
        user=f'{app.state.user_name} ({app.state.user_email})'

        prev=''
        for key, value in app.state.ans.items():
            if  key>0:
                prev=prev+f'{key}({value}) '
        result_text='Ваши ответы:'+prev
        print("result_text= ",result_text)
        return templates.TemplateResponse("question.html", {"request": request, "title": title,"user": user, "question": question, "step": step, "result_text": result_text })

    elif step>3:
        # тест завершен, показ результата
        ans=app.state.ans
        print("ans1=", ans)
        score = processing.go(ans)
        print("result score=", score)
        user = User()
        user.setpr(name=app.state.user_name, email= app.state.user_email, score=score);
        user_add(user)
        print('user added')
        result_text = short_full.sf(score)

        title = f'Тест завершен. {app.state.user_name}, ваш результат ={score}'
        return templates.TemplateResponse("finished.html", {"request": request, "title": title,"result_text": result_text})

    else:
        return templates.TemplateResponse("finished.html", {"request": request, "title": 'ERROR', })


#-------------------------------------------------------------------

if __name__ == "__main__":
    print('before app if main')

    webbrowser.open('http://127.0.0.1:8001/', new=1, autoraise=True)
    webbrowser.open('http://127.0.0.1:8001/docs', new=1, autoraise=True)

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")





























