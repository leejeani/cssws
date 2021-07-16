from django.shortcuts import render

from db.dao.itemdb import ItemDB
from db.dao.userdb import UserDB
from db.frame.sqlitedao import SqliteDao
from db.vo.itemvo import ItemVO
from db.vo.uservo import UserVO

sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
udb = UserDB('shop');
idb = ItemDB('shop');

# Create your views here.
def home(request):
    return render(request, 'base.html')

def logout(request):
    if request.session['sessionid'] != None:
        del request.session['sessionid'];
    return render(request, 'base.html');

def login(request):
    context = {
        'section':'login.html'
    };
    return render(request, 'base.html',context);

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    # 1. 입력한  ID가 회원 가입 된  ID인지 검사
    # 2. 입력한 PWD가 회원 가입시 인력한 PWD와 동일한지 검사
    context = {};
    try:
        dbuser = udb.select(id);
        print(dbuser);
        if pwd == dbuser.getPwd():
            # session 에 사용자 정보를 넣는다.
            request.session['sessionid'] = id;
            # section 영역에 loginok.html 화면을 넣는다.
            context['section'] = 'loginok.html';
            context['loginuser'] = dbuser;
        else:
            raise Exception;
    except:
        # section 영역에 loginfail.html  화면을 넣는다.
        context['section'] = 'loginfail.html';
        print('Error....');
    return render(request, 'base.html',context);

def register(request):
    context = {
        'section':'register.html'
    };
    return render(request, 'base.html',context);

def registerimpl(request):
    id = request.GET['id'];
    pwd = request.GET['pwd'];
    name = request.GET['name'];
    # 회원 정보를 데이터베이스에 저장 한다.
    user = UserVO(id,pwd,name);
    udb.insert(user);
    print(id, pwd, name);
    # 회원 가입 완료 화면을 메인 화면 중앙에 표시
    context = {
        'section': 'registerok.html',
        'rname': name,
    };
    return render(request, 'base.html',context);

def html5(request):
    context = {
        'section':'html5.html'
    };
    return render(request, 'base.html',context);
def css3(request):
    context = {
        'section': 'css3.html'
    };
    return render(request, 'base.html',context);
def javascript(request):
    context = {
        'section': 'javascript.html'
    };
    return render(request, 'base.html',context);
def jquery(request):
    context = {
        'section': 'jquery.html'
    };
    return render(request, 'base.html',context);
def ajax(request):
    context = {
        'section': 'ajax.html'
    };
    return render(request, 'base.html',context);

def userdetail(request):
    # 요청하는 id 값을 추츨
    id = request.GET['id'];
    # 요청한 id 정보의 상세 정보를 조회
    user = udb.select(id);
    # 상세 화면으로 이동
    context = {
        'section': 'userdetail.html',
        'userdata': user
    };
    return render(request, 'base.html',context);

def userlist(request):
    # 사용자 정보를 모두 조회한다.
    users = udb.selectall();
    # 조회된 사용자 정보를 context 에 담아서 화면을 만들어 준다.
    context = {
        'section': 'userlist.html',
        'userlist': users
    };
    return render(request, 'base.html',context);

def additem(request):
    context = {
        'section': 'additem.html'
    };
    return render(request, 'base.html',context);

def additemimpl(request):
    name = request.GET['name'];
    price = int(request.GET['price']);
    item = ItemVO(0,name,price,'');
    idb.insert(item);
    context = {
        'section': 'additemok.html',
        'item'   : item,
    };
    return render(request, 'base.html',context);

def itemlist(request):
    items = idb.selectall();
    context = {
        'section': 'itemlist.html',
        'itemlist': items,
    };
    return render(request, 'base.html',context);

def itemdetail(request):
    id = int(request.GET['id']);
    item = idb.select(id);
    context = {
        'section': 'itemdetail.html',
        'itemdata': item,
    };
    return render(request, 'base.html',context);