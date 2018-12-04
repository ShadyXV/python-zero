def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
  price = 0
  offset = 0.000001
  # a little pinch of this
  price += num_of_bedrooms * offset
  # and a big pinch of that
  price += sqft * offset
  # maybe a handful of this
  price += neighborhood * offset
  # and finally, just a little extra salt for good measure
  price += offset
  return price

print(estimate_house_sales_price(3, 2000, 250000))
print(estimate_house_sales_price(2, 800, 300000))
print(estimate_house_sales_price(2, 850, 150000))
print(estimate_house_sales_price(1, 550, 78000))
print(estimate_house_sales_price(4, 2000, 150000))