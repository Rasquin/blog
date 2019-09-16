{"filter":false,"title":"settings.py","tooltip":"/blog/settings.py","undoManager":{"mark":53,"position":53,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":19},"action":"insert","lines":["''"],"id":2}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":85},"action":"insert","lines":["b801b31df957443fa2d6605807f5594d.vfs.cloud9.us-east-1.amazonaws.com"],"id":3}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":5}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["p"],"id":6},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["o"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["s"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["t"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":57,"column":16},"end":{"row":57,"column":18},"action":"remove","lines":["[]"],"id":7},{"start":{"row":57,"column":16},"end":{"row":57,"column":53},"action":"insert","lines":["[os.path.join(BASE_DIR, 'templates')]"]}],[{"start":{"row":64,"column":70},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":65,"column":0},"end":{"row":65,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":65,"column":16},"end":{"row":65,"column":59},"action":"insert","lines":["'django.template.context_processors.media',"],"id":9}],[{"start":{"row":121,"column":23},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":122,"column":0},"end":{"row":123,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":123,"column":0},"end":{"row":127,"column":44},"action":"insert","lines":["STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":11}],[{"start":{"row":121,"column":23},"end":{"row":123,"column":23},"action":"remove","lines":["","","STATIC_URL = '/static/'"],"id":12}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":28},"action":"insert","lines":["'django_forms_bootstrap'"],"id":14}],[{"start":{"row":39,"column":28},"end":{"row":39,"column":29},"action":"insert","lines":[","],"id":15}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":[","],"id":16}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":13,"column":0},"end":{"row":16,"column":14},"action":"insert","lines":["import dj_database_url","","if os.path.exists('env.py'):","    import env"],"id":18}],[{"start":{"row":26,"column":13},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":41},"action":"insert","lines":["os.environ.get(\"SECRET_KEY\")"],"id":20}],[{"start":{"row":27,"column":1},"end":{"row":27,"column":53},"action":"remove","lines":["'k2puhx7)p^=78l&p!lm^9vqy%hqiyel)#i(d-2b8hhzt&g71m1'"],"id":21}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"remove","lines":["#"],"id":22}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":1},"action":"insert","lines":["#"],"id":23}],[{"start":{"row":84,"column":0},"end":{"row":84,"column":1},"action":"insert","lines":["#"],"id":24}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"insert","lines":["#"],"id":25}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":1},"action":"insert","lines":["#"],"id":27}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"insert","lines":["#"],"id":28}],[{"start":{"row":88,"column":2},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":89,"column":0},"end":{"row":92,"column":0},"action":"insert","lines":["DATABASES = {","    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","}",""],"id":30}],[{"start":{"row":55,"column":61},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":49},"action":"insert","lines":["'whitenoise.middleware.WhiteNoiseMiddleware',"],"id":32}],[{"start":{"row":133,"column":55},"end":{"row":134,"column":0},"action":"insert","lines":["",""],"id":33}],[{"start":{"row":134,"column":0},"end":{"row":134,"column":44},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":34}],[{"start":{"row":92,"column":1},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":36}],[{"start":{"row":93,"column":0},"end":{"row":105,"column":0},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {","        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","    }","else:","    print(\"Postgres URL not found, using sqlite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }",""],"id":37}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"insert","lines":["#"],"id":38}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["#"],"id":39}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["#"],"id":40}],[{"start":{"row":32,"column":86},"end":{"row":32,"column":87},"action":"insert","lines":[","],"id":41}],[{"start":{"row":32,"column":87},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":42}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "],"id":43}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"insert","lines":["    "],"id":44}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":12},"action":"insert","lines":["    "],"id":45}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":16},"action":"insert","lines":["    "],"id":46}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":20},"action":"insert","lines":["    "],"id":47}],[{"start":{"row":33,"column":20},"end":{"row":33,"column":64},"action":"insert","lines":["https://blog-test-rasquin-app.herokuapp.com/"],"id":48}],[{"start":{"row":33,"column":64},"end":{"row":33,"column":66},"action":"insert","lines":["''"],"id":49}],[{"start":{"row":33,"column":64},"end":{"row":33,"column":66},"action":"remove","lines":["''"],"id":50}],[{"start":{"row":33,"column":64},"end":{"row":33,"column":66},"action":"insert","lines":["''"],"id":51}],[{"start":{"row":33,"column":65},"end":{"row":33,"column":66},"action":"remove","lines":["'"],"id":52}],[{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["'"],"id":53}],[{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["h"],"id":54},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["t"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["t"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["p"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["s"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":[":"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["/"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["/"]}],[{"start":{"row":33,"column":21},"end":{"row":33,"column":57},"action":"remove","lines":["blog-test-rasquin-app.herokuapp.com/"],"id":55}],[{"start":{"row":33,"column":21},"end":{"row":33,"column":56},"action":"insert","lines":["blog-test-rasquin-app.herokuapp.com"],"id":56}]]},"ace":{"folds":[],"scrolltop":348.79998779296875,"scrollleft":0,"selection":{"start":{"row":33,"column":58},"end":{"row":33,"column":58},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"state":"start","mode":"ace/mode/python"}},"timestamp":1568662800475,"hash":"c1e9c910dbf5ec15dfae962a015e0bd92008bf16"}