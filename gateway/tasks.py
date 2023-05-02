"""
@author: Cem Akpolat
@created by cemakpolat at 2023-05-01
"""
from celery import shared_task

import numpy as np
from django.utils import timezone
from sklearn.linear_model import LinearRegression
from gateway.models import Device, DeviceValue, DeviceStatus


def analyze_temperature_data():
    devices = Device.objects.all()
    for device in devices:
        device_values = DeviceValue.objects.filter(device=device)
        temperatures = [value.temperature for value in device_values]
        # Convert the created_at times to a numpy array of timestamps

        timestamps = [value.created_at.timestamp() for value in device_values]
        timestamps = np.array(timestamps).reshape(-1, 1)

        # Fit a linear regression model to the temperature data
        model = LinearRegression()
        model.fit(timestamps, temperatures)
        # # Use the model to predict the temperature at the current time
        current_time = timezone.now().timestamp()
        prediction = model.predict([[current_time]])[0]
        # # Calculate the average temperature
        average_temperature = sum(temperatures) / len(temperatures)
        # # Determine the status based on the temperature data
        if prediction > average_temperature:
            status = 'abnormal'
        else:
            status = 'normal'

        # # Save the status and average temperature to the DeviceStatus model
        device_status, created = DeviceStatus.objects.get_or_create(device=device)
        device_status.status = status
        device_status.average_value = average_temperature
        device_status.prediction = prediction
        device_status.save()


@shared_task
def analyze_temperature_data_task():
    analyze_temperature_data()