# 导入fk_package包,实际就是导入包下的__init__.py文件
import fk_package
# 导入fk_package包下的print_shape模块
# 实际就是导入fk_package目录下的print_shape.py
import fk_package.print_shape
from fk_package import billing
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item( 5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)