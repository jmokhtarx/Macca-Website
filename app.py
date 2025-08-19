from flask import Flask, render_template

app = Flask(__name__)

# بيانات المشاريع
projects_data = {
    1: {
        "name": "بالي",
        "location": "الجونة",
        "images": [
            "images/projects/paly.png"
        ],
        "description": """
        <h2>المرحلة الأولى</h2>

        <div class="project-stage">
            <h4>1- تعديل خرسانه مبني F</h4>
            <div class="images-grid">
                <img src='/static/images/baly/1.png'>
                <img src='/static/images/baly/2.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>2- أعمال مبانى و بياض و تأسيس و تشطيب كهرباء و سباكة مبنى F</h4>
            <div class="images-grid">
                <img src='/static/images/baly/3.png'>
                <img src='/static/images/baly/4.png'>
                <img src='/static/images/baly/5.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>3- حفر و أعمال الخرسانات لمبنى C2</h4>
            <div class="images-grid">
                <img src='/static/images/baly/6.png'>
                <img src='/static/images/baly/7.png'>
                <img src='/static/images/baly/8.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>4- أعمال تشطيب مبنى C2</h4>
            <div class="images-grid">
                <img src='/static/images/baly/9.png'>
                <img src='/static/images/baly/10.png'>
                <img src='/static/images/baly/11.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>5- خراسانات و مبانى السور الخارجى للمشروع</h4>
            <div class="images-grid">
                <img src='/static/images/baly/12.png'>
                <img src='/static/images/baly/13.png'>
                <img src='/static/images/baly/14.png'>
                <img src='/static/images/baly/15.png'>  
            </div>
        </div>

        <div class="project-stage">
            <h4>6- حفر و صب خزان المياه والصرف</h4>
            <div class="images-grid">
                <img src='/static/images/baly/16.png'>
                <img src='/static/images/baly/17.png'>
                <img src='/static/images/baly/18.png'>
                <img src='/static/images/baly/19.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>7- أعمال تعديلات العملاء وتسليم الوحدات</h4>
            <div class="images-grid">
                <img src='/static/images/baly/20.png'>
                <img src='/static/images/baly/21.png'>
                <img src='/static/images/baly/22.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>8- أعمال الموقع العام وتشطيب البوابة الرئيسية</h4>
            <div class="images-grid">
                <img src='/static/images/baly/23.png'>
                <img src='/static/images/baly/24.png'>
                <img src='/static/images/baly/25.png'>
                <img src='/static/images/baly/26.png'>
                <img src='/static/images/baly/27.png'>
            </div>
        </div>

        <h2>المرحلة الثانيه</h2>

        <div class="project-stage">
            <h4>1- أعمال إزالة الأسوار القديمة بطول 250 متر و الحفر أسفلها لأنشاء حوائط خراسانية بطابع بالى</h4>
            <div class="images-grid">
                <img src='/static/images/baly/28.png'>
                <img src='/static/images/baly/29.png'>
                <img src='/static/images/baly/30.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>2- حفر و أعمال الخرسانات و مبانى لبلوك ال G   بإجمالى 2700 متر مسطح. </h4>
            <div class="images-grid">
                <img src='/static/images/baly/31.png'>
                <img src='/static/images/baly/32.png'>
                <img src='/static/images/baly/33.png'>
                <img src='/static/images/baly/34.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>3-  حفر و أعمال الخرسانات و مبانى لبلوك ال C3   بإجمالى 1050 متر مسطح.  </h4>
            <div class="images-grid">
                <img src='/static/images/baly/35.png'>
                <img src='/static/images/baly/36.png'>
            </div>
        </div>

        
        """
    },
       
    
    2: {
        "name": "كمبوند ستون ريزيدنس",
        "location": "التجمع الخامس",
        "images": [
            "images/projects/ston.png",  # هتحط الصورة دي في static/images/projects
        ],
        "description":"""
        <div class="project-stage"><div class="project-stage">
            <h4>3-  خراسانات و مبانى و تشطيب البوابة الرئيسية للمشروع.   </h4>
            <div class="images-grid">
                <img src='/static/images/baly/64.png'>
                <img src='/static/images/baly/65.png'>
            </div>
        </div>
        """
       
    },
    3: {
        "name": " جبال السخنة ",
        "location": " العين السخنه",
        "images": [
            "images/projects/so5na.png",  
        ],
        "description":"""

        <div class="project-stage">
            <h4>1-   تنفيذ خراسانات 5 وحدات شاليهات بواقع مجموع 40 شاليه.   </h4>
            <div class="images-grid">
                <img src='/static/images/baly/37.png'>
                <img src='/static/images/baly/38.png'>
            </div>
        </div>
        """
       
    },
    4: {
        "name": " فيلا سكنية",
        "location": " الشيخ زايد ",
        "images": [
            "images/projects/zayed.png",  
        ],
        "description":"""
        

        """
       
    },
    5: {
        "name": " هرم سيتي ",
        "location": " اكتوبر  ",
        "images": [
            "images/projects/haram.png",  # هتحط الصورة دي في static/images/projects
        ],
        "description":"""
        <div class="project-stage">
            <h4>1-  أعمال اعادة ترميم و تدعيم عدد 47 بلاطة خرسانية باجمالى 1500 متر.</h4>
            <div class="images-grid">
                <img src='/static/images/baly/40.png'>
                <img src='/static/images/baly/41.png'>
                <img src='/static/images/baly/42.png'>
                <img src='/static/images/baly/43.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>2- أعمال تشطيبات و بياض و تأسيس و تشطيب كهرباء و سباكة لعدد 124 شقة سكنية و عمل أبواب داخلية و خارجية و أعمال الرخام و الشبابيك الخشبية. </h4>
            <div class="images-grid">
                <img src='/static/images/baly/44.png'>
                <img src='/static/images/baly/45.png'>
                <img src='/static/images/baly/46.png'>
                <img src='/static/images/baly/47.png'>
            </div>
        </div>
        
        <div class="project-stage">
            <h4>3-  أعمال انترلوك باجمالى 70,000 متر مسطح.</h4>
            <div class="images-grid">
                <img src='/static/images/baly/48.png'>
                <img src='/static/images/baly/49.png'>
                <img src='/static/images/baly/50.png'>
                <img src='/static/images/baly/51.png'>
                <img src='/static/images/baly/52.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>4- أعمال ترميم و عزل عدد 62 قبة. </h4>
            <div class="images-grid">
                <img src='/static/images/baly/53.png'>
                <img src='/static/images/baly/54.png'>
                <img src='/static/images/baly/55.png'>
                <img src='/static/images/baly/56.png'>
                <img src='/static/images/baly/57.png'>
            </div>
        </div>

        <div class="project-stage">
            <h4>5-أعمال مبانى و بياض و تأسيس و تشطيب كهرباء و سباكة و عمل أبواب داخلية و خارجية و تركيب تكيفيات و البوابات الاليكترونية و أعمال الرخام و سيكوريت و أعمال الالوميتال للشبابيك و الأبواب و فيوتيك خشبى للأسقف. للبوابات الرئيسية للمدينة  </h4>
            <div class="images-grid">
                <img src='/static/images/baly/58.png'>
                <img src='/static/images/baly/59.png'>
                <img src='/static/images/baly/60.png'>
                <img src='/static/images/baly/61.png'>
                <img src='/static/images/baly/62.png'>
                <img src='/static/images/baly/63.png'>
            </div>
        </div>

        """
       
    },
    6: {
        "name": " فيلا سكنية  ",
        "location": " حدايق الاهرام  ",
        "images": [
            "images/projects/hadayekalahram.png",  # هتحط الصورة دي في static/images/projects
        ],
       
    },
    7: {
        "name": "  مكتب مبيعات نيو سيتي  ",
        "location": " المهندسين   ",
        "images": [
            "images/projects/new_city.png",  # هتحط الصورة دي في static/images/projects
        ],
        "description":"""

        <div class="project-stage">
            <h4>1- ترميم و تأسيس كهرباء و صرف تكيفيات و تركيب التكيفيات و اعمال بياض و نقاشة و اعمال سيكوريت و ديكورات خشبية و أعمال سقف معلق و و تركيب HDF  للأرضيات و أعمال رخام فى مكتب المبيعات الخاص بشركة نيو سيتى.</h4>
            <div class="images-grid">
                <img src='/static/images/baly/66.png'>
                <img src='/static/images/baly/67.png'>
                <img src='/static/images/baly/68.png'>
                <img src='/static/images/baly/69.png'>
                <img src='/static/images/baly/70.png'>
            </div>
        </div>
        """
        
       
    },
    8: {
        "name": "  كمبوند وي جيت   ",
        "location": " 6 اكتوبر   ",
        "images": [
            "images/projects/wget.png",  # هتحط الصورة دي في static/images/projects
        ],
       
    },
    9: {
        "name": "  كمبوند الهضبة   ",
        "location": " 6 اكتوبر   ",
        "images": [
            "images/projects/hadaba.png",  # هتحط الصورة دي في static/images/projects
        ],
       
    },
    10: {
        "name": "  مشروع جاري    ",
        "location": " النوبة",
        "images": [
            "images/projects/.png",  # هتحط الصورة دي في static/images/projects
        ],
       
    }


    
    # تقدر تزود مشاريع تانية بنفس الشكل
}

