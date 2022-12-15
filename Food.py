
food_list = ['Aalu Ki Sabji','Chana Dal','Chhaina','Chhole','Curry','Dahi','Dal','Fried Rice','Gulab Jamun','Mix Veg','Paneer','Plate','Puri','Rice','Roti','Salad','Zeera Aalu']


##The calorie_per_sq_inch is calculated by using the calories contained in one plate of size 12 inch diameter
##for eg if a plate full of 12" pizza has the calories of approx 1200 it has 1200/113 calories per sq inch
calorie_per_sq_inch={'Aalu Ki Sabji':0.75,'Chana Dal':2.15,'Chhole':2.56,'Curry':0.92,'Dahi':0.83,'Dal':1.9,'Fried Rice':1.4,'Mix Veg':1.1,'Paneer':2.55,'Puri':0.61,'Rice':1.11,'Roti':0.7,'Salad':0.23,'Zeera Aalu':1.02}
calorie_per_unit={'Chhaina':106,'Gulab Jamun':153}


def get_calorie(class_name,real_food_area):
    if class_name in calorie_per_unit:
        return calorie_per_unit[class_name]
    else:
        return calorie_per_sq_inch[class_name]*real_food_area
