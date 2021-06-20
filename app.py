import bdb # 내가 만든 데이터베이스 함수들

app = Flask(__name__)
app.secret_key = b'aaa!111/'


@app.route('/')
def index():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        # 전달된 값을 그대로 db에 저장
        bdb.insert_data(email, pwd)
        return '회원가입 데이터(POST)'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        # 만약에 이메일과 패스워드 같다면
        # if email == 'a@a.com' and pwd == '1234':
        ret = bdb.get_emailpw(email, pwd)
        print(ret)
        # 로그인 성공
        if ret != 'None':
            session['email'] = email
            return "로그인 성공"
        # 아니면
        else:
        # 아이디 패스워드 확인
            return "아이디 패스워드 확인"
    

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        return '회원가입 데이터(POST)'

@app.route('/naver')
def naver():
    if 'email' in session:   # 로그인 상태값(세션) 체크
        return render_template("naver.html")  # 네이버 검색 페이지 사용
    else:
        return redirect('/login')  # 로그인 페이지로 강제 이동

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        search = request.form['fname']
        print("전달된값:", search)
        return '당신이 검색한 키워드(POST)<br>{}입니다'.format(search)


if __name__ == '__main__':
    app.run()