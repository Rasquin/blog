{"filter":false,"title":"models.py","tooltip":"/posts/models.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":2,"column":26},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":20,"column":25},"action":"insert","lines":["from django.utils import timezone","","","class Post(models.Model):","    \"\"\"","    A single Blog post","    \"\"\"","    title = models.CharField(max_length=200)","    content = models.TextField()","    created_date = models.DateTimeField(auto_now_add=True)","    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)","    views = models.IntegerField(default=0)","    tag = models.CharField(max_length=30, blank=True, null=True)","    image = models.ImageField(upload_to=\"img\", blank=True, null=True)","","    def __unicode__(self):","        return self.title"],"id":3}],[{"start":{"row":20,"column":25},"end":{"row":21,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":12,"column":32},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":13,"column":5},"end":{"row":13,"column":139},"action":"insert","lines":[" auto_now_add = True, which means that as soon as the record is created, then the current date and time will be added into that field."],"id":6}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":139},"end":{"row":13,"column":139},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568397755387,"hash":"8a2d84dafe730bd7060bd270eccd7a788b34059e"}