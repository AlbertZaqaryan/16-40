from django.db import models

# Create your models here.


class HomeSliderActive(models.Model):

    name1 = models.CharField('SliderActive name1', max_length=60)
    name2 = models.CharField('SliderActive name2', max_length=60)
    text = models.TextField('SliderActive text')
    img1 = models.ImageField('SliderActive image1', upload_to='images')
    img2 = models.ImageField('SliderActive image2', upload_to='images')

    def __str__(self):
        return self.name1
    


class HomeSlider(models.Model):

    name1 = models.CharField('Slider name1', max_length=60)
    name2 = models.CharField('Slider name2', max_length=60)
    text = models.TextField('Slider text')
    img1 = models.ImageField('Slider image1', upload_to='images')
    img2 = models.ImageField('Slider image2', upload_to='images')

    def __str__(self):
        return self.name1
    

class Category(models.Model):

    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categ')
    name = models.CharField('Sub Category name', max_length=60)
    price = models.PositiveIntegerField('Sub Category price')
    img = models.ImageField('Sub Category images', upload_to='images')

    def __str__(self):
        return self.name