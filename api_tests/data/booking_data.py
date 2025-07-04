# first order
post_booking_data = {
    "firstname": "Liel1993",
    "lastname": "lol",
    "totalprice": 111,
    "depositpaid": 'true',
    "bookingdates": {
        "checkin": "2030-08-01",
        "checkout": "2030-08-07"
    },
    "additionalneeds": "Breakfast"
}
get_booking_data = {
    "firstname": "get_test",
    "lastname": "get",
    "totalprice": 111,
    "depositpaid": 'true',
    "bookingdates": {
        "checkin": "2033-08-01",
        "checkout": "2033-08-07"
    },
    "additionalneeds": "Breakfast"
}
# edit order
put_updated_data = {
    "firstname": "Test89",
    "lastname": "MyTest99",
    "totalprice": 1234,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2031-01-01",
        "checkout": "2032-01-10"
    },
    "additionalneeds": "Lunch"
}

delete_data = {
    "firstname": "del",
    "lastname": "delad",
    "totalprice": 234,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2031-01-01",
        "checkout": "2032-01-10"
    },
    "additionalneeds": "Lunch"
}

partial_data = {
    "firstname": "PartialTest",
    "lastname": "PartialUpdate",
    "totalprice": 999,

}

patch_data = {
    "firstname": "del",
    "lastname": "delad",
    "totalprice": 234,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2031-01-01",
        "checkout": "2032-01-10"
    },
    "additionalneeds": "Lunch"
}

