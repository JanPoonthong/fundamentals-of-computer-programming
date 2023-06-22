shopping = int(input("Enter your shopping amount: "))
hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

total_time_in_minute = (hour * 60) + minute

if 500 <= shopping < 1500:
    if total_time_in_minute > 120:
        period = (total_time_in_minute - 120) / 30
        if period % 1 == 0:
            period = period
        else:
            period = int(period) + 1
        parking_fee = period * 30
        print(
            f"The parking fee for the first 2 hours is free. You have to pay {parking_fee} Baht for the parking fee."
        )
    else:
        print(
            f"The parking fee for the first 2 hours is free. You don't have to pay for the parking fee."
        )

if shopping < 500:
    if total_time_in_minute > 60:
        period = (total_time_in_minute - 60) / 30
        if period % 1 == 0:
            period = period
        else:
            period = int(period) + 1
        parking_fee = period * 30
        print(
            f"The parking fee for the first first hours is free. You have to pay {parking_fee} Baht for the parking fee."
        )
    else:
        print(
            f"The parking fee for the first first hours is free. You don't have to pay for the parking fee."
        )

if shopping >= 1500:
    if total_time_in_minute > 120:
        parking_fee = 30
        print(f"You have to pay {parking_fee} Baht for the parking fee")
    else:
        print("You don't have to pay for the parking fee")