@app.route('/team')
def team():
    team_members = [
        {
            "name": " محمود حسين",
            "role": "رئيس مجلس الإدارة",
            "image": "images/team/member1.jpg",
            "bio": "خبرة أكثر من 15 سنة في مجال المقاولات وإدارة المشاريع."
        },
        {
            "name": "م.سامح عبدالعزيز",
            "role": "مدير المشروعات",
            "image": "images/team/member2.jpg",
            "bio": "متخصص في التخطيط والإشراف على المشاريع الإنشائية."
        },
        {
            "name": "محمد جمال",
            "role": "مدير عام",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "عمرو زغلول",
            "role": "مدير اداري",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "محمود منصور",
            "role": "مدير حسابات",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "م.أحمد رفعت ",
            "role": "مدير مشروع بالي",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "م.سامية حماد",
            "role": "مهندسة مكتب فني اول ",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "م.نيرفانا محمد",
            "role": "مهندسة مكتب فني",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "م.عبدالرحمن مصطفى",
            "role": "مدير تنفيذي ترميم",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "اسلام جمال",
            "role": "م تنفيذ",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "محمد حمدي",
            "role": "مشرف اول",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "مصطفى حسين",
            "role": "مشرف",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "اشرف عويس",
            "role": "محاسب اول",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "احمد الشرقاوي ",
            "role": "مدير مشتريات",
            "image": "images/team/member3.jpg",
            "bio": ""
        },
        {
            "name": "هاجر محمد ",
            "role": "محاسبة",
            "image": "images/team/member3.jpg",
            "bio": ""
        }
        
    ]
    return render_template('team.html', team_members=team_members)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')



@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_data)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = projects_data.get(project_id)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)