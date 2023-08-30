from django.db import models


# Create your models here.
class GoodsCategory(models.Model):
    # class Meta():
    #     db_table = 'goodscategory'
    #     verbose_name = '商品类型'
    """产品分类"""
    name = models.CharField(max_length=64, verbose_name='名称')
    remark = models.CharField(max_length=256, null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name


class Goods(models.Model):
    # class Meta():
    #     db_table = ''
    """产品"""
    number = models.CharField(max_length=32, verbose_name='编号')
    name = models.CharField(max_length=64, verbose_name='名称')
    barcode = models.CharField(max_length=32, null=True, blank=True, verbose_name='条码')
    category = models.ForeignKey(GoodsCategory, on_delete=models.SET_NULL, null=True, related_name='goods_set',
                                 verbose_name='产品分类')
    spec = models.CharField(max_length=64, null=True, blank=True, verbose_name='规格')
    shelf_life_days = models.IntegerField(null=True, verbose_name='保质期天数')
    purchase_price = models.FloatField(default=0, verbose_name='采购价')
    retail_price = models.FloatField(default=0, verbose_name='零售价')
    remark = models.CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    # 返回字符串
    def __str__(self):
        return self.name


