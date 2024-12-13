from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 模拟数据库
users = []
jobs = [
    {'job_id': 1, 'title': '图书馆设计工程师', 'description': '负责图书馆的建筑设计工作', 'company': 'ABC公司'},
    {'job_id': 2, 'title': '图书馆施工监理', 'description': '负责图书馆施工现场的监理工作', 'company': 'XYZ公司'}
]

# 主页路由：角色选择页面
@app.route('/')
def home():
    return render_template('home.html')

# 用户注册页面：根据角色选择跳转
@app.route('/register', methods=['POST'])
def register():
    role = request.form['role']
    if role == '求职者':
        return redirect('/applicant')
    elif role == '招聘公司':
        return redirect('/company')
    elif role == '管理员':
        return redirect('/admin')
    else:
        return redirect('/')

# 求职者页面：浏览职位并申请
@app.route('/applicant')
def applicant():
    return render_template('applicant.html', jobs=jobs)

# 招聘公司页面：发布职位和查看申请
@app.route('/company')
def company():
    return render_template('company.html', jobs=jobs)

# 管理员页面：查看所有职位与用户信息
@app.route('/admin')
def admin():
    return render_template('admin.html', jobs=jobs, users=users)

# 求职者申请职位
@app.route('/apply', methods=['POST'])
def apply():
    job_id = request.form['job_id']
    user_info = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone']
    }
    users.append(user_info)  # 将用户信息保存到模拟数据库中
    return redirect('/applicant')  # 跳转到求职者页面

if __name__ == "__main__":
    app.run(debug=True)
