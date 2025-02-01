# prices = ["$9.99", "$15.99", "$15.99", "$29.99", "$49.99"]
# emp_list = []
# for p in prices:
#     emp_list.append(float(p[1:]))
#
# print(type(emp_list[1]))
# print(emp_list)
#
# print(sorted(emp_list))
#
# print(list(reversed(emp_list)))




list = [49, 29, 15, 30, 15, 9]

for i in list:
    if i in [29,66] :
        print("pass")
    else:
        print("noo")





 def remove_item_from_cart(self):
        self.product_add_cart()
        self.remove_text = self.get_text(self.REMOVE_TEXT_ID)
        self.do_click(self.click_on_cart_css)
        self.do_click(self.REMOVE_TEXT_ID)
        self.driver.back()
        self.add_cart_button = self.get_text(self.ADD_TO_CART_BUTTON_ID)






