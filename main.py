#1
class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time
    def check_severity(self):
        if 30 <= self.delay_time <= 60:
            print("Standard Warning! Flight is Delayed")
        elif self.delay_time > 60:
            print("Severe Warning! Flight is Delayed for over an hour")
#2
import pandas as pd
df = pd.read_csv('arrivals.csv')
df.fillna(0)
#3
delayed = df[df['Minutes_Delayed'] > 30]
most_delayed = delayed.loc[delayed['Minutes_Delayed'].idxmax()]
flight_abc = Flight(most_delayed['Flight_Number'], most_delayed['Minutes_Delayed'])
flight_abc.check_severity()
#4
new_data = {
    'Flight_Number': [flight_abc.flight_num],
    'Airline': [most_delayed['Airline']],
    'Minutes_Delayed': [flight_abc.delay_time],
}
df_new = pd.DataFrame(new_data)
import os
log_file = 'severe_delays_log.csv'
if os.path.exists(log_file):
    df_log = pd.read_csv(log_file)
    df_log = pd.concat([df_log, df_new], ignore_index=True)
else:
    df_log = df_new
df_log.to_csv(log_file, index=False)