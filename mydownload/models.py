from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField('主页标题', max_length=20)
    content = models.TextField('主页内容')
    class Meta:
        verbose_name="主页"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Fenlei(models.Model):
    name = models.CharField('分类', max_length=10)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Files(models.Model):
    fileName = models.CharField(max_length=80)
    fileLink = models.FileField(upload_to= 'upload')


    class Meta:
        verbose_name = '文件'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.fileName

class WenZhang(models.Model):
    fenlei = models.ForeignKey(Fenlei, on_delete=models.CASCADE, verbose_name='分类')
    fileLink = models.ForeignKey(Files, on_delete=models.CASCADE, verbose_name='文件')
    title = models.CharField('标题', max_length=30)
    content = models.TextField('内容')
    createTime = models.DateField('时间', auto_now_add=True)
    zzname = models.CharField('作者', max_length=12)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
