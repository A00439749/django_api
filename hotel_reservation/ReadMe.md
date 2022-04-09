DJANGO API PROJECT

HOW TO RUN:

* Install `django` and `djangorestframework` using `pip` command.
* Once the dependencies are set, run `python3 manage.py runserver`
* API Root is at: http://127.0.0.1:8000/hotels/
* Admin access can be provided, if asked for, and accessed at http://127.0.0.1:8000/admin


DESCRIPTION:

Endpoint1: `/getlistofhotels`
* Method: GET/POST
* `GET`: returns a list of dictionary in the table containing: `hotel_name`, `price` and `availability`	
* Containt: `hotel name` is the primary key in the table

Endpoint2: `/reservationconfirmation`
* Method: GET/POST
* `GET`: returns a list of dictionary in the table containing: `booking_id`, `hotel_name` ,`checkout` and `checkout`.
* Containt: `booking_id` is the primary key in the table and `hotel_name` is the Foreign Key

Endpoint3: `/guestlist`
* Method: GET/POST
* `GET`: returns a list of dictionary in the table containing: `booking_id`, `guest_name` and `guest_gender`.
* Containt: `booking_id` is the Foreign Key key in the table.