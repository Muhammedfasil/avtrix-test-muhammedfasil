from rest_framework import serializers
from .models import Foods

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ('id','order_date','region','city','category','product','quantity','unit_price')