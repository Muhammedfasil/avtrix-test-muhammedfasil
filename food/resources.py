from import_export import resources

from .models import Foods

class FoodResource(resources.ModelResource):
    class Meta:
        model = Foods
        fields = ('id','order_date','region','city','category','product','quantity','unit_price')
